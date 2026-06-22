# SDD — Marc.IA

**Software Design Document**

| Campo | Valor |
|---|---|
| Produto | Marc.IA |
| Versão | 1.0 |
| Data | 21/06/2026 |
| Autor | Victor Giusepp Almeida |
| Status | Em desenvolvimento |

---

## 1. Visão Geral da Arquitetura

Marc.IA é uma aplicação web monolítica em Flask com arquitetura em camadas:

```
+-----------------------------------------------------+
|                   CLIENTE (Browser)                   |
|          HTML + CSS (8-bit) + JS vanilla             |
+-----------------------------------------------------+
|                   SERVIDOR (Flask)                    |
|  +----------+  +----------+  +------------------+   |
|  |  Rotas   |  |   Auth   |  |   Validacao      |   |
|  | (app.py) |  | (OAuth)  |  | (validacao.py)   |   |
|  +----+-----+  +----+-----+  +--------+---------+   |
|       |              |                  |            |
|  +----+--------------+------------------+--------+   |
|  |              CAMADA DE DOMINIO                 |   |
|  |  +---------+ +----------+ +---------------+   |   |
|  |  | Sessao  | |Progresso | |  Exercicios   |   |   |
|  |  +---------+ +----------+ +---------------+   |   |
|  +---------------------------+-------------------+   |
|                          |                           |
|  +-----------------------+-------------------+       |
|  |              CAMADA DE AGENTES             |      |
|  |  +-----------+    +-----------+            |      |
|  |  |AgentBase  |<---|  AgenteIP |            |      |
|  |  |(abstrata) |    | (heranca) |            |      |
|  |  +-----+-----+    +-----------+            |      |
|  |        |                                   |      |
|  |  +-----+-----+                             |      |
|  |  | Retriever | (RAG)                       |      |
|  |  +-----------+                             |      |
|  +--------------------------------------------+      |
+-----------------------------------------------------+
|                 CAMADA DE DADOS                       |
|  +----------+  +----------+  +------------------+   |
|  |  SQLite/ |  |   JSON   |  |    ChromaDB      |   |
|  | Postgres |  |(estatico)|  |   (vetores)      |   |
|  +----------+  +----------+  +------------------+   |
+-----------------------------------------------------+
|                SERVICOS EXTERNOS                      |
|  +------------------+  +------------------------+   |
|  |  Anthropic API   |  |    Google OAuth 2.0    |   |
|  |  (Claude LLM)    |  |  (Autenticacao)        |   |
|  +------------------+  +------------------------+   |
+-----------------------------------------------------+
```

---

## 2. Estrutura de Pastas

```
Marc.IA/
├── app.py                      # ENTRADA — Flask app, rotas HTTP
├── requirements.txt            # Dependências Python
├── README.md                   # Documentação de uso
├── .env                        # Variáveis de ambiente (não commitado)
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── sessao.py               # Classe Sessao — estado do aluno
│   ├── agente_base.py          # AgentBase — classe abstrata (herança)
│   ├── agente_ip.py            # AgenteIP(AgentBase) — tutor Python/IP
│   ├── disciplina_manager.py   # Factory: disciplina → agente
│   ├── rota_loader.py          # Carrega plano.json, controla progresso
│   ├── progresso.py            # Lógica de XP/nível
│   ├── exercicios.py           # Carrega e valida exercícios
│   ├── validacao.py            # Sanitização de input
│   ├── auth.py                 # Google OAuth + Flask-Login
│   ├── database.py             # SQLAlchemy engine + models
│   └── rag/
│       ├── __init__.py
│       ├── indexador.py        # Indexa KB no ChromaDB
│       └── retriever.py        # Busca semântica top-k
│
├── templates/
│   └── index.html              # Página única (SPA-like)
│
├── static/
│   ├── style.css               # Visual 8-bit
│   └── chat.js                 # Lógica de chat + fetch
│
├── data/
│   ├── plano.json              # Rota de tópicos por disciplina
│   ├── exercicios.json         # Banco de exercícios
│   ├── kb_ip/                  # Materiais da KB (TXTs)
│   └── marcia.db              # SQLite (apenas dev local)
│
├── docs/                       # Documentação do projeto
│   ├── PRD.md
│   ├── ADR.md
│   ├── SDD.md
│   └── diagramas/
│
└── tests/                      # pytest
    ├── conftest.py
    ├── test_sessao.py
    ├── test_agente.py
    └── test_rotas.py
```

---

## 3. Módulos e Responsabilidades

### 3.1 app.py (Entrada)

**Responsabilidade:** Inicializar Flask, registrar rotas, orquestrar request/response.

**Rotas:**

| Método | Rota | Função | Auth? |
|---|---|---|---|
| GET | `/` | Serve index.html | Sim |
| GET | `/login` | Inicia fluxo Google OAuth | Não |
| GET | `/login/callback` | Recebe token do Google | Não |
| GET | `/logout` | Encerra sessão | Sim |
| GET | `/rota` | Retorna plano de tópicos | Sim |
| POST | `/chat` | Processa mensagem do aluno | Sim |
| POST | `/feedback` | Registra avaliação de resposta | Sim |

### 3.2 src/auth.py (Autenticação)

**Responsabilidade:** Gerenciar fluxo OAuth 2.0 com Google.

**Dependências:** Authlib, Flask-Login

**Fluxo:**
1. Aluno acessa `/` sem sessão → redireciona para `/login`
2. `/login` redireciona para Google consent screen
3. Google retorna token para `/login/callback`
4. Callback valida token, extrai google_id/email/nome
5. Cria ou carrega usuário no banco
6. Inicia sessão Flask (cookie seguro)

### 3.3 src/database.py (Persistência)

**Responsabilidade:** Definir models SQLAlchemy e gerenciar conexão.

**Models:**

```python
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.String(64), unique=True, nullable=False)
    nome = db.Column(db.String(128))
    email = db.Column(db.String(128))
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

class SessaoEstudo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    disciplina = db.Column(db.String(64))
    topico_ativo = db.Column(db.String(64))
    historico = db.Column(db.JSON)
    xp = db.Column(db.Integer, default=0)
    nivel = db.Column(db.Integer, default=1)
    atualizado_em = db.Column(db.DateTime, onupdate=datetime.utcnow)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    sessao_id = db.Column(db.Integer, db.ForeignKey('sessao_estudo.id'))
    tipo = db.Column(db.String(16))
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

class Metrica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    tipo = db.Column(db.String(32))
    valor = db.Column(db.Integer)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
```

**Configuração:**
```python
# Dev local
DATABASE_URL = "sqlite:///data/marcia.db"

# Produção (Railway)
DATABASE_URL = "postgresql://user:pass@host:5432/marcia"
```

### 3.4 src/sessao.py (Estado do Aluno)

**Responsabilidade:** Gerenciar estado da conversa — histórico, XP, nível, tópico ativo.

**Interface:**
```python
class Sessao:
    def __init__(self, usuario_id: str): ...
    def adicionar_mensagem(self, role: str, content: str) -> None: ...
    def adicionar_xp(self, pontos: int) -> None: ...
    def salvar(self) -> None: ...
    def carregar(self) -> None: ...
    @property
    def nivel_nome(self) -> str: ...
```

### 3.5 src/agente_base.py (Classe Abstrata)

**Responsabilidade:** Definir contrato comum para todos os agentes-tutor. Gerencia comunicação com API Claude.

**Interface:**
```python
class AgentBase:
    disciplina: str = ""
    kb_path: str = ""
    system_prompt: str = ""

    def __init__(self): ...
    def responder(self, mensagem: str, sessao: Sessao) -> str: ...
    def buscar_contexto(self, query: str) -> list[str]: ...
    def _montar_messages(self, msg, sessao, chunks) -> list[dict]: ...
    def _extrair_texto(self, response) -> str: ...
```

**Modelo primário:** Claude Opus 4.8 (effort medium)
**Modelo fallback:** Claude Sonnet 4.6 (effort medium)
**Retry:** 5 tentativas com backoff exponencial. Timeout de 60s por chamada.

### 3.6 src/agente_ip.py (Tutor IP)

**Responsabilidade:** Implementação concreta do tutor de Introdução à Programação.

**Herda:** AgentBase

**Customizações:**
- `disciplina = "Introdução à Programação"`
- `kb_path = "data/kb_ip/"`
- `system_prompt` = persona PyAI Professor com lógica adaptativa

### 3.7 src/rag/ (Retrieval-Augmented Generation)

**Responsabilidade:** Indexar materiais do professor e buscar chunks relevantes por query.

**Componentes:**
- `indexador.py` — lê TXTs de `data/kb_ip/`, chunka (500 tokens, overlap 50), gera embeddings, salva no ChromaDB
- `retriever.py` — recebe query do aluno, busca top-3 chunks mais similares, retorna lista de strings

**Modelo de embedding:** `all-MiniLM-L6-v2` (sentence-transformers) — leve, roda sem GPU

### 3.8 src/progresso.py (XP e Níveis)

**Responsabilidade:** Calcular nível a partir de XP, definir ganhos por ação.

| Ação | XP |
|---|---|
| Mensagem enviada | +5 |
| Exercício correto | +50 |
| Exercício parcial | +20 |
| Tópico concluído | +100 |

| Nível | Nome | Faixa XP |
|---|---|---|
| 1 | Aprendiz | 0–499 |
| 2 | Intermediário | 500–999 |
| 3 | Avançado | 1000–1999 |
| 4 | Mestre | 2000+ |

### 3.9 src/exercicios.py (Exercícios)

**Responsabilidade:** Carregar exercícios de `data/exercicios.json`, selecionar por tópico, validar resposta.

**Tipos de exercício:**
- Múltipla escolha
- Resposta curta (comparação fuzzy)
- Código (comparação de output esperado)

### 3.10 src/validacao.py (Sanitização)

**Responsabilidade:** Validar e sanitizar input do aluno antes de processar.

**Regras:**
- Limite de 2000 caracteres por mensagem
- Strip de HTML/scripts (XSS prevention)
- Rejeitar mensagem vazia ou só whitespace

---

## 4. Fluxo de Dados

### 4.1 Fluxo de Mensagem (happy path)

```
Aluno (browser)
  │
  ▼
chat.js → POST /chat {mensagem}
  │
  ▼
app.py
  ├── validacao.py (sanitiza input)
  ├── auth (verifica sessão)
  ├── Sessao.carregar(google_id)
  │
  ▼
AgenteIP.responder(mensagem, sessao)
  ├── Retriever.buscar(mensagem) → top-3 chunks
  ├── _montar_messages(histórico + chunks + system_prompt)
  ├── Anthropic API → messages.create(model="claude-opus-4-8")
  │
  ▼
Resposta do Claude
  │
  ▼
app.py
  ├── Sessao.adicionar_mensagem()
  ├── Sessao.adicionar_xp(5)
  ├── Sessao.salvar()
  │
  ▼
JSON {resposta, pontos, nivel} → chat.js → renderiza
```

### 4.2 Fluxo de Autenticação

```
Aluno acessa /
  │
  ▼
Tem sessão Flask válida?
  ├── Sim → Serve index.html
  └── Não → Redireciona /login
              │
              ▼
         Google OAuth consent
              │
              ▼
         /login/callback
              ├── Valida token
              ├── Cria/carrega Usuario no banco
              ├── Inicia Flask session
              └── Redireciona /
```

---

## 5. Dependências Externas

| Dependência | Versão | Função |
|---|---|---|
| Flask | ≥3.0 | Framework web |
| anthropic | ≥0.30 | SDK da API Claude |
| SQLAlchemy | ≥2.0 | ORM (SQLite/PostgreSQL) |
| Authlib | ≥1.3 | OAuth 2.0 client |
| Flask-Login | ≥0.6 | Gerenciamento de sessão |
| python-dotenv | ≥1.0 | Carrega .env |
| chromadb | ≥0.4 | Vector store para RAG |
| sentence-transformers | ≥2.2 | Embeddings para RAG |
| pytest | ≥7.0 | Testes |
| pytest-cov | ≥4.0 | Coverage |
| psycopg2-binary | ≥2.9 | Driver PostgreSQL (produção) |

---

## 6. Configuração de Ambiente

### Variáveis de Ambiente (.env)

```env
# API
ANTHROPIC_API_KEY=sk-ant-...

# Auth
GOOGLE_CLIENT_ID=...
GOOGLE_CLIENT_SECRET=...
SECRET_KEY=...

# Database
DATABASE_URL=sqlite:///data/marcia.db
```

### Execução Local

```bash
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\Activate.ps1 no Windows
pip install -r requirements.txt
python app.py
# Acessa http://localhost:5001
```

---

## 7. Diagramas

Os diagramas Mermaid estão em `docs/diagramas/`:

| Arquivo | Conteúdo |
|---|---|
| `diagrama_arquitetura.mmd` | Fluxo completo com autenticação e RAG |
| `diagrama_fluxo_mensagem.mmd` | Diagrama de sequência (request → response) |
| `diagrama_dependencias.mmd` | Grafo de dependências entre módulos/tarefas |
| `diagrama_jornada_usuario.mmd` | Jornada do aluno por persona (perdido/intermediário/avançado) |

---

## 8. Segurança

| Aspecto | Implementação |
|---|---|
| Autenticação | Google OAuth 2.0 (tokens validados server-side) |
| Sessão | Cookie seguro (httponly, samesite=lax) |
| Input | Sanitização contra XSS, limite de tamanho |
| API key | Em .env, nunca commitada, variável de ambiente no Railway |
| HTTPS | Forçado no Railway (automático) |
| CORS | Não necessário (monolito, mesmo domínio) |

---

## 9. Escalabilidade e Limitações

**Escopo atual (acadêmico):**
- ~30 alunos simultâneos no máximo
- 1 disciplina (IP)
- Deploy single-instance no Railway

**Para escalar (visão futura):**
- Adicionar disciplina = criar novo `agente_*.py` que herda AgentBase
- Múltiplas instâncias = PostgreSQL já suporta, Flask stateless
- Rate limiting na API Claude = implementar fila com Celery se necessário

---

## 10. Referências

- PRD: `docs/PRD.md`
- ADRs: `docs/ADR.md`
- Diagramas: `docs/diagramas/`
- Backlog: `CONTEXTO_PROJETO.md` §10

---

*Documento vivo — atualizar conforme a implementação evolui.*
