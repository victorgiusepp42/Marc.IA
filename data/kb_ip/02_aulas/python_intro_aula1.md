---
tipo: slide_ou_roteiro
etapa: 2
topico: geral
fonte: docs/materiais_kb/AULAS/python_intro_aula1 (2).txt
data_processamento: 2026-07-04
autor_original: Prof. Dr. Márcio de Souza Dias (UFCAT/IMTec)
status: extraido_pdf_bruto
ordem_aula: '0'
observacao: Texto extraído automaticamente do PDF; revisar figuras/diagramas que não vieram.
---

# python_intro_aula1

🐍
Introdução à
Programaçãocom Python
Fundamentos essenciais para começar a programar
O que é um programa?
Execução Python
1º Programa
Operadores
Tipos
Debug

===PAGE_BREAK===

O Que É um Programa? CONCEITO FUNDAMENTAL
Definição: Um programa é uma sequência de instruções que especifica como executar uma computação.
➕
  Entrada
Receber dados do teclado, arquivo ou rede
🔧
  Processamento
Executar cálculos e operações sobre os dados
🔀
  Decisão
Verificar condições e executar ações diferentes
🔁
  Repetição
Repetir ações — geralmente com alguma variação
📤
  Saída
Exibir resultados na tela, arquivo ou rede

===PAGE_BREAK===

Execução do Python AMBIENTE & INTERPRETADOR
Python é uma linguagem interpretada — o código é lido e executado linha a linha pelo interpretador.
💻
  Modo Interativo (REPL)
Digite comandos diretamente no terminal.
O interpretador executa e mostra o resultado imediatamente.
Ideal para testes rápidos e exploração.
$ python3
>>> 2 + 3
5
>>> print('Olá!')
Olá!
📄
  Modo Script (Arquivo .py)
Escreva o código em um arquivo de texto.
Execute com o comando python3 arquivo.py.
Ideal para programas completos e reutilizáveis.
# meu_programa.py
nome = 'Maria'
print('Olá,', nome)
$ python3 meu_programa.py
Olá, Maria
Fluxo de execução:
Código fonte
(.py) →
 Interpretador
Python →
 Bytecode
(.pyc) →
 Máquina Virtual
Python →
 Resultado
na tela

===PAGE_BREAK===

O Primeiro Programa: "Olá, Mundo!"
Por tradição, o primeiro programa em qualquer linguagem exibe a mensagem "Olá, Mundo!".
# Este é o nosso primeiro programa em Python
print('Olá, Mundo!')
# Também podemos usar variáveis
nome = input('Qual é o seu nome? ')
print('Olá,', nome, '! Seja bem-vindo(a) ao Python!')
#  Linhas que começam com # são comentários — 
ignoradas pelo interpretador
print()  Função que exibe texto na tela
input()  Função que recebe texto digitado pelo 
usuário
nome =  Variável: armazena um valor na memória 
com um nome
Saída esperada:
Qual é o seu nome? Ana
Olá, Ana ! Seja bem-vindo(a) ao Python!
💡
 Dica
Strings podem usar aspas simples (') ou duplas ("). O 
resultado é o mesmo!

===PAGE_BREAK===

Operadores Aritméticos MATEMÁTICA COM PYTHON
Operador Símbolo Exemplo Resultado
Adição + 10 + 3 13
Subtração − 10 - 3 7
Multiplicação ×  * 10 * 3 30
Divisão ÷  / 10 / 3 3.3333...
Divisão inteira // 10 // 3 3  (sem decimal)
Módulo (resto) % 10 % 3 1
Exponenciação ** 2 ** 8 256
⚡
 Precedência: () → ** → * / // % → + −    (igual à matemática!)

===PAGE_BREAK===

Operadores — Exemplos Práticos
a = 10
b = 3
print(a + b)   # 13        → adição
print(a - b)   # 7         → subtração
print(a * b)   # 30        → multiplicação
print(a / b)   # 3.3333... → divisão real
print(a // b)  # 3         → divisão inteira
print(a % b)   # 1         → resto da divisão
print(a ** b)  # 1000      → 10³
# Precedência com parênteses
print(2 + 3 * 4)    # 14  (mult. antes da soma)
print((2 + 3) * 4)  # 20  (parênteses forçam soma antes)
Como o Python calcula:
2 + 3 * 4  →  2 + (3 * 4)  →  2 + 12  
→  14
2 + 3 * 4
(2+3) * 4  →  (5) * 4  →  5 * 4  →  
20
(2+3) * 4
10 // 3  →  3
10 // 3
10 % 3  →  1  (resto)
10 % 3

===PAGE_BREAK===

Valores e Tipos TIPOS DE DADOS
int Inteiro
Números inteiros (sem parte decimal)
42, -7, 0
float Ponto Flutuante
Números reais com casas decimais
3.14, -0.5, 2.0
str String (texto)
Sequência de caracteres (texto)
'Olá', "Python"
bool Booleano
Apenas dois valores: verdadeiro ou falso
True, False
complex Complexo
Números complexos (parte real + imaginária)
3+2j, 1j
🔍
 Descobrir o tipo:  type(42)   →  <class 'int'>     type('Oi')   →  <class 'str'>     type(3.14)   →  <class 
'float'>

===PAGE_BREAK===

Linguagens Formais e Naturais
🗣
  Linguagem Natural
📖
 Origem:  Evoluiu naturalmente entre pessoas
🔀
 Ambiguidade:  Alta — o contexto define o sentido
💬
 Redundância:  Alta — repetição para clareza
🎭
 Literalidade:  Baixa — expressões, metáforas
📝
 Exemplos:  Português, Inglês, Espanhol
⚙
  Linguagem Formal
🏗
 Origem:  Projetada por pessoas para fins específicos
✅
 Ambiguidade:  Nenhuma — sentido único e preciso
✂
 Redundância:  Baixa — concisa e exata
🔤
 Literalidade:  Alta — significado exato dos símbolos
💻
 Exemplos:  Python, C, SQL, notação matemática
vs
💡
 Atenção: Em linguagens formais, detalhes importam muito! Erros de sintaxe pequenos (vírgula, dois-pontos) travam o programa.

===PAGE_BREAK===

🐛
  Depuração (Debugging)
Bugs são erros no programa. Depuração é o processo de encontrá-los e corrigi-los.
Erro de Sintaxe
SyntaxError
O código viola as regras gramaticais do Python.
# Faltou os dois-pontos
if x > 0
    print(x)
SyntaxError: expected ':'
Erro de Execução
RuntimeError / Exception
Sintaticamente correto, mas falha ao executar.
a = 10
b = 0
print(a / b)  # divisão por zero!
ZeroDivisionError: division by zero
Erro Semântico
Logic Bug
O código roda sem erros, mas produz resultado 
errado.
# Quer calcular média, mas soma 
errado
media = a + b / 2  # bug!
# Correto: media = (a + b) / 2
Resultado errado sem mensagem de erro
💡
 Estratégia: Leia a mensagem de erro do fim para o início. O número da linha indica onde o Python detectou o problema.

===PAGE_BREAK===

✏
  Exercícios Práticos
1 Olá personalizado
Modifique o programa "Olá, Mundo!" para pedir o nome e a idade do usuário e 
exibir uma mensagem como: "Olá, Ana! Você tem 20 anos."
2 Calculadora básica
Peça dois números ao usuário e exiba: a soma, a subtração, a multiplicação, a 
divisão real e a divisão inteira entre eles.
3 Conversor de temperatura
Peça uma temperatura em Celsius e converta para Fahrenheit.
Fórmula: F = (C × 9/5) + 32
Exemplo: 100°C → 212°F
4 Identificar tipos
Execute no Python shell e anote os tipos:
type(42)   type(3.14)   type("Python")
type(True)   type(42 / 2)   type(42 // 2)
5 Caça ao bug 🐛
O código abaixo tem um erro semântico:
  media = 7 + 8 + 9 / 3
Qual o resultado errado? Como corrigir?
6 Desafio: IMC
Peça peso (kg) e altura (m) do usuário.
Calcule o IMC: peso / altura²
Exiba o resultado com 2 casas decimais.

===PAGE_BREAK===

✅
  Gabarito — Soluções Comentadas
# EX 1 – Olá personalizado
nome = input('Nome: ')
idade = input('Idade: ')
print(f'Olá, {nome}! Você tem {idade} anos.')
# EX 2 – Calculadora básica
a = float(input('Número 1: '))
b = float(input('Número 2: '))
print(a+b, a-b, a*b, a/b, a//b)
# EX 3 – Conversor de temperatura
c = float(input('Temperatura em °C: '))
f = (c * 9/5) + 32
print(f'{c}°C = {f}°F')
# EX 4 – Tipos
type(42)     # int
type(3.14)   # float
type('Python')  # str
type(True)   # bool
type(42/2)   # float (/ sempre float!)
type(42//2)  # int
# EX 5 – Bug: operação incorreta
# ERRADO:  media = 7 + 8 + 9 / 3  → 18.0
# CORRETO: media = (7 + 8 + 9) / 3  → 8.0
media = (7 + 8 + 9) / 3
print(media)   # 8.0
# EX 6 – IMC
peso = float(input('Peso (kg): '))
altura = float(input('Altura (m): '))
imc = peso / altura ** 2
print(f'Seu IMC é: {imc:.2f}')
💡
  f-string: f'...' permite inserir variáveis diretamente no texto com {variavel} — recurso moderno do Python 3.6+

===PAGE_BREAK===

📌
  Resumo dos Conceitos
💡
 Programa
Sequência de instruções: entrada, processamento, decisão, repetição, saída
⚙
 Execução Python
Interpretador lê e executa linha a linha. Modo interativo (REPL) ou script (.py)
👋
 Primeiro Programa
print("Olá!") exibe na tela. input() lê do usuário. Comentários com #
➕
 Operadores Aritméticos
+ − * / // % ** com precedência: () > ** > * / // % > + −
🔢
 Tipos de Dados
int (inteiro), float (real), str (texto), bool (True/False). Use type() para verificar.
🗣
 Formal vs Natural
Natural: ambígua, redundante. Formal: exata, concisa. Em código, cada detalhe 
importa!
🐛
 Depuração
Sintaxe: regra gramatical violada. Execução: falha ao rodar. Semântico: 
resultado errado.
📖
 Boas Práticas
Use nomes descritivos para variáveis. Comente o código. Teste com casos 
extremos.

===PAGE_BREAK===

🚀
Continue Aprendendo!
Você deu o primeiro passo. A jornada do programador começa com
uma linha de código — e evolui com prática e curiosidade.
📘
 docs.python.org/pt-br
🎓
 py.checkio.org (prática interativa)
📖
 Pense em Python – Allen Downey (pt-BR gratuito)
Introdução à Programação com Python