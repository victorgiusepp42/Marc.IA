# Marc.IA — Tutor Inteligente de Programação 🤖

Plataforma web de ensino adaptativo com tutor IA. Chatbot interativo que guia o aluno por uma rota de aprendizado, tirando dúvidas, explicando conceitos e propondo exercícios — tudo com inteligência artificial.

Desenvolvido como projeto final da disciplina de Introdução à Programação — UFCAT/IMTec (2025/1).

---

## 📋 Funcionalidades

- Chat interativo com tutor IA (persona PyAI Professor)
- Rota de aprendizado com 10 tópicos de Python
- Sistema de XP e níveis (Aprendiz → Mestre)
- Persistência de sessão (histórico salvo em JSON)
- Interface retro 8-bit responsiva
- Fallback automático de API key para alta disponibilidade

---

## 🚀 Como Rodar

### Pré-requisitos

- Python 3.10+
- Chave de API da Anthropic ([console.anthropic.com](https://console.anthropic.com))

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

# 4. Configure a API key
# Crie um arquivo .env na raiz com:
# ANTHROPIC_API_KEY=sua-chave-aqui
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
├── .env                    # API keys (não commitado)
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── sessao.py           # Classe Sessao — histórico, XP, níveis
│   ├── agente_base.py      # AgentBase — classe abstrata do tutor
│   └── agente_ip.py        # AgenteIP — tutor de Python (herda AgentBase)
│
├── templates/
│   └── index.html          # Página principal
│
├── static/
│   ├── style.css           # Visual retro 8-bit
│   └── chat.js             # Lógica de chat (fetch + render)
│
└── data/
    ├── plano.json           # Rota de 10 tópicos
    └── sessoes/             # Sessões salvas por aluno (JSON)
```

### Fluxo de uma Mensagem

```
Aluno digita pergunta
  → chat.js envia POST /chat
    → app.py valida input, carrega sessão
      → AgenteIP.responder() monta prompt + histórico
        → API Claude (claude-sonnet-4-6) gera resposta
      → Sessão atualizada (histórico + XP)
    → JSON retornado ao front
  → Bolha renderizada no chat
```

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3.13 | Linguagem principal |
| Flask 3.1 | Servidor web |
| Anthropic SDK | Chamadas à API Claude |
| python-dotenv | Gerenciamento de variáveis de ambiente |
| HTML + CSS + JS | Interface (sem frameworks) |
| JSON | Persistência de sessões e dados |

---

## 📚 Conceitos de Programação Utilizados

1. **Variáveis e tipos** — str, int, list, dict, bool em todos os módulos
2. **Condicionais (if/elif/else)** — validação de input, fluxo de decisão
3. **Laços (for/while)** — iteração em níveis, retry de API
4. **Funções** — métodos e rotas Flask
5. **Listas, dicionários e tuplas** — histórico, messages, XP_NIVEIS
6. **Leitura/escrita de arquivos** — sessões em JSON
7. **Tratamento de exceções (try/except)** — API, I/O, JSON
8. **POO com herança** — AgentBase → AgenteIP

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

Projeto acadêmico — UFCAT/IMTec, Bacharelado em Inteligência Artificial, 2025.

