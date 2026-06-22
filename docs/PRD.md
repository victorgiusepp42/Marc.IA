# PRD — Marc.IA

**Tutor inteligente para disciplinas do curso de IA**

| Campo | Valor |
|---|---|
| Produto | Marc.IA |
| Versão | 1.0 |
| Data | 21/06/2026 |
| Autor | Victor Giusepp Almeida |
| Status | Em desenvolvimento |

---

## 1. Visão do Produto

Marc.IA é uma plataforma web de ensino adaptativo com tutor IA, projetada para balizar o acesso à aprendizagem via inteligência artificial para alunos do curso de Bacharelado em Inteligência Artificial da UFCAT.

**Visão de longo prazo:** Qualquer professor faz upload de seus materiais e gera um agente tutor especializado na sua disciplina.

---

## 2. Problema

Alunos dos 2 primeiros anos do curso de IA da UFCAT vêm de contextos totalmente diferentes. Quando travam em exercícios e buscam ajuda com ferramentas de IA genéricas (ChatGPT, NotebookLM), não sabem por onde começar, se perdem em materiais dispersos e gastam esforço desproporcional para pouco resultado.

Os recursos disponíveis hoje — vídeo-aulas no YouTube, NotebookLM, listas do professor, slides — não oferecem um caminho estruturado e contextualizado. O aluno precisa saber formular bem a pergunta e filtrar respostas que podem divergir do que é esperado na disciplina.

**O problema central:** falta um recurso que balize o acesso à aprendizagem via IA, otimize o tempo de estudo e dê suporte real para quem trava — sem exigir que o aluno já saiba o que perguntar.

---

## 3. Público-Alvo

### Persona Principal

- **Quem:** Alunos do 1º e 2º ano do Bacharelado em Inteligência Artificial — UFCAT
- **Contexto:** Vêm de backgrounds variados, todos os níveis de conhecimento prévio em programação
- **Motivação:** Querem aprender — não têm problema de motivação
- **Dor:** Gastam muito esforço usando ferramentas genéricas que não são contextualizadas para a disciplina específica
- **Comportamento atual:** YouTube, ChatGPT, NotebookLM, listas de exercícios, slides do professor

### Camadas de Usuário

| Perfil | Necessidade | Como usa o Marc.IA |
|---|---|---|
| Aluno perdido | Não sabe por onde começar | Segue a rota sugerida, tutor guia passo a passo |
| Aluno intermediário | Sabe o básico, trava em tópicos específicos | Pula tópicos que domina, foca no que trava |
| Aluno avançado | Quer aprofundar ou revisar | Ignora a rota, usa o agente direto como par de estudo |

---

## 4. Diferencial Competitivo

| Ferramenta | Limitação | Marc.IA resolve |
|---|---|---|
| ChatGPT / Claude direto | Genérico, aluno precisa saber perguntar bem | Tutor contextualizado na disciplina, guia o aluno |
| YouTube | Conteúdo disperso, pode divergir do curso | Rota estruturada alinhada com a matéria |
| NotebookLM | Precisa de input do aluno pra funcionar | Caminho pronto + liberdade de explorar |
| Monitoria | Horário fixo, vergonha de perguntar | Disponível 24/7, sem julgamento |

**Diferencial central:** Marc.IA baliza o acesso à aprendizagem via IA. Oferece rota estruturada para quem precisa e liberdade total para quem não precisa, sempre com contexto da disciplina específica.

---

## PDD — Product Design Document

> As seções 5, 6 e 6.1 a seguir compõem o PDD do Marc.IA: princípios de design, comportamento do tutor e fluxo de usuário.

## 5. Princípios de Design

### 5.1 Liberdade do Aluno

O Marc.IA **não é um curso linear obrigatório**. O aluno tem autonomia total:

- Seguir a rota sugerida na ordem
- Pular etapas que já domina
- Voltar para tópicos anteriores
- Avançar livremente
- Ignorar a rota completamente e usar apenas o chat com o tutor

O produto respeita que o aluno sabe o que precisa.

### 5.2 Contextualização

Toda resposta do tutor é informada pelo contexto da disciplina — materiais do professor, estrutura do curso, estilo de avaliação. O aluno confia que a resposta é relevante para *aquela* matéria.

### 5.3 Acessibilidade ao Aprendizado

O aluno não precisa saber "promptar" bem para receber ajuda. O tutor entende o contexto e guia a conversa mesmo quando a pergunta é vaga ou mal formulada.

---

## 6. Comportamento do Tutor

O tutor (agente IA) segue uma lógica adaptativa que respeita a autonomia do aluno:

### Fluxo Principal

```
1. Aluno faz pergunta ou pede ajuda com exercício
   │
   ├─ Tutor tenta ensinar sem dar a resposta
   │   → Usa perguntas guiadas, dicas, analogias
   │   → Adapta ao nível demonstrado na conversa
   │
   ├─ Se o aluno trava após múltiplas tentativas:
   │   → Entrega a resposta
   │   → Explica o raciocínio por trás
   │   → Propõe exercício equivalente sobre o mesmo tópico
   │
   └─ Se o aluno pede a resposta diretamente:
       → Dá a resposta sem resistência
       → Explica baseado na resposta
       → Sugere exercício equivalente (aluno pode recusar)
```

### Princípios do Tutor

- Paciente e didático, usa analogias do cotidiano
- Responde no contexto do tópico ativo
- Usa histórico da sessão para adaptar profundidade
- **Nunca é teimoso** — se o aluno quer a resposta, recebe a resposta
- Celebra acertos, encoraja sem ser infantil
- Tom: informal, respeitoso, encorajador

### 6.1 Fluxo de Usuário

```
┌─────────────────────────────────────────────────────────────┐
│                    FLUXO DO ALUNO                             │
└─────────────────────────────────────────────────────────────┘

   Acessa URL
       │
       ▼
   ┌──────────┐    Não     ┌──────────────────┐
   │ Logado?  │──────────► │ Login com Google  │
   └──────────┘            └────────┬─────────┘
       │ Sim                        │
       ▼                            ▼
   ┌──────────────────────────────────────────┐
   │           TELA PRINCIPAL                  │
   │                                          │
   │  ┌─────────┐    ┌────────────────────┐  │
   │  │  ROTA   │    │   CHAT COM TUTOR   │  │
   │  │         │    │                    │  │
   │  │ Tópicos │    │  Conversa livre    │  │
   │  │ com     │    │  sobre qualquer    │  │
   │  │ status  │    │  tópico de IP      │  │
   │  │         │    │                    │  │
   │  └────┬────┘    └────────┬───────────┘  │
   │       │                   │              │
   │       ▼                   ▼              │
   │  Clica tópico      Envia mensagem       │
   │       │                   │              │
   │       ▼                   ▼              │
   │  Tutor inicia      Tutor responde       │
   │  contexto do       adaptivamente        │
   │  tópico                                  │
   │                                          │
   │  ┌──────────────────────────────────┐   │
   │  │        BARRA DE PROGRESSO        │   │
   │  │   XP: 120  │  Nível: Aprendiz   │   │
   │  └──────────────────────────────────┘   │
   └──────────────────────────────────────────┘

CAMINHOS DO ALUNO:
─────────────────
A) Segue a rota → clica próximo tópico → estuda com tutor → avança
B) Pula tópicos → vai direto no que precisa → estuda → volta se quiser
C) Ignora rota → usa só o chat → pergunta o que quiser sobre IP
D) Faz exercício → acerta (+50 XP) → avança │ erra → tutor explica
```

### 6.2 Mockup e Diagramas de Referência

- Diagrama de jornada do usuário (por persona): `docs/diagramas/diagrama_jornada_usuario.mmd`
- Wireframe ASCII: seção 7 do `CONTEXTO_PROJETO.md`
- Materiais visuais: `C:\Users\victo\Meu Drive\Introdução a Programação\Marc.IA_Projeto_IP\`

---

## 7. Escopo por Entrega

### E2 — Checkpoint de Progresso (25/06/2026)

**Objetivo:** Demonstrar progresso real ao professor. Não é avaliação final.

| Funcionalidade | Status esperado |
|---|---|
| Chat funcional com tutor contextualizado | Funcionando |
| Rota de tópicos visível | Funcionando (navegação básica) |
| Arquitetura de código limpa e modular | Implementada |
| Estrutura preparada para RAG | Definida |

**Entregáveis:** Relatório 1 página + vídeo 1-3min + repo funcional

### E3 — Produto Completo (~10/07/2026)

**Objetivo:** Entrega final para nota. Produto demonstrável na Mostra UFCAT.

| Funcionalidade | Critério |
|---|---|
| Autenticação Google OAuth | Aluno entra com @discente.ufcat.edu.br, progresso persistente entre sessões e devices |
| RAG com materiais reais do curso | Tutor usa conteúdo do professor nas respostas |
| Navegação livre na rota | Pular, voltar, avançar — qualquer ordem |
| Exercícios com feedback | Propõe, avalia, dá XP |
| Sistema de XP e níveis | Funcional e visível |
| Coleta de métricas (NPS, qualidade, Sean Ellis) | Feedback in-app vinculado ao usuário |
| Testes automatizados | ≥50% coverage |
| Deploy em nuvem | URL pública acessível |
| Documentação técnica | 3-5 páginas + README completo |
| Pôster | A1, visual 8-bit |

### Visão Futura (pós-disciplina)

- Multi-disciplina (qualquer matéria do curso)
- Upload de materiais pelo professor
- Painel analytics para o professor
- Geração automática de agente por disciplina

---

## 8. Dados e Persistência

Estratégia híbrida: **JSON para conteúdo estático + banco relacional para dados dinâmicos de usuário**.

### JSON (conteúdo estático — leitura/escrita de arquivos)

| Arquivo | Conteúdo | Acesso |
|---|---|---|
| `data/plano.json` | Rota de tópicos por disciplina | Leitura (carregado no boot) |
| `data/exercicios.json` | Banco de exercícios por tópico | Leitura |

### Banco Relacional (dados dinâmicos — bônus +5 pontos)

**Estratégia dual-environment:**
- **Desenvolvimento local:** SQLite (`data/marcia.db`) — zero config, rápido pra iterar
- **Produção (Railway):** PostgreSQL (addon gratuito) — persistente entre deploys, concorrência real

O código usa **SQLAlchemy** como ORM — mesma codebase, troca de banco via variável de ambiente (`DATABASE_URL`).

| Tabela | Campos principais | Função |
|---|---|---|
| `usuarios` | google_id, nome, email, criado_em | Cadastro via Google OAuth |
| `sessoes` | id, usuario_id, disciplina, topico_ativo, historico (JSON), xp, nivel, atualizado_em | Estado do aluno |
| `feedback` | id, usuario_id, sessao_id, mensagem_id, tipo (👍/👎 ou 1-5), criado_em | Qualidade do tutor |
| `metricas` | id, usuario_id, tipo (nps/sean_ellis), valor, criado_em | NPS e retenção |

### ChromaDB (Knowledge Base — RAG)

| Coleção | Fonte | Função |
|---|---|---|
| `kb_ip` | `data/kb_ip/*.txt` (materiais do professor) | Busca semântica — top-3 chunks por query |

**Por que híbrido:**
- JSON atende requisito obrigatório de "leitura/escrita de arquivos" da rubrica
- SQLAlchemy permite dev local com SQLite e produção com PostgreSQL sem mudar código
- Banco relacional habilita queries reais (ex: média de XP, taxa de retorno, NPS agregado)
- PostgreSQL no Railway garante dados persistentes e concorrência segura com múltiplos alunos
- ChromaDB usa SQLite internamente — consistente com a escolha

---

## 9. Métricas de Sucesso

### Métricas de Uso (automáticas via dados de sessão)

| Métrica | Como medir |
|---|---|
| Sessões ativas | Total de sessões criadas e mensagens trocadas (banco de dados) |
| Engajamento | Média de mensagens por sessão, taxa de retorno |
| Progressão | % de alunos que avançam na rota, XP médio acumulado |

### Métricas de Qualidade e Satisfação

| Métrica | Como medir |
|---|---|
| Qualidade do tutor | Avaliação por resposta (👍/👎 ou 1-5 estrelas) |
| NPS | "De 0 a 10, quanto você recomendaria o Marc.IA para um colega?" |
| Valor percebido (Sean Ellis) | "Se o Marc.IA parasse de existir hoje, como você se sentiria?" — muito desapontado / um pouco desapontado / indiferente |

### Critérios de Sucesso Funcionais

- Aluno abre → sabe o que fazer (zero fricção)
- Pergunta sobre tópico → resposta contextualizada e útil
- Trava em exercício → tutor desbloqueia com lógica adaptativa
- Navega livremente → sem bloqueios ou obrigatoriedades

---

## 10. Riscos e Mitigações

| Risco | Impacto | Prob. | Mitigação |
|---|---|---|---|
| RAG não agregar valor perceptível | Alto — diferencial fica fraco | Média | Fallback: contexto fixo via TXTs em memória. Testar com alunos reais antes da E3 |
| API key estourar durante demo | Crítico | Baixa | Cache de respostas pra demo, limitar max_tokens, monitorar uso |
| Escopo grande demais → nada 100% | Alto | Alta | PRD define corte claro E2/E3. Priorizar profundidade sobre features |
| Avaliador não entender o diferencial | Médio | Média | Demo começa pelo problema, não pela tech. Mostrar comparativo com ChatGPT |
| ChromaDB complexo demais pro prazo | Médio | Média | Alternativa simples: busca por similaridade com sentence-transformers + JSON |
| Materiais do professor insuficientes pra RAG | Médio | Baixa | Complementar com conteúdo curado pela equipe, validado contra ementa |

---

## 11. Equipe

| Integrante | Papel | Foco |
|---|---|---|
| Victor Giusepp Almeida | Coordenação técnica + Core IA | Arquitetura, agentes, RAG, PRD |
| Diogo Alves Ribeiro | Líder formal + Front-end | Interface 8-bit, UX |
| Kevynson Gabriel Silva | Back-end / DevOps | Infraestrutura, deploy, APIs |
| Natan Alves Cotinguiba Araujo | Core IA + Testes | Agentes, QA, cobertura |

---

## 12. Referências Internas

- Arquitetura técnica: `CONTEXTO_PROJETO.md`
- Backlog detalhado: `CONTEXTO_PROJETO.md` §10
- Materiais para RAG: `C:\Users\victo\Meu Drive\Introdução a Programação\`

---

*Documento vivo — atualizar conforme decisões evoluem.*
