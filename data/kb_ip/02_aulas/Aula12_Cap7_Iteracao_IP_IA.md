---
tipo: slide_ou_roteiro
etapa: 2
topico: repeticao_recursao
fonte: docs/materiais_kb/AULAS/Aula12_Cap7_Iteracao_IP_IA.txt
data_processamento: 2026-07-04
autor_original: Prof. Dr. Márcio de Souza Dias (UFCAT/IMTec)
status: extraido_pdf_bruto
ordem_aula: '0'
observacao: Texto extraído automaticamente do PDF; revisar figuras/diagramas que não vieram.
---

# Aula12_Cap7_Iteracao_IP_IA

Capítulo 7
Iteração
Pense em Python – Allen B. Downey
1º Período • Bacharelado em Inteligência Artificial • UFCAT
x = 0
while x < 5:
    print(x)
    x = x + 1
# Saída:
# 0  1  2  3  4
while True:
    r = input('> ')
    if r == 'sair':
        break
    print(r)
Tópicos: Reatribuição • Atualização de variáveis • while • break • Raízes Quadradas • Algoritmos • Depuração por bisseção

===PAGE_BREAK===

📋
  Roteiro da Aula
2
1
Reatribuição
Atribuir novos valores a variáveis existentes
 2
Atualização de variáveis
Incremento, decremento e inicialização
3
Instrução while
Loops condicionais e fluxo de execução
 4
break
Sair do loop em qualquer ponto do corpo
5
Raízes Quadradas
Método de Newton com loop iterativo
 6
Algoritmos
O conceito de algoritmo e sua importância
7
Depuração por bisseção
Técnica eficiente para encontrar bugs
 8
Exercícios práticos
Aplicar o que aprendemos

===PAGE_BREAK===

🔄
  Reatribuição de Variáveis
3
Uma variável pode receber um novo valor a qualquer momento. O valor antigo é substituído.
Exemplo no interpretador Python
>>> x = 5
>>> x
5
>>> x = 7   # reatribuição!
>>> x
7
>>> a = 5
>>> b = a   # a e b são iguais
>>> a = 3   # apenas a muda!
>>> b
5           # b permanece 5
= é atribuição, não igualdade
Na matemática a=b implica b=a. Em Python, 'a = 7' é legal, mas 
'7 = a' gera erro!
Igualdade não é permanente
a = b torna as variáveis iguais naquele momento, mas depois 
cada uma pode mudar independentemente.
Use com cuidado
Reatribuições frequentes podem dificultar a leitura e depuração 
do código.

===PAGE_BREAK===

🔢
  Atualização de Variáveis
4
Atualização = reatribuição onde o novo valor depende do antigo. É o coração de qualquer loop!
# ERRADO — variável não inicializada:
x = x + 1   # NameError: name 'x' is not defined
# CORRETO — inicializar antes de atualizar:
x = 0        # inicialização
x = x + 1    # atualização → x agora vale 1
x = x + 1    # atualização → x agora vale 2
Inicialização
Dar valor inicial antes de usar.
x = 0   →   obrigatório!
Incremento
Aumentar valor (normalmente +1).
x = x + 1   ou   x += 1
Decremento
Diminuir valor (normalmente -1).
x = x - 1   ou   x -= 1
Atalhos Python
x += 5   x -= 3   x *= 2
x //= 2   x **= 3   x %= 4

===PAGE_BREAK===

🔁
  Instrução while — Como Funciona
5
O while repete um bloco enquanto a condição for verdadeira. Estrutura essencial para iteração controlada.
Exemplo: countdown
def countdown(n):
    while n > 0:    # condição
        print(n)    # corpo
        n = n - 1   # atualização
    print('Blastoff!')
countdown(5)
# 5
# 4
# 3
# 2
# 1
# Blastoff!
Fluxo de execução do while:
Passo 1
Avalia a condição:
verdadeira ou falsa?
Passo 2
Se FALSA: sai do while
e continua o programa.
Passo 3
Se VERDADEIRA: executa
o corpo do loop.
Passo 4
Volta ao Passo 1 e
repete o ciclo.
⚠
  O CORPO do loop deve alterar a condição! Senão: loop infinito.

===PAGE_BREAK===

🔁
  while — Exemplos: countdown, print_n e sequence
6
Três padrões clássicos de while:
# 1. Countdown — decrementa até 0:
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print('Blastoff!')
# 2. print_n — iterativo:
def print_n(s, n):
    while n > 0:
        print(s)
        n -= 1
# 3. Conjectura de Collatz — será que sempre termina?
def sequence(n):
    while n != 1:
        print(n, end=' ')
        if n % 2 == 0:   # par
            n = n // 2
        else:            # ímpar
            n = n * 3 + 1
    print(n)
sequence(3)   # 3 10 5 16 8 4 2 1
sequence(27)  # 82 termos antes de chegar em 1!
🤔
  Conjectura de Collatz: Ninguém provou ainda se este loop termina para TODOS os inteiros positivos!

===PAGE_BREAK===

⛔
  break — Saindo do Loop a Qualquer Momento
7
O break encerra o loop imediatamente, mesmo que a condição ainda seja verdadeira. Útil quando a condição de 
parada só é conhecida dentro do corpo.
Padrão: while True + break
while True:
    linha = input('> ')
    if linha == 'done':
        break      # sai do loop
    print(linha)
print('Encerrado!')
# Execução:
# > olá
# olá
# > Python
# Python
# > done
# Encerrado!
Por que usar while True + break?
Verificar a condição de parada em qualquer ponto, não só 
no topo.
Expressar 'pare quando X acontecer' em vez de 'continue 
até X não ocorrer'.
Outro uso: busca em sequência
nums = [3, 7, 2, 9, 4, 8]
i = 0
while True:
    if nums[i] > 7:
        print('Achei:', nums[i])
        break
    i += 1
# Achei: 9
⚠
  Todo while True DEVE ter um break acessível, senão o programa trava em loop infinito!
   Sempre garanta que algum caminho de execução atinja o break.

===PAGE_BREAK===

√  Raízes Quadradas — Método de Newton
8
Loops são usados para refinar estimativas iterativamente até atingir precisão desejada.
Fórmula de Newton:  y = (x + a/x) / 2
Onde 'a' é o número e 'x' é a estimativa atual. Repita até y ≈ x.
 Exemplo: √4 (resposta = 2)
a = 4
x = 3        # estimativa inicial
y = (x + a/x) / 2
print(y)     # 2.1666...
x = y
y = (x + a/x) / 2
print(y)     # 2.0064...
x = y
y = (x + a/x) / 2
print(y)     # 2.0000102...
x = y
y = (x + a/x) / 2
print(y)     # 2.0          ← convergiu!
Versão com loop while + break
import math
def mysqrt(a):
    x = a / 2.0   # estimativa inicial
    epsilon = 1e-10
    while True:
        y = (x + a/x) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return x
print(mysqrt(4))    # 2.0
print(mysqrt(9))    # 3.0
print(mysqrt(2))    # 1.4142135...

===PAGE_BREAK===

⚠
  Comparação de Floats — Armadilha Clássica
9
Nunca compare floats com == ! Floats são representações aproximadas — podem nunca ser exatamente iguais.
❌
  Versão PERIGOSA
# Pode nunca parar!
while True:
    y = (x + a/x) / 2
    if y == x:      # PERIGO!
        break       # pode nunca atingir
    x = y
✅
  Versão SEGURA com epsilon
epsilon = 1e-10  # tolerância
while True:
    y = (x + a/x) / 2
    if abs(y - x) < epsilon:
        break   # 'próximo o suficiente'
    x = y
Por que floats não são exatos?
>>> 0.1 + 0.2
0.30000000000000004   # não é 0.3!
>>> 1/3
0.3333333333333333    # aproximado!
# Solução: use abs(a - b) < epsilon em vez de a == b

===PAGE_BREAK===

🧠
  Algoritmos — O Conceito Fundamental
10
O Método de Newton é um exemplo de algoritmo: um processo mecânico para resolver uma categoria de 
problemas.
Algoritmo: processo geral e mecânico para resolver uma categoria inteira de problemas.
Não exige inteligência para ser executado — cada passo segue de uma regra clara.
Tabuada (NÃO é algoritmo)
Memorizar 100 respostas específicas. Você sabe 7×8=56, mas não tem processo geral.
Truque 'vezes 9' (É algoritmo)
n×9: escreva (n-1) como 1º dígito e (10-n) como 2º. Funciona para qualquer n!
Divisão longa (É algoritmo)
Conjunto de regras que você aplica passo a passo para dividir quaisquer dois números.
🤖
  Conexão com IA: Algoritmos de ML (gradiente descendente, backpropagation) são iterativos exatamente como o Método de Newton!

===PAGE_BREAK===

🔍
  Depuração por Bisseção — Debug Eficiente
11
100 linhas de código → 100 locais para verificar. Usar bisseção reduz para ~7 verificações!
Passo 1 — Divida ao meio
Identifique o ponto central do programa (ou perto disso). Adicione um print ou verificação no meio.
Passo 2 — Teste o meio
Execute e verifique se o valor no ponto central está correto. Se incorreto → bug está na 1ª metade.
Passo 3 — Reduza o espaço
Se correto → bug está na 2ª metade. Em 6 passos de bisseção: 100 → 50 → 25 → 12 → 6 → 3 → 1 linha!
Passo 4 — Repita
Aplique bisseção novamente na metade onde o bug está. Continue até isolar o problema.
💡
  Bisseção é O(log n): log₂(100) ≈ 7. Quanto maior o programa, maior a vantagem sobre verificação linear!

===PAGE_BREAK===

📖
  Glossário — Termos do Capítulo 7
12
Reatribuição
Atribuir um novo valor a uma variável que já existe.
Atualização
Reatribuição onde o novo valor depende do antigo (ex: x = x + 1).
Inicialização
Atribuição que dá valor inicial a uma variável antes de 
atualizá-la.
Incremento
Atualização que aumenta o valor de uma variável (normalmente 
por 1).
Decremento
Atualização que reduz o valor de uma variável.
Iteração
Execução repetida de instruções usando recursividade ou loop.
Loop infinito
Loop cuja condição de término nunca é satisfeita — programa 
trava!
Algoritmo
Processo geral e mecânico para resolver uma categoria inteira de 
problemas.

===PAGE_BREAK===

✏
  Exercício para os Alunos
13
Exercício 1 — Reescreva print_n com Iteração
📌
  Enunciado
O livro mostra print_n usando recursividade (Cap. 5). Reescreva-a usando while, sem recursividade.
A função deve imprimir a string s exatamente n vezes.
Versão recursiva (original)
# Versão recursiva — Cap. 5:
def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)
print_n('Python!', 3)
# Python!
# Python!
# Python!
Sua versão iterativa:
# Complete com while:
def print_n(s, n):
    # Seu código aqui
    pass
print_n('IA UFCAT!', 4)
# IA UFCAT!
# IA UFCAT!
# IA UFCAT!
# IA UFCAT!

===PAGE_BREAK===

✏
  Exercício para os Alunos
15
Exercício 2 — eval_loop: Calculadora Interativa (Exercício 7.2)
📌
  A função eval() avalia uma string Python. Escreva eval_loop() que:
  • Peça expressões ao usuário repetidamente  • Avalie cada uma com eval()  • Imprima o resultado
  • Pare quando o usuário digitar 'done' e exiba o valor da última expressão avaliada.
# Primeiro, experimente eval() no terminal:
# >>> eval('1 + 2 * 3')       →  7
# >>> eval('math.sqrt(25)')    →  5.0
# >>> eval('type(3.14)')       →  <class 'float'>
import math
# Implemente:
def eval_loop():
    ultimo = None
    while True:
        expr = input('Digite uma expressão (ou done): ')
        if expr == 'done':
            print('Último resultado:', ultimo)
            break
        # Seu código aqui
        pass
eval_loop()
💡
  Dicas
• Use while True + break para o loop.
• Guarde o resultado de eval() numa variável.
• Exiba o resultado de cada expressão.
• Ao encontrar 'done', imprima o último resultado.
• Pesquise: o que eval() retorna para expressões 
inválidas? Como tratar?

===PAGE_BREAK===

✏
  Exercício para os Alunos
16
Exercício 3 — estimate_pi: Série de Ramanujan (Exercício 7.3)
📌
  Srinivasa Ramanujan descobriu esta série infinita para aproximar π:
  1/π ≈ (2√2 / 9801) × Σ [ (4k)! × (1103 + 26390k) ] / [ (k!)⁴ × 396⁴ᵏ ]
  Implemente estimate_pi() usando while. Pare quando o último termo for < 1e-15.
import math
def estimate_pi():
    # Constante da série
    fator = 2 * math.sqrt(2) / 9801
    soma = 0
    k = 0
    while True:
        numerador   = math.factorial(4*k) * (1103 + 26390*k)
        denominador = (math.factorial(k) ** 4) * (396 ** (4*k))
        termo = fator * numerador / denominador
        soma += termo
        if termo < 1e-15:  # convergiu!
            break
        k += 1
    return 1 / soma
pi_est = estimate_pi()
print(f'Estimativa: {pi_est}')
print(f'math.pi:    {math.pi}')
print(f'Diferença:  {abs(pi_est - math.pi)}')

===PAGE_BREAK===

✏
  Exercício para os Alunos
17
Exercício 4 — Conjectura de Collatz: Análise e Contador
📌
  A função sequence(n) do livro implementa a Conjectura de Collatz.
Extenda-a: conte quantos passos são necessários para chegar a 1 e encontre qual n < 1000 leva mais passos.
# Parte A — conte os passos:
def collatz_passos(n):
    passos = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        passos += 1
    return passos
print(collatz_passos(3))   # quantos passos?
print(collatz_passos(27))  # famoso por 
muitos passos!
# Parte B — busca do campeão < 1000:
def maior_collatz(limite):
    maior_n = 1
    maior_p = 0
    n = 1
    while n < limite:
        p = collatz_passos(n)
        if p > maior_p:
            maior_p = p
            maior_n = n
        n += 1
    return maior_n, maior_p
n_max, p_max = maior_collatz(1000)
print(f'n={n_max} → {p_max} passos')
🧪
  Desafio bônus: trace o caminho completo de n=27. Descubra: qual o valor MÁXIMO que n atinge no caminho até 1?

===PAGE_BREAK===

✏
  Exercício para os Alunos
18
Exercício 5 — for vs while: Quando Usar Cada Um?
📌
  Reescreva cada função pedida abaixo DUAS VEZES: uma com for e outra com while.
Depois responda: qual versão ficou mais clara? Por quê?
Problema A — soma dos primeiros n inteiros:
def soma_n_for(n):     # versão com for
    # ...
def soma_n_while(n):   # versão com while
    # ...
print(soma_n_for(10))    # 55
print(soma_n_while(10))  # 55
Problema B — imprimir ímpares até N:
def impares_for(n):    # com for
    # ...
def impares_while(n):  # com while
    # ...
impares_for(10)
# 1 3 5 7 9
✅
  Use for quando...
• Número de iterações é conhecido de antemão
• Iterar sobre sequência (lista, string, range)
• Código fica mais legível e compacto
✅
  Use while quando...
• Número de iterações desconhecido (convergência)
• Condição de parada é avaliada no meio do corpo
• Loop infinito com break explícito (entrada do usuário)

===PAGE_BREAK===

📚
  Resumo do Capítulo 7 — Iteração
Reatribuição
= é atribuição, não igualdade matemática. Variáveis podem 
mudar.
Atualização
x = x + 1 (incremento) exige inicialização prévia.
while
Repete enquanto condição verdadeira. Corpo DEVE modificar 
condição.
break
Encerra o loop imediatamente. Padrão: while True + break.
Método de Newton
Convergência iterativa para √a. Use abs(y-x) < epsilon, não 
y==x.
Algoritmo
Processo mecânico para categoria de problemas (ex: 
gradiente descendente em ML!).
Próximo capítulo: Strings (Capítulo 8) — sequências, índices, fatiamento e métodos de string. 19