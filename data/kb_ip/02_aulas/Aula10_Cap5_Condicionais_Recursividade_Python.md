---
tipo: slide_ou_roteiro
etapa: 2
topico: condicionais
fonte: docs/materiais_kb/AULAS/Aula10_Cap5_Condicionais_Recursividade_Python (4).txt
data_processamento: 2026-07-04
autor_original: Prof. Dr. Márcio de Souza Dias (UFCAT/IMTec)
status: extraido_pdf_bruto
ordem_aula: '0'
observacao: Texto extraído automaticamente do PDF; revisar figuras/diagramas que não vieram.
---

# Aula10_Cap5_Condicionais_Recursividade_Python

UFCAT · Curso de Inteligência Artificial · 1° Período
Capítulo 5
Condicionais e 
Recursividade
Baseado em: Pense em Python — Allen B. Downey
Divisão e Módulo Booleanos Condicionais Recursividade Entrada de Dados

===PAGE_BREAK===

📋  Agenda do Capítulo
01Divisão pelo Piso e Módulo
Operadores // e %
02Expressões Booleanas
True, False e operadores relacionais
03Operadores Lógicos
and, or, not
04Condicionais (if / else / elif)
Execução condicional e alternativa
05Recursividade
Funções que chamam a si mesmas
06Entrada de Teclado
Função input()
07Exercícios
Fixação do conteúdo

===PAGE_BREAK===

01Divisão pelo Piso e Módulo
Operadores // e %

===PAGE_BREAK===

01 · Divisão pelo Piso  ( // )
O operador // divide dois números e arredonda o resultado para baixo (número inteiro).
Exemplo: converter minutos em horas completas
minutes = 105
hours = minutes // 60    # resultado: 1  (ignora fração)
print(hours)              # → 1
# Divisão comum (retorna float)
print(minutes / 60)       # → 1.75
105 ÷ 60 
= 1,75  (float) 
// → 1 (inteiro)
💡  Dica:  A divisão // sempre arredonda para baixo (floor), mesmo para negativos! 
  Exemplo: -7 // 2  →  -4  (não -3)
Usos comuns do operador //
▸  Converter segundos em horas/min/seg
▸  Calcular número de páginas a imprimir
▸  Dividir elementos em grupos iguais

===PAGE_BREAK===

01 · Operador Módulo  ( % )
O operador % divide dois números e retorna o RESTO da divisão inteira.
minutes = 105
remainder = minutes % 60
print(remainder)   # → 45
n = 8
if n % 2 == 0:
    print("par")   # → par
x = 1234
print(x % 10)   # → 4
print(x % 100)  # → 34
105 % 60 = 45 
8 % 2 = 0 
1234 % 10 = 4 
7 % 3 = 1Aplicações do módulo %
▸  Paridade:  x % 2 == 0  →  par;   x % 2 != 0  →  ímpar
▸  Divisibilidade:  x % y == 0  →  x é divisível por y
▸  Ciclos/relógio:  hora % 24, minuto % 60
▸  Alternância de linhas:  if i % 2 == 0: fundo cinza

===PAGE_BREAK===

02Expressões Booleanas
True, False e Operadores Relacionais

===PAGE_BREAK===

02 · Expressões Booleanas
Uma expressão booleana é uma expressão que resulta em True (verdadeiro) ou False (falso).
 >>> type(True)
 <class 'bool'>
True e False são do tipo bool — não são strings!
Operadores Relacionais
Operador Significado Exemplo Resultado
== igual a 5 == 5 True
!= diferente de 5 != 6 True
> maior que 7 > 3 True
< menor que 2 < 1 False
>= maior ou igual 5 >= 5 True
<= menor ou igual 4 <= 3 False
⚠  Erro Comum
= (atribuição)  ≠  == (comparação)
x = 5   →  guarda o valor 5
x == 5  →  verifica se x é igual a 5
>>> 5 == 5
True
>>> 5 == 6
False
>>> 'hello' == 'world'
False
>>> 10 != 5
True
💡  Expressões booleanas são a 
base de todas as decisões 
num programa.

===PAGE_BREAK===

02 · Operadores Lógicos
Combinam expressões booleanas: and · or · not
and
Verdadeiro se AMBOS forem True
Exemplo: x > 0 and x < 10
True se 0 < x < 10
or
Verdadeiro se PELO MENOS UM for True
Exemplo: n%2==0 or n%3==0
True se div. por 2 ou 3
not
Inverte o valor booleano
Exemplo: not (x > y)
True se x <= y

===PAGE_BREAK===

03Instruções Condicionais
if · else · elif

===PAGE_BREAK===

03 · Execução Condicional  —  if
A instrução if executa um bloco de código apenas se a condição for True.
Sintaxe
if <condição>:
    <bloco de código>
# Exemplo
x = 10
if x > 0:
    print('x é positivo')
Fluxo de Execução
condição:
bloco 
if pulaFalse →
💡  Instrução pass
Quando o corpo do if não está pronto, use pass (espaço reservado): if x < 0:
    pass  # A FAZER: tratar negativos
⚠  Atenção à indentação! Python usa espaços/tabulação para definir blocos.
# Testando no Python
temperatura = 38
if temperatura > 37.5:
    print("Febre detectada!")
print("Fim do programa")
True ↓

===PAGE_BREAK===

03 · Execução Alternativa  —  if / else
Com else, garantimos que EXATAMENTE UM dos dois blocos será executado.
if x % 2 == 0:
    print('x é par')
else:
    print('x é ímpar')
Fluxo
condição:bloco if
bloco else
True ↓False ↓
Exemplo contextualizado — Inteligência Artificial:
# Sistema de classificação simples
score = float(input("Informe a pontuação: "))
if score >= 7.0:
    print("
✅ Aprovado")
else:
    print("
❌ Reprovado")
📌  Ramos (branches): as duas alternativas são chamadas de ramos porque são ramos 
no fluxo de execução — exatamente um deles sempre será executado.

===PAGE_BREAK===

03 · Condicionais Encadeadas  —  elif
Quando há mais de duas possibilidades, usamos elif (abreviação de else if).
if x < y:
    print('x é menor que y')
elif x > y:
    print('x é maior que y')
else:
    print('x e y são iguais')
Regras importantes:
✓  Não há limite para o número de elif
✓  Apenas o PRIMEIRO ramo verdadeiro é executado
✓  O else é opcional e sempre vai por último
Classificação de notas — exemplo prático:
nota = float(input("Nota: "))
if nota >= 9.0:
    conceito = "Excelente"
elif nota >= 7.0:
    conceito = "Bom"
elif nota >= 5.0:
    conceito = "Regular"
else:
    conceito = "Insuficiente"
print(f"Conceito: {conceito}")
⚠  Condicionais Aninhadas
Condicionais dentro de outras condicionais funcionam, mas deixam o código difícil de ler. 
Sempre que possível, use elif ou operadores lógicos em vez de aninhar condicionais.

===PAGE_BREAK===

04Recursividade
Funções que chamam a si mesmas

===PAGE_BREAK===

04 · O que é Recursividade?
Uma função recursiva é aquela que chama a si própria como parte de sua execução.
Exemplo clássico — contagem regressiva:
def countdown(n):
    if n <= 0:          # caso-base
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)  # chamada recursiva
>>> countdown(3)
3
2
1
Blastoff!
Diagrama da Pilha (Stack Diagram)
__main__
→
countdown
n = 3
→
countdown
n = 2
→
countdown
n = 1
→
countdown
n = 0  ← caso-base
↑ pilha cresce caso-base para execução ↑
Anatomia de uma função recursiva:
1.  Caso-base: condição de parada (sem chamada recursiva)
2.  Chamada recursiva: função chama a si mesma com argumento modificado

===PAGE_BREAK===

04 · Recursividade Infinita e Caso-Base
Toda função recursiva PRECISA de um caso-base — condição que encerra a recursão.
🚨  Recursividade Infinita — o que NUNCA fazer:
def recurse():
    recurse()   # sem caso-base!
RuntimeError: Maximum recursion
depth exceeded
Checklist para funções recursivas:
☐  Existe um caso-base?
☐  O caso-base é atingível para todos os inputs válidos?
☐  A chamada recursiva se aproxima do caso-base?
Outro exemplo — imprimir string n vezes:
def print_n(s, n):
    if n <= 0:      # caso-base
        return
    print(s)
    print_n(s, n-1) # se aproxima do caso-base
>>> print_n('IA', 3)
IA
IA
IA
💡  O Python limita a pilha em ~1000 chamadas por padrão. Isso evita que o programa trave o sistema em caso de recursão 
infinita. O limite pode ser ajustado com sys.setrecursionlimit().

===PAGE_BREAK===

04 · Mais Recursividade — Fatorial
A recursividade brilha em problemas matematicamente recursivos, como o fatorial.
Definição matemática:
n! = n × (n-1)!     com   0! = 1 (caso-base)
def factorial(n):
    if n == 0:              # caso-base
        return 1
    else:
        return n * factorial(n-1)  # recursão
print(factorial(3))  # → 6
print(factorial(5))  # → 120
Rastreamento de factorial(3):
factorial(3)
3 × factorial(2)
factorial(2)
2 × factorial(1)
factorial(1)
1 × factorial(0)
factorial(0)
retorna 1
→ 3×2×1×1 = 6Fibonacci recursivo — outro clássico:
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(6))  # → 8
⚠  Fib recursivo é ineficiente para n grande. Mais 
tarde veremos memorização!

===PAGE_BREAK===

05Entrada de Teclado
Função input()

===PAGE_BREAK===

05 · Função input()
A função input() pausa o programa e aguarda o usuário digitar algo, retornando uma string.
# Uso básico
text = input()              # aguarda o usuário digitar
# Com prompt (mensagem de instrução)
name = input('Qual o seu nome? ')
print(f'Olá, {name}!')
# Convertendo para inteiro
age = int(input('Sua idade: '))
if age >= 18:
    print('Maior de idade')
# Convertendo para float
height = float(input('Altura (m): '))
⚠  ATENÇÃO
input() SEMPRE retorna uma string. 
Para operar matematicamente, 
converta com int() ou float().
x = input('Número: ')
# x é uma string!
# x + 1 → ERRO
x = int(input('Número: '))
# agora x é inteiro ✓
🚨  ValueError — o que acontece se o usuário digitar texto em vez de número?
speed = int(input('Velocidade: '))
# Se o usuário digitar 'rápido': ValueError: invalid literal for int()
Tratamento de erros com try/except será visto em capítulos futuros!

===PAGE_BREAK===

✏Exercícios
Fixação do conteúdo — Capítulo 5

===PAGE_BREAK===

Exercício 1 · Converter Tempo (Nível: Básico)
📋  Enunciado
O módulo time fornece a função time.time() que retorna os segundos decorridos desde 1º de janeiro de 1970 (época 
UNIX). 
Escreva um script que leia a hora atual e a converta em horas, minutos, segundos e número de dias desde a época.
import time
total_segundos = int(time.time())
# Dica de estrutura
dias    = total_segundos // ?
resto   = total_segundos % ?
horas   = resto // ?
# ... complete o código
💡  Dicas:
▸  1 dia = 86.400 segundos
▸  Use // e % em cascata
▸  1 hora = 3.600 segundos
▸  1 minuto = 60 segundos
Saída esperada (exemplo):
Dias desde a época: 19858
Horas: 14
Minutos: 32
Segundos: 7
Objetivo: praticar operadores // e % em contexto real.

===PAGE_BREAK===

Exercício 2 · Teorema de Fermat (Nível: Intermediário)
📋  Enunciado
O último teorema de Fermat afirma que não existem inteiros positivos a, b, c tais que 
aⁿ + bⁿ = cⁿ  para n > 2. 
1. Escreva check_fermat(a, b, c, n) que verifique se o teorema se mantém. 
2. Escreva uma função que leia os valores do usuário e chame check_fermat.
def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("Fermat estava errado!")
    else:
        print("Isso não funciona.")
def solicitar_valores():
    a = int(input('a: '))
    # complete o restante...
💡  Dicas:
▸  a**n é a^n em Python
▸  Teste com: a=3, b=4, c=5, n=2 (triângulo!)
▸  Nenhum caso viola para n > 2
▸  Combine if / else
Reflexão: Por que é impossível encontrar um contra-exemplo? 
Dica: o teorema foi provado por Andrew Wiles em 1995 após 358 anos em aberto!
Objetivo: praticar if/else, funções e operadores aritméticos.

===PAGE_BREAK===

Exercício 3 · Formação de Triângulo (Nível: Intermediário)
📋  Enunciado
Para três segmentos formarem um triângulo, nenhum lado pode ser maior que a soma dos outros dois. 
1. Escreva is_triangle(a, b, c) que imprima 'Sim' ou 'Não'. 
2. Escreva uma função que leia os três lados do usuário e chame is_triangle.
def is_triangle(a, b, c):
    if ??? > ??? + ???:
        print('Não')
    elif ???:  # outro caso
        print('Não')
    ???:
        print('Sim')
💡  Dicas:
▸  Regra: se lado > soma dos outros dois → NÃO
▸  Teste: (12, 1, 1) → Não   (3, 4, 5) → Sim
▸  Simplifique com or
▸  Triângulo degenerado: a + b == c
Tabela de Testes:
a b c Esperado
3 4 5 Sim (triângulo retângulo)
12 1 1 Não (lado muito grande)
5 5 5 Sim (equilátero)
1 2 3 Não (degenerado)

===PAGE_BREAK===

Exercício 4 · Recursividade — Trace e do_n (Nível: Avançado)
📋  Enunciado
1. Qual é a saída de recurse(3, 0)? Desenhe o diagrama da pilha. 
2. O que acontece com recurse(-1, 0)? 
3. Escreva a função do_n(func, n) que chama func n vezes usando recursão.
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
Trace manual — preencha a tabela:
Chamada n s Ação
recurse(3, 0) 3 0 chama recurse(2, 3)
recurse(?, ?) ? ? ?
recurse(?, ?) ? ? ?
recurse(0, ?) 0 ? print(?)
Escreva a função do_n:
def do_n(func, n):
    """Chama func n vezes.
    func: qualquer função sem argumentos
    n: número de vezes (inteiro >= 0)
    """
    if n <= 0:
        ???
    ???
    do_n(func, n-1)
Uso esperado de do_n:
def diz_oi():
    print("Oi!")
do_n(diz_oi, 3)
# Saída:
# Oi!
# Oi!
# Oi!Objetivo: compreender recursividade, pilha e docstrings.

===PAGE_BREAK===

Exercício 5 · Desafio IA — Classificador com elif (Nível: Criativo)
🤖  Desafio — Inteligência Artificial
Crie um classificador simples de IMC (Índice de Massa Corporal) usando condicionais. 
O IMC é calculado como: imc = peso / altura² 
Classifique conforme a tabela da OMS: 
< 18,5 → Abaixo do peso    18,5–24,9 → Normal    25–29,9 → Sobrepeso    ≥ 30 → Obesidade
# Estrutura base — complete o código
peso   = float(input('Peso (kg): '))
altura = float(input('Altura (m): '))
imc    = peso / altura**2
print(f'IMC: {imc:.2f}')
if imc < 18.5:
    categoria = '???'
elif ???:
    ???
# ... continue
Saída esperada:
IMC: 22.86
Categoria: Normal
(Para peso=80kg, altura=1.87m)
IMC: 27.34
Categoria: Sobrepeso
🚀  Desafio extra:
Adicione um sistema de recomendação: para cada categoria, imprima uma mensagem de saúde. 
Conexão com IA: classificadores são a base de sistemas de diagnóstico médico por ML!

===PAGE_BREAK===

📚  Resumo do Capítulo 5
÷%
Divisão e Módulo
// divide e trunca; % retorna o resto
⚖
Booleanos
True/False, operadores == != > < >= <=
🔗
Lógicos
and, or, not combinam expressões
🔀
Condicionais
if, else, elif controlam o fluxo
🔁
Recursividade
Função que chama a si mesma + caso-base
⌨
input()
Lê entrada do usuário como string

===PAGE_BREAK===

Bons estudos! 
🚀
UFCAT · Curso de Inteligência Artificial · Capítulo 5
Referência: Pense em Python — Allen B. Downey (tradução de Júlio C. Nievola) 
docs.python.org  |  pythontutor.com  |  realpython.com
"A recursividade é uma das coisas mais mágicas que um programa pode fazer." — Allen Downey