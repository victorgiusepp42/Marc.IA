---
tipo: slide_ou_roteiro
etapa: 2
topico: variaveis_expressoes
fonte: docs/materiais_kb/AULAS/cap2_variaveis_expressoes_instrucoes_python (1).txt
data_processamento: 2026-07-04
autor_original: Prof. Dr. Márcio de Souza Dias (UFCAT/IMTec)
status: extraido_pdf_bruto
ordem_aula: '0'
observacao: Texto extraído automaticamente do PDF; revisar figuras/diagramas que não vieram.
---

# cap2_variaveis_expressoes_instrucoes_python

# Capítulo 2
message = 'Bem-vindo!'
n = 17
pi = 3.14159
>>> n + 25
42
>>> 'Spam' * 3
'SpamSpamSpam'
# ordem das operações
resultado = 2*(3-1)
print(resultado)  # 4
Pense em Python
Capítulo 2
Variáveis,
Expressões
e Instruções
Baseado em Allen B. Downey – Pense em Python, 2ª edição
Atribuição Variáveis
Expressões Modo Script
Operações Strings
Comentários Depuração

===PAGE_BREAK===

Instruções de Atribuição
VARIÁVEIS
Definição: Uma instrução de atribuição cria uma nova variável e atribui um valor a ela usando o operador =.
>>> message = 'And now for something completely different'
>>> n = 17
>>> pi = 3.141592653589793
message  →  str (texto / string)
n  →  int (número inteiro)
pi  →  float (ponto flutuante)
Diagrama de estado:
message → 'And now for something...'
n → 17
pi → 3.141592653589793
💡
 Lembre-se
= não é igualdade matemática!
É 
atribuição: avalia a expressão do lado
direito e armazena na variável
do lado esquerdo.

===PAGE_BREAK===

Nomes de Variáveis
REGRAS & CONVENÇÕES
✅
  Permitido
Letras, números e _ (sublinhado)
Qualquer comprimento
Convenção: letras minúsculas
Ex.: nome, total_2025, velocidade_m_s
❌
  Proibido
Começar com número  (76trombones)
Caracteres especiais  (more@, preco-venda)
Palavras-chave reservadas  (class, if)
Espaços em branco no nome
>>> 76trombones = 'big parade'
SyntaxError: invalid syntax
>>> more@ = 1000000
SyntaxError: invalid syntax
>>> class = 'Advanced Zymurgy'
SyntaxError: invalid syntax
🔑
 Palavras-chave do Python 3
False  None  True  and  as  assert  break  class  continue  
def  del  elif  else  except  finally  for  from  global  if  
import  in  is  lambda  nonlocal  not  or  pass  raise  
return  try  while  with  yield
💡
  Editores de código colorem palavras-chave diferente — você perceberá o conflito automaticamente!

===PAGE_BREAK===

Expressões e Instruções
CONCEITOS CENTRAIS
🔢
  Expressão
Combinação de valores, variáveis e operadores avaliada pelo 
interpretador, produzindo um único valor.
>>> 42
42
>>> n    # n = 17
17
>>> n + 25
42
💡
 No modo interativo, o interpretador exibe o resultado automaticamente.
⚡
  Instrução
Unidade de código que tem um efeito (criar variável, exibir, etc.). Em 
geral, não produz valor visível.
>>> n = 17       # atribuição
>>> print(n)     # exibição
17
💡
 O interpretador executa a instrução e faz o que ela diz. Sem exibição 
automática no modo script.
vs

===PAGE_BREAK===

Modo Script
ARQUIVO .py
Aspecto Modo Interativo (REPL) Modo Script (.py)
Onde executar Terminal › python3 Arquivo salvo › python3 arq.py
Expressões soltas Exibe resultado automaticamente Não exibe — precisa de print()
Uso indicado Testes rápidos / exploração Programas completos e reutilizáveis
Extensão — .py (convenção)
Mesmo código, comportamentos diferentes:
# Modo interativo
>>> miles = 26.2
>>> miles * 1.61
42.182     ← exibe sozinho!
# Modo script (arquivo .py)
miles = 26.2
miles * 1.61   # silêncio!
print(miles * 1.61)  # → 42.182
⚠
  No modo script, expressões sozinhas não produzem saída. Sempre use print() para exibir resultados!

===PAGE_BREAK===

Ordem das Operações — PEMDAS
PRECEDÊNCIA
P
Parênteses
Maior precedência — força a ordem desejada
2 * (3-1) = 4      (1+1)**(5-2) = 8
E
Exponenciação  **
Segunda maior precedência
1 + 2**3 = 9  (não 27)     2 * 3**2 = 18
MD
Multiplicação / Divisão  * / // %
Mesma prioridade — avaliados da esquerda para a direita
2*3-1 = 5  (não 4)     6+4/2 = 8  (não 5)
AS
Adição / Subtração  + -
Menor prioridade — avaliados da esquerda para a direita
degrees/2*pi  →  divide primeiro, depois multiplica
💡
  Quando houver dúvida, use parênteses — deixa o código mais claro e nunca é erro!

===PAGE_BREAK===

Operações com Strings
CONCATENAÇÃO E REPETIÇÃO
Regra geral: operações matemáticas com strings são ilegais. Exceções: + e *
+   Concatenação
Une strings pelas extremidades.
>>> first = 'throat'
>>> second = 'warbler'
>>> first + second
'throatwarbler'
>>> 'Oi' + ', ' + 'mundo!'
'Oi, mundo!'
*   Repetição
Repete a string N vezes. N deve ser inteiro!
>>> 'Spam' * 3
'SpamSpamSpam'
>>> '-' * 30
'------------------------------'
>>> 'Ha' * 3 + '!'
'HaHaHa!'
❌
 Ilegais: '2'-'1'    'eggs'/'easy'    'abc'**2    2+'anos'

===PAGE_BREAK===

Comentários
BOAS PRÁTICAS
Comentários são notas em linguagem natural para explicar o código. Começam com # e são completamente ignorados pelo 
interpretador.
Comentário em linha própria
# computa a percentagem da hora que passou
percentage = (minute * 100) / 60
Comentário no final da linha
percentage = (minute * 100) / 60  # percentagem de uma hora
Comentário de múltiplas linhas
# Calcula velocidade média
# Fórmula: distância / tempo
velocidade = distancia / tempo
Bom vs mau comentário:
v = 5  # atribui 5 a v  ← redundante!❌
 v = 5  # velocidade em metros/segundo  ← útil!✅


===PAGE_BREAK===

Mapa de Conceitos do Capítulo 2
REVISÃO
📦
 Variável
Nome que referencia um valor na 
memória.
Ex.: nome = 'Ana'
= Atribuição
Cria/atualiza variável com valor.
Lado esq. recebe lado dir.
🔢
 Expressão
Combinação de valores e operadores 
que produz um único valor.
⚡
 Instrução
Comando com efeito.
Ex.: print(), n = 17
📜
 Modo Script
Código em arquivo .py executado pelo 
interpretador. Use print()!
📐
 PEMDAS
Parênteses > Expo > Mult/Div > 
Adi/Sub. Da esq. p/ dir.
🔗
 Strings
+ concatena, * repete.
Demais operações matemáticas = 
ilegais.
# Comentários
Notas para humanos iniciadas com #. 
Ignoradas pelo Python.

===PAGE_BREAK===

✏
  Exercícios Práticos
FIXAÇÃO
1 Experimentos de Atribuição
Teste no interpretador:
a) 42 = n → o que acontece?
b) x = y = 1 → é legal?
c) n = 42; (com ponto-e-vírgula) → legal?
d) xy = 5 funciona como mult.?
2 Volume da Esfera
Volume = (4/3) × π × r³
Calcule para r = 5.
Dica: use math.pi ou 3.14159.
Exiba com 2 casas decimais.
3 Custo de Livros
Preço capa: R$24,95. Desconto: 40%.
Frete: R$3,00 no 1º + R$0,75/adicional.
Custo total para 60 cópias?
4 Corrida Cronometrada
Saída 6h52. Ritmos:
• 1 km a 8min15s/km
• 3 km a 7min12s/km
• 1 km a 8min15s/km
Que horas chega em casa?
5 Operações com Strings
No interpretador:
a) 'Python' * 3 → resultado?
b) 'py' + 'thon' → resultado?
c) 'abc' - 'a' → é legal?
d) '5' + 5 → é legal? Por quê?
6 Caça ao Tipo de Erro
Classifique cada erro:
a) print('Olá'
b) x = 10 / 0
c) media = 3+4+5 / 3
d) class = 'Python'
e) n = 'abc' + 5

===PAGE_BREAK===

✅
  Gabarito — Soluções Comentadas
RESPOSTAS
# Ex.2 – Volume da esfera (r=5)
import math
r = 5
volume = (4/3) * math.pi * r**3
print(f'Volume: {volume:.2f}')  # 523.60
# Ex.3 – Custo de livros (60 cópias)
preco_capa = 24.95
preco_loja = preco_capa * (1 - 0.40)
frete = 3.00 + 0.75 * (60 - 1)
total = 60 * preco_loja + frete
print(f'R$ {total:.2f}')  # R$ 945.45
# Ex.4 – Chegada em casa
saida = 6*60 + 52              # 412 min
seg1 = 1*(8*60+15)             # 495 seg
seg2 = 3*(7*60+12)             # 1296 seg
seg3 = seg1
total_min = (seg1+seg2+seg3)/60  # ≈ 38.1
chegada = saida + total_min
h = int(chegada//60)           # 7
m = int(chegada%60)            # 30
print(f'{h:02d}:{m:02d}')      # 07:30
# Ex.5 – Strings
>>> 'Python' * 3
'PythonPythonPython'
>>> 'py' + 'thon'
'python'
>>> 'abc' - 'a'
TypeError  ← ilegal
>>> '5' + 5
TypeError  ← str e int incompatíveis
Ex.1: a)SyntaxError  b)Legal  c)Legal  d)SyntaxError Ex.6: a)Sintaxe  b)Execução  c)Semântico  d)Sintaxe  e)Execução

===PAGE_BREAK===

Glossário Rápido — Capítulo 2
REFERÊNCIA
variável  Nome que referencia um valor na memória.
atribuição  Instrução que associa um nome a um valor (operador =).
diagrama de estado  Representação gráfica de variáveis e seus valores.
palavra-chave  Palavra reservada (não pode ser nome de variável).
expressão  Combinação de valores e operadores que produz um único valor.
instrução  Comando com efeito. Ex.: print(), n = 17.
modo interativo  Digitação direta no prompt >>>; resultado exibido 
automaticamente.
modo script  Código em arquivo .py executado pelo interpretador.
concatenar  Juntar strings pelas extremidades com o operador +.
comentário  Nota para programadores iniciada por #; ignorada pelo Python.
erro de sintaxe  Viola regras gramaticais; impede execução.
exceção  Erro detectado durante a execução (RuntimeError).
erro semântico  Programa roda mas produz resultado errado — bug lógico.
Pense em Python, 2ª ed. — Allen B. Downey  |  Capítulo 2: Variáveis, Expressões e Instruções