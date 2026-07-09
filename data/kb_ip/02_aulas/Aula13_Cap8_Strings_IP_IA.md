---
tipo: slide_ou_roteiro
etapa: 2
topico: strings
fonte: docs/materiais_kb/AULAS/Aula13_Cap8_Strings_IP_IA.txt
data_processamento: 2026-07-04
autor_original: Prof. Dr. Márcio de Souza Dias (UFCAT/IMTec)
status: extraido_pdf_bruto
ordem_aula: '0'
observacao: Texto extraído automaticamente do PDF; revisar figuras/diagramas que não vieram.
---

# Aula13_Cap8_Strings_IP_IA

Capítulo 8
Strings
Pense em Python – Allen B. Downey
1º Período • Bacharelado em Inteligência Artificial • UFCAT
>>> s = 'banana'
>>> s[0]
'b'
>>> s[1:4]
'ana'
>>> s[::-1]
'ananab'
>>> len(s)
6
>>> s.upper()
'BANANA'
>>> 'na' in s
True
Tópicos: Sequências • Índices • len() • Fatiamento • Imutabilidade • Busca • Métodos • Operador in • Comparação

===PAGE_BREAK===

📋
  Roteiro da Aula
2
1
Strings são sequências
Acesso por índice, indexação a partir do zero
2
len() e índices negativos
Comprimento, limite superior, índices -1 -2 ...
3
Travessia com while e for
Percorrer caractere a caractere
4
Fatiamento (slicing)
s[n:m], omissão de índices, passo
5
Strings são imutáveis
Por que não podemos alterar no lugar
6
Busca e contagem
Padrão find() e contador com loop
7
Métodos de strings
upper, lower, strip, find, replace...
8
Operador in e comparação
Verificar substrings e ordenar strings
9
Exercícios práticos
Aplicar todos os conceitos vistos

===PAGE_BREAK===

🔤
  Strings São Sequências — Índices
3
Uma string é uma coleção ordenada de caracteres. Cada caractere tem um índice inteiro começando em 0.
b
0
-6
a
1
-5
n
2
-4
a
3
-3
n
4
-2
a
5
-1
Índice positivo 
→
Índice negativo →
fruit = 'banana'
# Acesso por índice positivo:
print(fruit[0])   # 'b'  ← índice 0!
print(fruit[1])   # 'a'
print(fruit[5])   # 'a'
# Acesso por índice negativo:
print(fruit[-1])  # 'a'  ← último
print(fruit[-2])  # 'n'  ← penúltimo
# Erro clássico — índice float:
print(fruit[1.5]) # TypeError!
Começa em ZERO
fruit[0] é 'b', não 'b' no índice 1.
Cientistas da computação contam do zero!
Índice deve ser int
fruit[1.5] gera TypeError.
Variáveis e expressões inteiras são OK.
Índices negativos
fruit[-1] = último, fruit[-2] = penúltimo.
Contam de trás para a frente.

===PAGE_BREAK===

📏
  len() — Comprimento e Limites do Índice
4
len() retorna o número de caracteres. O índice válido vai de 0 até len-1. Cuidado com o off-by-one!
fruit = 'banana'
print(len(fruit))        # 6
# Índices válidos: 0, 1, 2, 3, 4, 5
# Índice 6 → IndexError!
length = len(fruit)
# last = fruit[length]  ← IndexError!
last = fruit[length - 1]  # ← correto: 'a'
# Forma idiomática com índice negativo:
last = fruit[-1]          # 'a'  ✓
# Loop com len:
i = 0
while i < len(fruit):
    print(fruit[i])
    i += 1
'banana'  →  len = 6
Índices válidos: 0 a 5
Último elemento: fruit[5] = fruit[-1] = 'a'
fruit[6] → ERRO (fora do intervalo)!
⚠
  Erro off-by-one
Erro mais comum com strings!
Sempre que acessar o último elemento:
use len(s)-1 ou simplesmente s[-1].
✅
  Boa prática
Prefira for letter in fruit: em vez
de while com índice manual.
Mais seguro e mais pythônico!

===PAGE_BREAK===

🔁
  Travessia de Strings — while vs for
5
Travessia = percorrer todos os caracteres um a um. O for é mais simples e seguro; o while oferece mais controle.
Versão com while (manual)
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index += 1
Versão com for (pythônica) ✅
fruit = 'banana'
for letter in fruit:
    print(letter)
# b a n a n a
Exemplo: Patinhos de McCloskey — concatenação no loop for
prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    print(letter + suffix)   # Jack, Kack, Lack... mas 'Ouack' e 'Quack' saem errados!

===PAGE_BREAK===

✂
  Fatiamento de Strings (Slicing)
6
Uma fatia é um segmento da string. Sintaxe: s[início:fim:passo] — inclui início, exclui fim.
M
0
o
1
n
2
t
3
y
4
 
5
P
6
y
7
t
8
h
9
o
10
n
11
s = 'Monty Python'
s = 'Monty Python'
s[0:5]    # 'Monty'   ← inclui 0, exclui 5
s[6:12]   # 'Python'
# Omitir índices:
fruit = 'banana'
fruit[:3]  # 'ban'   ← do início até 3
fruit[3:]  # 'ana'   ← de 3 até o fim
fruit[:]   # 'banana' ← cópia completa
# Com passo (step):
fruit[0:5:2] # 'bnn'  ← a cada 2 chars
fruit[::-1]  # 'ananab' ← invertida!
# Fatia vazia:
fruit[3:3]  # ''  (string vazia)
[n:m]
Inclui índice n, exclui m.
Pense: 'de n até m (exclusive)'.
[:m]
Do início até m-1.
Equivalente a [0:m].
[n:]
De n até o final.
Equivalente a [n:len(s)].
[::k]
Passo k: pega de k em k.
[::-1] inverte a string!

===PAGE_BREAK===

🔒
  Strings São Imutáveis
7
Você NÃO pode alterar um caractere de uma string existente. Deve criar uma nova string.
❌
  Tentativa de modificar in-place
greeting = 'Hello, world!'
greeting[0] = 'J'   # TypeError!
# 'str' object does not support
# item assignment
✅
  Criar uma nova string
greeting = 'Hello, world!'
new_greeting = 'J' + greeting[1:]
print(new_greeting)  # 'Jello, world!'
Por que strings são imutáveis?
# Padrão correto: criar variação com concatenação e fatiamento:
s = 'Python'
s = s[:3] + 'H' + s[4:]   # 'PytHon'
# Substituição global com replace():
s = 'banana'
s = s.replace('a', 'o')   # 'bonono'
# Strings imutáveis garantem segurança: múltiplas variáveis
# podem referenciar o mesmo objeto sem risco de corrupção.

===PAGE_BREAK===

🔍
  Busca e Contagem em Strings
8
Dois padrões fundamentais: busca (interrompe quando acha) e contador (acumula ao longo da travessia).
# PADRÃO BUSCA — retorna quando acha:
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index   # achou!
        index += 1
    return -1   # não encontrou
print(find('banana', 'n'))  # 2
print(find('banana', 'z'))  # -1
# Versão com 3ºparâmetro (onde começar):
def find_from(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1
# PADRÃO CONTADOR — acumula:
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count += 1
print(count)  # 3
# Versão como função generalizada:
def count_char(word, letter):
    count = 0
    for ch in word:
        if ch == letter:
            count += 1
    return count
print(count_char('banana', 'a'))  # 3
print(count_char('python', 'p'))  # 1

===PAGE_BREAK===

🛠
  Métodos de Strings
9
Strings possuem métodos built-in: invocados com notação de ponto  palavra.método(args). Retornam novas strings.
word = 'banana'
# Maiúsculas / minúsculas:
word.upper()        # 'BANANA'
word.lower()        # 'banana'
word.capitalize()   # 'Banana'
# Busca:
word.find('na')     # 2  ← 1ª ocorrência
word.find('na', 3)  # 4  ← a partir do índice 3
word.count('a')     # 3
# Verificação (retornam bool):
word.startswith('ban')   # True
word.endswith('ana')     # True
'123'.isdigit()          # True
'abc'.isalpha()          # True
# Substituição / limpeza:
word.replace('a', 'o')   # 'bonono'
'  olá  '.strip()        # 'olá'
Função vs Método
# Função:
len(word)
# Método:
word.upper()
word.find('a')
split(sep) Divide em lista:  'a,b'.split(',') → 
['a','b']
join(lista) '–'.join(['a','b']) → 'a–b'
in operador 'na' in 'banana' → True
format() 'Olá {}!'.format('IA') → 'Olá IA!'

===PAGE_BREAK===

🔎
  Operador in e Comparação de Strings
10
O operador 'in' verifica substrings. Os operadores == < > funcionam em ordem lexicográfica (alfabética ASCII).
# OPERADOR in — booleano:
'a' in 'banana'     # True
'seed' in 'banana'  # False
'Ban' in 'banana'   # False  (case-sensitive!)
# Uso em função:
def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)
in_both('apples', 'oranges')
# a  e  s  (letras em comum)
# COMPARAÇÃO — lexicográfica:
word = 'Pineapple'
if word == 'banana':
    print('igual')
elif word < 'banana':
    print('vem antes de banana')  # ← 
imprime!
elif word > 'banana':
    print('vem depois de banana')
# Maiúsculas ANTES de minúsculas em ASCII!
# 'P' (80) < 'b' (98) → 'Pineapple' < 
'banana'
# Normalizar para comparar:
word.lower() < 'banana'   # False (correto!)
💡
  Tabela ASCII simplificada (ordem de comparação):
'A'=65  'B'=66 ... 'Z'=90   <   'a'=97  'b'=98 ... 'z'=122
→ Toda letra MAIÚSCULA é 'menor' que qualquer letra minúscula!
Boa prática: use word.lower() antes de comparar para ignorar capitalização.

===PAGE_BREAK===

🐛
  Depuração — is_reverse com Bugs de Índice
11
Exemplo clássico do livro: função com dois erros de índice. Como diagnosticá-los sistematicamente?
❌
  Versão com 2 bugs
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2)   # BUG 1: deveria ser -1
    while j > 0:
        if word1[i] != word2[j]:  # IndexError!
            return False
        i += 1
        j -= 1
    return True  # BUG 2: não verifica j==0
✅
  Versão corrigida
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1  # corrigido
    while j >= 0:       # corrigido
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1
    return True
print(is_reverse('pots','stop'))  # True
Técnica: adicionar print de diagnóstico antes da linha com erro
while j > 0:
    print(i, j)           # ← scaffolding de debug
    if word1[i] != word2[j]:
        return False
# Saída: '0 4' → j=4 fora do intervalo de 'pots' (índices 0-3)!

===PAGE_BREAK===

📖
  Glossário — Termos do Capítulo 8
12
objeto Algo ao qual uma variável pode se referir. 
Por ora equivale a valor.
sequência Coleção ordenada de valores identificados 
por índice inteiro.
item / elemento Um dos valores individuais de uma 
sequência.
índice Inteiro que seleciona um item. Em Python 
começa sempre em 0.
fatia (slice) Segmento de string definido por intervalo 
de índices [n:m:passo].
imutável Sequência cujos itens não podem ser 
alterados no lugar.
travessia Percorrer todos os itens de uma sequência 
executando operação em cada um.
busca Travessia interrompida ao encontrar o que 
procura (retorna índice ou -1).
contador Variável inicializada em zero e 
incrementada a cada ocorrência 
encontrada.
invocação Instrução que chama um método usando 
notação de ponto.
arg. opcional Parâmetro de função/método que não é 
obrigatório.
string vazia String sem caracteres, comprimento 0. 
Representada por '' ou "".

===PAGE_BREAK===

✏
  Exercício para os Alunos
13
Exercício 1 — Reverso de String e Patinhos Corrigidos
📌
  Parte A: escreva print_reverse(s) que exibe as letras de trás para frente, uma por linha.
        Parte B: corrija o loop dos patinhos para 'Ouack' e 'Quack' aparecerem certos.
# Parte A — template:
def print_reverse(s):
    # Seu código aqui
    pass
print_reverse('Python')
# n
# o
# h
# t
# y
# P
# Parte B — patinhos BUGADO:
prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    print(letter + suffix)
# Problema: 'Ouack' e 'Quack' saem como
# 'Oack' e 'Qack'
# Corrija para gerar os nomes certos:
# Jack Kack Lack Mack Nack Ouack Pack 
Quack
💡
  Dica A: use índice negativo com while, ou use  [::-1]  para inverter.
        Dica B: verifique se letter é 'O' ou 'Q' e adicione 'u' antes de 'ack'.

===PAGE_BREAK===

✏
  Exercício para os Alunos
14
Exercício 2 — count() Generalizado e find() com Início (Exercícios 8.2 e cap. 8)
📌
  Parte A: escreva count(word, letter) que conta ocorrências de letter em word.
        Parte B: escreva find(word, letter, start) que busca a partir do índice start.
# Parte A — count generalizado:
def count(word, letter):
    # Seu código aqui
    pass
print(count('banana', 'a'))   # 3
print(count('python', 'p'))   # 1
print(count('abcabc', 'x'))   # 0
# Compare com o método built-in:
print('banana'.count('a'))    # 3
# Parte B — find com início:
def find(word, letter, start=0):
    # Seu código aqui
    pass
print(find('banana', 'a'))     # 1
print(find('banana', 'a', 2))  # 3
print(find('banana', 'a', 4))  # 5
print(find('banana', 'z'))     # -1
# Compare com o método built-in:
print('banana'.find('a', 2))   # 3
💡
  Use start=0 como valor padrão em find para torná-lo retrocompatível com a versão de 2 parâmetros.

===PAGE_BREAK===

✏
  Exercício para os Alunos
15
Exercício 3 — Análise de Bugs: any_lowercase (Exercício 8.4 do livro)
📌
  Descreva o que cada função faz (assumindo que o parâmetro seja uma string). Qual(is) está(ão) certa(s)?
any_lowercase1
❌
 Retorna na 1ª iteração — só verifica s[0]!
any_lowercase2
❌
 Testa a string literal 'c', não a variável c! Sempre True.
any_lowercase3
⚠
 Só retorna resultado do último char. Erro se s=''.
any_lowercase4
✅
 Correta! Acumula True se qualquer char for minúsculo.
any_lowercase5
⚠
 Verifica se TODOS são minúsculos, não qualquer um. Lógica 
diferente da pedida!

===PAGE_BREAK===

✏
  Exercício para os Alunos
16
Exercício 4 — Cifra de César: rotate_word() (Exercício 8.5 do livro)
📌
  Implemente rotate_word(word, n) que rotaciona cada letra da string por n posições no alfabeto.
  'A' rotacionado por 3 → 'D'  |  'Z' rotacionado por 1 → 'A'  |  'cheer' +7 → 'jolly'
  Use ord() para char → número e chr() para número → char.
# Funções úteis:
# ord('a') = 97, ord('z') = 122
# ord('A') = 65, ord('Z') = 90
# chr(97) = 'a'
# ord('c') - ord('a') = 2  → 'c' é a 2ª letra
def rotate_word(word, n):
    result = ''
    for letter in word:
        if letter.isalpha():
            # Seu código aqui
            pass
        else:
            result += letter
    return result
print(rotate_word('cheer', 7))   # 'jolly'
print(rotate_word('melon', -10)) # 'cubed'
print(rotate_word('HAL', -1))    # 'IBM' ← 2001!
💡
  Algoritmo de rotação
• 1. Obtenha a posição no alfabeto:
   pos = ord(c) - ord('a')
• 2. Some n e aplique módulo 26:
   nova_pos = (pos + n) % 26
• 3. Converta de volta:
   chr(nova_pos + ord('a'))
• Separe maiúsculas (ord('A'))
• de minúsculas (ord('a'))!

===PAGE_BREAK===

✏
  Exercício para os Alunos
17
Exercício 5 — Palíndromo com Fatiamento (Exercício 8.3 do livro)
📌
  O livro mostra que [::-1] inverte uma string. Use isso para escrever is_palindrome() em uma única linha.
        Depois compare com a versão recursiva do Capítulo 6. Qual é mais clara? Qual é mais eficiente?
Versão com fatiamento [::-1]
# Uma linha!
def is_palindrome(word):
    return word == word[::-1]
print(is_palindrome('osso'))     # True
print(is_palindrome('reviver'))  # True
print(is_palindrome('python'))   # False
print(is_palindrome(''))         # True
print(is_palindrome('a'))        # True
# Versão que ignora maiúsculas e espaços:
def is_palindrome_flex(s):
    s = s.lower().replace(' ', '')
    return s == s[::-1]
print(is_palindrome_flex('A man a plan a canal Panama'))
# True!
Versão recursiva (Cap. 6) — comparação
# Versão recursiva:
def first(w):  return w[0]
def last(w):   return w[-1]
def middle(w): return w[1:-1]
def is_palindrome_rec(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome_rec(middle(word))
# Qual é melhor?
# [::-1] → mais concisa e pythônica
# Recursiva → mais didática e
# mostra o raciocínio passo a passo

===PAGE_BREAK===

✏
  Exercício para os Alunos
18
Exercício 6 — Explorando Métodos de Strings + Mini Desafio
📌
  Parte A: explore os métodos e preveja a saída antes de executar.
        Parte B: escreva word_stats(text) que retorna estatísticas de uma frase.
# Parte A — preveja a saída (não execute ainda!):
# O que cada linha produz?
s = '  Olá, Mundo!  '
print(s.strip())           # ?
print(s.strip().lower())   # ?
print(s.strip().split())   # ?
print(s.strip().replace('Mundo', 'IA'))  # ?
print(s.strip().count('o'))              # ?
print(len(s.strip()))                    # ?
frase = 'Python é incrível'
print(frase.startswith('Python'))  # ?
print(frase.endswith('vel'))       # ?
print(frase.upper())               # ?
print(frase.find('é'))             # ?
print('IA' in frase)               # ?
# Parte B — word_stats:
def word_stats(text):
    # Retorne um dicionário com:
    # 'chars': número total de chars
    # 'chars_no_space': sem espaços
    # 'words': número de palavras
    # 'upper': contagem de maiúsculas
    # 'lower': contagem de minúsculas
    # 'digits': contagem de dígitos
    pass
texto = 'IA na UFCAT 2024!'
stats = word_stats(texto)
for k, v in stats.items():
    print(f'{k}: {v}')

===PAGE_BREAK===

📚
  Resumo do Capítulo 8 — Strings
Sequências e índices
Índice começa em 0. Negativos contam do fim. Deve ser 
inteiro!
len() e limites
len(s) = nº de chars. Válido: 0 a len-1. Use -1 para o último.
Fatiamento [::-1]
s[n:m] exclui m. Omitir = início/fim. Passo -1 inverte.
Imutabilidade
Strings não mudam. Crie novas: 'J' + s[1:] ou s.replace().
Métodos built-in
upper, lower, strip, find, replace, split, count, startswith...
Operador in
'na' in 'banana' → True. Verifica substrings booleano.
19