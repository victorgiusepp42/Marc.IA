# Cronograma Revisado — Marc.IA

**Atualizado:** 22/06/2026
**Baseado em:** PRD, ADR, SDD (docs/)

---

## Visao Geral de Entregas

| Entrega | Data | Tipo | Foco |
|---|---|---|---|
| E2 | 25/06/2026 | Checkpoint (progresso) | App funcional + docs do planejamento |
| E3 | ~10/07/2026 | Final (nota) | Produto completo + apresentacao Mostra |

---

## Epicos

### FUND — Fundacao

**Descricao:** Preparar todo o ambiente de desenvolvimento — Python, Git, estrutura de pastas, venv, dependencias. Eh a base sobre a qual tudo roda. Sem isso, ninguem consegue codar.

**Responsavel:** Victor

---

### DEC — Decisoes

**Descricao:** Tomar e registrar decisoes tecnicas que afetam todo o projeto — qual modelo de IA usar, como autenticar, onde persistir dados. Cada decisao vira um ADR documentado.

**Responsavel:** Victor

---

### NUC — Nucleo

**Descricao:** Modulos centrais que sustentam a aplicacao — gerenciamento de sessao do aluno, conexao com banco de dados (SQLAlchemy), calculo de progresso/XP, e carregamento da rota de topicos. Eh o backend core.

**Responsavel:** Victor + Kevynson

---

### AUTH — Autenticacao

**Descricao:** Implementar login via Google OAuth 2.0 para que o aluno entre com sua conta @discente.ufcat.edu.br. Isso permite persistir progresso entre sessoes e devices, e vincular metricas ao usuario.

**Responsavel:** Kevynson

**Aprendizado necessario:** Se nunca implementou OAuth, use este prompt na IA:
> "Explique passo a passo como implementar Google OAuth 2.0 em Flask usando Authlib e Flask-Login. Inclua: como criar credenciais no Google Cloud Console, configurar redirect URI, e proteger rotas com login_required."

---

### AGE — Agentes

**Descricao:** Implementar a camada de IA — classe base abstrata (AgentBase) que se comunica com a API Claude, e a implementacao concreta (AgenteIP) que eh o tutor de Introducao a Programacao. Inclui logica de retry, fallback, montagem de prompt com historico e RAG.

**Responsavel:** Victor + Natan

**Aprendizado necessario:** Se nunca usou a API da Anthropic, use este prompt:
> "Me ensine a usar a SDK Python da Anthropic (anthropic). Quero: criar um client, enviar mensagens com system prompt, usar historico de conversa, configurar model e max_tokens, e tratar erros/timeouts com retry."

---

### CONT — Conteudo

**Descricao:** Criar todo o conteudo que alimenta a plataforma — rota de topicos (plano.json), banco de exercicios (exercicios.json), e materiais da knowledge base (TXTs do professor para o RAG).

**Responsavel:** Natan

---

### RAG — Retrieval-Augmented Generation

**Descricao:** Implementar busca semantica nos materiais do professor. O indexador le os TXTs, divide em chunks, gera embeddings e salva no ChromaDB. O retriever busca os chunks mais relevantes para cada pergunta do aluno e injeta no prompt.

**Responsavel:** Victor + Natan

**Aprendizado necessario:** Se nunca trabalhou com RAG, use este prompt:
> "Explique RAG (Retrieval-Augmented Generation) de forma pratica. Quero implementar em Python: 1) ler arquivos TXT, 2) dividir em chunks de 500 tokens com overlap, 3) gerar embeddings com sentence-transformers (all-MiniLM-L6-v2), 4) salvar no ChromaDB, 5) buscar top-3 chunks por query. Me de o codigo completo."

---

### FRO — Front-end

**Descricao:** Interface web com visual retro 8-bit — pagina unica com chat, painel de rota lateral, barra de XP/nivel, e componentes de exercicio/feedback. HTML + CSS + JS vanilla, sem framework.

**Responsavel:** Diogo

---

### MET — Metricas

**Descricao:** Coletar dados de satisfacao e uso — feedback por resposta (like/dislike), NPS ("recomendaria?"), e Sean Ellis test ("se parasse de existir?"). Salvar no banco vinculado ao usuario.

**Responsavel:** Kevynson

---

### QA — Quality Assurance

**Descricao:** Garantir qualidade do codigo com testes automatizados (pytest), validacao de input, e coverage minimo de 50%. Inclui mock da API Claude pra nao gastar tokens em teste.

**Responsavel:** Natan

**Aprendizado necessario:** Se nunca usou pytest, use este prompt:
> "Me ensine pytest do zero para um projeto Flask. Quero: criar fixtures para o app Flask, mockar chamadas HTTP externas (API Claude) com unittest.mock, rodar testes com coverage, e gerar relatorio. Me de exemplos praticos."

---

### MOS — Deploy (Mostra)

**Descricao:** Colocar a aplicacao no ar via Railway — configurar deploy automatico via GitHub, provisionar PostgreSQL, configurar variaveis de ambiente, e garantir que a URL publica funciona na Mostra UFCAT.

**Responsavel:** Kevynson

**Aprendizado necessario:** Se nunca usou Railway, use este prompt:
> "Como fazer deploy de uma aplicacao Flask no Railway? Inclua: criar projeto, conectar repo GitHub, configurar variavel DATABASE_URL com addon PostgreSQL, adicionar variaveis de ambiente, e configurar Procfile."

---

### DOC — Documentacao

**Descricao:** Produzir todos os entregaveis academicos — relatorios, documentacao tecnica (3-5 paginas), README completo, poster A1 para Mostra, e videos demonstrativos.

**Responsavel:** Todos

---

## Sprint 1 Revisada (18-25/06) — Walking Skeleton + E2

**Objetivo:** App rodando local com chat funcional. E2 entregue (checkpoint de progresso).

### Tarefas Concluidas

| ID | Tarefa | Status |
|---|---|---|
| FUND-01 | venv + .gitignore | Feito |
| FUND-02 | requirements.txt | Feito |
| DEC-01 | Definir modelo API | Feito |
| DEC-02 | API key com billing | Feito |
| CONT-01 | plano.json | Feito |
| FRO-01 | index.html | Feito |
| FRO-02 | style.css | Feito |
| FRO-03 | chat.js | Feito |
| NUC-02 | app.py minimo | Feito |
| AGE-01 | AgentBase | Feito |
| AGE-02 | AgenteIP | Feito |
| AGE-03 | Integracao app-agente | Feito |
| NUC-01 | Classe Sessao | Feito (versao JSON, migra na Sprint 2) |

---

### Pendentes Sprint 1 (22-25/06)

---

#### DOC-01: Relatorio E2

**Prioridade:** P0 (obrigatorio para entrega)

**Descricao:** Criar um PDF de 1 pagina resumindo o projeto para o checkpoint do professor. Deve conter: problema identificado, solucao proposta, arquitetura escolhida, status atual, e proximos passos.

**Passo a passo:**
1. Abrir o PRD.md e extrair: problema (secao 2), diferencial (secao 4), arquitetura (secao 8)
2. Escrever 1 pagina em formato academico (introducao, desenvolvimento, conclusao)
3. Incluir 1 screenshot do app rodando
4. Exportar como PDF (pode usar pandoc ou Google Docs)
5. Salvar em docs/relatorio_e2.pdf

**Criterio de aceite:** PDF de 1 pagina entregue com problema + solucao + arquitetura + status.

---

#### DOC-02: Video E2

**Prioridade:** P0 (obrigatorio para entrega)

**Descricao:** Gravar video de 1-3 minutos demonstrando o app funcionando. Mostrar: abrir no browser, enviar pergunta, receber resposta do tutor, painel de rota visivel.

**Passo a passo:**
1. Rodar python app.py no terminal
2. Abrir http://localhost:5001 no browser
3. Iniciar gravacao de tela (OBS Studio ou Win+G no Windows)
4. Demonstrar: enviar 2-3 perguntas variadas sobre Python
5. Mostrar painel de rota com topicos
6. Encerrar e exportar em formato mp4 (max 50MB)

**Criterio de aceite:** Video de 1-3min mostrando chat funcional + rota.

---

#### AGE-04: Historico no prompt

**Prioridade:** P1

**Descricao:** Fazer o agente enviar as ultimas 10 mensagens da conversa junto com a nova pergunta para a API Claude. Isso permite que o tutor tenha contexto do que ja foi discutido e nao repita informacoes.

**Passo a passo:**
1. Abrir src/agente_base.py
2. No metodo _montar_messages(), pegar sessao.historico[-10:] (ultimas 10)
3. Formatar como lista de dicts [{role: "user", content: "..."}, {role: "assistant", content: "..."}]
4. Adicionar a mensagem atual no final
5. Passar essa lista completa no parametro messages= da API
6. Testar: enviar 2 perguntas seguidas e verificar se a 2a resposta leva em conta a 1a

**Criterio de aceite:** Ultimas 10 mensagens incluidas no messages[] enviado a API.

---

#### NUC-04: Rota loader

**Prioridade:** P1

**Descricao:** Criar endpoint GET /rota que le data/plano.json e retorna a lista de topicos para o front-end renderizar no painel lateral.

**Passo a passo:**
1. Criar src/rota_loader.py com funcao carregar_rota()
2. Ler data/plano.json usando json.load()
3. Retornar lista de topicos com id, titulo, descricao
4. Em app.py, criar rota GET /rota que chama carregar_rota() e retorna jsonify()
5. Testar: acessar http://localhost:5001/rota no browser e verificar JSON

**Criterio de aceite:** GET /rota retorna topicos de plano.json como JSON.

---

#### FRO-04: Painel rota dinamico

**Prioridade:** P2

**Descricao:** Fazer o painel lateral de topicos carregar dinamicamente do endpoint /rota ao inves de ser HTML estatico. Cada topico deve mostrar status visual.

**Passo a passo:**
1. Em chat.js, no carregamento da pagina, fazer fetch("/rota")
2. Com o JSON retornado, renderizar lista de topicos no painel lateral
3. Cada topico mostra: titulo + icone de status (circulo vazio, seta, check)
4. Por enquanto todos com status "nao iniciado" (circulo vazio) — Sprint 2 ativa progresso real
5. Testar: recarregar pagina e verificar que topicos carregam do servidor

**Criterio de aceite:** Topicos carregam de GET /rota com status visual.

---

## Sprint 2 (26/06-03/07) — Core Features

**Objetivo:** RAG funcional + banco de dados + exercicios + navegacao livre.

---

### Bloco A: Banco de Dados (26-27/06)

---

#### NUC-06: SQLAlchemy setup

**Descricao:** Configurar SQLAlchemy como ORM da aplicacao. Criar os models (Usuario, SessaoEstudo, Feedback, Metrica), configurar engine que le DATABASE_URL do .env, e criar as tabelas automaticamente no boot.

**Passo a passo:**
1. Adicionar sqlalchemy e flask-sqlalchemy no requirements.txt
2. Criar src/database.py
3. Configurar engine: ler DATABASE_URL do os.environ (default: sqlite:///data/marcia.db)
4. Definir models conforme SDD secao 3.3 (Usuario, SessaoEstudo, Feedback, Metrica)
5. Em app.py, importar db e chamar db.create_all() no startup
6. Testar: rodar app, verificar que data/marcia.db eh criado com as tabelas
7. Adicionar data/marcia.db no .gitignore

**Criterio de aceite:** Models criados, tabelas geradas no boot, DATABASE_URL configuravel.

**Aprendizado necessario:**
> "Me ensine a configurar SQLAlchemy com Flask. Quero: definir models com db.Model, configurar DATABASE_URL para funcionar com SQLite local e PostgreSQL em producao, e criar tabelas automaticamente. Mostre o padrao completo com db.create_all()."

---

#### NUC-07: Migrar Sessao para banco

**Descricao:** Refatorar a classe Sessao para ler/salvar via SQLAlchemy ao inves de arquivos JSON. O google_id do usuario vira a chave. Historico de mensagens fica como campo JSON no banco.

**Passo a passo:**
1. Abrir src/sessao.py
2. Remover logica de json.load/json.dump de arquivo
3. Importar db e SessaoEstudo de src/database
4. Em carregar(): fazer query SessaoEstudo.query.filter_by(usuario_id=id).first()
5. Em salvar(): fazer db.session.commit()
6. Em adicionar_mensagem(): append no campo historico (lista JSON)
7. Manter interface publica identica (adicionar_mensagem, salvar, carregar, adicionar_xp)
8. Testar: enviar mensagem no chat, verificar que aparece no banco (usar DB Browser for SQLite)

**Criterio de aceite:** Sessao le/salva via SQLAlchemy. Interface publica nao muda.

---

#### NUC-05: Progresso (XP/nivel)

**Descricao:** Implementar logica de calculo de nivel a partir de XP acumulado. Definir faixas (Aprendiz 0-499, Intermediario 500-999, Avancado 1000-1999, Mestre 2000+) e persistir no banco.

**Passo a passo:**
1. Criar src/progresso.py
2. Definir funcao calcular_nivel(xp: int) -> tuple[int, str] que retorna (nivel_num, nivel_nome)
3. Usar if/elif para as faixas de XP (atende requisito de if/elif/else da rubrica)
4. Definir constantes XP_POR_MENSAGEM=5, XP_EXERCICIO_CORRETO=50, XP_EXERCICIO_PARCIAL=20, XP_TOPICO=100
5. Integrar com Sessao: quando adicionar_xp() eh chamado, recalcular nivel
6. Testar: simular XP crescente e verificar que nivel muda nos pontos corretos

**Criterio de aceite:** Calcula nivel a partir de XP, persiste no banco, usa if/elif/else.

---

### Bloco B: Autenticacao (27-28/06)

---

#### DEC-03: Google Cloud OAuth credentials

**Descricao:** Criar projeto no Google Cloud Console e obter Client ID + Client Secret para OAuth 2.0. Configurar tela de consentimento e redirect URIs.

**Passo a passo:**
1. Acessar https://console.cloud.google.com
2. Criar projeto "Marc-IA" (ou selecionar existente)
3. Ir em APIs e Servicos > Credenciais
4. Configurar Tela de consentimento OAuth: tipo Externo, nome "Marc.IA", email de suporte
5. Criar credencial "ID do cliente OAuth": tipo Aplicativo Web
6. Adicionar URI de redirecionamento: http://localhost:5001/login/callback
7. Copiar Client ID e Client Secret
8. Adicionar no .env: GOOGLE_CLIENT_ID=... e GOOGLE_CLIENT_SECRET=...
9. Adicionar redirect URI do Railway quando deploy estiver pronto (Sprint 3)

**Criterio de aceite:** Client ID + Secret funcionais, redirect URI configurada.

**Aprendizado necessario:**
> "Me guie passo a passo para criar credenciais OAuth 2.0 no Google Cloud Console para uma aplicacao Flask. Quero entender: o que eh a tela de consentimento, como configurar redirect URIs para dev local e producao, e quais scopes pedir (email, profile, openid)."

---

#### AUTH-01: OAuth config

**Descricao:** Configurar a lib Authlib no Flask para se comunicar com o Google OAuth. Definir scopes, redirect URI, e endpoints do Google.

**Passo a passo:**
1. Adicionar authlib no requirements.txt
2. Em src/auth.py, importar OAuth de authlib.integrations.flask_client
3. Registrar provider "google" com: client_id, client_secret, authorize_url, token_url, scopes
4. Configurar server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"
5. Testar: chamar oauth.google.authorize_redirect() e verificar que redireciona pro Google

**Criterio de aceite:** Redirect URI configurada, scopes definidos, redirecionamento funciona.

---

#### AUTH-02: Flask-Login + Authlib

**Descricao:** Implementar rotas /login, /login/callback, e /logout. Integrar Flask-Login para gerenciar sessao autenticada com cookie seguro.

**Passo a passo:**
1. Adicionar flask-login no requirements.txt
2. Em src/auth.py, configurar LoginManager
3. Criar rota GET /login: chama oauth.google.authorize_redirect(redirect_uri)
4. Criar rota GET /login/callback: recebe token, extrai userinfo (email, name, sub)
5. Criar rota GET /logout: chama logout_user() e redireciona pra /login
6. Implementar user_loader que busca usuario no banco por ID
7. Em app.py, proteger rotas com @login_required (GET /, POST /chat, GET /rota)
8. Testar: acessar / sem login -> redireciona pra Google -> volta autenticado

**Criterio de aceite:** Login/logout funcional, rotas protegidas, cookie seguro.

---

#### AUTH-03: Sessao por google_id

**Descricao:** Quando o usuario loga pela primeira vez, criar registro na tabela usuarios. Em logins seguintes, carregar o usuario existente. Vincular a SessaoEstudo ao usuario.

**Passo a passo:**
1. No callback do OAuth, extrair google_id (campo "sub" do userinfo)
2. Buscar Usuario.query.filter_by(google_id=sub).first()
3. Se nao existe: criar Usuario(google_id=sub, nome=name, email=email)
4. Se existe: atualizar ultimo_acesso (opcional)
5. Chamar login_user(usuario) do Flask-Login
6. Em /chat, usar current_user.id para carregar a SessaoEstudo correta
7. Testar: logar com 2 contas Google diferentes, verificar que progresso eh separado

**Criterio de aceite:** Usuario criado/carregado no login, vinculado a sessao de estudo.

---

### Bloco C: RAG (28-30/06)

---

#### CONT-03: KB materiais IP

**Descricao:** Reunir e preparar os materiais do professor de Introducao a Programacao para alimentar o RAG. Converter PDFs/slides em TXT limpo, organizar por topico.

**Passo a passo:**
1. Coletar materiais do Drive: listas de exercicios, correcoes de prova, slides, resumos
2. Para cada material, extrair texto limpo (copiar/colar ou usar ferramenta de conversao)
3. Salvar como .txt em data/kb_ip/ com nome descritivo (ex: lista01_variaveis.txt, correcao_prova1.txt)
4. Garantir minimo 5 arquivos com conteudo relevante
5. Revisar: remover lixo de formatacao, manter so conteudo util
6. Nao incluir gabaritos puros — incluir explicacoes e raciocinio

**Criterio de aceite:** 5+ arquivos .txt em data/kb_ip/ com conteudo real da disciplina.

---

#### RAG-01: Indexador

**Descricao:** Criar script que le todos os TXTs da KB, divide em chunks de ~500 tokens com overlap de 50, gera embeddings usando sentence-transformers, e salva numa colecao do ChromaDB.

**Passo a passo:**
1. Adicionar chromadb e sentence-transformers no requirements.txt
2. Criar src/rag/indexador.py
3. Funcao carregar_documentos(): le todos os .txt de data/kb_ip/ com open()
4. Funcao chunkar(texto, tamanho=500, overlap=50): divide texto em pedacos (usar split por paragrafos ou por tokens)
5. Funcao indexar(): para cada chunk, gerar embedding e adicionar ao ChromaDB
6. Usar ChromaDB com PersistentClient (salva em data/chroma_db/)
7. Criar colecao "kb_ip" com embedding function = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
8. Rodar uma vez: python -m src.rag.indexador (cria o indice)
9. Testar: verificar que a colecao tem N documentos indexados

**Criterio de aceite:** Le kb_ip/, chunka, gera embeddings, salva no ChromaDB.

**Aprendizado necessario:**
> "Me ensine a usar ChromaDB com Python. Quero: criar um PersistentClient, criar uma colecao com SentenceTransformerEmbeddingFunction, adicionar documentos com metadados, e fazer query por similaridade retornando top-k resultados. Codigo completo com exemplos."

---

#### RAG-02: Retriever

**Descricao:** Criar modulo que recebe a pergunta do aluno, busca os 3 chunks mais similares no ChromaDB, e retorna como lista de strings para injetar no prompt.

**Passo a passo:**
1. Criar src/rag/retriever.py
2. Classe Retriever com __init__ que conecta ao ChromaDB (PersistentClient) e carrega colecao "kb_ip"
3. Metodo buscar(query: str, top_k: int = 3) -> list[str]
4. Internamente: collection.query(query_texts=[query], n_results=top_k)
5. Retornar lista de documents (textos dos chunks)
6. Tratar caso de colecao vazia (retorna lista vazia)
7. Testar: chamar buscar("o que eh uma variavel") e verificar que retorna chunks relevantes

**Criterio de aceite:** Busca top-3 chunks por query, retorna texto.

---

#### RAG-03: Integracao RAG com Agente

**Descricao:** Conectar o Retriever ao AgentBase para que todo responder() busque contexto relevante antes de chamar a API. Os chunks sao injetados no system prompt ou como mensagem de contexto.

**Passo a passo:**
1. Em src/agente_base.py, no __init__(), instanciar self.retriever = Retriever() (ou None se KB nao existe)
2. No metodo buscar_contexto(query): chamar self.retriever.buscar(query) se disponivel
3. No metodo _montar_messages(): se chunks existem, adicionar antes da mensagem do usuario:
   - Opcao A: incluir no system_prompt como "Contexto da disciplina: ..."
   - Opcao B: adicionar como mensagem role="user" com prefixo "[Contexto]: ..."
4. Garantir que funciona sem RAG (fallback graceful — se retriever eh None, pula)
5. Testar: fazer pergunta que esta nos materiais e verificar que resposta usa o contexto

**Criterio de aceite:** buscar_contexto() usa Retriever, chunks injetados no prompt. Funciona sem RAG tambem.

---

### Bloco D: Exercicios + Navegacao (01-03/07)

---

#### CONT-02: exercicios.json

**Descricao:** Criar banco de exercicios em JSON com minimo 5 exercicios por topico. Cada exercicio tem enunciado, tipo (multipla_escolha, resposta_curta, codigo), e resposta esperada.

**Passo a passo:**
1. Abrir data/plano.json e listar os 10 topicos
2. Para cada topico, criar 5+ exercicios variados
3. Formato por exercicio: {topico_id, id, enunciado, tipo, opcoes (se multipla escolha), resposta, explicacao}
4. Tipos: "multipla_escolha" (com campo opcoes[]), "resposta_curta" (texto livre), "codigo" (output esperado)
5. Salvar em data/exercicios.json
6. Validar: JSON valido (usar python -m json.tool data/exercicios.json)

**Criterio de aceite:** 5+ exercicios por topico, formato padronizado, JSON valido.

---

#### EXE-01: Validacao exercicios

**Descricao:** Criar modulo que carrega exercicios do JSON, seleciona por topico, compara resposta do aluno com a esperada, e retorna resultado (certo/parcial/errado) + XP ganho.

**Passo a passo:**
1. Criar src/exercicios.py
2. Funcao carregar_exercicios(topico_id: str) -> list[dict]: filtra por topico
3. Funcao selecionar_exercicio(topico_id: str) -> dict: retorna 1 aleatorio do topico
4. Funcao validar_resposta(exercicio: dict, resposta_aluno: str) -> dict:
   - Se tipo == "multipla_escolha": comparacao exata com resposta correta
   - Se tipo == "resposta_curta": comparacao case-insensitive, strip whitespace
   - Se tipo == "codigo": comparacao do output (flexivel)
5. Retornar {correto: bool, parcial: bool, xp_ganho: int, explicacao: str}
6. Usar for/while para iterar exercicios (atende rubrica de loops)
7. Testar: validar respostas certas e erradas pra cada tipo

**Criterio de aceite:** Compara resposta, retorna certo/parcial/errado + XP. Usa for/while.

---

#### AGE-05: Prompt adaptativo

**Descricao:** Atualizar o system_prompt do AgenteIP para incluir: topico ativo do aluno, logica de quando entregar/nao entregar resposta, e instrucoes de propor exercicios.

**Passo a passo:**
1. Abrir src/agente_ip.py
2. Refatorar system_prompt para ser dinamico (metodo que monta com base no topico ativo)
3. Incluir no prompt:
   - Persona: PyAI Professor, paciente, didatico
   - Topico ativo: nome + descricao (vem da sessao)
   - Regra 1: Tente ensinar sem dar resposta (perguntas guiadas, dicas)
   - Regra 2: Se aluno pede resposta diretamente, de sem resistencia + explique + sugira exercicio
   - Regra 3: Se aluno travou apos varias tentativas, entregue + explique + proponha exercicio novo
   - Regra 4: Exercicio sugerido pode ser recusado pelo aluno
4. Usar f-string ou .format() para injetar topico dinamicamente
5. Testar: mudar topico ativo e verificar que resposta muda de contexto

**Criterio de aceite:** system_prompt inclui topico ativo + logica adaptativa de entrega de respostas.

---

#### FRO-05: Exercicio inline

**Descricao:** Implementar componente no chat que exibe exercicio proposto pelo tutor, coleta resposta do aluno, envia para validacao, e mostra feedback visual (certo/errado + XP ganho).

**Passo a passo:**
1. Em app.py, criar rota POST /exercicio/validar que recebe {exercicio_id, resposta}
2. Chamar validar_resposta() de src/exercicios.py
3. Retornar JSON {correto, parcial, xp_ganho, explicacao}
4. Em chat.js, quando tutor propoe exercicio, renderizar card especial (nao bolha normal)
5. Card tem: enunciado, campo de resposta, botao "Enviar resposta"
6. Ao submeter: fetch /exercicio/validar, mostrar resultado com animacao de XP
7. Atualizar sidebar com novo XP/nivel
8. Testar: completar exercicio certo e errado, verificar feedback e XP

**Criterio de aceite:** Exibe exercicio, coleta resposta, mostra feedback + XP.

---

#### FRO-04b: Navegacao livre na rota

**Descricao:** Permitir que o aluno clique em qualquer topico da rota (nao apenas o proximo). Ao clicar, o tutor muda o contexto para aquele topico. Aluno pode pular, voltar, avancar.

**Passo a passo:**
1. Em chat.js, tornar cada topico no painel lateral clicavel
2. Ao clicar: enviar requisicao para atualizar topico_ativo na sessao
3. Em app.py, criar rota POST /rota/selecionar {topico_id}
4. Atualizar sessao.topico_ativo no banco
5. Front-end: destacar topico ativo com estilo diferente (borda amarela, icone seta)
6. Proxima mensagem do tutor ja usa o novo contexto do topico
7. Nenhum topico eh bloqueado — todos clicaveis desde o inicio
8. Testar: clicar topico 5 sem ter feito 1-4, verificar que funciona

**Criterio de aceite:** Aluno pode clicar qualquer topico. Sem bloqueios.

---

## Sprint 3 (04-10/07) — Polimento + Deploy + Mostra

**Objetivo:** Produto pronto pra nota maxima. Deploy publico. Documentacao final.

---

### Bloco A: Metricas e Feedback (04-05/07)

---

#### MET-01: Feedback por resposta

**Descricao:** Adicionar botoes de like/dislike em cada resposta do tutor. Ao clicar, salvar no banco vinculado ao usuario e a sessao. Isso alimenta a metrica de qualidade do tutor.

**Passo a passo:**
1. Em chat.js, ao renderizar bolha do assistant, adicionar 2 botoes pequenos (polegar pra cima/baixo)
2. Ao clicar: fetch POST /feedback {sessao_id, mensagem_idx, tipo: "like"|"dislike"}
3. Em app.py, criar rota POST /feedback
4. Salvar no model Feedback (usuario_id, sessao_id, tipo, criado_em)
5. Desabilitar botoes apos clique (evitar duplicata)
6. Estilizar botoes no visual 8-bit (pequenos, nao intrusivos)
7. Testar: clicar like/dislike, verificar registro no banco

**Criterio de aceite:** Botao em cada resposta, salva no banco, vinculado ao usuario.

---

#### MET-02: NPS + Sean Ellis

**Descricao:** A cada N sessoes (ex: 5), exibir modal perguntando NPS ("De 0-10, recomendaria?") e Sean Ellis ("Se parasse de existir, como se sentiria?"). Salvar na tabela metricas.

**Passo a passo:**
1. Em app.py, ao carregar sessao, contar total de sessoes do usuario
2. Se total_sessoes % 5 == 0 e nao respondeu nesta sessao: flag mostrar_pesquisa=true
3. Retornar flag no JSON de resposta do /chat
4. Em chat.js, se flag=true, exibir modal com:
   - Pergunta 1: slider 0-10 (NPS)
   - Pergunta 2: radio (muito desapontado / um pouco / indiferente)
5. Ao submeter: fetch POST /metricas {tipo: "nps", valor: N} e {tipo: "sean_ellis", valor: X}
6. Em app.py, salvar no model Metrica
7. Modal pode ser fechado sem responder (nao obrigatorio)
8. Testar: simular 5 sessoes, verificar que modal aparece

**Criterio de aceite:** Prompt a cada N sessoes, salvo na tabela metricas, nao obrigatorio.

---

#### FRO-06: UI de feedback

**Descricao:** Estilizar os componentes de feedback (botoes like/dislike e modal NPS) no visual 8-bit consistente com o resto da interface.

**Passo a passo:**
1. Botoes like/dislike: icones pixel art pequenos, cor neutra, hover com amarelo
2. Modal NPS: fundo escuro semi-transparente, caixa central com borda pixel
3. Slider: estilizado com CSS custom (thumb quadrado, track com borda)
4. Radio buttons: custom com quadrados 8-bit ao inves de circulos
5. Botao fechar modal: X pixelado no canto
6. Responsivo: modal centralizado em qualquer tamanho de tela
7. Testar: verificar que visual eh consistente com style.css existente

**Criterio de aceite:** Feedback visual 8-bit, nao intrusivo, consistente.

---

### Bloco B: QA (05-07/07)

---

#### QA-01: pytest + conftest

**Descricao:** Configurar pytest para o projeto. Criar conftest.py com fixtures reutilizaveis — app Flask de teste, client HTTP, mock da API Claude (para nao gastar tokens).

**Passo a passo:**
1. Adicionar pytest e pytest-cov no requirements.txt
2. Criar tests/__init__.py (vazio)
3. Criar tests/conftest.py com:
   - Fixture app(): cria app Flask com config de teste (DATABASE_URL=sqlite:///:memory:)
   - Fixture client(): retorna app.test_client()
   - Fixture mock_claude(): usa unittest.mock.patch para mockar anthropic.Anthropic.messages.create
   - Mock retorna resposta fixa: {content: [{text: "Resposta mockada"}]}
4. Criar pytest.ini ou pyproject.toml com config basica (testpaths = tests)
5. Testar: rodar pytest -v e verificar que descobre os testes

**Criterio de aceite:** Fixtures funcionais, mock da API Claude, pytest roda.

**Aprendizado necessario:**
> "Me ensine a configurar pytest para um projeto Flask com SQLAlchemy. Quero: fixtures com app de teste usando banco in-memory, test_client para testar rotas, e como mockar chamadas externas (API da Anthropic) com unittest.mock.patch. Codigo completo do conftest.py."

---

#### QA-02: Testes unitarios

**Descricao:** Escrever testes para os modulos principais ate atingir 50%+ de coverage. Priorizar: sessao, progresso, exercicios, validacao, rotas.

**Passo a passo:**
1. Criar tests/test_sessao.py: testar criar, salvar, carregar, adicionar_mensagem, adicionar_xp
2. Criar tests/test_progresso.py: testar calcular_nivel em todas as faixas
3. Criar tests/test_exercicios.py: testar validar_resposta para cada tipo
4. Criar tests/test_validacao.py: testar sanitizacao, limite tamanho, vazio
5. Criar tests/test_rotas.py: testar GET /, GET /rota, POST /chat (com mock)
6. Rodar: pytest --cov=src --cov-report=term-missing
7. Verificar que coverage >= 50%
8. Se < 50%, adicionar testes nos modulos com menor cobertura

**Criterio de aceite:** 50%+ coverage em src/, testes passam.

---

#### QA-03: Validacao input

**Descricao:** Implementar modulo de sanitizacao que valida e limpa toda entrada do usuario antes de processar. Previne XSS, limita tamanho, trata vazios.

**Passo a passo:**
1. Criar src/validacao.py
2. Funcao sanitizar(texto: str) -> str:
   - Strip whitespace
   - Remover tags HTML (usar html.escape ou regex simples)
   - Limitar a 2000 caracteres (truncar)
3. Funcao validar_mensagem(texto: str) -> tuple[bool, str]:
   - Se vazio apos strip: return (False, "Mensagem vazia")
   - Se > 2000 chars: return (False, "Mensagem muito longa")
   - Se so whitespace: return (False, "Mensagem vazia")
   - Senao: return (True, sanitizar(texto))
4. Em app.py no POST /chat, chamar validar_mensagem() antes de processar
5. Usar try/except no entorno (atende rubrica)
6. Testar: enviar mensagem vazia, gigante, com HTML, com script tag

**Criterio de aceite:** Sanitiza HTML, limita tamanho, trata vazio. Usa try/except.

---

### Bloco C: Deploy (07-08/07)

---

#### MOS-01: Deploy Railway

**Descricao:** Configurar deploy automatico da aplicacao no Railway via GitHub. App deve estar acessivel por URL publica.

**Passo a passo:**
1. Criar conta no Railway (railway.app) se nao tiver
2. Criar novo projeto, conectar ao repo GitHub (victorgiusepp42/Marc.IA)
3. Railway detecta Python automaticamente
4. Criar Procfile na raiz: web: python app.py (ou usar gunicorn em prod)
5. Configurar porta: Railway injeta PORT env var, app.py deve ler: port = int(os.environ.get("PORT", 5001))
6. Fazer push no GitHub — Railway faz deploy automatico
7. Verificar URL publica (ex: marcia.up.railway.app)
8. Testar: acessar URL no browser e verificar que chat funciona

**Criterio de aceite:** App acessivel via URL publica, deploy automatico via GitHub push.

**Aprendizado necessario:**
> "Como fazer deploy de app Flask no Railway com deploy automatico via GitHub? Inclua: Procfile, como ler a variavel PORT, e como usar gunicorn em producao. Tambem explique como adicionar um addon PostgreSQL gratuito."

---

#### MOS-02: PostgreSQL Railway

**Descricao:** Provisionar addon PostgreSQL no Railway e configurar DATABASE_URL para que a aplicacao use banco persistente em producao.

**Passo a passo:**
1. No painel Railway, clicar "New" > "Database" > PostgreSQL
2. Copiar a variavel DATABASE_URL gerada pelo Railway
3. Em app.py/database.py, garantir que le DATABASE_URL do ambiente
4. Railway injeta automaticamente se o addon esta linkado ao servico
5. Fazer deploy e verificar que tabelas sao criadas (db.create_all())
6. Testar: criar conta via Google OAuth no deploy, verificar que dados persistem entre deploys

**Criterio de aceite:** PostgreSQL provisionado, dados persistem entre deploys.

---

#### MOS-03: Variaveis de ambiente Railway

**Descricao:** Configurar todas as variaveis de ambiente necessarias no Railway para que a aplicacao funcione em producao.

**Passo a passo:**
1. No painel Railway > Settings > Variables, adicionar:
   - ANTHROPIC_API_KEY=sk-ant-...
   - GOOGLE_CLIENT_ID=...
   - GOOGLE_CLIENT_SECRET=...
   - SECRET_KEY=... (gerar com python -c "import secrets; print(secrets.token_hex(32))")
   - DATABASE_URL (ja configurada pelo addon PostgreSQL)
2. Adicionar redirect URI de producao no Google Cloud Console
3. Fazer redeploy apos configurar variaveis
4. Testar: login com Google funciona na URL publica

**Criterio de aceite:** Todas as env vars configuradas, app funciona em producao.

---

### Bloco D: Documentacao Final (08-10/07)

---

#### DOC-03: README final

**Descricao:** Reescrever README.md com todas as informacoes necessarias para qualquer pessoa instalar, rodar e entender o projeto.

**Passo a passo:**
1. Estrutura: Sobre | Problema | Solucao | Screenshots | Instalacao | Uso | Arquitetura | Tech Stack | Equipe | Licenca
2. Incluir badges (Python version, License)
3. Secao Instalacao: passo a passo clone > venv > pip install > .env > python app.py
4. Secao Uso: como logar, como usar o chat, como navegar na rota
5. Incluir 2-3 screenshots do app rodando
6. Secao Arquitetura: diagrama simplificado + link pros docs/
7. Tabela de tech stack com versoes
8. Creditos da equipe

**Criterio de aceite:** README completo com instalacao, uso, arquitetura, screenshots.

---

#### DOC-04: Documentacao tecnica

**Descricao:** Documento de 3-5 paginas baseado no SDD, formatado para entrega academica. Inclui diagramas renderizados.

**Passo a passo:**
1. Usar SDD.md como base, converter para formato academico
2. Adicionar: capa, sumario, introducao, desenvolvimento (arquitetura + modulos + fluxos), conclusao
3. Renderizar diagramas Mermaid como imagens (usar mermaid.live ou CLI mermaid)
4. Incluir imagens dos diagramas no documento
5. Exportar como PDF
6. Revisar formatacao e ortografia

**Criterio de aceite:** 3-5 paginas, diagramas renderizados, formato academico.

---

#### DOC-05: Poster

**Descricao:** Criar poster A1 para Mostra UFCAT. Visual 8-bit consistente com a interface. Conteudo: problema, solucao, arquitetura, resultados/metricas.

**Passo a passo:**
1. Definir layout A1 (594 x 841 mm) em ferramenta de design (Canva, Figma, ou PowerPoint)
2. Usar paleta de cores do projeto (azul escuro #1A3F6B, amarelo #F5C518, fundo #0D1B2A)
3. Usar fonte pixel consistente com a interface
4. Secoes: Titulo + Logo | Problema | Solucao | Como Funciona (diagrama simplificado) | Resultados | Equipe | QR code da URL
5. Incluir screenshot do app
6. Revisar com o grupo
7. Exportar em alta resolucao para impressao

**Criterio de aceite:** Poster A1, visual 8-bit, conteudo completo.

---

#### DOC-06: Video final

**Descricao:** Gravar video demonstrativo completo do produto para a Mostra UFCAT. Mostrar fluxo completo: login, navegacao, chat, exercicio, progresso.

**Passo a passo:**
1. Roteirizar: login Google > tela principal > seguir rota > conversar com tutor > fazer exercicio > ver XP subir > navegar livre
2. Usar URL de producao (Railway)
3. Gravar tela + narrar (ou usar legendas)
4. Duracao: 2-5 minutos
5. Editar: cortar pausas, adicionar transicoes simples
6. Exportar mp4, max 100MB

**Criterio de aceite:** Demo completa do produto, 2-5min, URL de producao.

---

### Bloco E: Polimento (paralelizavel)

---

#### FRO-07: Responsivo mobile

**Descricao:** Adaptar layout para funcionar em telas a partir de 360px (celular). Painel de rota colapsa ou vira aba, chat ocupa tela cheia.

**Passo a passo:**
1. Adicionar media queries em style.css para breakpoints: 360px, 768px
2. Em mobile: esconder painel lateral, adicionar botao hamburguer para abrir
3. Chat ocupa 100% da largura
4. Input de mensagem fica fixo no bottom
5. Testar: usar DevTools do Chrome (toggle device toolbar)
6. Verificar que nao quebra em nenhuma resolucao

**Criterio de aceite:** Funciona em tela 360px+, chat usavel em mobile.

---

#### FRO-08: Loading states

**Descricao:** Mostrar indicador visual "Pensando..." enquanto aguarda resposta do Claude. Evita que aluno ache que travou.

**Passo a passo:**
1. Em chat.js, apos enviar mensagem: inserir bolha temporaria com animacao "..."
2. Animacao: 3 pontos piscando (CSS animation)
3. Desabilitar botao Enviar durante loading
4. Quando resposta chegar: remover bolha temporaria, inserir resposta real
5. Se timeout/erro: remover bolha, mostrar mensagem de erro amigavel
6. Testar: verificar que aparece durante a espera (2-5s tipicos)

**Criterio de aceite:** Indicador visual durante espera, botao desabilitado.

---

#### POL-01: Tratamento de erros completo

**Descricao:** Garantir que toda chamada a API externa (Claude, Google OAuth) tem try/except com mensagem amigavel para o usuario. Nenhum erro 500 sem tratamento.

**Passo a passo:**
1. Em src/agente_base.py: try/except em messages.create() — retornar msg amigavel se falhar
2. Em src/auth.py: try/except no callback OAuth — redirecionar pra /login com flash msg
3. Em app.py: handler global @app.errorhandler(500) retornando JSON de erro
4. Em app.py: handler @app.errorhandler(404) retornando pagina ou JSON
5. Logar erros com logging.error() para debug
6. Testar: simular API offline (desconectar internet), verificar que usuario ve mensagem amigavel

**Criterio de aceite:** try/except em toda API call, msg amigavel, sem 500 sem tratamento.

---

#### POL-02: Garantir while no codigo

**Descricao:** Requisito da rubrica exige uso de while. Implementar em contexto real (ex: retry loop do agente, ou polling de status).

**Passo a passo:**
1. Local natural: retry com backoff no agente_base.py
2. Implementar: while tentativas < max_tentativas: try API call, except: sleep e retry
3. Ja existe na logica do AGE-04 — garantir que usa while explicito (nao for range)
4. Comentar no codigo: # Uso de while — requisito da rubrica

**Criterio de aceite:** while usado em pelo menos 1 modulo com proposito real.

---

#### POL-03: Garantir tupla no codigo

**Descricao:** Requisito da rubrica exige uso de tupla. Usar em contexto real (ex: retorno de funcao, constantes imutaveis).

**Passo a passo:**
1. Local natural: src/progresso.py — NIVEIS como tupla de tuplas
2. Implementar: NIVEIS = ((1, "Aprendiz", 0), (2, "Intermediario", 500), (3, "Avancado", 1000), (4, "Mestre", 2000))
3. Funcao calcular_nivel() itera sobre NIVEIS (tupla imutavel, nao lista)
4. Comentar no codigo: # Uso de tupla — requisito da rubrica

**Criterio de aceite:** Tupla usada em pelo menos 1 modulo com proposito real.

---

## Ordem de Corte (se faltar tempo)

Prioridade de corte — do menos critico pro mais critico:

1. **Cortar primeiro:** Poster elaborado (pode ser simples), responsivo mobile (FRO-07)
2. **Cortar segundo:** Sean Ellis (manter so NPS), UI de feedback elaborada
3. **Cortar terceiro:** ChromaDB — substituir por contexto fixo em TXT no system prompt
4. **Nunca cortar:** Chat funcional, Auth Google, Banco SQLAlchemy, RAG (mesmo simplificado), Testes minimos, Deploy

---

## Capacidade Estimada

| Sprint | Dias | Horas estimadas (4 pessoas x 3h/dia) | Carga |
|---|---|---|---|
| Sprint 1 (resto) | 3 dias (22-25/06) | ~36h | Leve (foco E2) |
| Sprint 2 | 8 dias (26/06-03/07) | ~96h | Pesada (core features) |
| Sprint 3 | 7 dias (04-10/07) | ~84h | Media (polish + docs) |

---

## Decisoes Tecnicas Firmes

- **Modelo:** Claude Opus 4.8 (effort medium) primario + Sonnet 4.6 fallback
- **Persistencia:** SQLAlchemy (SQLite dev / PostgreSQL prod) + JSON (conteudo estatico)
- **Auth:** Google OAuth apenas (@discente.ufcat.edu.br)
- **RAG:** ChromaDB + sentence-transformers (all-MiniLM-L6-v2)
- **Deploy:** Railway (PostgreSQL addon gratuito)
- **Testes:** pytest + pytest-cov (50%+ coverage)
- **requirements.txt escrito a mao** (nunca pip freeze)
- **Imports via pacote src:** from src.sessao import Sessao
- **Commits so com aprovacao explicita do Victor**

---

*Referencias: PRD.md, ADR.md, SDD.md, CONTEXTO_PROJETO.md*
