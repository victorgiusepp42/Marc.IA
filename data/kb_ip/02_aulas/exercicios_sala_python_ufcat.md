---
tipo: lista_exercicios
etapa: 2
topico: geral
fonte: docs/materiais_kb/AULAS/exercicios_sala_python_ufcat.txt
data_processamento: 2026-07-04
autor_original: Prof. Dr. Márcio de Souza Dias (UFCAT/IMTec)
status: extraido_pdf_bruto
ordem_aula: '0'
observacao: Texto extraído automaticamente do PDF; revisar figuras/diagramas que não vieram.
---

# exercicios_sala_python_ufcat

🐍
  Lista de Exercícios
Introdução à Programação
em Python
Bacharelado em Inteligência Artificial  ·  UFCAT
1.  Variáveis, Expressões e Instruções
2.  Funções em Python
3.  Condicionais e Recursividade
4.  Funções com Resultado, Iteração e Strings
5.  Listas, Dicionários e Tuplas
6.  Arquivos em Python

===PAGE_BREAK===

01
Tópico 1
Variáveis, Expressões
e Instruções
Tipos de dados, atribuição, operadores e entrada/saída.

===PAGE_BREAK===

1.1 — Apresentação Pessoal
Tópico 1 · Variáveis, Expressões e Instruções
Declare variáveis para armazenar seu nome, sua idade e seu curso.
Em seguida, imprima uma mensagem de apresentação usando 
essas variáveis.
Conceitos trabalhados:
• Declaração e inicialização de variáveis
• Tipos int, float e str
• Uso de f-strings para saída formatada

===PAGE_BREAK===

1.2 — Operações Básicas com Inteiros
Tópico 1 · Variáveis, Expressões e Instruções
Leia dois números inteiros digitados pelo usuário. Exiba a soma, 
subtração, multiplicação, divisão inteira e o resto da divisão.
Operadores envolvidos:
Operador Operação
  + Adição
  - Subtração
  * Multiplicação
  // Divisão inteira
  % Resto (módulo)

===PAGE_BREAK===

1.3 — Conversão de Temperatura
Tópico 1 · Variáveis, Expressões e Instruções
Leia uma temperatura em graus Celsius e converta-a para 
Fahrenheit e Kelvin.
Fórmulas:   F = C × 9/5 + 32     K = C + 273,15
Dicas:
• Use float() para leitura com casas decimais
• f-strings com :.2f formatam 2 casas decimais
• Atenção à precedência de operadores!

===PAGE_BREAK===

1.4 — Troca de Variáveis (Sem Auxiliar)
Tópico 1 · Variáveis, Expressões e Instruções
Declare duas variáveis x e y. Troque os valores entre elas SEM usar 
uma variável auxiliar. Exiba os valores antes e após a troca.
O truque do desempacotamento:
Python permite atribuição múltipla simultânea.
O lado direito é avaliado todo primeiro — por isso a troca 
funciona sem variável auxiliar!

===PAGE_BREAK===

1.5 — Cálculo do IMC
Tópico 1 · Variáveis, Expressões e Instruções
Leia o peso (kg) e a altura (m) de uma pessoa.
Calcule o IMC = peso / altura² e classifique conforme 
a tabela ao lado.
IMC Classificação
< 18,5 Abaixo do peso
18,5–24,9 Peso normal
25,0–29,9 Sobrepeso
≥ 30,0 Obesidade

===PAGE_BREAK===

02
Tópico 2
Funções em Python
Definição, parâmetros, retorno e parâmetros padrão.

===PAGE_BREAK===

2.1 — Saudação Personalizada
Tópico 2 · Funções em Python
Crie uma função chamada saudar(nome) que receba um nome 
como parâmetro e imprima:
"Olá, <nome>! Bem-vindo(a) ao curso de IA."
Chame a função com pelo menos dois nomes diferentes.
Anatomia de uma função:
def  →  palavra-chave de definição
nome_da_função  →  identificador
(parâmetros)  →  dados de entrada
corpo (indentado)  →  instruções a 
executar

===PAGE_BREAK===

2.2 — Área do Retângulo
Tópico 2 · Funções em Python
Escreva uma função area_retangulo(base, altura) que retorne a 
área de um retângulo.
Teste-a com pelo menos três pares de valores.
Diferença entre print e return:
print() → exibe, mas não devolve valor ao chamador.
return → devolve o resultado para quem chamou a função.
Use return quando o valor for usado em outro cálculo.

===PAGE_BREAK===

2.3 — Máximo de Três Números
Tópico 2 · Funções em Python
Crie uma função maximo(a, b, c) que receba três números e 
retorne o maior deles.
Restrição: não use a função embutida max().
Estratégia de solução:
1. Assuma que o primeiro é o maior.
2. Compare com o segundo; se maior, atualize.
3. Compare com o terceiro; se maior, atualize.
4. Retorne o maior encontrado.

===PAGE_BREAK===

2.4 — Fatorial Iterativo
Tópico 2 · Funções em Python
Implemente uma função fatorial(n) que calcule n! de forma 
iterativa (usando um laço for).
Garanta que a função valide n ≥ 0 e trate n = 0 corretamente.
Lembrete — Definição de fatorial:
0! = 1   (caso base)
n! = 1 × 2 × 3 × … × n
range(2, n+1) itera de 2 até n (inclusive).

===PAGE_BREAK===

2.5 — Calculadora com Parâmetros Padrão
Tópico 2 · Funções em Python
Crie uma função calcular(a, b, operacao='soma') que aceite as 
operações:
'soma', 'sub', 'mult' e 'div'.
Trate divisão por zero e operações inválidas retornando 
mensagem de erro.
Parâmetro padrão (default):
Quando definido como operacao='soma', a chamada 
calcular(10,3) usa 'soma' automaticamente.
O chamador pode sobrescrever: calcular(10,3,'div').

===PAGE_BREAK===

03
Tópico 3
Condicionais e
Recursividade
if/elif/else e funções que chamam a si mesmas.

===PAGE_BREAK===

3.1 — Positivo, Negativo ou Zero
Tópico 3 · Condicionais e Recursividade
Leia um número real do usuário e informe se ele é positivo, 
negativo ou zero.
Fluxo do if/elif/else:
• if: avalia a primeira condição.
• elif: avaliado apenas se a anterior for falsa.
• else: executado quando todas as anteriores forem falsas.
Apenas um bloco é executado por vez!

===PAGE_BREAK===

3.2 — Par ou Ímpar
Tópico 3 · Condicionais e Recursividade
Escreva uma função par_ou_impar(n) que retorne a string "par" 
ou "ímpar" conforme o valor de n.
O operador ternário:
valor_se_verdadeiro  if  condição  else  valor_se_falso
Condensa um if/else simples em uma única linha,
mantendo a clareza de leitura.

===PAGE_BREAK===

3.3 — Fibonacci Recursivo
Tópico 3 · Condicionais e Recursividade
Implemente fibonacci(n) de forma recursiva, retornando o n-ésimo 
termo.
(fibonacci(0)=0  e  fibonacci(1)=1)
Estrutura da recursão:
1. Caso base → para a recursão (n=0, n=1).
2. Caso recursivo → reduz o problema.
3. fibonacci(n) chama fibonacci(n-1) e fibonacci(n-2)
   até atingir os casos base.
Atenção: essa versão é exponencial em tempo (O(2ⁿ)).

===PAGE_BREAK===

3.4 — Potência Recursiva
Tópico 3 · Condicionais e Recursividade
Escreva potencia(base, exp) que calcule base^exp de forma 
recursiva, sem usar o operador **.
Assuma exp ≥ 0.
Raciocínio:
base^0 = 1  (caso base)
base^n = base × base^(n−1)  (redução)
Cada chamada reduz exp em 1 até chegar a 0.
Trace a pilha de chamadas para exp=3:
potencia(2,3) → 2 × potencia(2,2)
  → 2 × 2 × potencia(2,1)
    → 2 × 2 × 2 × potencia(2,0) → × 1

===PAGE_BREAK===

3.5 — Torre de Hanói
Tópico 3 · Condicionais e Recursividade
Implemente hanoi(n, origem, destino, aux) que imprima cada 
movimento para transferir n discos da haste origem para 
destino usando aux como auxiliar.
Lógica recursiva:
1. Mova n-1 discos de origem → aux.
2. Mova o disco n (maior) de origem → destino.
3. Mova n-1 discos de aux → destino.
Número de movimentos = 2ⁿ − 1.


===PAGE_BREAK===

04
Tópico 4
Iteração e Strings
Laços while/for, manipulação de strings e funções que retornam valores.

===PAGE_BREAK===

4.1 — Contar Vogais
Tópico 4 · Iteração e Strings
Escreva contar_vogais(texto) que receba uma string e retorne o 
número de vogais (maiúsculas e minúsculas).
Conceitos:
• for letra in texto → itera sobre cada caractere.
• in → verifica pertencimento em uma string.
• Variável contador acumula a contagem.
• Poderia ser reescrita com sum() e expressão geradora:
  return sum(1 for c in texto if c in vogais)

===PAGE_BREAK===

4.2 — Reverter String
Tópico 4 · Iteração e Strings
Crie reverter(s) que retorne a string ao contrário, caractere a 
caractere com um laço (sem usar fatiamento [::-1]).
range(início, fim, passo):
range(len(s)-1, -1, -1)
  início: último índice da string
  fim:    -1 (não incluído → chega em 0)
  passo:  -1 (decrementa)
Atenção: concatenação de strings em laço é O(n²).
Em produção, use list + join.

===PAGE_BREAK===

4.3 — Palíndromo
Tópico 4 · Iteração e Strings
Escreva is_palindromo(s) que retorne True se a string for um 
palíndromo, ignorando maiúsculas/minúsculas e espaços.
Pipeline de pré-processamento:
1. lower() → normaliza maiúsculas.
2. replace(" ","") → remove espaços.
3. Compara a string com seu reverso [::-1].
Fatiamento s[::-1] é o idioma Python para reverter
strings de forma eficiente.

===PAGE_BREAK===

4.4 — Tabuada
Tópico 4 · Iteração e Strings
Crie tabuada(n) que imprima a tabuada de n de 1 a 10 e retorne 
uma lista com todos os produtos calculados.
Formatação avançada com f-strings:
{i:2d}  → inteiro com 2 dígitos (alinha à direita).
{res:3d} → inteiro com 3 dígitos.
Função retorna dois resultados:
  • Imprime a tabuada (efeito colateral)
  • Retorna lista de produtos (valor de retorno)
Boa prática: separar efeitos de valores de retorno.

===PAGE_BREAK===

4.5 — Anagramas
Tópico 4 · Iteração e Strings
Escreva sao_anagramas(s1, s2) que retorne True se as duas 
strings forem anagramas. Ignore maiúsculas, minúsculas e 
espaços.
Estratégia:
Dois anagramas têm as mesmas letras, logo ao ordenar (sorted) 
ambas as strings pré-processadas, os resultados devem ser iguais.
sorted(s) retorna uma lista de caracteres em ordem.
lambda → função anônima de uso único.

===PAGE_BREAK===

05
Tópico 5
Listas, Dicionários
e Tuplas
Estruturas de dados fundamentais de Python.

===PAGE_BREAK===

5.1 — Estatísticas de Lista
Tópico 5 · Listas, Dicionários e Tuplas
Dada uma lista de números, calcule e exiba soma, média, maior e 
menor valor — sem usar sum(), max() e min().
Pontos-chave:
• Acumulador inicializado antes do laço.
• maior/menor inicializados com o primeiro elemento.
• Retorno múltiplo via tupla: return a, b, c, d
• Desempacotamento: s, m, mx, mn = estatisticas(nums)

===PAGE_BREAK===

5.2 — Frequência de Palavras
Tópico 5 · Listas, Dicionários e Tuplas
Dado um texto (string), construa um dicionário onde cada chave é 
uma palavra (em minúsculas) e o valor é a quantidade de 
ocorrências.
dict.get(chave, padrão):
freq.get(palavra, 0)
  → retorna o valor atual, ou 0 se a chave não existir.
Evita KeyError e elimina a necessidade de
checkar if palavra in freq antes de incrementar.

===PAGE_BREAK===

5.3 — Agenda de Contatos
Tópico 5 · Listas, Dicionários e Tuplas
Crie uma agenda usando dicionário. Implemente funções para: 
adicionar contato, buscar contato, remover contato e listar todos.
Operações com dicionários:
d[chave] = valor  → inserir/atualizar
d.get(chave)       → buscar com segurança
del d[chave]       → remover
d.items()          → pares (chave, valor)
sorted(d.items())  → ordenado por chave

===PAGE_BREAK===

5.4 — Pontos 2D com Tuplas
Tópico 5 · Listas, Dicionários e Tuplas
Represente pontos em 2D como tuplas (x, y). Escreva funções 
para calcular a distância e o ponto médio entre dois pontos.
Tuplas como registros:
Tuplas são imutáveis — ideais para dados que não
mudam (como coordenadas de um ponto).
p[0] → componente x
p[1] → componente y
Fórmula da distância euclidiana:
  d = √((x₂−x₁)² + (y₂−y₁)²)

===PAGE_BREAK===

5.5 — Matriz NxN com Listas Aninhadas
Tópico 5 · Listas, Dicionários e Tuplas
Represente uma matriz NxN como lista de listas. Implemente: 
a) criar matriz identidade, b) transpor a matriz, c) imprimir 
formatada.
List comprehension 2D:
[[expr for j in range(n)] for i in range(n)]
  → laço externo = linhas (i)
  → laço interno = colunas (j)
  → m[linha][coluna]
Transposição: troca índices i↔j:
  m_transposta[i][j] = m_original[j][i]

===PAGE_BREAK===

06
Tópico 6
Arquivos em Python
Leitura, escrita, append e persistência de dados em disco.

===PAGE_BREAK===

6.1 — Escrever e Ler Arquivo de Texto
Tópico 6 · Arquivos em Python
Crie um arquivo notas.txt com nome e nota de cinco alunos (um 
por linha). Em seguida, leia o arquivo e exiba seu conteúdo.
Modos de abertura:
"w"  → escrita (cria ou sobrescreve)
"r"  → leitura
"a"  → append (adiciona ao final)
"x"  → cria (erro se já existir)
with garante que o arquivo seja fechado mesmo
se ocorrer uma exceção.

===PAGE_BREAK===

6.2 — Contar Linhas, Palavras e Caracteres
Tópico 6 · Arquivos em Python
Leia o arquivo notas.txt criado anteriormente e exiba o 
número total de linhas, palavras e caracteres.
Métodos úteis de string:
split()         → divide em lista de palavras
len(linha)      → número de caracteres
len(linha.split()) → número de palavras
rstrip()        → remove \n e espaços finais
Contar palavras: split() sem argumentos
also split por múltiplos espaços.

===PAGE_BREAK===

6.3 — Média da Turma a partir de Arquivo
Tópico 6 · Arquivos em Python
Releia notas.txt, calcule a média da turma e indique o 
aluno com maior e menor nota.
Parsing de arquivo:
split(": ") → divide em [nome, nota].
float(partes[1]) → converte a nota.
max/min com key= → compara pelo 2º elemento da tupla.
List comprehension: [n for _, n in registros]
O _ indica variável não usada (convenção).

===PAGE_BREAK===

6.4 — Append e Busca em Arquivo
Tópico 6 · Arquivos em Python
Adicione novos alunos ao arquivo notas.txt (modo append). 
Implemente uma busca: dado um nome, exiba a nota 
correspondente.
Modo "a" (append):
Abre o arquivo posicionando o cursor
no final — as escritas anteriores são preservadas.
Busca sequencial: O(n) no pior caso.
Retorna None se não encontrar — verifique
o retorno com  if resultado is not None.

===PAGE_BREAK===

6.5 — Agenda Persistida em CSV
Tópico 6 · Arquivos em Python
Implemente uma agenda em agenda.csv com cabeçalho 
'nome,telefone,email'. Funções: adicionar_contato(), listar_contatos() e 
remover_contato().
Estratégia de remoção:
CSV não suporta remoção direta de linha.
Estratégia: ler tudo → filtrar → reescrever.
f.readlines() → lista com todas as linhas.
f.writelines(lista) → escreve várias linhas de uma vez.
Melhoria futura: usar módulo csv da stdlib.

===PAGE_BREAK===

Bons estudos! 🚀
• 1 · Variáveis, Expressões e Instruções
• 2 · Funções em Python
• 3 · Condicionais e Recursividade
• 4 · Iteração e Strings
• 5 · Listas, Dicionários e Tuplas
• 6 · Arquivos em Python