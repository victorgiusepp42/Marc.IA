---
tipo: slide_ou_roteiro
etapa: 2
topico: funcoes
fonte: docs/materiais_kb/AULAS/cap3_funcoes_python (1).txt
data_processamento: 2026-07-04
autor_original: Prof. Dr. Márcio de Souza Dias (UFCAT/IMTec)
status: extraido_pdf_bruto
ordem_aula: '0'
observacao: Texto extraído automaticamente do PDF; revisar figuras/diagramas que não vieram.
---

# cap3_funcoes_python

def saudacao(nome):
    msg = 'Olá, ' + nome
    print(msg)
>>> saudacao('Python')
Olá, Python
import math
>>> math.sqrt(16)
4.0
def dobro(x):
    return x * 2
>>> dobro(21)
42
Capítulo 3
Funções
Como organizar, reutilizar e estruturar código com funções em Python
Chamada de função Funções matemáticas
Composição Definindo funções
Parâmetros Fluxo de execução
Variáveis locais Diagrama da pilha
Funções com resultado Por que funções?
Baseado em Allen B. Downey – Pense em Python, 2ª ed.

===PAGE_BREAK===

O que é uma Função?
CONCEITO
Definição: Uma função é uma sequência nomeada de instruções que executa uma operação de computação. Ao definir uma 
função, você especifica o nome e as instruções. Depois, pode chamar a função pelo nome.
📛
  Nome
Identifica a função e permite 
chamá-la de qualquer lugar do 
programa
📥
  Parâmetros
Entradas opcionais que a função 
recebe quando chamada (entre 
parênteses)
⚙
  Corpo
Sequência de instruções que 
serão executadas — a lógica da 
função
📤
  Retorno
Valor (opcional) que a função 
devolve ao chamador após 
executar
Anatomia de uma função:
def nome_da_funcao(parametro1, parametro2):
    # corpo da função (endentado 4 espaços)
    resultado = parametro1 + parametro2
    return resultado

===PAGE_BREAK===

Chamada de Função e Funções de Conversão
FUNÇÕES EMBUTIDAS
📞
  Como funciona uma chamada
>>> type(42)
<class 'int'>
# nome_função(argumento) → valor de retorno
# 'type' recebe 42 e retorna <class 'int'>
argumento
O valor que passamos para a função na chamada
Ex: o 42 em type(42)
valor de retorno
O resultado que a função nos devolve
Ex: <class 'int'>
Funções de conversão de tipo:
int()
>>> int('32')
32
>>> int(3.99)
3  # corta a fração!
>>> int('Hello')
ValueError!
float()
>>> float(32)
32.0
>>> float('3.14')
3.14
str()
>>> str(42)
'42'
>>> str(3.14)
'3.14'

===PAGE_BREAK===

Funções Matemáticas — Módulo math
MÓDULOS
Módulo: Um arquivo que contém uma coleção de funções relacionadas. Para usá-lo, precisamos importá-lo com import math.
>>> import math
>>> math               # o objeto módulo
<module 'math' (built-in)>
# Notação de ponto: módulo.função(argumento)
>>> math.sqrt(16)      # raiz quadrada
4.0
>>> math.log10(1000)   # logaritmo base 10
3.0
Principais funções do math
math.sqrt(x) Raiz quadrada de x
math.pow(x, y) x elevado a y
math.sin / cos / tan Funções trigonométricas
math.log(x) Logaritmo natural (base e)
math.log10(x) Logaritmo base 10
math.ceil(x) Arredondamento para cima
math.floor(x) Arredondamento para baixo
math.pi π ≈ 3.14159265...
math.e e ≈ 2.71828182...
Conversão de graus → radianos:
>>> degrees = 45
>>> radians = degrees / 180.0 * math.pi
>>> math.sin(radians)
0.7071067811865476
>>> math.sqrt(2) / 2   # mesma coisa!
0.7071067811865476
💡
  Notação de ponto: math.sqrt() — especifique o módulo + ponto + nome da função. Isso evita conflitos de nomes.

===PAGE_BREAK===

Composição — Combinando Expressões e Funções
PODER DAS FUNÇÕES
Composição: usar o resultado de uma expressão ou chamada de função como argumento de outra função. Isso torna o código 
conciso e poderoso.
1
Nível 1 — Valor literal como argumento
x = math.sin(0.7)    # argumento: número literal
2
Nível 2 — Expressão aritmética como argumento
x = math.sin(degrees / 360.0 * 2 * math.pi)  # expressão!
3
Nível 3 — Chamada de função como argumento
x = math.exp(math.log(x + 1))  # função dentro de função!
4
Nível 4 — Composição completa em atribuição
# Calcula a hipotenusa de um triângulo retângulo
hip = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
⚠
  Exceção: O lado esquerdo de uma atribuição DEVE ser um nome de variável — nunca uma expressão!   hours * 60 = minutes  # ❌
 
SyntaxError!

===PAGE_BREAK===

Como Definir Suas Próprias Funções
def
Estrutura de uma definição de função:
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
def  → palavra-chave print_lyrics  → nome da função ()  → sem parâmetros :  → cabeçalho termina com dois-pontos
📝
Cabeçalho
Primeira linha — sempre termina com dois-pontos (:). Contém def, 
nome e parâmetros.
📦
Corpo
Restante das instruções, todas endentadas com 4 espaços. Executa 
quando a função é chamada.
🔤
Nomenclatura
Mesmas regras das variáveis: letras, números e _. Não pode começar 
com número.
🔒
Objeto de função
Definir a função cria um objeto de função. As instruções dentro NÃO 
executam até ser chamada.
💡
  A definição precisa vir ANTES da chamada! O Python lê o código de cima para baixo.

===PAGE_BREAK===

Uso, Definições e Fluxo de Execução
ORDEM DE EXECUÇÃO
Programa completo — como o Python executa:
def print_lyrics():                    # 1. define print_lyrics
    print("I'm a lumberjack.")
    print("I sleep all night.")
def repeat_lyrics():                   # 2. define repeat_lyrics
    print_lyrics()                     #    chama print_lyrics
    print_lyrics()
repeat_lyrics()                        # 3. chama repeat_lyrics → execução!
🔄
 Fluxo de execução
1 Início em __main__
2 Define print_lyrics
(não executa corpo)
3 Define repeat_lyrics
(não executa corpo)
4 Chama repeat_lyrics
→ salta para o corpo
5 Chama print_lyrics (×2)
→ executa instruções
6 Retorna para repeat_lyrics
→ retorna para __main__
💡
 Desvio no fluxo: Uma chamada de função interrompe a execução sequencial, salta para o 
corpo da função, executa todas as instruções lá, e retorna ao ponto onde estava.
💡
  Às vezes é mais útil seguir o fluxo de execução do que ler o código de cima para baixo.

===PAGE_BREAK===

Parâmetros e Argumentos
ENTRADAS DA FUNÇÃO
Parâmetro: variável dentro da função que recebe o valor do argumento.   Argumento: o valor que passamos quando chamamos a 
função.
def print_twice(bruce):    # 'bruce' é o PARÂMETRO
    print(bruce)
    print(bruce)
A mesma função com diferentes argumentos:
>>> print_twice('Spam')      # str como argumento
Spam
Spam
>>> print_twice(42)          # int como argumento
42
42
>>> print_twice(math.pi)     # float como argumento
3.14159265359
3.14159265359
>>> print_twice('Spam ' * 4) # expressão como argumento
Spam Spam Spam Spam
Spam Spam Spam Spam
🔁
  Argumento → Parâmetro
Quem chama:
michael = 'Eric, the half a bee.'
print_twice(michael)
↓
Dentro da função:
bruce ← 'Eric, the half a bee.'
O nome da variável passada (michael) não tem relação 
com o nome do parâmetro (bruce). O valor é o mesmo!
💡
  O argumento é avaliado ANTES de ser passado. 'Spam'*4 vira 'Spam Spam Spam Spam' e então é passado para a função.

===PAGE_BREAK===

Variáveis Locais e Diagrama da Pilha
ESCOPO
Variável local: criada dentro de uma função, existe apenas dentro dela e é 
destruída quando a função termina.
def cat_twice(part1, part2):
    cat = part1 + part2   # 'cat' é local!
    print_twice(cat)
>>> line1 = 'Bing tiddle '
>>> line2 = 'tiddle bang.'
>>> cat_twice(line1, line2)
Bing tiddle tiddle bang.
Bing tiddle tiddle bang.
>>> print(cat)   # fora da função!
NameError: name 'cat' is not defined
📚
 Diagrama da Pilha
__main__
line1 → 'Bing tiddle '
line2 → 'tiddle bang.'
cat_twice
part1 → 'Bing tiddle '
part2 → 'tiddle bang.'
cat → 'Bing tiddle tiddle bang.'
print_twice
bruce → 'Bing tiddle tiddle bang.'
💡
  O traceback mostra a pilha de chamadas de baixo para cima, com a função em execução no final.

===PAGE_BREAK===

Funções com Resultado vs Funções Nulas
TIPOS DE RETORNO
🍎
  Função com resultado (fruitful)
Calcula e devolve um valor usando return. O chamador pode usar esse valor 
em expressões ou atribuições.
# Sempre produz um valor de retorno
x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2
>>> math.sqrt(5)
2.2360679774997898
# PERIGO: ignorar o retorno!
math.sqrt(5)  # calculou mas perdeu o valor
⚠
 Se ignorar o retorno em um script, o valor é perdido para sempre!
🕳
  Função nula (void)
Realiza uma ação (ex: imprimir) mas não devolve valor útil. Retorna 
implicitamente None.
>>> result = print_twice('Bing')
Bing
Bing
>>> print(result)
None
>>> type(result)
<class 'NoneType'>
⚠
 None não é a string 'None' — é um valor especial do tipo NoneType.
vs

===PAGE_BREAK===

Por que Usar Funções?
BOAS PRÁTICAS
1 📖
  Legibilidade
Nomear um grupo de instruções torna o programa mais fácil de ler e entender. 
O nome documenta a intenção do código.
# Sem função — o que faz isso?
r = a**2 * 3.14159
# Com função — claro!
area = calcular_area(raio)
2 ♻
  Reutilização
Elimina código repetitivo. Uma única definição pode ser chamada quantas vezes 
quiser, de qualquer lugar.
# Sem função: copiar e colar
print('Spam'); print('Spam')
print('Spam'); print('Spam')
# Com função
print_four_times('Spam')
3 🔧
  Depuração
Dividir o programa em funções permite testar e depurar cada parte 
isoladamente, depois reunir o todo.
def calcular_media(lista):
    # testa só essa lógica
    return sum(lista)/len(lista)
# testa isoladamente:
print(calcular_media([1,2,3]))
4 🏗
  Reaproveitamento
Funções bem projetadas funcionam em múltiplos programas. Escreva uma vez, 
use para sempre.
# Esta função serve em qualquer
# programa que precise de validação
def e_par(n):
    return n % 2 == 0
# Reutilizada em projetos futuros

===PAGE_BREAK===

✏
  Exercícios Práticos
FIXAÇÃO
1 right_justify
Escreva right_justify(s) que exibe a string com espaços à 
esquerda para que o último caractere fique na coluna 
70.
Dica: use len() para medir o comprimento.
>>> right_justify('monty')
                                                                 monty
2 do_twice e do_four
a) Crie do_twice(f) que chama a função f duas vezes.
b) Altere para do_twice(f, valor) que passa valor para f.
c) Crie do_four(f, valor) que chama f quatro vezes — 
com apenas 2 instruções no corpo!
3 Calculadora com funções
Crie as funções:
• calcular_imc(peso, altura)
• classificar_imc(imc) → 'normal', 'sobrepeso', etc.
• celsius_para_fahrenheit(c)
• segundos_para_hms(segundos) → h, min, seg
4 Funções matemáticas
Use o módulo math para criar:
• hipotenusa(a, b) → raiz de a²+b²
• area_circulo(r) → π×r²
• distancia(x1,y1,x2,y2) entre dois pontos
Teste cada função com print().
5 Traceback — caça ao bug
O código abaixo tem erros. Identifique o tipo de cada 
erro e corrija:
a) exibir_dobro(5)  
b) def soma(a b): return a+b
c) def quadrado(x): return x*x
   print(quadrado)  
6 Grau de composição
Reescreva em uma única linha usando composição:
a = math.sqrt(4)
b = math.log10(a)
c = math.floor(b)
print(c)
Depois: escreva uma função composta que receba um 
número e retorne math.floor(math.log10(math.sqrt(n))).

===PAGE_BREAK===

Glossário — Capítulo 3: Funções
REFERÊNCIA
função  Sequência nomeada de instruções que executa uma operação de 
computação.
definição de função  Instrução que cria uma função nova, especificando 
nome, parâmetros e corpo.
objeto de função  Valor criado por uma definição de função; o nome da 
função é uma variável que o referencia.
cabeçalho  Primeira linha de uma definição de função (def nome():).
corpo  Sequência de instruções endentadas dentro de uma definição de função.
parâmetro  Nome usado dentro de uma função para receber o valor passado 
como argumento.
argumento  Valor passado para uma função quando ela é chamada.
variável local  Variável definida dentro de uma função; só existe durante sua 
execução.
valor de retorno  Resultado que a função devolve ao chamador via return.
função com resultado  Função que devolve um valor (ex: math.sqrt).
função nula  Função que sempre devolve None (ex: print).
módulo  Arquivo com coleção de funções relacionadas (ex: math).
notação de ponto  Sintaxe módulo.função() para acessar funções de um 
módulo.
composição  Usar o resultado de uma expressão como argumento de outra 
função.
fluxo de execução  Ordem em que as instruções são executadas pelo Python.
diagrama da pilha  Representação gráfica das funções em execução, seus 
frames e variáveis.
frame  Caixa no diagrama da pilha representando uma chamada de função.
traceback  Lista de funções em execução exibida quando ocorre uma exceção.
Pense em Python, 2ª ed. — Allen B. Downey  |  Capítulo 3: Funções