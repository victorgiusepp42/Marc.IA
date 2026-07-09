---
nome: prova1_2026_relatorio_correcao
tipo: relatorio_correcao
etapa: transversal
topico: geral
fonte: docs/materiais_kb/Listas_Exercicios/202600434_Victor_Giusepp_Prova.txt
autor_reforma: claude-opus-4-8
data_processamento: 2026-07-04
uso: |
  Este arquivo documenta os PONTOS PERDIDOS pelo Victor na Prova 1 (2026).
  Serve pro Marc:
  - Antecipar onde o aluno VAI errar (mesmo sendo outro aluno)
  - Reforçar boas práticas quando der feedback
  - Explicar POR QUE cada erro custa nota
status: exemplo_pedagogico
---

# Prova 1 — 2026 — Relatório de correção (exemplo)

> **Aluno avaliado:** Victor Giusepp (matrícula 202600434)
> **Disciplina:** Introdução à Programação — UFCAT/IMTec
> **Professor:** Prof. Dr. Márcio de Souza Dias
> **Nota final:** 6,5 / 10,0

Este relatório é um **estudo de caso**, não uma crítica. Ele serve pro Marc entender **como o Prof. corrige** e onde alunos reais perdem pontos.

---

## 📋 Resumo da correção

| Questão | Tema | Pontos perdidos | Status |
|---|---|---|---|
| Q1 | Salário líquido + classificação por faixa | 0,0 / 2,0 | ✅ Nota máxima |
| Q2 | Produto de vetores, divisíveis por 3 | **-1,5** / 2,5 | ❌ |
| Q3 | MDC Euclides iterativo + MMC | 0,0 / 2,5 | ✅ Nota máxima |
| Q4 | Potência recursiva (só soma) + bubble sort | **-2,0** / 3,0 | ❌ |

**Total perdido:** 3,5 pontos — todos pelos **mesmos motivos**.

---

## ❌ Padrão de erros que custaram pontos

### 1. Operação errada (Q2: perdeu 1.5 pts)

> **Enunciado:** "*Produto de vetores A e B, exibição de C e elementos divisíveis por 3*"
>
> **Erro:** escreveu `c[i] = a[i] + b[i]` em vez de `c[i] = a[i] * b[i]`.

**Por que perdeu:** O enunciado diz literalmente "produto" e o aluno somou. Lê-se por alto.

### 2. Validação de constraint ausente (Q2: perdeu pts adicionais)

> **Enunciado:** "*N <= 20*" no cabeçalho
>
> **Erro:** nenhum `if` validando.

**Por que perdeu:** Aluno nem olhou a borda "N <= 20" ou esqueceu de validar.

### 3. Ignorar restrição de método (Q4: perdeu 2.0 pts — o pior)

> **Enunciado:** "*implementar potência usando **apenas** soma e recursão*"
>
> **Erro:** escreveu `return base * potencia(base, exp-1)` — o `*` é proibido.

**Por que perdeu:** A função recursiva TINHA que somar `exp` vezes o `base`. O `*` viola o constraint do enunciado.

---

## ✅ Padrões que GANHARAM pontos

### Q1 — Nota máxima (2,0/2,0)
- Constantes explícitas (`total = base+horasExtras*25`)
- Exibição limpa do salário líquido
- Classificação por faixa bem comentada
- **Lição:** estrutura clara, comentários que ajudam a ler.

### Q3 — Nota máxima (2,5/2,5)
- Função `calcMDC(a,b)` com **algoritmo de Euclides iterativo** — exatamente o método esperado
- `MMC = (a*b)/mdc` simples e correto
- **Lição:** seguir o método pedido pelo enunciado dá pontos.

---

## 🧠 O que isso ensina pro Marc

### Quando o aluno pedir código de prática ou ajuda em prova:

| Caso | Marc deve fazer |
|---|---|
| Enunciado menciona "produto" / "soma" / "diferença" | Pedir pro aluno **sublinhar** qual operação é pedida |
| Enunciado tem "N <= 20" / "restrição X" | Pedir pro aluno **listar constraints** antes de codar |
| Enunciado diz "apenas X método" | Confirmar: "Você pode usar Y? Tá nas restrições?" |
| Aluno propõe uma operação | Antes de aceitar, **reler o enunciado juntos** |

### Quando mostrar exemplo / resolução:

- Estrutura clara primeiro (quais funções, quais entradas, quais saídas)
- Constraints **literais** destacadas em comentário
- Operações seguindo o enunciado, sem "atalho"
- Comentários que AJUDAM a ler, sem barulho

---

## 💬 Mensagens-modelo do Marc (quando aluno cair nesse padrão)

**Se o aluno errar por "li por alto":**
> "Calma. Antes da gente mexer em código, vamos sublinhar juntos cada verbo do enunciado. 'Produto' é palavra-chave: você tá somando ou multiplicando?"

**Se o aluno esquecer de validar constraint:**
> "'N <= 20' tá no enunciado. O que acontece se o usuário digitar 30? O código reclama?"

**Se o aluno usar operação proibida:**
> "Releu o constraint do método? O enunciado proíbe X — qual alternativa Y a gente tem?"

**Se o aluno seguir tudo certinho:**
> "Boa. Você seguiu o método pedido, validou o constraint e operação tá certa. Esse é o nível. Mantém."

---

## 🎯 Resumo pra KB

A Prova 1 mostra que o Prof. **corrige por aderência literal** ao enunciado. Não é "código elegante" nem "código robusto" — é código que faz **exatamente** o que o enunciado pediu, nem mais nem menos.

Esse é o modo de pensar que o Marc precisa ensinar.
