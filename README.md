# Marc.IA — Tutor Inteligente para Disciplinas do Curso de IA 🤖

Plataforma web de ensino adaptativo com tutor IA. Baliza o acesso à aprendizagem via inteligência artificial para alunos do curso de Bacharelado em IA da UFCAT. Oferece rota estruturada para quem precisa e liberdade total para quem não precisa, sempre com contexto da disciplina específica.

Desenvolvido como projeto final da disciplina de Introdução à Programação — UFCAT/IMTec (2026/S1).

---

## 📋 Funcionalidades

- Chat interativo com tutor IA (persona PyAI Professor)
- Rota de aprendizado com 10 tópicos de Python (navegação livre)
- Autenticação via Google OAuth (@discente.ufcat.edu.br)
- RAG — respostas contextualizadas com materiais do professor (ChromaDB)
- Sistema de XP e níveis (Aprendiz → Mestre)
- Exercícios com feedback e progressão
- Persistência via SQLAlchemy (SQLite dev / PostgreSQL prod)
- Métricas de qualidade: feedback por resposta, NPS, Sean Ellis
- Interface retro 8-bit responsiva
- Fallback automático de modelo (Opus 4.8 → Sonnet 4.6)

---

## 🚀 Como Rodar

### Pré-requisitos

- Python 3.10+
- Chave de API da Anthropic ([console.anthropic.com](https://console.anthropic.com))
- Credenciais Google OAuth ([console.cloud.google.com](https://console.cloud.google.com))

### Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/victorgiusepp42/Marc.IA.git
cd Marc.IA

# 2. Crie e ative o ambiente virtual
python -m venv venv

# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure as variáveis de ambiente
# Crie um arquivo .env na raiz com:
# ANTHROPIC_API_KEY=sua-chave-aqui
# GOOGLE_CLIENT_ID=seu-client-id
# GOOGLE_CLIENT_SECRET=seu-client-secret
# SECRET_KEY=chave-secreta-flask
# DATABASE_URL=sqlite:///data/marcia.db
```

### Executar

```bash
python app.py
```

Acesse **http://localhost:5000** no navegador.

---

## 🏗️ Arquitetura

```
Marc.IA/
├── app.py                  # Entrada — servidor Flask
├── requirements.txt        # Dependências
├── .env                    # Variáveis de ambiente (não commitado)
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── sessao.py           # Classe Sessao — histórico, XP, níveis
│   ├── agente_base.py      # AgentBase — classe abstrata do tutor
│   ├── agente_ip.py        # AgenteIP — tutor de Python (herda AgentBase)
│   ├── auth.py             # Google OAuth + Flask-Login
│   ├── database.py         # SQLAlchemy models + engine
│   ├── progresso.py        # Lógica de XP e níveis
│   ├── exercicios.py       # Carrega e valida exercícios
│   ├── validacao.py        # Sanitização de input
│   ├── rota_loader.py      # Carrega plano.json
│   └── rag/
│       ├── indexador.py    # Indexa KB no ChromaDB
│       └── retriever.py    # Busca semântica top-k
│
├── templates/
│   └── index.html          # Página principal
│
├── static/
│   ├── style.css           # Visual retro 8-bit
│   └── chat.js             # Lógica de chat (fetch + render)
│
├── data/
│   ├── plano.json          # Rota de 10 tópicos
│   ├── exercicios.json     # Banco de exercícios
│   └── kb_ip/              # Materiais da disciplina (RAG)
│
├── docs/                   # PRD, ADR, SDD, cronograma, diagramas
└── tests/                  # pytest + coverage
```

### Fluxo de uma Mensagem

```
Aluno digita pergunta
  → chat.js envia POST /chat
    → app.py valida input, verifica auth, carrega sessão do banco
      → AgenteIP.responder() busca contexto (RAG) + monta prompt + histórico
        → API Claude Opus 4.8 (effort medium) gera resposta
        → Fallback: Sonnet 4.6 se Opus falhar
      → Sessão atualizada no banco (histórico + XP)
    → JSON retornado ao front
  → Bolha renderizada no chat
```

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3.13 | Linguagem principal |
| Flask 3.1 | Servidor web |
| Anthropic SDK | API Claude (Opus 4.8 + Sonnet 4.6) |
| SQLAlchemy | ORM (SQLite dev / PostgreSQL prod) |
| ChromaDB | Vector store para RAG |
| sentence-transformers | Embeddings (all-MiniLM-L6-v2) |
| Authlib + Flask-Login | Google OAuth 2.0 |
| python-dotenv | Gerenciamento de variáveis de ambiente |
| HTML + CSS + JS | Interface retro 8-bit (sem frameworks) |
| Railway | Deploy + PostgreSQL |
| pytest + pytest-cov | Testes + coverage |

---

## 📚 Conceitos de Programação Utilizados

1. **Variáveis e tipos** — str, int, list, dict, bool em todos os módulos
2. **Condicionais (if/elif/else)** — validação de input, cálculo de nível, fluxo de decisão
3. **Laços (for/while)** — iteração em níveis, retry de API com backoff
4. **Funções** — métodos, rotas Flask, helpers
5. **Listas, dicionários e tuplas** — histórico, messages, NIVEIS como tupla
6. **Leitura/escrita de arquivos** — plano.json, exercicios.json, KB TXTs
7. **Tratamento de exceções (try/except)** — API calls, OAuth, I/O
8. **POO com herança** — AgentBase → AgenteIP

---

## 📖 Documentação

| Documento | Descrição |
|---|---|
| [PRD](docs/PRD.md) | Product Requirements Document — problema, público, diferencial, métricas |
| [ADR](docs/ADR.md) | Architecture Decision Records — 10 decisões técnicas documentadas |
| [SDD](docs/SDD.md) | Software Design Document — módulos, fluxos, interfaces, segurança |
| [Cronograma](docs/CRONOGRAMA.md) | Sprints, épicos, tarefas detalhadas com passo a passo |
| [Diagramas](docs/diagramas/) | Arquitetura, fluxo de mensagem, dependências, jornada do usuário (Mermaid) |

---

## 👥 Equipe

| Nome | RA | Papel |
|---|---|---|
| Diogo Alves Ribeiro | 202600442 | Líder formal + Front-end |
| Victor Giusepp Almeida | 202600434 | Core IA + Coordenação técnica |
| Kevynson Gabriel Silva | 202600450 | Back-end / DevOps |
| Natan Alves Cotinguiba Araujo | 202601003 | Core IA + Testes |

---

## 📄 Licença

Projeto acadêmico — UFCAT/IMTec, Bacharelado em Inteligência Artificial, 2026.

