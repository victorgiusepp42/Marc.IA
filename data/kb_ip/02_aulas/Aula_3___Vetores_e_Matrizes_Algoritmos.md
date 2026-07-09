---
tipo: slide_ou_roteiro
etapa: 1
topico: vetores_matrizes_listas
fonte: docs/materiais_kb/AULAS/Aula_3___Vetores_e_Matrizes_Algoritmos (1).txt
data_processamento: 2026-07-04
autor_original: Prof. Dr. Márcio de Souza Dias (UFCAT/IMTec)
status: extraido_pdf_bruto
ordem_aula: '0'
observacao: Texto extraído automaticamente do PDF; revisar figuras/diagramas que não vieram.
---

# Aula_3___Vetores_e_Matrizes_Algoritmos

Estruturas Homogêneas
Vetores e Matrizes em Algoritmos
10
[0]
25
[1]
8
[2]
42
[3]
17
[4]
33
[5]
5
[6]
vetor[ ]
Introdução à Programação 

===PAGE_BREAK===

AGENDA
O que vamos aprender?
2 / 22
01
O problema antes dos vetores
Por que precisamos de estruturas homogêneas?
02
O que são Vetores?
Conceito, índices, declaração e exemplos
03
Operações com Vetores
Leitura, escrita, busca, soma e média
04
O que são Matrizes?
Conceito bidimensional, linhas e colunas
05
Operações com Matrizes
Percorrendo com laços aninhados
06
Exemplos Práticos
Casos reais do cotidiano da programação
07
Exercícios de Fixação
Pratique e consolide o conhecimento!

===PAGE_BREAK===

MOTIVAÇÃO
Por que precisamos de vetores?
O problema sem estruturas homogêneas
3 / 22
😱  Sem vetores:
// Guardar notas de 5 alunos...
var nota1, nota2, nota3,
    nota4, nota5: real
leia(nota1)
leia(nota2)
leia(nota3)
leia(nota4)
leia(nota5)
// E se fossem 100 alunos?! 
😰
✅  Com vetores:
// Guardar notas de 100 alunos!
var notas: vetor[1..100]
        de real
var i: inteiro
para i de 1 ate 100 faca
  leia(notas[i])
fimpara
// Simples e elegante! 
😎

===PAGE_BREAK===

VETORES
O que é um Vetor?
4 / 22
💡  Pense em um vetor como uma fileira de gavetas numeradas!
Ana
[0]
Bob
[1]
Cia
[2]
Dan
[3]
Eva
[4]
nomes
📋 Definição
Coleção de variáveis do MESMO TIPO, 
identificadas por um único nome e 
acessadas por um índice numérico.
📏 Tamanho Fixo
O vetor nasce com um tamanho 
definido e não muda. Se precisa de 
mais espaço, cria-se um vetor maior.
🔢 Índices
Cada posição tem um número (índice) 
que começa em 0 (em muitas 
linguagens) ou 1 (em Portugol).

===PAGE_BREAK===

VETORES
Declarando um Vetor
Sintaxe em Portugol / Pseudocódigo
5 / 22
📝 Declaração
// Sintaxe geral:
var nomeDoVetor: vetor[1..tamanho] de tipoDeDado
// Exemplos práticos:
var idades:    vetor[1..10] de inteiro
var notas:     vetor[1..5]  de real
var nomes:     vetor[1..30] de caractere
var aprovados: vetor[1..50] de logico
Anatomia da declaração:
idades
Nome do 
vetor
1
Índice 
inicial
10
Tamanho 
(índice final)
inteiro
Tipo de 
dado

===PAGE_BREAK===

VETORES
Acessando e Modificando Elementos
6 / 22
📖 Código
var notas: vetor[1..5] de real
var i: inteiro
// Atribuir valores diretamente:
notas[1] <- 8.5
notas[2] <- 7.0
notas[3] <- 9.5
// Acessar e exibir:
escreva(notas[1])   // Imprime: 8.5
escreva(notas[3])   // Imprime: 9.5
// Modificar um valor:
notas[2] <- 8.0     // Agora notas[2] vale 8.0
Estado do vetor na memória:
notas[1] 8.5
notas[2] 8.0
notas[3] 9.5
notas[4] ?
notas[5] ?

===PAGE_BREAK===

VETORES
Vetores + Laços de RepetiçãoA combinação mais poderosa!
7 / 22
🔄 O laço PARA percorre cada posição do vetor automaticamente:
💻 Exemplo Completo: Média da Turma
algoritmo "MediaTurma"
var notas: vetor[1..5] de real
var i: inteiro
var soma, media: real
inicio
  soma <- 0 
  // Ler todas as notas:
  para i de 1 ate 5 faca
    escreva("Digite a nota ", i, ": ")
    leia(notas[i])
  fimpara
  // Calcular soma:
  para i de 1 ate 5 faca
    soma <- soma + notas[i]
  fimpara
  media <- soma / 5
  escreval("Média da turma: ", media)
fimalgoritmo
Como o laço funciona:
i=1 notas[1] ← leitura
i=2 notas[2] ← leitura
i=3 notas[3] ← leitura
i=4 notas[4] ← leitura
i=5 notas[5] ← leitura

===PAGE_BREAK===

VETORES
Operações Comuns com Vetores
8 / 22
🔍 Busca Linear
para i de 1 ate n faca
  se vetor[i] = buscado
    escreva("Encontrado!")
  fimse
fimpara
📊 Maior Valor
maior <- vetor[1]
para i de 2 ate n faca
  se vetor[i] > maior
    maior <- vetor[i]
  fimse
fimpara
➕ Soma Total
soma <- 0
para i de 1 ate n faca
  soma <- soma + vetor[i]
fimpara
media <- soma / n
🔄 Inverter
para i de 1 ate n/2 faca
  temp <- v[i]
  v[i] <- v[n-i+1]
  v[n-i+1] <- temp
fimpara

===PAGE_BREAK===

VETORES
Exemplo Prático: Sistema de NotasLê notas de alunos e classifica aprovados/reprovados
9 / 22
💻 Código Completo
algoritmo "SistemaNotas"
var notas: vetor[1..5] de real
var i, aprovados: inteiro
inicio
  aprovados <- 0
  // Leitura das notas
  para i de 1 ate 5 faca
    escreva("Nota do aluno ", i, ": ")
    leia(notas[i])
  fimpara
  // Verificação e relatório
  escreval("=== RESULTADO ===") 
  para i de 1 ate 5 faca
    escreva("Aluno ", i, ": ")
    se notas[i] >= 6.0 entao
      escreval("APROVADO (", notas[i], ")")
      aprovados <- aprovados + 1
    senao
      escreval("REPROVADO (", notas[i], ")")
    fimse
  fimpara
  escreval("Total aprovados: ", aprovados)
fimalgoritmo
Saída do programa:
Nota do aluno 1: 8.5
Nota do aluno 2: 4.0
Nota do aluno 3: 7.5
Nota do aluno 4: 5.5
Nota do aluno 5: 9.0
=== RESULTADO ===
Aluno 1: APROVADO (8.5)
Aluno 2: REPROVADO (4.0)
Aluno 3: APROVADO (7.5)
Aluno 4: REPROVADO (5.5)
Aluno 5: APROVADO (9.0)
Total aprovados: 3

===PAGE_BREAK===

MATRIZES
O que é uma Matriz?
10 / 22
💡  Matriz = Tabela! Pense em linhas e colunas como uma planilha do Excel.
Col 0 Col 1 Col 2 Col 3
Lin 0 10 20 30 40
Lin 1 50 60 70 80
Lin 2 90 15 25 35
↑ mat[1][2] = 70
📐 2 Dimensões
Linha [i] e Coluna [j] 
Sempre dois índices!
📋 Usos Comuns
Tabelas, tabuleiros, 
imagens, notas, mapas
🧮 Tamanho
Linhas × Colunas 
elementos no total

===PAGE_BREAK===

MATRIZES
Declarando uma Matriz
Sintaxe com dois índices
11 / 22
📝 Declaração e Atribuição
// Sintaxe geral:
var nomeDaMatriz: vetor[1..linhas, 1..colunas] de tipoDeDado
// Exemplos:
var tabela:  vetor[1..3, 1..4] de inteiro    // 3 linhas, 4 colunas
var notas:   vetor[1..30, 1..4] de real      // 30 alunos, 4 provas
var grade:   vetor[1..8, 1..8] de caractere  // tabuleiro xadrez
// Atribuição:
tabela[1,1] <- 10    // linha 1, coluna 1
tabela[2,3] <- 75    // linha 2, coluna 3
notas[5,2]  <- 8.5   // nota do aluno 5 na prova 2
Lendo o índice da matriz:
notas
Nome da matriz
5
Índice de LINHA
2
Índice de COLUNA
<-
Operação
8.5
Valor atribuído

===PAGE_BREAK===

MATRIZES
Percorrendo Matrizes
Laços aninhados: o segredo das matrizes!
12 / 22
💻 Laços Aninhados
// Preencher e exibir uma matriz 3x3:
var mat: vetor[1..3, 1..3] de inteiro
var i, j: inteiro
// Leitura:
para i de 1 ate 3 faca           // i = linha
  para j de 1 ate 3 faca         // j = coluna
    escreva("mat[",i,"][",j,"]: ")
    leia(mat[i,j])
  fimpara
fimpara
// Exibição:
para i de 1 ate 3 faca
  para j de 1 ate 3 faca
    escreva(mat[i,j], "  ")
  fimpara
  escreval("")    // pula linha
fimpara
Ordem de percurso:
1 2 3
4 5 6
7 8 9
Números indicam a ordem de visita cada célula

===PAGE_BREAK===

MATRIZES
Exemplo: Notas de Turma30 alunos × 4 provas = Matriz [30,4]
13 / 22
💻 Código: 3 Alunos × 4 Provas
algoritmo "NotasTurma"
var notas: vetor[1..3, 1..4] de real
var i, j: inteiro
var soma, media: real
inicio
  // Entrada de dados
  para i de 1 ate 3 faca
    para j de 1 ate 4 faca
      escreva("Aluno ",i," - Prova ",j,": ")
      leia(notas[i,j])
    fimpara
  fimpara
  // Calcular media por aluno
  para i de 1 ate 3 faca
    soma <- 0
    para j de 1 ate 4 faca
      soma <- soma + notas[i,j]
    fimpara
    media <- soma / 4
    escreva("Media aluno ",i,": ",media)
    se media >= 6 entao
      escreval(" - APROVADO")
    senao
      escreval(" - REPROVADO")
    fimse  fimpara   fimalgoritmo
Visualização da matriz notas:
P1 P2 P3 P4
A1 8.5 7 9 88.1
A2 4 5.5 6 55.1
A3 9 8.5 9.5 99.0
Legenda: verde = aprovado, vermelho = reprovado
Saída:
Media aluno 1: 8.1 - APROVADO
Media aluno 2: 5.1 - REPROVADO
Media aluno 3: 9.0 - APROVADO

===PAGE_BREAK===

COMPARAÇÃO
Vetor vs Matriz: Resumo Comparativo
14 / 22
Característica Vetor (1D) Matriz (2D)
Dimensões 1 (apenas índice i) 2 (índices i e j)
Declaração vetor[1..n] vetor[1..m, 1..n]
Acesso v[i] m[i,j]
Percurso 1 laço PARA 2 laços PARA aninhados
Analogia Lista / Fila Tabela / Planilha
Uso típico Lista de nomes, notas Tabela de dados, imagens

===PAGE_BREAK===

APLICAÇÕES
Onde Vetores e Matrizes são Usados?
Exemplos do mundo real
15 / 22
🎮  Jogos
Tabuleiro de xadrez, campo de batalha, 
labirintos — tudo usa matriz 2D!
📸  Imagens
Uma foto é uma matriz de pixels. Cada pixel 
tem valores RGB armazenados em posições 
[linha,coluna].
📊  Planilhas
Tabelas do Excel/Google Sheets são matrizes. 
Cada célula é acessada por linha e coluna.
🧭  GPS / Mapas
Grades de coordenadas geográficas. Mapas 
de grade usam matrizes para armazenar 
elevações.
🏫  Sistemas Acadêmicos
Notas de alunos por disciplina. vetor[aluno, 
prova] armazena todo o histórico.
🤖  Inteligência Artificial
Redes neurais usam matrizes gigantes 
(tensores) para guardar pesos e fazer 
cálculos.

===PAGE_BREAK===

DICAS
Dicas e Erros Comuns
Aprenda com os erros mais frequentes!
16 / 22
❌ Índice fora do limite
🚫 Errado
var v: vetor[1..5] de inteiro
v[6] <- 10  // ERRO!
// O vetor só tem até 5!
✅ Correto
var v: vetor[1..5] de inteiro
v[5] <- 10  // CORRETO 
✅
// Sempre dentro do limite
❌ Começar do índice errado
🚫 Errado
// Se declarou [1..n], não use [0]:
para i de 0 ate n faca  // ERRO!
  v[i] <- i
fimpara
✅ Correto
// Começar do índice correto:
para i de 1 ate n faca  // OK 
✅
  v[i] <- i
fimpara
💡 Dica de ouro: sempre verifique o tamanho do vetor antes de acessar qualquer posição!

===PAGE_BREAK===

✏Exercícios de Fixação
Pratique para consolidar o aprendizado!

===PAGE_BREAK===

🟢 EXERCÍCIOS
Exercícios Básicos — Vetores
18 / 22
01
Saudação Personalizada
Declare um vetor de 5 nomes (caractere). Leia os 5 nomes e depois exiba uma mensagem de boas-vindas para cada um: "Olá, 
[nome]! Bem-vindo!"
💡 Dica: Use um laço para leitura e outro para exibição.
02
Soma e Média
Leia 6 números inteiros em um vetor. Calcule e exiba: a soma de todos os números e a média aritmética.
💡 Dica: Use uma variável 'soma' iniciada em 0 e vá somando cada vetor[i].
03
Maior e Menor
Leia um vetor de 8 números reais. Encontre e exiba o maior e o menor valor armazenado no vetor.
💡 Dica: Comece assumindo que maior = menor = vetor[1] e compare com os demais.

===PAGE_BREAK===

🟢 EXERCÍCIOS
Exercícios Básicos — Vetores (cont.)
19 / 22
04
Contar Pares e Ímpares
Leia 10 números inteiros em um vetor. Conte e exiba quantos são pares e quantos são ímpares.
💡 Dica: Use o operador MOD (resto da divisão): se vetor[i] MOD 2 = 0, é par.
05
Inversão de Vetor
Leia um vetor de 5 elementos inteiros e exiba-os na ordem inversa (do último para o primeiro), sem criar um segundo vetor.
💡 Dica: Basta fazer o laço de i=5 até i=1 com passo -1, ou de i=n até i=1.
06
Classificação de Temperaturas
Leia as temperaturas de 7 dias da semana em um vetor. Exiba os dias com temperatura acima da média semanal.
💡 Dica: Primeiro calcule a média com um laço, depois percorra de novo para comparar cada temperatura.

===PAGE_BREAK===

🟡 EXERCÍCIOS
Exercícios Médios — Matrizes
20 / 22
07
Preencher e Exibir Matriz
Declare uma matriz 3x3 de inteiros. Preencha com os valores de 1 a 9 (usando laços) e exiba a matriz formatada em forma de tabela.
💡 Dica: Após imprimir todos os j de uma linha i, use escreval para pular de linha.
08
Soma de Linhas e Colunas
Leia uma matriz 4x4 de números reais. Calcule e exiba a soma de cada linha e a soma de cada coluna separadamente.
💡 Dica: Para somar linhas, faça um laço externo em i e interno em j. Para colunas, inverta os laços.
09
Maior Elemento da Matriz
Leia uma matriz 3x4 de inteiros. Encontre o maior elemento da matriz e exiba seu valor e em qual linha e coluna ele está.
💡 Dica: Guarde três variáveis: maior, linMaior e colMaior. Atualize as três quando encontrar um valor maior.

===PAGE_BREAK===

🟡 EXERCÍCIOS
Exercícios Médios — Matrizes (cont.)
21 / 22
10
Diagonal Principal
Leia uma matriz 4x4 de inteiros. Calcule e exiba a soma dos elementos da diagonal principal (onde o índice de linha = índice de 
coluna).
💡 Dica: Os elementos da diagonal são onde i = j. Você não precisa de laço duplo para este caso!
11
Tabuleiro de Xadrez
Crie uma matriz 8x8 de caractere. Preencha com 'B' (branco) e 'P' (preto) seguindo o padrão do xadrez. Exiba o tabuleiro formatado.
💡 Dica: Se (i+j) for par, coloque 'B'; se for ímpar, coloque 'P'. Use o operador MOD para verificar.
12
Sistema de Notas Completo
Leia uma matriz [5,3] com notas de 5 alunos em 3 provas. Para cada aluno, calcule a média das 3 notas e classifique: >=7=Aprovado, 
>=5=Recuperação, <5=Reprovado.
💡 Dica: Combine laços aninhados para leitura com um laço simples para calcular e exibir as médias.

===PAGE_BREAK===

🔴 DESAFIO
Exercício Desafio Final
22 / 22
🔴  Desafio #13: Jogo da Velha — Verificação de Vencedor
Enunciado: Crie um algoritmo que represente um tabuleiro do Jogo da Velha usando uma matriz 3x3 de caractere. O programa 
deve: 
1) Ler o estado atual do tabuleiro (cada célula pode ser 'X', 'O' ou ' '); 
2) Verificar se há um vencedor (3 iguais em linha, coluna ou diagonal); 
3) Exibir: "X ganhou!", "O ganhou!", "Empate!" ou "Jogo em andamento".
Estruturas que você vai precisar:
Matriz 3x3 
de caractere
Laços para 
leitura do tabuleiro
Verificar 
3 em linha
Verificar 
3 em coluna
Verificar 
diagonais
🏆 Quem resolver este desafio domina vetores e matrizes!