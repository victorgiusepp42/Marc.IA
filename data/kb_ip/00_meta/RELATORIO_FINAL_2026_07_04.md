# Relatório final — Construção da KB Marc.IA (IP)

**Data:** 2026-07-04
**Atualizado em:** 2026-07-05 (Lista 2 adicionada via screenshots do aluno)
**Status:** ✅ Concluído, aguardando validação do Victor.

---

## 🎯 Resultado final

| Categoria | Quantidade | Detalhe |
|---|---|---|
| **Arquivos totais na KB** | **79** | ~894KB no total |
| **Chunks no Chroma** | **391** | Indexação concluída |
| **Documentos da Origem** | 23 PDFs + 56 arquivos de código + skill.md + Prova.txt | |

---

## 📂 Estrutura final da KB

```
data/kb_ip/
├── 00_meta/                            # LEIAME + skill (origem + versão Marc)
├── 01_listas/                          # Listas 1-5 com resoluções do aluno
│   ├── lista1_portugol/                # 11 resoluções em Portugol/VisuAlg
│   ├── lista2_portugol/                # 11 resoluções
│   ├── lista3_vetores_matrizes/        # 15 resoluções (.por)
│   └── lista5_python/                  # 15 resoluções em Python
├── 02_aulas/                           # 20 PDFs extraídos com metadata
├── 03_livros/                          # Fundamentos podado + nota Pense Python
└── 04_provas/                          # Relatório da Prova 1 do Victor (revisado)
```

---

## ✅ O QUE ENTROU

### **`00_meta/`** (3 arquivos)
| Arquivo | Conteúdo |
|---|---|
| `LEIA-ME.md` | Status + instruções gerais |
| `skill_regras_estilo_original.md` | Cópia integral do skill.md original — referência |
| `skill_regras_marc.md` | Reforma do skill em guia pedagógico pro Marc (com matriz Lista×Conceitos) |

### **`01_listas/`** (52 resoluções do Victor)
- **Lista 1 (Portugol/VisuAlg)**: 11 exercícios
- **Lista 2 (Portugol/VisuAlg)**: 11 exercícios
- **Lista 3 (Vetores/Matrizes/Portugol)**: 15 exercícios (formato `.por`)
- **Lista 5 (Python)**: 15 exercícios

### **`02_aulas/`** (21 PDFs extraídos)
Aulas 0, 1, 2, 3, 9-cap5, 9-cap, 10, 11, 12, 13, 14, 15 + materiais avulsos (cap2, cap3 do livro, Funções Recursivas Portugol, exercícios de sala Python, especificação do trabalho final, prova 1, **Lista 2** — entrada tardia via screenshots) — cada um com metadata cabeçalho (etapa, tipo, tópico).

### **`03_livros/`** (2 arquivos)
- **`fundamentos_programacao_ascencio_campos.md`** — podado pra caps 1, 3, 4, 5, 6, 7, 8 (~294KB). Justificativa de cada pulo no cabeçalho.
- **`PENSE_PYTHON_NOTA.md`** — explica por que o Pense em Python ficou de fora desta leva.

### **`04_provas/`** (1 arquivo)
- `prova1_2026_relatorio_correcao.md` — reformulação do relatório original com padrões de perda de pontos e mensagens-modelo pro Marc.

---

## ⚠️ O QUE **NÃO** ENTROU (atualizado 2026-07-05)

| Item | Status |
|---|---|
| **Lista 2 (PDF escaneado)** | ✅ **Resolvido via screenshots do aluno** — transcrito pra `02_aulas/Lista_2_-_Exerccios_de_IP.md` |
| **Pense em Python (Downey)** | ⚠️ Pendente. PDF extraído veio com lixo (propaganda da Novatec no fim). Etapa 2 tá coberta pelas AULAS do Prof., então não é bloqueante. |
| **Arquivo `.key` do Prof.** | ⚠️ Pendente. Formato Keynote (Apple), sem extrator nativo. Pedir PDF exportado quando voltar a tratar. |

---

## 🧪 Validação por queries de teste (já feita)

Rodei queries em PT-BR contra o Chroma. **Resumo:**

| Query | Topo retornado | Avaliação |
|---|---|---|
| `como funcionam vetores em Portugol` | Aula 3 (Vetores/Matrizes) | ✅ |
| `como fazer função em Python` | cap3_funcoes_python + python_intro_aula1 | ✅ |
| `recursividade exemplos Python` | Aula 14 + Aula 12 | ✅ |
| `estrutura de repetição para enquanto` | Aula 2 + Fundamentos caps 5 | ✅ |
| `lista 5 exercício 8 fibonacci` | 8_fibonacci.py do aluno | ✅ perfeito |
| `algoritmo MDC` | Fundamentos (cap 8) + Lista 2 | 🟡 parcial (devolveu dedicatória no topo) |
| `strings em Python métodos` | Lista 5 (analisador_texto.py) + Aula 14 | ✅ |
| `dicionários exemplos` | Fundamentos cap 7 | 🟡 parcial (ordenação + paradigma OO em vez de dicionários) |

**Observação:** as queries funcionam, mas o **chunk 0 sempre traz o frontmatter YAML** em vez de conteúdo útil. Isso ainda é trabalho fino — pulável por agora, já que o agente responde com a parte útil dos chunks seguintes.

---

## 🎯 O QUE VALIDAÇÃO DE VOCÊ DEVE FAZER (em ordem)

### 1. **Olhar 1 PDF-aula aleatório** (`data/kb_ip/02_aulas/Aula1_Fundamentos_Computacao_Algoritmos.md`)
Verificar se a extração ficou:
- Legível
- Com metadata correta no cabeçalho
- Ordem coerente (sem cortes no meio de seção)

### 2. **Olhar 1 resolução sua** (`data/kb_ip/01_listas/lista1_portugol/resolucoes_aluno/4_media_aprov.visualg`)
Verificar se ficou idêntica ao original.

### 3. **Olhar o livro podado** (`data/kb_ip/03_livros/fundamentos_programacao_ascencio_campos.md`)
Verificar se os capítulos 1, 3, 4, 5, 6, 7, 8 entraram completos.

### 4. **Olhar o skill_regras_marc.md** (`data/kb_ip/00_meta/skill_regras_marc.md`)
Verificar se a interpretação que fiz das regras de estilo bate com o que o Prof. e você esperam que o Marc aplique.

### 5. **Decidir se vale buscar:**
- PDF do Pense em Python (talvez outra fonte)
- PDF da Lista 2 (tentar OCR ou pdfplumber)
- PDF exportado do `.key`

---

## 🚧 Próximos passos sugeridos (depois da validação)

### Fase 2 do Projeto Marc.IA
1. **Testar o agente com cenários reais** — você cola prompts de aluno no chat do Marc e a gente vê se ele acerta.
2. **Ajustar o system prompt** com base nos achados (Fase 3 da tabela que eu fiz antes).
3. **Reformatar Lista 2 com OCR** se o aluno precisar dela na prática.

### Fase 3
1. Migrar conteúdo pedagógico do `00_meta/skill_regras_marc.md` para o `system_prompt` de `src/agente_ip.py`.
2. Adicionar exemplos poucos-shot (bom diálogo socrático) na KB em `00_meta/exemplos_socraticos/`.

---

## 📍 Status atual do agente

O `src/agente_ip.py` **continua intacto**. Nenhuma alteração de comportamento ainda — toda a KB nova tá disponível pra ele consultar via RAG, mas o `system_prompt` (193 linhas) ainda é o anterior. **A reforma do prompt é a próxima rodada** depois da validação da KB.
