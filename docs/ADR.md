# ADR — Marc.IA

**Registro de Decisões Arquiteturais**

> Cada decisão documenta o contexto, as opções avaliadas, a escolha feita e o motivo. Formato baseado no modelo MADR (Markdown Any Decision Records).

---

## ADR-001: Linguagem e Framework Web

**Status:** Aceita  
**Data:** 18/06/2026  
**Contexto:** Projeto acadêmico exige Python 3.10+ e interface web obrigatória.

**Opções consideradas:**
1. Flask (micro-framework, minimalista)
2. Django (full-stack, batteries-included)
3. FastAPI (async, moderno)

**Decisão:** Flask

**Motivo:**
- Requisito acadêmico favorece simplicidade e controle explícito
- Menor curva de aprendizado pro time
- Suficiente para o escopo (poucas rotas, SSR simples)
- Django seria overkill; FastAPI exigiria async que complica o código pra iniciantes

---

## ADR-002: Modelo de IA (LLM)

**Status:** Aceita  
**Data:** 18/06/2026  
**Contexto:** O tutor precisa de um LLM capaz de responder sobre programação com qualidade didática, respeitando instruções complexas de persona.

**Opções consideradas:**
1. Claude (Anthropic) — Opus 4.8 / Sonnet 4.6
2. GPT-4o (OpenAI)
3. Gemini (Google)
4. Modelos open-source (Llama, Mistral)

**Decisão:** Claude Opus 4.8 (primário) + Claude Sonnet 4.6 (fallback), ambos com effort medium

**Motivo:**
- Opus 4.8 oferece qualidade máxima de resposta didática; effort medium equilibra custo e latência
- Sonnet 4.6 como fallback garante disponibilidade se Opus falhar ou estourar rate limit
- Excelente seguimento de instruções (system prompt com persona complexa)
- API simples e bem documentada
- Custo acessível pro volume acadêmico com effort medium
- Time já tem familiaridade com a API
- Open-source exigiria infra de GPU que não temos

---

## ADR-003: Estratégia de Persistência

**Status:** Aceita  
**Data:** 21/06/2026  
**Contexto:** A aplicação precisa armazenar dados de usuário (sessões, XP, métricas) e conteúdo estático (rota, exercícios). Deploy em Railway tem filesystem efêmero.

**Opções consideradas:**
1. Tudo em JSON (filesystem)
2. Tudo em SQLite
3. PostgreSQL direto
4. Híbrido: JSON (conteúdo estático) + SQLAlchemy (SQLite local / PostgreSQL prod)

**Decisão:** Híbrido (opção 4)

**Motivo:**
- JSON atende requisito obrigatório de "leitura/escrita de arquivos" na rubrica
- SQLite local permite dev rápido sem setup
- PostgreSQL no Railway garante persistência entre deploys e concorrência real
- SQLAlchemy abstrai a diferença — mesmo código, troca via DATABASE_URL
- Ganha bônus de +5 pontos por usar banco relacional

---

## ADR-004: Autenticação

**Status:** Aceita  
**Data:** 21/06/2026  
**Contexto:** Precisamos identificar o aluno para persistir progresso entre sessões e devices, e vincular métricas (NPS, feedback) a usuários reais.

**Opções consideradas:**
1. Sem autenticação (sessão anônima)
2. Email + senha próprio
3. Google OAuth apenas
4. Google OAuth + magic link

**Decisão:** Google OAuth apenas

**Motivo:**
- 100% dos alunos de IA UFCAT têm conta @discente.ufcat.edu.br (Google)
- Zero fricção — login com 1 clique, sem cadastro
- Não precisa gerenciar senhas (hash, reset, validação)
- Libs maduras disponíveis (Authlib + Flask-Login)
- Email/senha adicionaria complexidade pra atender edge case inexistente no público-alvo

---

## ADR-005: RAG — Knowledge Base

**Status:** Aceita  
**Data:** 21/06/2026  
**Contexto:** O diferencial do produto é contextualização na disciplina. O tutor precisa acessar materiais do professor para responder com relevância.

**Opções consideradas:**
1. Contexto fixo no system prompt (TXT hardcoded)
2. ChromaDB (vector store local)
3. FAISS (Meta, vector search)
4. Pinecone / Weaviate (cloud)

**Decisão:** ChromaDB

**Motivo:**
- Roda local sem servidor externo
- API Python simples, boa documentação
- Suporta embeddings de múltiplos providers
- Usa SQLite internamente (consistente com nossa stack)
- Fallback: se ChromaDB der problema, contexto fixo via TXT em memória resolve pro MVP
- Cloud (Pinecone) seria dependência desnecessária e custo

---

## ADR-006: Arquitetura de Agentes (POO)

**Status:** Aceita  
**Data:** 18/06/2026  
**Contexto:** Requisito acadêmico exige POO com herança. A visão futura é multi-disciplina (cada matéria tem seu agente).

**Opções consideradas:**
1. Função simples que chama a API
2. Classe única com configuração por parâmetro
3. Classe base abstrata + herança por disciplina

**Decisão:** AgentBase (abstrata) → AgenteIP (herda)

**Motivo:**
- Atende requisito obrigatório de herança
- Extensível: novo agente = nova classe que herda AgentBase e define system_prompt + kb_path
- Separa lógica genérica (API call, retry, histórico) de lógica específica (persona, contexto)
- Alinhado com visão futura de multi-disciplina

---

## ADR-007: Interface Visual

**Status:** Aceita  
**Data:** 18/06/2026  
**Contexto:** A interface precisa ser funcional, atrativa na apresentação, e viável de implementar em 4 semanas sem framework JS.

**Opções consideradas:**
1. UI genérica/corporativa
2. Visual retro 8-bit (pixel art)
3. Material Design (componentes prontos)
4. Assets de alta definição (trabalhos existentes dos integrantes)

**Decisão:** Visual retro 8-bit

**Motivo:**
- Identidade visual forte e memorável pra apresentação/mostra
- Diferencia dos outros projetos da turma
- Não exige assets pesados — CSS puro com fontes pixel
- Alinhado com público gamer/tech do curso de IA
- HTML + CSS + JS vanilla, sem dependência de framework
- Assets em alta definição (opção 4) foram descartados: aumentariam peso de carregamento e risco de travar a aplicação em conexões lentas, sem ganho proporcional na experiência

---

## ADR-008: Deploy

**Status:** Aceita  
**Data:** 21/06/2026  
**Contexto:** Requisito de bônus (+5) pede deploy em nuvem. App precisa estar acessível via URL pública na Mostra UFCAT.

**Opções consideradas:**
1. Railway
2. Render
3. Heroku
4. VPS (DigitalOcean, AWS)

**Decisão:** Railway

**Motivo:**
- Free tier suficiente pro volume acadêmico
- Addon PostgreSQL gratuito integrado
- Deploy via GitHub push (CI/CD automático)
- Variáveis de ambiente nativas
- Mais simples que VPS, mais confiável que Heroku free (descontinuado)

---

## ADR-009: Estratégia de Testes

**Status:** Aceita  
**Data:** 21/06/2026  
**Contexto:** Requisito de bônus (+5) pede pytest com ≥50% coverage.

**Opções consideradas:**
1. unittest (stdlib)
2. pytest
3. pytest + pytest-cov

**Decisão:** pytest + pytest-cov

**Motivo:**
- Sintaxe mais simples que unittest (menos boilerplate)
- pytest-cov gera relatório de coverage automático
- Fixtures facilitam mock da API Claude (sem gastar tokens em teste)
- Padrão da indústria Python

---

## ADR-010: Comportamento do Tutor — Entrega de Respostas

**Status:** Aceita  
**Data:** 21/06/2026  
**Contexto:** Definir quando o tutor deve ou não entregar a resposta direta ao aluno.

**Opções consideradas:**
1. Nunca entrega resposta (100% socrático)
2. Entrega só se o aluno pedir
3. Lógica adaptativa (tenta guiar → entrega se travar → sugere exercício)

**Decisão:** Lógica adaptativa (opção 3)

**Motivo:**
- Respeita autonomia do aluno (princípio de design do produto)
- Tutor 100% socrático frustra alunos que já tentaram várias vezes
- Se o aluno pede a resposta, tem motivo — o tutor não deve ser teimoso
- Após entregar, sugere exercício equivalente (reforça aprendizado sem forçar)
- Exercício sugerido pode ser recusado pelo aluno

---

*Novas decisões devem ser adicionadas seguindo o mesmo formato.*
