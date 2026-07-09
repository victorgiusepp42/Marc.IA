---
tipo: slide_ou_roteiro
etapa: 2
topico: funcoes
fonte: docs/materiais_kb/AULAS/Aula_11__Cap6_Funcoes_com_Resultado_Python (2).txt
data_processamento: 2026-07-04
autor_original: Prof. Dr. Márcio de Souza Dias (UFCAT/IMTec)
status: extraido_pdf_bruto
ordem_aula: '0'
observacao: Texto extraído automaticamente do PDF; revisar figuras/diagramas que não vieram.
---

# Aula_11__Cap6_Funcoes_com_Resultado_Python

Capítulo 6
Funções com 
Resultado
Pense em Python – Allen B. Downey
1º Período • Bacharelado em Inteligência Artificial • UFCAT
def area(raio): 
    return math.pi * raio**2 
def factorial(n): 
    if n == 0: 
        return 1 
    return n * factorial(n-1)
Tópicos: Retorno de valores • Desenvolvimento incremental • Composição • Funções booleanas • Recursividade • Verificação de tipos

===PAGE_BREAK===

📋  Roteiro da Aula
2
1
Valores de retorno
Como funções devolvem resultados ao chamador
2
Desenvolvimento incremental
Escrever e testar código passo a passo
3
Composição de funções
Chamar funções dentro de funções
4
Funções booleanas
Funções que retornam True ou False
5
Mais recursividade
Fatorial e Fibonacci
6
Verificação de tipos
Guardiões e isinstance()
7
Exercícios práticos
Aplicar o que aprendemos

===PAGE_BREAK===

🔁  Revisão Rápida — Funções Nulas vs. Funções com Resultado
3
Função NULA (void)
Não retorna valor útil. 
Valor de retorno = None.
def saudar(nome): 
    print('Olá,', nome) 
saudar('Ana') 
# saída: Olá, Ana 
# retorno: None
➜  Usada para efeitos colaterais 
    (imprimir, modificar variável global...)
Função COM RESULTADO
Retorna valor que pode ser 
usado pelo chamador.
def dobrar(x): 
    return x * 2 
resultado = dobrar(5) 
print(resultado)  # 10
➜  Usado quando precisamos 
    trabalhar com o valor retornado.

===PAGE_BREAK===

🔙  A Instrução return
4
Anatomia de uma Função com Resultado
import math 
def area(raio): 
    a = math.pi * raio**2   # calcula 
    return a                 # devolve o valor 
# Usando a função: 
circulo = area(5) 
print(circulo)   # 78.53...
🔑  return termina a função 
imediatamente.
🔑  A expressão após return é 
        avaliada e devolvida.
🔑  Versão mais concisa: 
        return math.pi * 
raio**2
⚠  Código morto (dead code) 
Qualquer código após o return nunca é executado! 
def f(x): 
    return x * 2 
    print('isso nunca roda')  # ← código morto!

===PAGE_BREAK===

🔀  Múltiplos Returns — Valor Absoluto
5
Uma função pode ter vários return, um em cada ramo da condicional. 
Apenas UM é executado a cada chamada.
✅  Versão Correta
def absolute_value(x): 
    if x < 0: 
        return -x 
    else: 
        return x 
print(absolute_value(-7))  # 7 
print(absolute_value(5))   # 5
❌  Versão com Bug
def absolute_value(x): 
    if x < 0: 
        return -x 
    if x > 0: 
        return x 
# Bug: se x == 0, retorna None! 
print(absolute_value(0))  # None
💡  Boa prática: garanta que TODOS os caminhos possíveis da função tenham um return. 
        Python tem uma função integrada  abs()  que faz a mesma coisa! 
        Exemplo: abs(-7) → 7     abs(3.14) → 3.14

===PAGE_BREAK===

🛠  Desenvolvimento Incremental — O Que É?
6
Estratégia para escrever programas maiores sem se perder. 
Adicionamos e testamos pequenas partes de cada vez.
1
1. Comece funcionando
Escreva um rascunho que ao menos 
executa — mesmo que retorne 0 ou 
None. Depois evolua.
2
2. Variáveis intermediárias
Guarde resultados parciais em 
variáveis com print para inspecioná-
los. Facilita a depuração.
3
3. Remova o scaffolding
Quando funcionar, retire os prints de 
depuração. Consolide expressões se 
não prejudicar a leitura.
Problema-exemplo: calcular a distância entre dois pontos (x1,y1) e (x2,y2) usando o Teorema de Pitágoras.

===PAGE_BREAK===

🛠  Desenvolvimento Incremental — Passo a Passo
7
Problema: distância entre (x1,y1) e (x2,y2)  →  √( (x2-x1)² + (y2-y1)² )
Passo 1
Rascunho — só retornar 0
def distance(x1, y1, x2, y2): 
    return 0.0 
>>> distance(1, 2, 4, 6) 
0.0   # sintaticamente correto!
Passo 2
Calcular dx e dy
def distance(x1, y1, x2, y2): 
    dx = x2 - x1 
    dy = y2 - y1 
    print('dx:', dx, 'dy:', dy) 
    return 0.0
Passo 3
Soma dos quadrados
def distance(x1, y1, x2, y2): 
    dx = x2 - x1 
    dy = y2 - y1 
    dsquared = dx**2 + dy**2 
    print('dsquared:', dsquared) 
    return 0.0
Passo 4
Resultado final
def distance(x1, y1, x2, y2): 
    dx = x2 - x1 
    dy = y2 - y1 
    dsquared = dx**2 + dy**2 
    result = math.sqrt(dsquared) 
    return result

===PAGE_BREAK===

🧩  Composição de Funções
8
Funções podem chamar outras funções! Isso permite reutilizar código e construir soluções elegantes.
Problema: calcular a área de um círculo dado seu centro (xc, yc) e um ponto no perímetro (xp, yp)
# Já temos estas funções prontas: 
def distance(x1, y1, x2, y2):          # calcula distância 
    dx = x2 - x1 
    dy = y2 - y1 
    return math.sqrt(dx**2 + dy**2) 
def area(raio):                          # calcula área 
    return math.pi * raio**2 
# Composição — versão legível: 
def circle_area(xc, yc, xp, yp): 
    raio = distance(xc, yc, xp, yp)    # reutiliza distance! 
    resultado = area(raio)              # reutiliza area! 
    return resultado 
# Versão compacta (uma linha): 
def circle_area_v2(xc, yc, xp, yp): 
    return area(distance(xc, yc, xp, yp))

===PAGE_BREAK===

✅  Funções Booleanas
9
Funções que retornam True ou False. Ótimas para esconder testes complexos e tornar o código mais legível.
Versão verbosa (mas correta)
def is_divisible(x, y): 
    if x % y == 0: 
        return True 
    else: 
        return False
Versão concisa (preferida!)
def is_divisible(x, y): 
    return x % y == 0 
# O resultado de == já é bool!
Usando funções booleanas
# Uso direto em condicional — limpo e natural: 
if is_divisible(x, y): 
    print('x é divisível por y') 
# 
❌ ERRADO — comparação desnecessária: 
if is_divisible(x, y) == True:   # redundante! 
    print('x é divisível por y')

===PAGE_BREAK===

🛡  Verificação de Tipos — Guardiões
12
O que acontece se chamarmos  factorial(1.5)? → Recursividade infinita! Precisamos validar os argumentos.
def factorial(n): 
    # Guardiões — validam entradas antes de calcular 
    if not isinstance(n, int): 
        print('Fatorial só aceita inteiros.') 
        return None 
    elif n < 0: 
        print('Fatorial não é definido para negativos.') 
        return None 
    # Caso base 
    elif n == 0: 
        return 1 
    # Caso recursivo 
    else: 
        return n * factorial(n-1) 
print(factorial('ai'))  # Fatorial só aceita inteiros. 
print(factorial(-3))    # Fatorial não é definido para negativos. 
print(factorial(5))     # 120
isinstance(n, int) — verifica se n é do tipo int  •  isinstance(x, float) — verifica float  •  
isinstance(s, str) — verifica string

===PAGE_BREAK===

🐛  Depuração — Scaffolding e Dicas
13
Ao depurar funções com resultado, adicione prints estratégicos para rastrear o fluxo.
def factorial(n): 
    espacos = ' ' * (4 * n) 
    print(espacos, 'factorial', n)    # scaffolding 
    if n == 0: 
        print(espacos, 'retornando 1') 
        return 1 
    else: 
        recurse = factorial(n-1) 
        result = n * recurse 
        print(espacos, 'retornando', result) 
        return result 
# Saída de factorial(3): 
#             factorial 3 
#          factorial 2 
#       factorial 1 
#    factorial 0 
#    retornando 1 
#       retornando 1 
#          retornando 2 
#             retornando 6
1. Verifique as entradas
Imprima os parâmetros no início da função 
para confirmar que os valores corretos estão 
chegando.
2. Verifique as saídas
Imprima antes de cada return para conferir o 
valor calculado.
3. Remova o scaffolding
Após confirmar que funciona, remova os 
prints de depuração do código final.

===PAGE_BREAK===

📖  Glossário — Termos do Capítulo 6
14
Valor de retorno
Valor que uma função produz como resultado, especificado pela 
instrução return.
Variável temporária
Variável usada para guardar um resultado intermediário em um 
cálculo complexo.
Código morto (dead code)
Parte do código que nunca é executada, normalmente porque 
aparece após um return.
Desenvolvimento incremental
Adicionar e testar pequenas partes do código de cada vez, 
facilitando a depuração.
Scaffolding (código-muleta)
Código temporário usado na fase de desenvolvimento e removido 
no produto final.
Guardião (guardian)
Condicional que verifica e trata situações que poderiam causar 
erros antes de executar o código principal.

===PAGE_BREAK===

✏  Exercício para os Alunos
15
Exercício 1 — Função compare()
📌  Enunciado 
Escreva uma função  compare(x, y)  que receba dois valores e retorne: 
  • 1  se  x > y   •  0  se  x == y   •  -1  se  x < y
# Template — complete a função: 
def compare(x, y): 
    # Escreva seu código aqui 
    pass 
# Testes esperados: 
print(compare(3, 5))   # deve exibir -1 
print(compare(5, 5))   # deve exibir  0 
print(compare(8, 5))   # deve exibir  1
💡  Dicas
• Use if/elif/else para os três casos. 
• Cada ramo deve ter um return. 
• Revise: todos os caminhos retornam? 
• Teste com x negativo, zero e positivo.

===PAGE_BREAK===

✏  Exercício para os Alunos
16
Exercício 2 — Função is_between()
📌  Enunciado 
Escreva uma função booleana  is_between(x, y, z)  que retorne  True  se  x ≤ y ≤ z, 
 ou  False  caso contrário.
# Template: 
def is_between(x, y, z): 
    # Sua solução aqui 
    pass 
# Testes: 
print(is_between(1, 5, 10))  # True  (1 ≤ 5 ≤ 10) 
print(is_between(1, 0, 10))  # False (0 < 1) 
print(is_between(5, 5, 5))   # True  (5 ≤ 5 ≤ 5) 
print(is_between(3, 7, 5))   # False (7 > 5)
💡  Dicas
• Python aceita  x <= y <= z  diretamente! 
• O resultado de comparação já é bool. 
• Lembre: não compare bool com True. 
• Teste com valores nos limites (x==y, y==z).

===PAGE_BREAK===

✏  Exercício para os Alunos
17
Exercício 3 — Desenvolvimento Incremental: hipotenusa()
📌  Use desenvolvimento incremental para escrever  hypotenuse(a, b)  que retorna 
 o comprimento da hipotenusa de um triângulo retângulo. Registre cada etapa!
import math 
# Etapa 1 — rascunho (retorna 0): 
def hypotenuse(a, b): 
    return 0.0 
print(hypotenuse(3, 4))   # 0.0 — ok sintaticamente 
# Etapa 2 — calcular quadrados: 
def hypotenuse(a, b): 
    a2 = a**2 
    b2 = b**2 
    print('a2:', a2, 'b2:', b2) 
    return 0.0 
# Etapa 3 — resultado final: 
def hypotenuse(a, b): 
    soma_quadrados = a**2 + b**2 
    return math.sqrt(soma_quadrados) 
print(hypotenuse(3, 4))   # 5.0  ✓ 

===PAGE_BREAK===

✏  Exercício para os Alunos
18
Exercício 4 — Palíndromo Recursivo (Exercício 6.3 do livro)
📌  Um palíndromo lê-se igual nos dois sentidos ('osso', 'reviver'). Implemente is_palindrome(word) 
 que retorna True se a palavra é palíndromo usando as funções auxiliares below.
def first(word):     return word[0]      # primeira letra 
def last(word):      return word[-1]     # última letra 
def middle(word):    return word[1:-1]   # parte do meio 
# Implemente: 
def is_palindrome(word): 
    # Dica: caso base — palavra vazia ou 1 letra 
    # Dica: verifique first == last, depois middle 
    pass 
# Testes: 
print(is_palindrome('osso'))    # True 
print(is_palindrome('reviver')) # True 
print(is_palindrome('python'))  # False 
print(is_palindrome('a'))       # True 
print(is_palindrome(''))        # True

===PAGE_BREAK===

✏  Exercício para os Alunos
19
Exercício 5 — MDC e Potência (Exercícios 6.4 e 6.5 do livro)
Parte A — is_power(a, b)
a é potência de b se for divisível por b e a/b também for potência 
de b. Pense no caso base!
def is_power(a, b): 
    # Implemente aqui 
    pass 
print(is_power(8, 2))   # True 
print(is_power(9, 3))   # True 
print(is_power(10, 2))  # False 
print(is_power(1, 5))   # True
Parte B — gcd(a, b)
Maior divisor comum pelo algoritmo de Euclides: 
gcd(a, b) = gcd(b, r)   onde r = a % b 
Caso base: gcd(a, 0) = a
def gcd(a, b): 
    # Implemente aqui 
    pass 
print(gcd(48, 18))  # 6 
print(gcd(100, 75)) # 25 
print(gcd(7, 13))   # 1

===PAGE_BREAK===

✏  Exercício para os Alunos
20
Exercício Extra (Desafio) — Função de Ackermann
📌  A função de Ackermann A(m, n) é definida: 
  • A(0, n) = n + 1 
  • A(m, 0) = A(m−1, 1)    se m > 0 
  • A(m, n) = A(m−1, A(m, n−1))    se m > 0 e n > 0 
Implemente e teste ack(3, 4) → deve retornar 125.
def ack(m, n): 
    # Implemente aqui 
    pass 
# Testes: 
print(ack(0, 5))   # 6 
print(ack(1, 1))   # 3 
print(ack(2, 2))   # 7 
print(ack(3, 4))   # 125  ← verificar! 
# 
⚠ Cuidado: ack(4, 1) explode a recursividade! 
# Teste apenas valores pequenos de m e n.
🌐  Referência 
Ackermann Function: 
en.wikipedia.org/wiki/ 
Ackermann_function 
Esta função cresce MUITO 
rápido — ack(4,1) = 65533! 
É um exemplo de função 
total computável que não é 
primitive recursive.

===PAGE_BREAK===

📚  Resumo do Capítulo 6
return
Termina a função e devolve um valor. Todos os caminhos devem 
ter return.
Incremental
Comece com rascunho funcionando. Adicione e teste partes 
pequenas.
Composição
Chame funções dentro de funções para reutilizar código 
elegantemente.
Bool functions
Retornam True/False. Nome no estilo pergunta: is_divisible, 
is_between.
Recursividade
Função que chama a si mesma. Sempre há um caso base para 
parar.
Guardiões
isinstance() e condicionais no início para validar entradas.
Próximo capítulo: Iteração (Capítulo 7) — while, for, break e algoritmos iterativos. 21