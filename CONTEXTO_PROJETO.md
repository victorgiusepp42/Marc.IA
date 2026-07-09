# Marc.IA — Contexto para Planejamento e Implementação

> Documento de referência para Plan Mode. Contém decisões firmes, restrições, dependências, critérios de aceite e backlog detalhado.

---

## 1. Identidade do Projeto

**Marc.IA** — Plataforma web de ensino adaptativo com tutor IA. Chatbot interativo via API Claude (Anthropic). Guia o aluno por rota de aprendizado predefinida. Deploy Railway. Gratuito.

**Visão futura:** qualquer professor faz upload de materiais e gera o agente da sua disciplina.

---

## 2. Equipe e Responsabilidades

| Integrante | Papel | Épicos principais |
|---|---|---|
| Diogo Alves Ribeiro | Líder formal + Front-end | FRO |
| Victor Giusepp Almeida | Core IA + Coord. técnica | AGE, NUC, DEC |
| Kevynson Gabriel Silva | Back-end / DevOps | NUC, MOS |
| Natan Alves Cotinguiba Araujo | Core IA + Testes | AGE, QA |

---

## 3. Ambientes

| Local | Caminho | Função |
|---|---|---|
| Dev (código) | `C:\Users\victo\Projetos\Marc.IA` | Repo Git — onde se coda |
| Backup código (Drive) | `C:\Users\victo\Meu Drive\Introdução a Programação\Marc.IA_Projeto_IP\backup_github\` | Espelho sincronizado a cada bloco de progresso |
| Docs/Entregas (Drive) | `C:\Users\victo\Meu Drive\Introdução a Programação\Marc.IA_Projeto_IP\` | PDFs, vídeos, pôster |
| Remote | `github.com/victorgiusepp42/Marc.IA` | Repo público |

**Fluxo:** codar local → Victor aprova commit → push GitHub → backup Drive automático pelo agente.

---

## 4. Restrições Acadêmicas (UFCAT)

- 4 semanas, **40 pts (40% da nota)**, apresentação Mostra UFCAT
- **3 entregas:**
  - E1: proposta ✅ (já entregue)
  - E2 (Semana 3, 25/06-01/07): relatório PDF 1p + repo funcional + vídeo 1-3min
  - E3 (Semana 4, ~10/07): código completo + requirements.txt + README + doc técnica 3-5p + pôster + apresentação
- **Requisitos obrigatórios:**
  - Python 3.10+
  - ≥3 módulos
  - Entrada via `app.py`
  - Comentários + docstrings
  - Repo público
  - Interface obrigatória (web)
  - Rodar com `pip install -r requirements.txt` (sem depender do Railway)
- **8 conceitos que DEVEM aparecer no código:**
  1. Variáveis e tipos
  2. if/elif/else
  3. for/while
  4. Funções
  5. Listas/dicts/tuplas
  6. Leitura/escrita de arquivos (JSON)
  7. try/except
  8. POO (≥1 classe com herança)
- **Avaliação:** Funcionamento 12 · Conceitos 10 · Interface 6 · Apresentação 6 · Doc/README 4 · Prazos 2
- **Bônus (+5):** API externa ✅ · deploy nuvem · SQLite · pytest ≥50% · .exe

---

## 5. Arquitetura

**Princípio:** Núcleo genérico + disciplinas acopladas via herança. Flask + sessão + roteamento suportam N disciplinas.

### Estrutura de Pastas (canônica)

```
Marc.IA/
├── app.py                      # ENTRADA — Flask app
├── requirements.txt            # escrito à mão
├── README.md
├── DECISOES.md
├── .env                        # ANTHROPIC_API_KEY (não commitado)
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── sessao.py               # classe Sessao (POO obrigatória)
│   ├── agente_base.py          # AgentBase — classe abstrata
│   ├── agente_ip.py            # AgenteIP(AgentBase) — tutor Python
│   ├── disciplina_manager.py   # factory: disciplina → agente
│   ├── rota_loader.py          # lê plano.json, controla progresso
│   ├── progresso.py            # lógica de XP/nível
│   ├── exercicios.py           # carrega e valida exercícios
│   ├── validacao.py            # sanitização de input
│   └── rag/
│       ├── __init__.py
│       ├── indexador.py        # indexa KB no ChromaDB
│       └── retriever.py        # busca semântica
│
├── templates/
│   └── index.html              # página única (SPA-like)
│
├── static/
│   ├── style.css               # visual 8-bit
│   └── chat.js                 # lógica de chat + fetch
│
├── data/
│   ├── plano.json              # rota de tópicos por disciplina
│   ├── exercicios.json         # banco de exercícios
│   ├── kb_ip/                  # materiais da KB (PDFs/TXTs)
│   └── sessoes/                # sessões salvas (JSON por usuário)
│
├── docs/                       # doc técnica, pôster
└── tests/                      # pytest
```

### Stack Tecnológica

| Tech | Uso | Obrigatório? |
|---|---|---|
| Flask | Back-end, rotas HTTP | Sim |
| Anthropic SDK (`anthropic`) | Chamadas ao Claude | Sim |
| ChromaDB | RAG — busca semântica | Sprint 2 (cortável) |
| python-dotenv | Carrega .env | Sim |
| HTML + CSS + JS vanilla | Interface chat | Sim |
| Railway | Deploy nuvem | Sprint 3 (cortável) |
| pytest | Testes | Sprint 3 (cortável) |

### Fluxo de uma Mensagem (sequência completa)

```
Aluno → [index.html] seleciona disciplina/tópico
       → [chat.js] POST /chat {mensagem, usuario_id, disciplina, topico}
       → [app.py] rota /chat
       → [disciplina_manager.py] resolve agente pela disciplina
       → [agente_*.py] .responder(mensagem, sessao)
           → [retriever.py] busca chunks relevantes na KB (RAG)
           → monta system_prompt + histórico + chunks
           → [Anthropic API] messages.create()
       → [sessao.py] atualiza histórico + XP
       → response JSON → [chat.js] renderiza bolha
```

### Dependências entre Módulos

```
app.py
 ├── src.sessao (Sessao)
 ├── src.disciplina_manager (carregar_agente)
 └── src.validacao (sanitizar)

disciplina_manager.py
 └── src.agente_ip (AgenteIP)

agente_ip.py
 ├── src.agente_base (AgentBase)  ← herança
 └── src.rag.retriever (Retriever)

agente_base.py
 ├── anthropic (SDK)
 └── src.sessao (tipo Sessao)

sessao.py
 └── src.progresso (calcular_nivel)

rota_loader.py
 └── data/plano.json

exercicios.py
 └── data/exercicios.json
```

---

## 6. Classes Principais (contratos)

### Sessao (POO obrigatória — herança não exigida aqui)

```python
class Sessao:
    """Gerencia estado do aluno: histórico, XP, nível, disciplina/tópico ativos."""
    
    def __init__(self, usuario_id: str):
        self.usuario_id = usuario_id
        self.historico: list[dict] = []    # [{role: "user"|"assistant", content: str}]
        self.nivel: int = 1                # 1-4
        self.pontos: int = 0               # XP acumulado
        self.disciplina_ativa: str | None = None
        self.topico_ativo: str | None = None

    def adicionar_mensagem(self, role: str, content: str) -> None: ...
    def salvar(self) -> None: ...          # json.dump → data/sessoes/{id}.json
    def carregar(self) -> None: ...        # json.load ← data/sessoes/{id}.json
```

### AgentBase (contrato de herança — POO obrigatória)

```python
class AgentBase:
    """Classe abstrata. Cada disciplina herda e customiza system_prompt + kb_path."""
    
    disciplina: str = ""
    kb_path: str = ""
    system_prompt: str = ""

    def __init__(self):
        self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.retriever = self._carregar_kb()

    def _carregar_kb(self) -> Retriever | None: ...
    def buscar_contexto(self, query: str) -> list[str]: ...
    def responder(self, mensagem: str, sessao: Sessao) -> str:
        """Método principal — RAG + prompt + API call."""
        chunks = self.buscar_contexto(mensagem)
        messages = self._montar_messages(mensagem, sessao, chunks)
        response = self.client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=self.system_prompt,
            messages=messages
        )
        return response.content[0].text
```

### AgenteIP (herda AgentBase)

```python
class AgenteIP(AgentBase):
    """Tutor especialista em Introdução à Programação (Python)."""
    disciplina = "Introdução à Programação"
    kb_path = "data/kb_ip/"
    system_prompt = "..."  # persona PyAI Professor
```

---

## 7. Interface — Especificação Visual

**Estilo:** Retro 8-bit. Sem anti-aliasing.

**Paleta:**
| Token | Hex | Uso |
|---|---|---|
| Azul escuro | `#1A3F6B` | Headers, bordas |
| Azul médio | `#2B6CB0` | Botões, links |
| Amarelo | `#F5C518` | Destaques, XP, acertos |
| Fundo | `#0D1B2A` | Background geral |
| Texto | `#E0E0E0` | Corpo de texto |

**Layout (desktop):**
```
┌─────────────────────────────────────────────────┐
│ MARC.IA                          [disciplina ▼] │
├──────────────┬──────────────────────────────────┤
│  ROTA        │         SALA DE AULA             │
│              │                                  │
│  ✓ Tópico 1 │  🤖 Olá! Sou o PyAI Professor   │
│  ▶ Tópico 2 │                                  │
│  ○ Tópico 3 │  👤 O que é uma variável?        │
│  ○ Tópico 4 │                                  │
│              │  🤖 Pense numa variável como...  │
│              │                                  │
│  XP: 120    │                                  │
│  Nível: 1   │                                  │
├──────────────┴──────────────────────────────────┤
│  [____________________] [Enviar]                │
└─────────────────────────────────────────────────┘
```

**Avatar:** PyAI Professor — pixel art 8-bit. Muda por disciplina no futuro.

---

## 8. Sistema de XP e Níveis

| Nível | Nome | XP |
|---|---|---|
| 1 | Aprendiz | 0–499 |
| 2 | Intermediário | 500–999 |
| 3 | Avançado | 1000–1999 |
| 4 | Mestre | 2000+ |

**Ganho de XP:**
- Mensagem enviada: +5 XP
- Exercício correto: +50 XP
- Exercício parcial: +20 XP
- Tópico concluído: +100 XP

---

## 9. Persona do Tutor — PyAI Professor

- Paciente, didático, usa analogias do cotidiano
- **Nunca entrega resposta direta** — estimula raciocínio com perguntas guiadas
- Responde no contexto do tópico ativo (não divaga)
- Usa histórico da sessão para adaptar profundidade
- Para IP: metáforas como "variável = baú de inventário", desafios progressivos, celebra acertos
- Tom: informal mas respeitoso, encorajador sem ser infantil

---

## 10. Backlog Detalhado por Sprint

### Sprint 1 (18-24/06) — Walking Skeleton

**Objetivo:** app rodando local com chat funcional (Claude respondendo).

| ID | Tarefa | Módulo(s) | Critério de Aceite | Deps |
|---|---|---|---|---|
| FUND-01 | venv + .gitignore | raiz | `python -m venv venv` funciona, .gitignore cobre venv/,.env,__pycache__,data/sessoes/ | — |
| FUND-02 | requirements.txt | raiz | `pip install -r requirements.txt` instala flask, anthropic, python-dotenv | — |
| DEC-01 | Definir modelo API | — | Decidido: claude-sonnet-4-6 | — |
| DEC-02 | API key com billing | .env | Variável ANTHROPIC_API_KEY no .env, key ativa | — |
| NUC-01 | Classe Sessao | src/sessao.py | Instancia, salva JSON, carrega JSON, adiciona mensagem | — |
| NUC-02 | app.py mínimo | app.py | Flask roda, rota GET / serve index.html, rota POST /chat recebe JSON | FUND-02 |
| AGE-01 | AgentBase | src/agente_base.py | Classe com responder() chamando API | FUND-02, DEC-02 |
| AGE-02 | AgenteIP | src/agente_ip.py | Herda AgentBase, system_prompt definido, responde sobre Python | AGE-01 |
| AGE-03 | Integração app↔agente | app.py | POST /chat retorna resposta do Claude via AgenteIP | NUC-02, AGE-02, NUC-01 |
| CONT-01 | plano.json | data/plano.json | 10 tópicos de IP ordenados, estrutura {disciplina, topicos: [{id, titulo, descricao}]} | — |
| FRO-01 | index.html | templates/ | Layout com painel rota + chat + input funcional | — |
| FRO-02 | style.css | static/ | Visual 8-bit, paleta definida, responsivo básico | FRO-01 |
| FRO-03 | chat.js | static/ | Envia msg via fetch, renderiza resposta, scroll automático | FRO-01, NUC-02 |

**Entregável Sprint 1:** rodar `python app.py`, abrir browser, digitar pergunta, receber resposta do Claude.

---

### Sprint 2 (25/06-01/07) — Integração + RAG + Entrega 2

| ID | Tarefa | Módulo(s) | Critério de Aceite | Deps |
|---|---|---|---|---|
| NUC-03 | Persistência sessão | src/sessao.py | Sessão salva/carrega de data/sessoes/{id}.json | NUC-01 |
| NUC-04 | Rota loader | src/rota_loader.py | Carrega plano.json, retorna tópicos com status | CONT-01 |
| NUC-05 | Progresso | src/progresso.py | Calcula nível a partir de XP, atualiza sessão | NUC-01 |
| AGE-04 | Histórico no prompt | agente_base.py | Últimas N mensagens incluídas no messages[] | AGE-01, NUC-03 |
| AGE-05 | Contexto do tópico | agente_ip.py | system_prompt inclui descrição do tópico ativo | AGE-02, NUC-04 |
| CONT-02 | exercicios.json | data/ | ≥5 exercícios por tópico, formato {topico_id, enunciado, tipo, resposta} | CONT-01 |
| CONT-03 | KB materiais IP | data/kb_ip/ | ≥3 arquivos .txt com conteúdo dos tópicos | — |
| RAG-01 | Indexador | src/rag/indexador.py | Lê kb_ip/, cria embeddings no ChromaDB | CONT-03 |
| RAG-02 | Retriever | src/rag/retriever.py | Busca top-3 chunks por query | RAG-01 |
| RAG-03 | Integração RAG↔Agente | agente_base.py | buscar_contexto() usa Retriever, chunks no prompt | RAG-02, AGE-04 |
| FRO-04 | Painel rota dinâmico | chat.js + index.html | Tópicos carregam de GET /rota, status visual ✓/▶/○ | NUC-04 |
| FRO-05 | Exercício inline | chat.js | Exibe exercício, coleta resposta, mostra feedback | CONT-02 |
| EXE-01 | Validação exercícios | src/exercicios.py | Compara resposta, retorna certo/parcial/errado + XP | CONT-02 |
| DOC-01 | Relatório E2 | docs/ | PDF 1 página + README atualizado | — |
| DOC-02 | Vídeo E2 | — | 1-3min demonstrando o app | — |

**Entregável Sprint 2:** app com RAG, exercícios, progresso visível. Entrega 2 submetida.

---

### Sprint 3 (02-10/07) — Polimento + Docs + Mostra

| ID | Tarefa | Módulo(s) | Critério de Aceite | Deps |
|---|---|---|---|---|
| QA-01 | pytest básico | tests/ | ≥50% coverage nos módulos src/ | tudo |
| QA-02 | Validação input | src/validacao.py | Sanitiza HTML, limita tamanho, trata vazio | — |
| MOS-01 | Deploy Railway | — | App acessível via URL pública | tudo |
| MOS-02 | Variáveis env Railway | — | ANTHROPIC_API_KEY configurada no Railway | MOS-01 |
| DOC-03 | README final | README.md | Instalação, uso, arquitetura, créditos | — |
| DOC-04 | Doc técnica | docs/ | 3-5 páginas, diagramas, decisões | — |
| DOC-05 | Pôster | docs/ | A1, visual 8-bit consistente | — |
| FRO-06 | Responsivo mobile | style.css | Funciona em tela ≥360px | FRO-02 |
| FRO-07 | Loading states | chat.js | Indicador de "pensando..." enquanto Claude responde | FRO-03 |
| POL-01 | Tratamento erros | app.py + agente | try/except em API call, mensagem amigável ao aluno | AGE-01 |
| POL-02 | While no código | — | Garantir uso de while em pelo menos 1 módulo | — |
| POL-03 | Tupla no código | — | Garantir uso de tupla em pelo menos 1 módulo | — |

---

## 11. Decisões Técnicas Firmes

- **Modelo plugável:** `AgentBase` aceita trocar Claude por modelo local no futuro
- **requirements.txt escrito à mão** (nunca `pip freeze`)
- **Imports via pacote `src`:** ex. `from src.sessao import Sessao`
- **`__init__.py`** em `src/` e `src/rag/`
- **Rodar sempre da raiz** do projeto: `python app.py`
- **Kanban no GitHub Projects** (board separado, não no repo)
- **Sem dono fixo por tarefa** — responsabilidade no nível do épico
- **Commits só com aprovação explícita do Victor**
- **Backup Drive automático** pelo agente a cada bloco de progresso

---

## 12. Ordem de Corte (se apertar o prazo)

1. RAG (ChromaDB) — agente funciona sem, só perde qualidade
2. Deploy Railway — pode apresentar local na Mostra
3. pytest — bônus, não obrigatório
4. Exercícios inline — chat puro já atende
5. **NUNCA cortar:** chat funcional, 8 conceitos, POO, interface, README

---

## 13. Riscos Identificados

| Risco | Impacto | Mitigação |
|---|---|---|
| Sprint 2 sobrecarregada (~58h vs 40h cap.) | Atraso E2 | Priorizar RAG-free path, cortar se necessário |
| Conceito "while" fraco no código | -pontos em Conceitos | Incluir while em validacao.py ou progresso.py |
| Conceito "tupla" fraco | -pontos em Conceitos | Usar tupla em XP_NIVEIS ou retornos |
| API key billing estourar | App para | Limitar max_tokens, monitorar usage |
| ChromaDB pesado demais | requirements quebra | Fallback: busca simples por keyword em TXT |

---

## 14. Estado Atual (20/06/2026)

- ✅ Proposta (Entrega 1) submetida
- ✅ Logo aprovado (pixel art 8-bit)
- ✅ Backlog completo (50 tarefas)
- ✅ Arquitetura definida
- ✅ Repo clonado + contexto documentado
- ⏳ **Código não iniciado — próximo: implementar Sprint 1**

---

## 15. Regras para o Agente (Claude Code)

- Português brasileiro em todo output
- Código Python: modular, comentado com docstrings, sem frameworks extras
- Visual 8-bit preservado, sem anti-aliasing
- Commits: preparar mas só executar com aprovação do Victor
- Backup Drive: copiar para `backup_github/` a cada bloco significativo
- Quando Victor pede para acumular alterações, aguardar "terminei" antes de aplicar
- Outputs diretos, sem over-explanation
