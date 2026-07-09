"""
Módulo base do agente tutor.
Define a classe abstrata AgentBase que todas as disciplinas herdam.
"""

import os
import re
import json
import time
import logging

import anthropic

from src.models import Sessao, AlunoPerfil
from src.rag import retriever

logger = logging.getLogger("marcia.agente")

# Limite de mensagens no histórico enviado à API (economia de tokens)
MAX_HISTORICO = 10

# Configuração de retry
MAX_TENTATIVAS = 5
ESPERA_RETRY = 5  # segundos entre tentativas

# Timeout da chamada à API (segundos)
API_TIMEOUT = 60.0

# Configuração dos modelos
# Limites calibrados por benchmark em 2026-07-06 (scripts/benchmark_tokens.py)
# e ajustados por decisão de Victor 2026-07-06: tier simples sobe pra 12288
# (mesmo budget do Opus) e Opus sobe pra 16384 (teto seguro abaixo do limite
# de 200k do Claude). Custo sobe ~$0.03/prompt, aceitável pro foco de
# "funcionar perfeitamente primeiro, escala depois".
# Fallback de emergência (rate limit / auth error) fica em 4096 — cliente
# só atende mensagens curtas nesse modo, então budget menor basta.
MODELO_PRIMARIO = "claude-opus-4-8"
MODELO_FALLBACK = "claude-sonnet-4-6"
MAX_TOKENS_PRIMARIO = 16384
MAX_TOKENS_SIMPLES = 12288
MAX_TOKENS_FALLBACK_EMERGENCIA = 4096

# Tier dinâmico baseado na complexidade da mensagem (inspirado em padrão do
# Hermes Agent — vide docs/MEMORIAL_IA/memorial_hermes_referencia.md, padrão 5).
# "complexo" → Opus 4.8 (exercícios novos, debugging, código anexado)
# "simples"  → Sonnet 4.6 (dúvidas conceituais curtas, saudações)
MODEL_TIERS = {
    "complexo": {
        "modelo": MODELO_PRIMARIO,
        "max_tokens": MAX_TOKENS_PRIMARIO,
        "label": "Opus 4.8 High",
        "esforco": "high",
    },
    "simples": {
        "modelo": MODELO_FALLBACK,
        "max_tokens": MAX_TOKENS_SIMPLES,
        "label": "Sonnet 4.6 Medium",
        "esforco": "medium",
    },
}

# Keywords que sugerem complexidade (exercício, debugging, código anexado).
# Heurística conservadora: na dúvida → simples (false negative é preferível
# a false positive pra economizar tokens).
KEYWORDS_COMPLEXO = {
    # exercício
    "exercício", "exercicio", "lista", "questão", "questao", "problema",
    # debugging
    "erro", "depurar", "debug", "não funciona", "nao funciona", "bug",
    "por que dá erro", "tá errado", "ta errado", "conserta", "corrige",
    # código anexado (Visualg/Portugol/Python)
    "```", "var ", "se ", "para ", "enquanto ", "repita ", "funcao ",
    "def ", "import ", "print(",
    # revisão
    "revisa", "otimiza", "melhora", "refaz",
}

# Tamanho máximo de mensagem pra ainda ser considerada "simples"
LIMITE_CHARS_SIMPLES = 500

# === Detecção de sinais do perfil do aluno (heurística pura, sem LLM extra) ===
# Mapeia keyword no texto → tópico canônico pra registrar no perfil.
KEYWORDS_TOPICO = {
    # Keywords mais ESPECÍFICAS primeiro (ordem importa — primeira que casa vence)
    "recurs": "recursão",
    "vetor": "vetores",
    "matriz": "matrizes",
    "condicional": "condicionais",
    "enquanto": "loops",
    "repita": "loops",
    "while": "loops",
    "for ": "loops",
    "para ": "loops",
    "função": "funções",
    "procedim": "funções",
    "string": "strings",
    "dicion": "listas/dicionários",
    "lista": "listas/dicionários",
    "arquivo": "arquivos",
    "f-string": "python",
    "def ": "python",
    "import ": "python",
    "python": "python",
    "visu": "portugol",
    "portugol": "portugol",
}

KEYWORDS_PREFERENCIA = [
    r"prefiro\s+([^.,;]+)",
    r"gosto de\s+([^.,;]+)",
    r"melhor\s+([^.,;]+)\s+do que",
    r"seria melhor\s+([^.,;]+)",
]

KEYWORDS_TOM_FORMAL = {
    "por favor", "por gentileza", "senhor", "senhora", "gostaria", "poderia",
}
KEYWORDS_TOM_INFORMAL = {
    "mano", "cara", "véi", "tipo", "aí", "tá ligado", "vlw", "tmj", "blz",
}


# === PLANO DE ENSINO ===
# Usado pra traduzir topico_id ("alg-vetores") em título legível
# ("Vetores e Matrizes") + descrição pro tutor entender o contexto da aula.
# Cache simples em memória — plano.json raramente muda.

_PLANO_CACHE: dict | None = None


def _carregar_plano() -> dict:
    """Carrega data/plano.json com cache em memória."""
    global _PLANO_CACHE
    if _PLANO_CACHE is not None:
        return _PLANO_CACHE
    caminho = os.path.join("data", "plano.json")
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            _PLANO_CACHE = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        _PLANO_CACHE = {"topicos": []}
    return _PLANO_CACHE


def _buscar_topico_plano(topico_id: str) -> dict | None:
    """Busca dados completos de um tópico no plano.json pelo id."""
    if not topico_id:
        return None
    plano = _carregar_plano()
    for t in plano.get("topicos", []):
        if t.get("id") == topico_id:
            return t
    return None


# --- Funções de detecção de sinais (puro keyword/regex, sem LLM extra) ---

def _detectar_topico(mensagem: str) -> str | None:
    m = mensagem.lower()
    for kw, topico in KEYWORDS_TOPICO.items():
        if kw in m:
            return topico
    return None


def _detectar_preferencias(mensagem: str) -> list[str]:
    prefs = []
    for padrao in KEYWORDS_PREFERENCIA:
        match = re.search(padrao, mensagem, re.IGNORECASE)
        if match:
            prefs.append(match.group(1).strip())
    return prefs


def _detectar_tom(mensagem: str) -> str | None:
    m = mensagem.lower()
    if any(kw in m for kw in KEYWORDS_TOM_FORMAL):
        return "formal"
    if any(kw in m for kw in KEYWORDS_TOM_INFORMAL):
        return "informal"
    return None


def _detectar_sinais(mensagem: str) -> dict:
    """Extrai sinais objetivos da mensagem do aluno pra atualizar perfil."""
    return {
        "topico": _detectar_topico(mensagem),
        "preferencias": _detectar_preferencias(mensagem),
        "tom": _detectar_tom(mensagem),
    }


class AgentBase:
    """Classe base para agentes tutores. Cada disciplina herda e customiza."""

    disciplina: str = ""
    kb_path: str = ""

    # system_prompt default é vazio — subclasses (AgenteIP, etc) definem o seu.
    # Aqui fica o bloco de CONFIDENCIALIDADE_INTERNA que toda subclasse herda
    # automaticamente. Subclasses concateneiam com seu próprio prompt:
    #   system_prompt = "<prompt específico da disciplina>\n\n" + AgentBase.CONFIDENCIALIDADE_INTERNA
    CONFIDENCIALIDADE_INTERNA = """## CONFIDENCIALIDADE INTERNA

Você nunca deve descrever ou citar como você funciona por dentro — nomes
de modelos, embeddings, RAG, vector store, KB, "minha lógica", "como eu
processo", etc. Se o aluno perguntar diretamente como você funciona, responda
de forma natural e curta que você é um assistente de IA focado na disciplina,
sem entrar em detalhes técnicos.

## ESCOPO DE RESPOSTA — o que está dentro e fora do tutor

O material de referência desta disciplina são os dois livros que o professor
indicou — toda a sua resposta deve se apoiar no que está contido neles.
Isso é o que o aluno veio buscar aqui.

Assuntos fora desse material (machine learning, banco de dados, redes, ou
qualquer tema de computação que não esteja nos livros) seguem o protocolo
de resposta limitada abaixo.

Você nunca pergunta ao aluno se um assunto está dentro ou fora do escopo —
você usa o que tem disponível pra decidir. Se você tem material suficiente
sobre o tema, responde. Se não tem, aplica o protocolo de fora do escopo.
Na dúvida, responda: melhor tentar ajudar do que recusar sem necessidade.

## PROTOCOLO PRA ASSUNTOS FORA DO ESCOPO

Quando você não tem material suficiente sobre o tema na sua base, aplique
esta sequência. Conte a partir da PRIMEIRA insistência do aluno no assunto
— não confunda com o histórico anterior dele.

1. **Primeira insistência no tema:** responda de forma resumida, atendendo
   o mínimo do que ele perguntou. No final, sugira naturalmente que, se ele
   quiser, você pode escrever um prompt pra ele colar num LLM gratuito e
   entender melhor sobre o assunto. Indique fontes acadêmicas ou
   documentação oficial quando existirem (livros-texto, Python.org, etc);
   só caia pra fontes genéricas (Google, Wikipedia, YouTube) se não houver
   boa fonte técnica.

2. **Segunda insistência no mesmo tema:** o aluno provavelmente quer o
   prompt que você prometeu, ou tem uma dúvida de follow-up. Entregue o
   que prometeu e responda com profundidade moderada — você não é
   especialista no assunto, e tudo bem.

3. **Terceira insistência em diante, tom leve:** diga de forma leve que
   esse ponto foge um pouquinho do que vocês vêm trabalhando na disciplina,
   e reforce como ele pode encontrar mais conteúdo (livros da área,
   documentação oficial, ou o prompt que você sugeriu pra ele testar em
   outro LLM). Não entre em novas explicações sobre o tema.

4. **Quarta insistência em diante, tom firme:** seja direto. Diga que já
   conversaram sobre isso, que não é da disciplina, e indique uma vez onde
   o aluno pode procurar. Não entre em novas explicações nem repita
   a oferta do prompt.

Esse limite existe pra você manter qualidade: melhor dizer "isso não é meu
forte" do que inventar conteúdo que pode confundir o aluno.
"""

    system_prompt: str = CONFIDENCIALIDADE_INTERNA

    def __init__(self):
        """Inicializa clientes Anthropic (primário + fallback) com timeout."""
        api_key = os.getenv("ANTHROPIC_API_KEY")
        api_key_fallback = os.getenv("ANTHROPIC_API_KEY_FALLBACK")
        # URL custom da chave primária (ex: proxy/rota alternativa). Fallback usa a default.
        base_url_primario = os.getenv("ANTHROPIC_BASE_URL")

        if not api_key and not api_key_fallback:
            raise ValueError(
                "Nenhuma API key encontrada. Defina ANTHROPIC_API_KEY no .env"
            )

        # Cliente primário (Opus 4.8, esforço médio, 8192 tokens)
        self.clients: list = []
        if api_key:
            kwargs_primario = {"api_key": api_key, "timeout": API_TIMEOUT}
            if base_url_primario:
                kwargs_primario["base_url"] = base_url_primario
                # Proxy hudapi.cloud bloqueia 'User-Agent: Anthropic/Python X'. Sobrescreve.
                kwargs_primario["default_headers"] = {"User-Agent": "MarcIA/1.0"}
            self.clients.append({
                "client": anthropic.Anthropic(**kwargs_primario),
                "model": MODELO_PRIMARIO,
                "max_tokens": MAX_TOKENS_PRIMARIO,
            })
        # Cliente fallback (Sonnet 4.6, 1024 tokens — mais barato) — usa URL oficial.
        # Precisa forçar base_url explícito: sem isso o SDK cai no ANTHROPIC_BASE_URL
        # do ambiente (setado pro proxy hudapi.cloud da chave primária), e a chave de
        # fallback acaba sendo enviada pro proxy errado — que a rejeita (401/403).
        if api_key_fallback:
            self.clients.append({
                "client": anthropic.Anthropic(
                    api_key=api_key_fallback,
                    base_url="https://api.anthropic.com",
                    timeout=API_TIMEOUT,
                ),
                "model": MODELO_FALLBACK,
                "max_tokens": MAX_TOKENS_FALLBACK_EMERGENCIA,
            })

        # Client ativo (começa pelo primário)
        self.client_idx = 0

        # Último log populado em cada responder() — consumido por app.py pra gravar em logs.db
        self.ultimo_log: dict = {
            "complexidade": None,
            "perfil_topico": None,
            "qtd_prefs": 0,
            "qtd_topicos": 0,
            "chunks": [],
        }

    @property
    def _active(self) -> dict:
        """Retorna configuração do client ativo."""
        return self.clients[self.client_idx]

    def buscar_contexto(self, query: str) -> list[str]:
        """Busca chunks relevantes na KB via RAG (ChromaDB + sentence-transformers)."""
        return retriever.buscar(query)

    def _montar_contexto_dinamico(self, sessao: Sessao) -> str | None:
        """Monta o bloco "CONTEXTO ATUAL" injetado no system_prompt.

        Inclui:
        - Tópico ativo (titulo legível + descrição do plano.json — não o id cru)
        - Categoria do tópico na trilha
        - Linguagem escolhida pro tópico (visualg/portugol/python)
        - Ordem na trilha (pra saber o que vem antes/depois)

        Se nenhum dos dois estiver setado, retorna None (sem injeção).
        """
        topico_id = getattr(sessao, "topico_ativo", None)
        linguagem = getattr(sessao, "linguagem_topico", None)
        if not topico_id and not linguagem:
            return None

        topico_info = _buscar_topico_plano(topico_id) if topico_id else None
        partes = ["## CONTEXTO ATUAL\n"]

        if topico_info:
            titulo = topico_info.get("titulo", topico_id)
            descricao = topico_info.get("descricao", "")
            categoria = topico_info.get("categoria", "")
            ordem = topico_info.get("ordem", "")
            linguagem_obrigatoria = topico_info.get("linguagem_obrigatoria")

            partes.append(f"**Aula atual (tópico ativo):** {titulo}")
            if categoria:
                partes.append(f"- Categoria na trilha: {categoria}")
            if ordem:
                partes.append(f"- Posição na trilha: #{ordem}")
            if descricao:
                partes.append(f"- O que essa aula cobre: {descricao}")
            if linguagem_obrigatoria:
                partes.append(
                    f"- Linguagem fixa desta aula: {linguagem_obrigatoria} "
                    f"(não use outras linguagens nos exemplos)"
                )
        elif topico_id:
            # Fallback — topico_id salvo mas não bate com plano.json
            partes.append(f"Tópico ativo (id): {topico_id}")

        # Linguagem SEMPRE injetada quando existir — sem isso o tutor adivinha
        # pela categoria e erra (responder em portugol quando aluno tá em
        # py-variaveis, por exemplo). Marcada como regra absoluta.
        if linguagem:
            partes.append(
                f"- **Linguagem que você DEVE usar nos exemplos:** {linguagem}\n"
                f"  Não mostre código em outra linguagem. Se o aluno não especificar,\n"
                f"  use exatamente {linguagem}."
            )

        if linguagem or topico_info:
            partes.append(
                "\nUse essas informações pra escolher a sintaxe dos "
                "exemplos e a linguagem de programação dos blocos de código."
            )
        return "\n".join(partes)

    def _montar_query_rag(self, mensagem: str, sessao: Sessao) -> str:
        """Monta a query usada pra buscar chunks na KB via RAG.

        Hoje o RAG usa só a mensagem do aluno, que pode ser genérica demais
        ("me explica esse tema", "oi", "continua"). Quando há tópico ativo,
        priorizamos o título + descrição do tópico — o aluno está Estudando
        aquela aula, então a KB daquela aula é o que importa.

        Retorna a string final que vai pro retriever.buscar().
        """
        topico_id = getattr(sessao, "topico_ativo", None)
        if not topico_id:
            return mensagem

        topico_info = _buscar_topico_plano(topico_id)
        if not topico_info:
            return mensagem

        titulo = topico_info.get("titulo", "")
        descricao = topico_info.get("descricao", "")
        partes_query = []
        if titulo:
            partes_query.append(titulo)
        if descricao:
            partes_query.append(descricao)
        # Adiciona a mensagem do aluno como complemento (não substitui)
        if mensagem and mensagem.strip():
            partes_query.append(mensagem.strip())
        return " | ".join(partes_query)

    def _montar_messages(self, mensagem: str, sessao: Sessao, chunks: list[str], perfil: AlunoPerfil | None = None, contexto_extra: str | None = None) -> tuple[list[dict], str]:
        """Monta a lista de messages E o system_prompt estendido.

        Retorna (messages, system_prompt). O system_prompt é o self.system_prompt
        concatenado com o resumo do perfil (se houver conteúdo) e com
        `contexto_extra` (informações dinâmicas injetadas por request — ex:
        "Tópico ativo: X, Linguagem: Y").

        Por que retornar tuple em vez de mutar self: cada request é independente,
        e mutar self._system_prompt_estendido causaria race condition entre
        requests concorrentes (Flask threaded).
        """
        messages = []

        # Histórico limitado às últimas N mensagens
        historico_recente = sessao.historico[-MAX_HISTORICO:]
        for msg in historico_recente:
            role = msg.get("role", "")
            content = msg.get("content", "")
            if role in ("user", "assistant") and content:
                messages.append({"role": role, "content": content})

        # Mensagem atual do aluno (com prefixo do contexto RAG se houver chunks)
        if chunks:
            contexto = "\n---\n".join(chunks)
            conteudo = (
                f"[Contexto relevante da KB]\n{contexto}\n\n"
                f"[Pergunta do aluno]\n{mensagem}"
            )
        else:
            conteudo = mensagem

        messages.append({"role": "user", "content": conteudo})

        # System prompt: prompt base + perfil + contexto dinâmico
        system = self.system_prompt
        extras = []
        if contexto_extra:
            extras.append(contexto_extra)
        if perfil and perfil.resumo_para_prompt():
            extras.append(
                "## PERFIL DO ALUNO (continuidade — não forçar tópicos)\n"
                + perfil.resumo_para_prompt()
            )
        if extras:
            system = system + "\n\n" + "\n\n".join(extras)

        return messages, system

    def _detectar_complexidade(self, mensagem: str) -> str:
        """Classifica a mensagem em 'simples' ou 'complexo' pra escolher o tier.

        Heurística CONSERVADORA — na dúvida vai pro Opus (tier complexo).
        Nesta fase só o professor testa, então priorizamos qualidade da resposta
        sobre economia de tokens. Quando tiver alunos reais (>10), recalibrar
        pra ser mais agressivo com Sonnet.

        Regras (em ordem):
        1. Keywords de exercício/debugging/código → complexo
        2. Mensagem longa (>500 chars) → complexo
        3. Mensagem muito curta (≤10 chars, tipo "oi", "ok", "valeu") → simples
        4. Tem '?' (pergunta) → complexo (perguntas pedagógicas merecem Opus)
        5. Caso contrário → complexo (default conservador)
        """
        m = mensagem.lower()

        # 1. Keywords explícitas de complexo
        if any(kw in m for kw in KEYWORDS_COMPLEXO):
            return "complexo"

        # 2. Mensagem longa
        if len(mensagem) > LIMITE_CHARS_SIMPLES:
            return "complexo"

        # 3. Saudações/curtas demais → simples (Sonnet basta)
        if len(mensagem.strip()) <= 10:
            return "simples"

        # 4. Pergunta → complexo (default conservador pra esta fase)
        if "?" in mensagem:
            return "complexo"

        # 5. Default conservador na fase de teste → Opus
        return "complexo"

    def _extrair_texto(self, response) -> str:
        """Extrai texto da resposta da API de forma segura.

        Se stop_reason == 'max_tokens', a resposta foi TRUNCADA. Adiciona
        aviso pro aluno + log de auditoria. Antes o aluno recebia resposta
        cortada sem saber — fragilidade reportada por Victor em 2026-07-06.
        """
        if not response.content:
            return "⚠️ O tutor não gerou resposta. Tente reformular sua pergunta."
        bloco = response.content[0]
        texto = getattr(bloco, "text", None)
        if not texto:
            return "⚠️ Resposta inesperada do tutor. Tente novamente."
        # Detecta truncamento e avisa
        if getattr(response, "stop_reason", None) == "max_tokens":
            logger.warning(
                "RESPOSTA TRUNCADA: stop_reason=max_tokens, output=%s tokens",
                getattr(response.usage, "output_tokens", "?"),
            )
            texto = texto.rstrip()
            if not texto.endswith((".", "!", "?", "```")):
                texto += " [...]"
            texto += (
                "\n\n_(⚠️ resposta cortada por limite de tokens — "
                "reformule sua pergunta ou peça uma continuação)_"
            )
        return texto

    def _tentar_fallback(self) -> bool:
        """Tenta trocar para o próximo client disponível. Retorna True se conseguiu."""
        if self.client_idx + 1 < len(self.clients):
            self.client_idx += 1
            return True
        return False

    def responder(self, mensagem: str, sessao: Sessao) -> tuple[str, str]:
        """Gera resposta do tutor via API Claude. Retry em erros transitórios.

        Retorna tupla (texto_resposta, tier_label) onde tier_label é algo como
        'Opus 4.8 High' ou 'Sonnet 4.6 Medium' — usado pela UI pra mostrar
        pro aluno qual modelo respondeu.

        Perfil de continuidade: carrega perfil do aluno, injeta resumo no
        system prompt, detecta sinais da mensagem e atualiza perfil.
        """
        # Query do RAG: prioriza o tópico ativo (título + descrição) sobre
        # a mensagem crua do aluno — quando o aluno tá Estudando uma aula
        # específica, a KB daquela aula é o material relevante, não a frase
        # genérica que ele digitou ("me explica", "oi", "continua").
        query_rag = self._montar_query_rag(mensagem, sessao)
        chunks = self.buscar_contexto(query_rag)

        # 1. Carregar perfil (cria se não existir)
        perfil = AlunoPerfil.carregar_ou_criar(sessao.usuario_id)

        # 2. Detectar sinais da mensagem do aluno (best-effort)
        sinais = _detectar_sinais(mensagem)
        if sinais["topico"]:
            perfil.atualizar_topico(sinais["topico"])
        for pref in sinais["preferencias"]:
            perfil.adicionar_preferencia(pref)
        if sinais["tom"]:
            perfil.estilo_comunicacao = sinais["tom"]

        # 3. Montar messages + system_prompt (com perfil + contexto dinâmico)
        contexto_extra = self._montar_contexto_dinamico(sessao)
        messages, system_prompt = self._montar_messages(
            mensagem, sessao, chunks, perfil, contexto_extra=contexto_extra,
        )

        # 4. Escolhe tier baseado na complexidade da mensagem
        complexidade = self._detectar_complexidade(mensagem)
        tier = MODEL_TIERS[complexidade]
        # Log interno (não vai pro aluno)
        logger.info(
            "responder: tier=%s perfil_topico=%s msg_chars=%d complexidade=%s",
            tier["label"], perfil.topico_atual or "novo",
            len(mensagem), complexidade,
        )

        # Expõe métricas pra app.py gravar em logs.db (LogExecucao)
        self.ultimo_log = {
            "complexidade": complexidade,
            "perfil_topico": perfil.topico_atual,
            "qtd_prefs": len(perfil.preferencias) if perfil else 0,
            "qtd_topicos": len(perfil.topicos_explicados) if perfil else 0,
            "chunks": chunks,
        }

        tentativa = 0
        while tentativa < MAX_TENTATIVAS:
            try:
                active = self._active
                response = active["client"].messages.create(
                    model=tier["modelo"],
                    max_tokens=tier["max_tokens"],
                    system=system_prompt,
                    messages=messages,
                )
                texto = self._extrair_texto(response)

                # 5. Atualizar perfil após sucesso (registrar tópico explicado)
                if sinais["topico"]:
                    perfil.registrar_topico_explicado(sinais["topico"])
                perfil.salvar()

                return (texto, tier["label"])

            except anthropic.APITimeoutError:
                tentativa += 1
                if tentativa < MAX_TENTATIVAS:
                    time.sleep(ESPERA_RETRY)
                else:
                    return ("⚠️ O tutor demorou para responder. Tente novamente em instantes.", tier["label"])

            except anthropic.APIConnectionError:
                tentativa += 1
                if tentativa < MAX_TENTATIVAS:
                    time.sleep(ESPERA_RETRY)
                else:
                    return ("⚠️ Falha na conexão com o tutor. Verifique sua internet.", tier["label"])

            except anthropic.RateLimitError:
                tentativa += 1
                if tentativa < MAX_TENTATIVAS:
                    time.sleep(ESPERA_RETRY * 2)
                else:
                    if self._tentar_fallback():
                        tentativa = 0
                        continue
                    return ("⚠️ Muitas requisições simultâneas. Aguarde um momento e tente novamente.", tier["label"])

            except anthropic.AuthenticationError:
                if self._tentar_fallback():
                    continue
                return ("⚠️ Erro de autenticação. Verifique a API key.", tier["label"])

            except anthropic.BadRequestError as e:
                # Proxy hudapi.cloud (chave primária) devolve limite de janela
                # esgotado como 400 invalid_request_error, não 429 RateLimitError.
                # Sem esse desvio, o fallback nunca é acionado nesse caso.
                msg_lower = (e.message or "").lower()
                if "limite" in msg_lower and self._tentar_fallback():
                    tentativa = 0
                    continue
                return (f"⚠️ Erro na requisição: {e.message}", tier["label"])

            except anthropic.APIError as e:
                # Proxy hudapi.cloud pode devolver 401/403 sem o formato que o SDK
                # reconhece como AuthenticationError — cai aqui como APIError genérico.
                # Nesse caso não adianta retry na mesma chave: troca pro fallback direto.
                status_code = getattr(e, "status_code", None)
                if status_code in (401, 403) and self._tentar_fallback():
                    tentativa = 0
                    continue
                tentativa += 1
                if tentativa < MAX_TENTATIVAS:
                    time.sleep(ESPERA_RETRY)
                else:
                    return (f"⚠️ Erro ao conectar com o tutor: {e.message}", tier["label"])

            except Exception:
                return ("⚠️ Ocorreu um erro inesperado. Tente novamente em instantes.", tier["label"])

        return ("⚠️ Não foi possível obter resposta. Tente novamente.", tier["label"])
