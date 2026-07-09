/**
 * chat.js — Lógica de chat do Marc.IA
 * Envia mensagens via fetch e renderiza bolhas.
 * Suporta 2 modos: DÚVIDA (texto) e CÓDIGO (bloco estruturado).
 * Onboarding "boot sequence" na primeira visita.
 *
 * Gamificação removida do MVP em 2026-07-06 (ADR-011) — XP, níveis e
 * progresso gamificado ficaram fora do escopo. Ver backlog/gamificacao.md.
 */

// === CARREGAR USUÁRIO LOGADO ===
// Removida em 2026-07-08: OAuth está pausado e a função só retornava `null`.
// Foi substituída em outros pontos por uma constante `usuarioId` definida
// no topo do arquivo (aluno segue como anônimo até o auth voltar).



async function carregarHistorico() {
    try {
        const r = await fetch("/chat/historico?usuario_id=" + encodeURIComponent(usuarioId), { credentials: "same-origin" });
        if (!r.ok) return;
        const data = await r.json();
        if (Array.isArray(data.mensagens)) {
            data.mensagens.forEach(function(msg) {
                if (msg.role === "user" || msg.role === "assistant") {
                    renderizarMensagem(msg.role, msg.content);
                }
            });
        }
    } catch (e) {
        console.warn("falha ao carregar histórico:", e);
    }
}

// Elementos do DOM
const chatMessages = document.getElementById("chat-messages");
const chatForm = document.getElementById("chat-form");
const chatInput = document.getElementById("chat-input");
const chatCodigo = document.getElementById("chat-codigo");
const chatCodigoPergunta = document.getElementById("chat-codigo-pergunta");
const linguagemSelect = document.getElementById("linguagem");
// Gamificação removida do MVP (decisão 2026-07-06, ADR-011).
// NIVEIS/XP eram usados só pra exibir barra lateral e após cada mensagem.
// Removidos pra focar em agente funcionando perfeitamente esta semana.
// Ver backlog/gamificacao.md pra reativação futura.
const xpValor = { textContent: "" };
const nivelValor = { textContent: "" };
const NIVEIS = {};
const topicosLista = document.getElementById("topicos");
const btnColab = document.getElementById("btn-colab");

// Timeout para chamadas ao backend (ms)
const FETCH_TIMEOUT = 45000;

// Flag para evitar double-submit
let enviando = false;

// Modo atual do formulário: "duvida" | "codigo"
let modoAtual = "duvida";

// Linguagem-alvo escolhida via picker (Visualg/Portugol).
// Vale pra AMBOS os modos: no modo Código já vinha via <select id="linguagem">,
// no modo Dúvida é o único jeito de dizer pro tutor "responde em Visualg".
// Resetada quando trocamos de tópico (em atualizarPickerLinguagem).
const LINGUAGENS_VALIDAS_PICKER = ["visualg", "portugol"];
let linguagemEscolhida = "";

// === IDENTIDADE DO ALUNO (anônimo, persistido em localStorage) ===
// O backend usa esse ID como chave da sessão (histórico, perfil, etc.).
// Quem tá logado via Google (futuro) vai ter um ID real — por enquanto,
// geramos um UUID e guardamos pra não perder o histórico entre reloads.
const USUARIO_ID_KEY = "marcia_usuario_id";
function obterUsuarioId() {
    try {
        let id = localStorage.getItem(USUARIO_ID_KEY);
        if (id) return id;
        // Gera UUID v4 simples (sem dependência externa)
        id = "anon-" + ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, function(c) {
            return (c ^ (crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c/4)).toString(16);
        });
        localStorage.setItem(USUARIO_ID_KEY, id);
        return id;
    } catch (e) {
        // localStorage bloqueado (modo privado raro) — fallback de sessão
        return "anon-temp";
    }
}
const usuarioId = obterUsuarioId();

// === BOOT SEQUENCE (ONBOARDING) ===
const BOOT_STORAGE_KEY = "marcia_onboarding_v1";

const bootOverlay = document.getElementById("boot-overlay");
const bootSlides = document.querySelectorAll(".boot-slide");
const bootDots = document.querySelectorAll(".boot-dots .dot");
const bootPrev = document.getElementById("boot-prev");
const bootNext = document.getElementById("boot-next");
const bootStart = document.getElementById("boot-start");
const bootSkip = document.getElementById("boot-skip");
let bootIdx = 0;

function mostrarSlideBoot(idx) {
    bootIdx = idx;
    bootSlides.forEach(function(s, i) {
        s.classList.toggle("active", i === idx);
    });
    bootDots.forEach(function(d, i) {
        d.classList.toggle("active", i === idx);
    });
    // Botão "PRÓXIMO" some no último; "PRESS START" aparece
    const isUltimo = idx === bootSlides.length - 1;
    bootNext.classList.toggle("hidden", isUltimo);
    bootStart.classList.toggle("hidden", !isUltimo);
    bootPrev.classList.toggle("hidden", idx === 0);
}

function fecharBoot() {
    bootOverlay.classList.add("hidden");
    try { localStorage.setItem(BOOT_STORAGE_KEY, "1"); } catch (e) { /* storage bloqueado */ }
}

function initBoot() {
    let jaViu = false;
    try { jaViu = localStorage.getItem(BOOT_STORAGE_KEY) === "1"; } catch (e) {}
    if (jaViu) {
        bootOverlay.classList.add("hidden");
    } else {
        mostrarSlideBoot(0);
    }
    bootPrev.addEventListener("click", function() {
        if (bootIdx > 0) mostrarSlideBoot(bootIdx - 1);
    });
    bootNext.addEventListener("click", function() {
        if (bootIdx < bootSlides.length - 1) mostrarSlideBoot(bootIdx + 1);
    });
    bootStart.addEventListener("click", fecharBoot);
    bootSkip.addEventListener("click", fecharBoot);
    // Navegação por teclado
    document.addEventListener("keydown", function(e) {
        if (bootOverlay.classList.contains("hidden")) return;
        if (e.key === "ArrowRight") bootNext.click();
        if (e.key === "ArrowLeft") bootPrev.click();
        if (e.key === "Enter" || e.key === " ") {
            if (!bootStart.classList.contains("hidden")) bootStart.click();
            else bootNext.click();
        }
        if (e.key === "Escape") fecharBoot();
    });
    // Click nos dots
    bootDots.forEach(function(dot) {
        dot.addEventListener("click", function() {
            const i = parseInt(dot.getAttribute("data-dot"), 10);
            mostrarSlideBoot(i);
        });
    });
}

// === MODO TOGGLE (DÚVIDA | CÓDIGO) ===
const modeBtns = document.querySelectorAll(".mode-btn");
const modePanels = document.querySelectorAll(".mode-panel");

function setModo(modo) {
    modoAtual = modo;
    modeBtns.forEach(function(b) {
        const ativo = b.getAttribute("data-mode") === modo;
        b.classList.toggle("active", ativo);
        b.setAttribute("aria-selected", ativo ? "true" : "false");
    });
    modePanels.forEach(function(p) {
        p.classList.toggle("active", p.getAttribute("data-panel") === modo);
    });
    // Foco automático no campo certo
    setTimeout(function() {
        if (modo === "duvida") chatInput.focus();
        else chatCodigo.focus();
    }, 50);
}

modeBtns.forEach(function(b) {
    b.addEventListener("click", function() {
        setModo(b.getAttribute("data-mode"));
    });
});

// === DETECÇÃO DE CÓDIGO NA RESPOSTA (aciona pulso do botão Colab) ===
function respostaTemCodigo(texto) {
    // Detecta blocos fenced ```...``` OU ```python/portugol
    return /```/.test(texto);
}

function pulsarBotaoColab() {
    btnColab.classList.add("pulse");
    setTimeout(function() {
        btnColab.classList.remove("pulse");
    }, 5000); // 5s × animação 0.8s = ~6 ciclos
}

/**
 * Renderiza uma mensagem como bolha no chat.
 * Suporta markdown básico (blocos de código ```).
 * Se `tierLabel` for passado (e role=assistant), adiciona tagzinha discreta
 * mostrando qual modelo respondeu (ex: 'Opus 4.8 High').
 */
function renderizarMensagem(role, content, tierLabel) {
    const div = document.createElement("div");
    div.classList.add("mensagem", role);

    const tag = document.createElement("span");
    tag.classList.add("role-tag");
    tag.textContent = role === "user" ? "👤 Aluno" : "🤖 Marc.IA";

    const corpo = document.createElement("div");
    corpo.classList.add("mensagem-corpo");
    renderizarConteudo(corpo, content);

    div.appendChild(tag);
    div.appendChild(corpo);

    // Tagzinha do tier (só pra mensagens do tutor)
    if (role === "assistant" && tierLabel) {
        const tierTag = document.createElement("small");
        tierTag.classList.add("tier-tag");
        tierTag.textContent = tierLabel;
        tierTag.title = "Modelo usado nesta resposta (escolha dinâmica baseada na complexidade)";
        div.appendChild(tierTag);
    }

    // Botões like/dislike (FRO-06) — só nas respostas do tutor
    if (role === "assistant") {
        const feedbackActions = document.createElement("div");
        feedbackActions.className = "feedback-actions";
        feedbackActions.innerHTML =
            '<button type="button" class="fb-btn fb-btn--like" aria-label="Resposta útil">👍</button>' +
            '<button type="button" class="fb-btn fb-btn--dislike" aria-label="Resposta não útil">👎</button>' +
            '<span class="fb-hint">Essa resposta foi útil? Ajude o Marc.IA a melhorar.</span>' +
            '<span class="fb-thanks" hidden>Obrigado pelo feedback!</span>';
        div.appendChild(feedbackActions);
        // Liga os handlers (precisam saber o índice da mensagem no histórico)
        const fbIdx = mensagemCounter++;
        div.dataset.fbIdx = fbIdx;
        const btnLike = feedbackActions.querySelector(".fb-btn--like");
        const btnDislike = feedbackActions.querySelector(".fb-btn--dislike");
        const hint = feedbackActions.querySelector(".fb-hint");
        const thanks = feedbackActions.querySelector(".fb-thanks");
        // Quando o aluno vota, esconde o hint e mostra "Obrigado"
        function dismissHint() { if (hint) hint.classList.add("hidden"); }
        function handlerLike() {
            dismissHint();
            enviarFeedback(fbIdx, "like", topicoIdAtual(), btnLike, btnDislike, thanks);
        }
        function handlerDislike() {
            dismissHint();
            enviarFeedback(fbIdx, "dislike", topicoIdAtual(), btnDislike, btnLike, thanks);
        }
        btnLike.addEventListener("click", handlerLike);
        btnDislike.addEventListener("click", handlerDislike);
    }

    chatMessages.appendChild(div);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    // FRO-06 / MET-02: dispara modal NPS a cada N=3 respostas do tutor
    if (role === "assistant") {
        contadorRespostasTutor++;
        if (contadorRespostasTutor % 3 === 0 && !npsJaExibido) {
            setTimeout(function () { abrirModalNPS(); }, 800);
        }
    }
}

/**
 * Renderiza conteúdo com suporte a blocos de código fenced.
 */
function renderizarConteudo(container, texto) {
    const partes = texto.split(/(```[\s\S]*?```)/g);
    partes.forEach(function(parte) {
        if (parte.startsWith("```") && parte.endsWith("```")) {
            // Bloco de código
            const inner = parte.slice(3, -3);
            // Remove a linha de linguagem opcional na primeira linha
            const linhas = inner.split("\n");
            let lang = "";
            let code = inner;
            if (linhas[0] && /^(python|portugol|py)$/i.test(linhas[0].trim())) {
                lang = linhas[0].trim();
                code = linhas.slice(1).join("\n");
            }
            const pre = document.createElement("pre");
            pre.classList.add("bloco-codigo");
            if (lang) pre.setAttribute("data-lang", lang);
            const codeEl = document.createElement("code");
            codeEl.textContent = code;
            pre.appendChild(codeEl);
            container.appendChild(pre);
        } else if (parte) {
            // Texto normal — converte \n em <br>
            const p = document.createElement("span");
            p.innerHTML = parte
                .replace(/&/g, "&amp;")
                .replace(/</g, "&lt;")
                .replace(/>/g, "&gt;")
                .replace(/\n/g, "<br>");
            container.appendChild(p);
        }
    });
}

/**
 * Mostra indicador "pensando..." e retorna referência para remover depois.
 */
function mostrarPensando() {
    // Remove indicador anterior se existir (proteção contra duplicatas)
    removerPensando();
    const div = document.createElement("div");
    div.classList.add("pensando");
    div.id = "indicador-pensando";
    div.textContent = "🤖 Marc.IA está pensando...";
    chatMessages.appendChild(div);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    return div;
}

/**
 * Remove o indicador de "pensando...".
 */
function removerPensando() {
    const el = document.getElementById("indicador-pensando");
    if (el) el.remove();
}

/**
 * Desabilita/habilita controles durante envio.
 */
function setControlesAtivos(ativo) {
    chatInput.disabled = !ativo;
    chatButton.disabled = !ativo;
    chatCodigo.disabled = !ativo;
    chatCodigoPergunta.disabled = !ativo;
    linguagemSelect.disabled = !ativo;
    enviando = !ativo;
}

const chatButton = chatForm.querySelector('button[type="submit"]');

/**
 * Envia mensagem do aluno para o backend e exibe a resposta.
 * Adapta payload conforme o modo ativo.
 */
async function enviarMensagem() {
    if (enviando) return;

    let mensagem = "";
    let codigo = "";
    let linguagem = "python";

    if (modoAtual === "duvida") {
        mensagem = chatInput.value.trim();
        if (!mensagem) return;
        renderizarMensagem("user", mensagem);
        chatInput.value = "";
    } else {
        codigo = chatCodigo.value;
        // Preserva indentação: NÃO trim nas laterais, mas remove trailing whitespace
        codigo = codigo.replace(/\s+$/, "");
        mensagem = chatCodigoPergunta.value.trim();
        linguagem = linguagemSelect.value;
        if (!codigo) return;
        // Renderiza o bloco de código no chat com indentação preservada
        const display = "```" + linguagem + "\n" + codigo + "\n```" +
            (mensagem ? "\n\n" + mensagem : "");
        renderizarMensagem("user", display);
        chatCodigo.value = "";
        chatCodigoPergunta.value = "";
    }

    setControlesAtivos(false);
    mostrarPensando();

    const controller = new AbortController();
    const timeoutId = setTimeout(function() {
        controller.abort();
    }, FETCH_TIMEOUT);

    try {
        const payload = { mensagem: mensagem, usuario_id: usuarioId };
        if (modoAtual === "codigo") {
            payload.codigo = codigo;
            payload.linguagem = linguagem;
        } else if (linguagemEscolhida && LINGUAGENS_VALIDAS_PICKER.indexOf(linguagemEscolhida) !== -1) {
            // Modo Dúvida: se o aluno escolheu Visualg/Portugol no picker,
            // envia como metadado pro tutor saber em qual linguagem responder.
            payload.linguagem = linguagemEscolhida;
        }

        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
            signal: controller.signal,
        });

        clearTimeout(timeoutId);

        let data;
        try {
            data = await response.json();
        } catch (parseError) {
            removerPensando();
            renderizarMensagem("assistant", "⚠️ Resposta inválida do servidor. Tente novamente.");
            setControlesAtivos(true);
            return;
        }

        removerPensando();

        if (response.ok && data.resposta) {
            renderizarMensagem("assistant", data.resposta, data.tier);
            // Se resposta tem código, pulsa o botão Colab
            if (respostaTemCodigo(data.resposta)) pulsarBotaoColab();
        } else {
            renderizarMensagem("assistant", data.erro || "⚠️ Erro ao obter resposta.");
        }
    } catch (error) {
        clearTimeout(timeoutId);
        removerPensando();
        if (error.name === "AbortError") {
            renderizarMensagem("assistant", "⚠️ O tutor demorou para responder. Tente novamente.");
        } else {
            renderizarMensagem("assistant", "⚠️ Erro de conexão. Verifique se o servidor está rodando.");
        }
    }

    setControlesAtivos(true);
    if (modoAtual === "duvida") chatInput.focus();
    else chatCodigo.focus();
}

/**
 * Carrega a rota de tópicos do backend e popula a sidebar.
 * Renderiza por categoria (Algoritmos / Python) e liga os sub-botões de
 * linguagem (Visualg/Portugol) pra tópicos que aceitam escolha.
 */
async function carregarRota() {
    try {
        const response = await fetch("/rota");
        if (!response.ok) throw new Error("Resposta não-OK do servidor");
        const data = await response.json();
        if (!data.topicos || !Array.isArray(data.topicos)) {
            throw new Error("Formato de dados inválido");
        }
        topicosLista.innerHTML = "";
        // Agrupa por categoria na ordem definida em categorias_ordem
        const ordemCategorias = data.categorias_ordem || ["algoritmos", "python"];
        // Cacheia tópicos pra uso posterior (ex: enviarSelecao precisa do
        // objeto completo pra repassar ao picker de linguagem).
        window.__topicosCache = data.topicos;
        const grupos = {};
        data.topicos.forEach(function(topico) {
            const cat = topico.categoria || "outros";
            if (!grupos[cat]) grupos[cat] = [];
            grupos[cat].push(topico);
        });

        // Estado persistido (topico + linguagem ativos)
        const estado = data.estado || {};
        const topicoAtivoId = estado.topico_ativo || null;
        const linguagemAtiva = estado.linguagem_topico || null;

        let ordemGlobal = 0;
        ordemCategorias.forEach(function(cat) {
            const lista = grupos[cat];
            if (!lista || lista.length === 0) return;
            // Header da categoria
            const header = document.createElement("li");
            header.className = "topic-category-header";
            header.textContent = cat === "algoritmos" ? "Algoritmos" : "Python";
            topicosLista.appendChild(header);

            lista.forEach(function(topico) {
                const li = document.createElement("li");
                li.className = "topic-item";
                li.dataset.topicoId = topico.id;
                if (topico.id === topicoAtivoId) li.classList.add("active");
                const mark = document.createElement("span");
                mark.className = "topic-mark";
                mark.textContent = topico.id === topicoAtivoId ? "▸" : "○";
                const txt = document.createElement("span");
                txt.className = "topic-text";
                txt.textContent = topico.titulo;
                li.appendChild(mark);
                li.appendChild(txt);
                // Click handler: seleciona tópico e mostra/define linguagem
                li.addEventListener("click", function() {
                    selecionarTopico(topico);
                });
                topicosLista.appendChild(li);
                ordemGlobal++;
            });
        });

        // Se tinha tópico ativo, sincroniza UI dos sub-botões
        if (topicoAtivoId) {
            const topicoAtivo = data.topicos.find(function(t) { return t.id === topicoAtivoId; });
            if (topicoAtivo) {
                atualizarPickerLinguagem(topicoAtivo, linguagemAtiva);
            }
        }
    } catch (error) {
        topicosLista.innerHTML = "";
        const li = document.createElement("li");
        li.className = "topic-item error";
        li.textContent = "Erro ao carregar tópicos";
        topicosLista.appendChild(li);
    }
}

/**
 * Exibe mensagem de boas-vindas do PyAI (sem API call).
 * Conteúdo varia por variante pra reforçar o tom de cada uma.
 */
function boasVindas() {
    // Tom único (não muda por tema visual). O tutor é sempre o Marc.IA.
    const msg = "E aí. Sou o Marc.IA, seu tutor de Introdução à Programação.\n\nTô aqui pra te ajudar a aprender do seu jeito — sem pressa, sem julgamento, um passo por vez.\n\n💡 Tem um código que tá te dando dor de cabeça? Troca pra aba Código e cola aqui que eu faço o tracing contigo.\n🎯 Antes de qualquer coisa: me diz o que você já sabe sobre o assunto — assim eu calibro tudo no seu nível.";
    renderizarMensagem("assistant", msg);
}

// === Event Listeners ===
chatForm.addEventListener("submit", function(e) {
    e.preventDefault();
    enviarMensagem();
});

// Tab no campo código insere 4 espaços (não tab character)
chatCodigo.addEventListener("keydown", function(e) {
    if (e.key === "Tab") {
        e.preventDefault();
        const start = chatCodigo.selectionStart;
        const end = chatCodigo.selectionEnd;
        const v = chatCodigo.value;
        chatCodigo.value = v.substring(0, start) + "    " + v.substring(end);
        chatCodigo.selectionStart = chatCodigo.selectionEnd = start + 4;
    }
});

// Enter envia / Shift+Enter quebra linha no campo de dúvida
chatInput.addEventListener("keydown", function(e) {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        chatForm.requestSubmit();
    }
});

// === SELEÇÃO DE TÓPICO E LINGUAGEM ===

/**
 * Quando o aluno clica num tópico na barra lateral.
 * Se o tópico aceita múltiplas linguagens (ex: Visualg/Portugol), mostra
 * os sub-botões. Se tem linguagem_obrigatoria (ex: recursao = portugol),
 * salva direto sem perguntar.
 */
/**
 * Limpa visualmente todas as mensagens do chat e re-renderiza a Apresentação.
 * NÃO toca no histórico persistido em data/marcia.db — é só limpeza visual
 * pra dar ao aluno um "começo limpo" quando ele muda de tópico.
 */
function limparChat() {
    // Limpa tudo que pode ter sido renderizado no #chat-messages
    chatMessages.innerHTML = "";
    // Re-renderiza a Apresentação do tutor (mesma que aparece no primeiro boot)
    boasVindas();
}

async function selecionarTopico(topico) {
    const linguagensAceitas = topico.linguagens_aceitas || [];

    // Limpa o chat ANTES de tudo — aluno tá começando uma aula nova.
    limparChat();

    // Primeiro: sincroniza o picker pro estado deste tópico
    // (esconde se não tem múltiplas linguagens OU tem obrigatória).
    atualizarPickerLinguagem(topico, null);

    if (topico.linguagem_obrigatoria) {
        // Linguagem fixa — salva direto
        await enviarSelecao(topico.id, topico.linguagem_obrigatoria);
    } else if (linguagensAceitas.length === 1) {
        // Única linguagem (ex: Python) — salva direto
        await enviarSelecao(topico.id, linguagensAceitas[0]);
    }
    // Se múltiplas linguagens: picker já tá visível, aluno escolhe via clicar nos botões

    // Marca o tópico como ativo visualmente
    document.querySelectorAll(".topic-item").forEach(function(el) {
        el.classList.toggle("active", el.dataset.topicoId === topico.id);
        const mark = el.querySelector(".topic-mark");
        if (mark) mark.textContent = el.dataset.topicoId === topico.id ? "▸" : "○";
    });

    // NOTA: a bolinha-intermediária de exercício FOI REMOVIDA daqui em 08/07
    // (feedback do Diogo: aluno não quer ver oferta de exercício toda vez que
    // troca de tópico). Agora o tutor oferece exercícios na resposta dele,
    // quando fizer sentido no fluxo da conversa — controlado pelo system prompt
    // de AgenteIP (bloco PROTOCOLO DE RESPOSTA, regra de exercícios).
}

/**
 * Mostra/esconde os sub-botões de linguagem conforme o tópico ativo.
 * Sincroniza o estado `linguagemEscolhida` (usada no payload /chat em modo Dúvida)
 * e marca visualmente a linguagem ativa (persistente ou recém-escolhida).
 *
 * Aparece pra AMBOS os modos (Dúvida e Código) quando o tópico aceita
 * múltiplas linguagens e não tem linguagem_obrigatoria.
 */
function atualizarPickerLinguagem(topico, linguagemAtiva) {
    const picker = document.getElementById("linguagem-picker");
    if (!picker) return;
    const linguagensAceitas = topico.linguagens_aceitas || [];

    if (linguagensAceitas.length > 1 && !topico.linguagem_obrigatoria) {
        // Sincroniza estado global: usa a linguagem vinda do backend, senão mantém a local
        if (linguagemAtiva && linguagensAceitas.indexOf(linguagemAtiva) !== -1) {
            linguagemEscolhida = linguagemAtiva;
        } else if (linguagensAceitas.indexOf(linguagemEscolhida) === -1) {
            // A escolha atual não é válida pro novo tópico → limpa
            linguagemEscolhida = "";
        }
        picker.classList.remove("hidden");
        picker.querySelectorAll(".lang-btn").forEach(function(btn) {
            const lang = btn.dataset.lang;
            const visivel = linguagensAceitas.indexOf(lang) !== -1;
            btn.classList.toggle("hidden", !visivel);
            btn.classList.toggle("active", lang === linguagemEscolhida);
        });
        // Espelha no <select id="linguagem"> do modo Código pra ficar coerente
        const sel = document.getElementById("linguagem");
        if (sel) sel.value = linguagemEscolhida || sel.value;
    } else {
        // Picker não se aplica — mas se for obrigatória, sincroniza estado
        if (topico.linguagem_obrigatoria) {
            linguagemEscolhida = topico.linguagem_obrigatoria;
        }
        picker.classList.add("hidden");
    }
}

async function enviarSelecao(topicoId, linguagem) {
    try {
        const r = await fetch("/rota/selecionar", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ topico_id: topicoId, linguagem: linguagem }),
        });
        if (r.ok) {
            const data = await r.json();
            // Recupera o topico completo do estado da rota (já carregado) pra
            // passar ao picker com linguagens_aceitas e linguagem_obrigatoria reais.
            // Sem isso, o picker escondia os sub-botões de linguagem.
            const topicoAtivo = (window.__topicosCache || []).find(function (t) {
                return t.id === topicoId;
            }) || {
                id: topicoId,
                linguagens_aceitas: linguagem === "portugol" ? ["visualg", "portugol"] : [linguagem],
            };
            atualizarPickerLinguagem(topicoAtivo, data.linguagem_topico);
        }
    } catch (e) {
        console.warn("falha ao selecionar tópico:", e);
    }
}

/**
 * === AÇÕES DO MODO AULA ===
 * Removidas em 2026-07-08: a toolbar de modo aula foi cortada do front
 * (UX final 07/07). Aluno digita "próximo"/"exercício"/"repetir" no chat
 * e o system prompt do AgenteIP trata.
 */

// Liga os sub-botões de linguagem
// Atualiza estado + visual otimisticamente (não espera o backend)
// pra que uma mensagem enviada em seguida já leve a linguagem certa.
document.querySelectorAll(".lang-btn").forEach(function(btn) {
    btn.addEventListener("click", async function() {
        const lang = btn.dataset.lang;
        const topicoAtivo = document.querySelector(".topic-item.active");
        if (!topicoAtivo) return;

        // Otimista: marca visual e global ANTES do backend confirmar
        linguagemEscolhida = lang;
        const picker = document.getElementById("linguagem-picker");
        if (picker) {
            picker.querySelectorAll(".lang-btn").forEach(function(b) {
                b.classList.toggle("active", b.dataset.lang === lang);
            });
        }
        // Espelha no <select id="linguagem"> do modo Código
        const sel = document.getElementById("linguagem");
        if (sel) sel.value = lang;

        await enviarSelecao(topicoAtivo.dataset.topicoId, lang);
    });
});

// === EXERCÍCIO INLINE (FRO-05) ===
//
// Card aparece quando o aluno seleciona um tópico com exercícios vinculados
// (via bolinha-intermediária clicável). NUNCA submete o composer principal.

function escapeHtml(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function(c) {
        return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
}

/**
 * NOTA: `verificarExerciciosDoTopico` FOI REMOVIDA em 2026-07-08.
 * Antes, essa função era chamada automaticamente em `selecionarTopico`
 * e injetava uma bolinha-intermediária "🎯 EXERCÍCIO DISPONÍVEL" toda
 * vez que o aluno selecionava um tópico com exercícios.
 *
 * Decisão (Diogo): o aluno NÃO quer oferta automática de exercício —
 * exercícios devem aparecer só quando o tutor achar natural oferecer,
 * através da resposta dele (controlado pelo system prompt de AgenteIP).
 *
 * O ponto de entrada pra abrir um card de exercício é `criarCardExercicio`,
 * que pode ser chamado por:
 *   - Handler em mensagem do tutor (futuro: parse de texto tipo "/exercicio X")
 *   - Toggle no header (futuro)
 * Por enquanto, o aluno inicia o card via JavaScript, pedindo ao tutor
 * por um exercício, e o sistema prompt orienta o tutor a oferecer.
 */

/**
 * Cria o card de exercício dentro do #chat-messages.
 * Idempotente — se já existe card pra este exercicioId, não duplica.
 */
function criarCardExercicio(exercicioObj) {
    if (!exercicioObj || !exercicioObj.id) return null;
    if (document.getElementById("ex-" + exercicioObj.id + "-card")) return null;

    const card = document.createElement("div");
    card.id = "ex-" + exercicioObj.id + "-card";
    card.className = "ex-card";
    card.dataset.exercicioId = exercicioObj.id;

    // Header
    const header = document.createElement("header");
    header.className = "ex-header";
    const titulo = document.createElement("span");
    titulo.className = "ex-titulo";
    titulo.textContent = exercicioObj.titulo;
    const meta = document.createElement("span");
    meta.className = "ex-meta";
    meta.innerHTML =
        '<span class="ex-meta-chip">' + escapeHtml(exercicioObj.topico_id || "") + '</span>' +
        '<span class="ex-meta-chip">' + escapeHtml(exercicioObj.lista_origem || "") +
        ' · #' + (exercicioObj.numero || "?") + '</span>';
    header.appendChild(titulo);
    header.appendChild(meta);

    // Enunciado
    const enunciado = document.createElement("div");
    enunciado.className = "ex-enunciado";
    const enunP = document.createElement("p");
    enunP.textContent = exercicioObj.enunciado || "";
    enunciado.appendChild(enunP);

    if (exercicioObj.entrada_exemplo || exercicioObj.saida_esperada) {
        const det = document.createElement("details");
        const sum = document.createElement("summary");
        sum.textContent = "Ver exemplo de entrada/saída";
        const pre = document.createElement("pre");
        pre.textContent =
            (exercicioObj.entrada_exemplo ? "Entrada:\n" + exercicioObj.entrada_exemplo + "\n\n" : "") +
            (exercicioObj.saida_esperada ? "Saída esperada:\n" + exercicioObj.saida_esperada : "");
        det.appendChild(sum);
        det.appendChild(pre);
        enunciado.appendChild(det);
    }

    // Textarea
    const ta = document.createElement("textarea");
    ta.className = "ex-textarea";
    ta.rows = 6;
    ta.placeholder = "Digite sua resposta em " + (exercicioObj.linguagem || "") + " aqui…";
    ta.spellcheck = false;

    // Actions
    const actions = document.createElement("div");
    actions.className = "ex-actions";
    const btnGabarito = document.createElement("button");
    btnGabarito.type = "button";
    btnGabarito.className = "ex-btn ex-btn-revelar";
    btnGabarito.textContent = "Mostrar gabarito";
    btnGabarito.addEventListener("click", function () {
        revelarGabarito(exercicioObj.id, card);
    });
    const btnEnviar = document.createElement("button");
    btnEnviar.type = "button";          // IMPORTANTE — não submete form
    btnEnviar.className = "ex-btn ex-btn-enviar";
    btnEnviar.textContent = "Enviar resposta";
    btnEnviar.addEventListener("click", function () {
        enviarRespostaExercicio(exercicioObj.id, card);
    });
    actions.appendChild(btnGabarito);
    actions.appendChild(btnEnviar);

    // Slot de feedback (hidden até validação)
    const fb = document.createElement("div");
    fb.className = "ex-feedback";
    fb.hidden = true;

    card.appendChild(header);
    card.appendChild(enunciado);
    card.appendChild(ta);
    card.appendChild(actions);
    card.appendChild(fb);

    chatMessages.appendChild(card);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    return card;
}

/**
 * Envia resposta do aluno pro backend e renderiza feedback inline.
 * Reaproveita o flag `enviando` (mesmo lock do composer).
 */
async function enviarRespostaExercicio(exercicioId, cardNode) {
    if (enviando) return;
    const ta = cardNode.querySelector(".ex-textarea");
    const fb = cardNode.querySelector(".ex-feedback");
    const btn = cardNode.querySelector(".ex-btn-enviar");
    const resposta = ta ? ta.value : "";
    if (!resposta.trim()) {
        fb.hidden = false;
        fb.className = "ex-feedback ex-feedback--err";
        fb.textContent = "Digite uma resposta antes de enviar.";
        return;
    }

    setControlesAtivos(false);
    btn.disabled = true;
    fb.hidden = false;
    fb.className = "ex-feedback";
    fb.textContent = "⏳ Validando…";

    try {
        const r = await fetch("/exercicio/validar", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                exercicio_id: exercicioId,
                resposta: resposta,
                usuario_id: usuarioId,
            }),
        });
        const data = await r.json();
        if (!r.ok) {
            fb.className = "ex-feedback ex-feedback--err";
            fb.textContent = "⚠️ " + (data.erro || "Erro ao validar.");
            return;
        }
        const ok = !!data.correta;
        fb.className = "ex-feedback " + (ok ? "ex-feedback--ok" : "ex-feedback--err");
        fb.innerHTML = "";   // limpa pra recriar
        const txt = document.createElement("div");
        txt.textContent = (ok ? "✅ " : "❌ ") + data.feedback + " (score " + data.score + "/100)";
        fb.appendChild(txt);
        if (data.gabarito) {
            const label = document.createElement("div");
            label.style.marginTop = "8px";
            label.style.fontWeight = "600";
            label.textContent = "📋 Gabarito (referência):";
            fb.appendChild(label);
            const pre = document.createElement("pre");
            pre.textContent = data.gabarito;
            fb.appendChild(pre);
        }
    } catch (e) {
        fb.className = "ex-feedback ex-feedback--err";
        fb.textContent = "⚠️ Erro de conexão ao validar.";
    } finally {
        setControlesAtivos(true);
        btn.disabled = false;
    }
}

/**
 * Mostra o gabarito sem precisar enviar a resposta (UX alternativa).
 * No esqueleto, simplesmente reapresenta a mensagem de "já incluído na validação".
 */
async function revelarGabarito(exercicioId, cardNode) {
    const fb = cardNode.querySelector(".ex-feedback");
    fb.hidden = false;
    fb.className = "ex-feedback";
    fb.innerHTML = "";
    const t = document.createElement("div");
    t.textContent = "💡 Dica: o gabarito completo aparece junto com o feedback de validação. Envie sua resposta em portugol/python — o sistema mostra o que faltou e o que estava certo.";
    fb.appendChild(t);
}

// === FEEDBACK + NPS (FRO-06 / MET-01 / MET-02) ===

// Contadores e flag pro modal NPS — incrementados a cada resposta do tutor
let mensagemCounter = 0;     // índice da próxima mensagem do tutor (FRO-06 metadata)
let contadorRespostasTutor = 0;  // quantas respostas o tutor já deu na sessão
let npsJaExibido = false;    // sessionStorage: abriu pelo menos 1x nesta sessão
try { npsJaExibido = sessionStorage.getItem("marcia_nps_v1") === "1"; } catch (_) {}

// Tópico ativo (lido do estado do front) — usado no payload do feedback
function topicoIdAtual() {
    const ativo = document.querySelector(".topic-item.active");
    return ativo ? (ativo.dataset.topicoId || null) : null;
}

/**
 * Envia like/dislike pro backend. Desabilita ambos botões após clique
 * (evita duplicata). Mostra "Obrigado" discreto.
 */
async function enviarFeedback(msgIdx, tipo, topicoId, btnAtivo, btnOutro, thanksEl) {
    if (btnAtivo.disabled) return;
    btnAtivo.disabled = true;
    btnOutro.disabled = true;
    try {
        const r = await fetch("/feedback", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                mensagem_idx: msgIdx,
                tipo: tipo,
                topico_id: topicoId,
                usuario_id: usuarioId,
            }),
        });
        if (r.ok) {
            btnAtivo.classList.add("fb-btn--active");
            thanksEl.hidden = false;
        } else {
            // Reabilita pra aluno tentar de novo
            btnAtivo.disabled = false;
            btnOutro.disabled = false;
            console.warn("feedback falhou:", await r.text());
        }
    } catch (e) {
        btnAtivo.disabled = false;
        btnOutro.disabled = false;
        console.warn("feedback erro de rede:", e);
    }
}

/**
 * === MODAL NPS + SEAN ELLIS ===
 * Aparece a cada 5 respostas do tutor (uma vez por sessão de browser).
 * Salva ambos os valores via /metricas.
 */
function abrirModalNPS() {
    if (document.getElementById("npsOverlay")) return;   // já aberto
    npsJaExibido = true;
    try { sessionStorage.setItem("marcia_nps_v1", "1"); } catch (_) {}

    // Markup
    const overlay = document.createElement("div");
    overlay.id = "npsOverlay";
    overlay.className = "nps-overlay";
    overlay.innerHTML =
        '<div class="nps-modal" role="dialog" aria-modal="true" aria-labelledby="npsTitle">' +
            '<button type="button" class="nps-close" aria-label="Fechar">×</button>' +
            '<h2 id="npsTitle">Como você avalia o Marc.IA?</h2>' +
            '<p>Sua opinião em 2 perguntas rápidas. Pode pular a qualquer momento.</p>' +
            '<div class="nps-nps-row">' +
                '<span class="nps-nps-label">De 0 a 10, quanto recomendaria?</span>' +
                '<input type="range" min="0" max="10" value="9" class="nps-nps-slider" id="npsSlider">' +
                '<span class="nps-nps-value" id="npsValue">9</span>' +
            '</div>' +
            '<div class="nps-sean-row">' +
                '<span class="nps-nps-label">Se o Marc.IA parasse de existir, como você se sentiria?</span>' +
                '<div class="nps-sean-options">' +
                    '<button type="button" class="nps-sean-opt" data-sean="muito">Muito desapontado</button>' +
                    '<button type="button" class="nps-sean-opt" data-sean="um_pouco">Um pouco desapontado</button>' +
                    '<button type="button" class="nps-sean-opt" data-sean="indiferente">Indiferente</button>' +
                '</div>' +
            '</div>' +
            '<div class="nps-actions">' +
                '<button type="button" class="nps-btn" id="npsPular">Pular</button>' +
                '<button type="button" class="nps-btn nps-btn--primary" id="npsEnviar" disabled>Enviar</button>' +
            '</div>' +
        '</div>';
    document.body.appendChild(overlay);

    // Handlers
    const slider = overlay.querySelector("#npsSlider");
    const valueEl = overlay.querySelector("#npsValue");
    const enviarBtn = overlay.querySelector("#npsEnviar");
    const pularBtn = overlay.querySelector("#npsPular");
    const closeBtn = overlay.querySelector(".nps-close");
    const seanOpts = overlay.querySelectorAll(".nps-sean-opt");
    let seanSelecionado = null;

    slider.addEventListener("input", function () { valueEl.textContent = slider.value; });

    seanOpts.forEach(function (btn) {
        btn.addEventListener("click", function () {
            seanOpts.forEach(function (b) { b.classList.remove("selected"); });
            btn.classList.add("selected");
            seanSelecionado = btn.dataset.sean;
            enviarBtn.disabled = false;
        });
    });

    function fechar() {
        overlay.remove();
    }
    closeBtn.addEventListener("click", fechar);
    pularBtn.addEventListener("click", fechar);
    overlay.addEventListener("click", function (e) {
        if (e.target === overlay) fechar();
    });
    document.addEventListener("keydown", function onEsc(e) {
        if (e.key === "Escape") { fechar(); document.removeEventListener("keydown", onEsc); }
    });

    enviarBtn.addEventListener("click", async function () {
        enviarBtn.disabled = true;
        const nps = parseInt(slider.value, 10);
        // Envia em paralelo — falha de um não bloqueia o outro
        const tarefas = [
            fetch("/metricas", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ tipo: "nps", valor: nps, usuario_id: usuarioId }),
            }).catch(function () { return null; }),
        ];
        if (seanSelecionado) {
            tarefas.push(fetch("/metricas", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ tipo: "sean_ellis", valor: seanSelecionado, usuario_id: usuarioId }),
            }).catch(function () { return null; }));
        }
        await Promise.all(tarefas);
        // Substitui conteúdo por agradecimento
        const modal = overlay.querySelector(".nps-modal");
        modal.innerHTML =
            '<h2>Valeu! 🎉</h2>' +
            '<p class="nps-thanks">Feedback registrado. Ajuda o Marc.IA a melhorar.</p>' +
            '<div class="nps-actions">' +
                '<button type="button" class="nps-btn nps-btn--primary" id="npsFechar">Fechar</button>' +
            '</div>';
        modal.querySelector("#npsFechar").addEventListener("click", fechar);
    });
}

// === DRAWER MOBILE (SIDEBAR) ===
// Em telas <= 768px, a sidebar vira drawer lateral controlado pelo
// botão hambúrguer. Toque no overlay ESCONDE a sidebar.
function setupSidebarToggle() {
    const toggle = document.getElementById("sidebarToggle");
    const sidebar = document.querySelector(".sidebar");
    const overlay = document.getElementById("sidebarOverlay");
    if (!toggle || !sidebar || !overlay) return;

    function abrir() {
        sidebar.classList.add("open");
        overlay.classList.add("visible");
        toggle.setAttribute("aria-expanded", "true");
    }
    function fechar() {
        sidebar.classList.remove("open");
        overlay.classList.remove("visible");
        toggle.setAttribute("aria-expanded", "false");
    }
    function alternar() {
        if (sidebar.classList.contains("open")) fechar();
        else abrir();
    }

    toggle.addEventListener("click", alternar);
    overlay.addEventListener("click", fechar);

    // Fecha o drawer automaticamente se a tela crescer (>768px)
    const mq = window.matchMedia("(min-width: 769px)");
    function onMq(e) { if (e.matches) fechar(); }
    if (mq.addEventListener) mq.addEventListener("change", onMq);
    else if (mq.addListener) mq.addListener(onMq);  // Safari antigo

    // ESC fecha
    document.addEventListener("keydown", function(e) {
        if (e.key === "Escape" && sidebar.classList.contains("open")) fechar();
    });
}

// === HISTÓRICO PERSISTIDO POR TÓPICO (carregado na sidebar) ===
// Marca tópicos da trilha que têm conversa salva no banco (data/marcia.db).
// Em cada um adiciona um badge discreto "💾 N" que vira botão "↺ Carregar"
// ao clicar — abre as mensagens antigas dentro do chat atual.
function marcarTopicosComHistorico(topicosComHist) {
    const mapa = {};
    topicosComHist.forEach(function (t) {
        mapa[t.topico_id] = t.qtd_mensagens;
    });
    document.querySelectorAll(".topic-item").forEach(function (li) {
        const tid = li.dataset.topicoId;
        const qtd = mapa[tid];
        if (!qtd) {
            // Remove badge antigo se existir (tópico esvaziado)
            const antigo = li.querySelector(".topic-history-badge");
            if (antigo) antigo.remove();
            return;
        }
        let badge = li.querySelector(".topic-history-badge");
        if (!badge) {
            badge = document.createElement("button");
            badge.type = "button";
            badge.className = "topic-history-badge";
            badge.title = "Carregar histórico desta aula";
            li.appendChild(badge);
            // Click → carrega
            badge.addEventListener("click", function (e) {
                e.stopPropagation();   // não aciona selecionarTopico
                carregarHistoricoTopico(tid);
            });
        }
        badge.textContent = "💾 " + qtd;
    });
}

async function carregarHistoricoPorTopico() {
    try {
        const r = await fetch("/sessao/topicos?usuario_id=" + encodeURIComponent(usuarioId));
        if (!r.ok) return;
        const data = await r.json();
        if (data.topicos && data.topicos.length) {
            marcarTopicosComHistorico(data.topicos);
        }
    } catch (e) {
        console.warn("falha ao carregar tópicos com histórico:", e);
    }
}

/**
 * Carrega o histórico persistido de um tópico e renderiza as mensagens
 * como bolhas no chat atual, com timestamp visível.
 */
async function carregarHistoricoTopico(topicoId) {
    try {
        const r = await fetch("/sessao/topico/" + encodeURIComponent(topicoId) +
                              "?usuario_id=" + encodeURIComponent(usuarioId));
        if (!r.ok) return;
        const data = await r.json();
        const mensagens = data.mensagens || [];
        if (mensagens.length === 0) {
            // Nenhuma mensagem — informa
            renderizarMensagem("assistant",
                "📂 Nenhuma mensagem salva neste tópico ainda.");
            return;
        }
        // Separador visual (mensagem do assistant explicando)
        renderizarMensagem("assistant",
            `📂 Histórico salvo de **${topicoId}** — ${mensagens.length} mensagens. Carregado em ${new Date().toLocaleString("pt-BR")}.`);
        // Renderiza cada par user/assistant com timestamp visível
        mensagens.forEach(function (m) {
            const ts = m.timestamp ? " — " + new Date(m.timestamp).toLocaleString("pt-BR") : "";
            renderizarMensagem(m.role, m.content + ts);
        });
        chatMessages.scrollTop = chatMessages.scrollHeight;
    } catch (e) {
        console.warn("falha ao carregar histórico do tópico:", e);
    }
}

// Inicialização
document.addEventListener("DOMContentLoaded", async function() {
    setupSidebarToggle();
    // OAuth pausado — fluxo original de sempre
    await carregarHistorico();
    initBoot();
    carregarRota();
    carregarHistoricoPorTopico();
    // Boas-vindas só aparecem depois que o boot fechar (se for primeira vez)
    if (bootOverlay.classList.contains("hidden")) {
        boasVindas();
    } else {
        // Espera o boot fechar para mostrar as boas-vindas
        const observer = new MutationObserver(function() {
            if (bootOverlay.classList.contains("hidden")) {
                if (!chatMessages.querySelector(".mensagem")) {
                    boasVindas();
                }
                observer.disconnect();
            }
        });
        observer.observe(bootOverlay, { attributes: true, attributeFilter: ["class"] });
    }
    chatInput.focus();
});

// === renderizarHeaderUsuario(usuario) ===
// Removida em 2026-07-08: dependia de OAuth (carregarUsuarioLogado) que está
// pausado. Header mostra "Sessão aberta" estático até o auth voltar.
