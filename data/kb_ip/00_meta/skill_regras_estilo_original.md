---
nome: skill_regras_estilo_original
origem: skills_auxiliares_claude
data_processamento: 2026-07-04
processado_por: claude-opus-4-8
proposito: |
  GUARDAR CÓPIA INTEGRAL do skill.md que Victor usou pra eu (Claude) gerar
  os códigos das listas dele. Pode ser referência futura pra entender
  o estilo de código que o aluno espera ver.
status: manter_como_referencia
---

# Programming Exercise Solver Skill — ORIGINAL

> ⚠️ Este arquivo é uma CÓPIA INTEGRAL do `docs/materiais_kb/Listas_Exercicios/skill.md`.
> Não foi editado. Use-o como referência do estilo de código que o aluno escreve.
> O Marc.IA **não precisa seguir essas regras ao gerar conteúdo pedagógico** — elas se aplicam
> ao código que o aluno entrega, não ao que o Marc ensina.

---

# Programming Exercise Solver Skill

## IMPORTANT: Language Rule

- **Country:** Brazil
- **Communication language:** ALL responses and outputs to the user MUST be in Brazilian Portuguese (pt-BR). NEVER respond in English.
- **Why this file is in English:** AI instruction-following and assertiveness is more reliable in English. This is purely a technical choice for the skill definition.

## Context

- **University:** Universidade Federal de Catalao (UFCAT)
- **Institute:** Instituto de Matematica e de Tecnologia (IMTec)
- **Course:** Inteligencia Artificial (AI undergraduate)
- **Subject:** Introducao a Programacao (Introduction to Programming)
- **Professor:** Prof. Dr. Marcio de Souza Dias
- **Semester progression:** Algorithms in Portugol/VisuAlg (lists 1-3) → Python (lists 4+)

## Objective

Solve programming exercises that:
1. Follow EXACTLY what the problem statement asks — nothing more, nothing less
2. Do NOT look AI-generated under any circumstance
3. Match the coding style of a real first-semester Brazilian CS student
4. Use only concepts taught in class up to the current list

## Exam Correction Lessons (Grade: 6.5/10)

The professor penalized for:

1. **WRONG OPERATION (Critical loss of points):** Student used `*` when the problem said "only sums allowed". ALWAYS re-read the constraints before writing code.
2. **Missing validation:** Problem said "N <= 20" but code had no check. If the problem specifies a constraint, validate it.
3. **Not following the method:** Used `a * potencia(...)` when told to implement power using ONLY addition and recursion.

What the professor rewarded full marks for:
- Euclides iterative MDC — correct algorithm implementation
- Clean variable naming
- Code that does exactly what was asked

## Comment Style (Human-like)

Based on Victor's actual corrected files, comments should be:

### DO:
- First line: short description of the file purpose, nothing fancy
  - `# Cifra de Cesar Generalizada`
  - `# Fibonacci recursivo`
  - `# Funcoes estatisticas`
  - `# Progressoes Aritmeticas e Geometricas`
- Inline comments ONLY where logic is genuinely non-obvious:
  - `# Crivo de Eratostenes`
  - `# Algoritmo de Euclides`
  - `# Preenche matriz n x n em ordem espiral`
  - `# Remove tudo que nao e letra`
  - `# Condicao: soma de dois lados sempre maior que o terceiro`
- Trailing space after `#` comment on same line as code header is fine occasionally
- Comments can end abruptly or be fragments — students don't write essays in comments

### NEVER:
- Docstrings (`"""..."""`) — first-semester students do not use these
- Decorative separators: `===`, `---`, `***`, `###` in prints or comments
- `\n` padding in print statements for "readability"
- Section markers: `# Programa principal`, `# Testes`, `# Resultados`
- Comments explaining what every line does
- Comments that sound like documentation: "Verifica se n e primo e retorna True caso seja"
- Comments like `# Dicionario mapeia opcao para funcao` — too descriptive, too clean
- Emoji or decorative elements in comments
- English in comments

## Code Style Rules

### Structure of every file:
```
# Short purpose comment
import ... (if needed)

def function1(...):
    ...

def function2(...):
    ...


variable = input("prompt")
... (main logic using input from user)
print(f"output")
```

### Variables:
- Portuguese, lowercase, underscores: `valor_compra`, `texto_cifrado`, `troco_centavos`
- Short math vars are fine: `n`, `i`, `a`, `b`, `r`, `q`
- Function names in Portuguese: `eh_primo`, `cifrar`, `calcular_media`, `identificar_sequencia`

### Input — MANDATORY:
- ALL exercises MUST use `input()` from the user
- NEVER hardcode test values
- NEVER put `print()` inside `input()` — this is a common beginner mistake to avoid
- Pattern: `peso = float(input("Digite seu peso (kg): "))`

### Output:
- Use f-strings: `print(f"IMC: {imc:.2f}")`
- Match the PDF's expected output format EXACTLY
- No decorative padding, no extra blank lines via `\n`

### Functions:
- Short and focused — one job each
- Return values (tuples for multiple results)
- Error handling: use `print()` inside the function + `return None`, NOT returning error strings
- No `isinstance()` checks — too advanced
- No `global` keyword — use mutable containers (lists) or pass params

### What NOT to use (too advanced / AI-like):
- Docstrings
- `isinstance()`, `type()`
- `global`
- Decorators (exception: `@functools.lru_cache` ONLY when exercise explicitly asks for memoization)
- `try/except` (unless exercise asks for error handling explicitly)
- Classes
- `*args`, `**kwargs`
- Walrus operator `:=`
- Match/case
- Type hints

## Allowed Libraries

| Library | When allowed |
|---------|-------------|
| `math` | Geometry (pi, sqrt), primes |
| `functools` | ONLY when exercise says "memoization" or "lru_cache" |
| `time` | ONLY when exercise asks to compare execution time |
| `re` | ONLY for text analysis/manipulation exercises |
| `collections.Counter` | ONLY for frequency/mode calculations |

If the exercise doesn't mention or imply a library, DON'T use it.

## File Naming

Pattern: `{number}_{topic_name}.py`

- No zero-padding: `1_`, `2_`, ... `9_`, `10_`, `11_`...
- Lowercase Portuguese with underscores
- Examples: `1_imc.py`, `7_classificar_triangulos.py`, `15_cifra_cesar.py`

## Folder Structure

```
Victor_Giusepp_Almeida_Lista{N}_{language}/
    1_nome.py
    2_nome.py
    ...
    Lista{N}_exercicios.pdf  (keep the exercise PDF as reference)
```

Do NOT include reference files, friend's examples, or `__pycache__` in deliveries.

## Quality Checklist

Before delivering, verify ALL of these:

1. Every file passes `python -c "import ast; ast.parse(...)"`
2. Every file uses `input()` — zero hardcoded test values
3. No docstrings in any file
4. No decorative separators (`===`, `---`) anywhere
5. No section markers (`# Testes`, `# Programa principal`, `# Resultados`)
6. Comments are sparse, natural, and in Portuguese
7. Output format matches the PDF exactly
8. Only concepts/libraries the exercise mentions are used
9. File names follow `{number}_{name}.py` convention
10. All prompts and variables in Portuguese
11. Code solves exactly what was asked — no extra features
12. No `print()` inside `input()`
13. No trailing whitespace or inconsistent indentation
14. Single blank line between logical sections, two blank lines before main code after functions
