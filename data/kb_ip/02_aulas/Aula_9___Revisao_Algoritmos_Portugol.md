---
tipo: slide_ou_roteiro
etapa: 1
topico: geral
fonte: docs/materiais_kb/AULAS/Aula_9_-_Revisao_Algoritmos_Portugol (1).txt
data_processamento: 2026-07-04
autor_original: Prof. Dr. Márcio de Souza Dias (UFCAT/IMTec)
status: extraido_pdf_bruto
ordem_aula: '0'
observacao: Texto extraído automaticamente do PDF; revisar figuras/diagramas que não vieram.
---

# Aula_9_-_Revisao_Algoritmos_Portugol

REVISÃO DE
ALGORITMOS
com Portugol
▸  Variáveis & Tipos
▸  Decisão
▸  Repetição
▸  Vetores & Matrizes
▸  Funções
▸  Ordenação & Busca
Aula de Revisão

===PAGE_BREAK===

O que é um Algoritmo?
Conceito fundamental 
"Sequência finita e ordenada de passos bem definidos para resolver um problema ou realizar uma tarefa."
Entrada
Recebe dados iniciais 
para processamento
Processamento
Executa operações 
sobre os dados
Saída
Produz um resultado 
ao final da execução
algoritmo "Soma de dois números" 
var 
   a, b, soma:  
inteiro 
inicio 
   leia(a, b) 
   soma <- a + b 
   escreva(soma) 
fimalgoritmo

===PAGE_BREAK===

Variáveis e Tipos de Dados
Fundamentos da programação 
inteiro
Números inteiros 
sem casas decimais idade: inteiro 
idade <- 20
real
Números com 
casas decimais salario: real 
salario <- 2500.50
caractere
Texto / cadeia 
de caracteres nome: caractere 
nome <- "Maria"
logico
Verdadeiro ou 
Falso ativo: logico 
ativo <- verdadeiro

===PAGE_BREAK===

Operadores
Aritméticos, relacionais e lógicos 
Aritméticos
Operador Significado Exemplo
+  Adiçãoa + b
- Subtraçãoa - b
*Multiplicaçãoa * b
/ Divisão a / b
MODResto divisão10 MOD 3  
→  1
DIV Divisão 
inteira
10 DIV 3  
→  3
Relacionais
Operador Significado Exemplo
= Igual a = b
<> Diferente a <> b
< Menor a < b
> Maior a > b
<=Menor ou iguala <= b
>=Maior ou iguala >= b
Lógicos
Operador Resultado
E (AND) Verdadeiro se 
ambos V
OU (OR) Verdadeiro se um 
V
NAO (NOT)Inverte o valor
Precedência:NAO > E > OU
Dica: Use () para 
clareza

===PAGE_BREAK===

Estruturas de Decisão
SE/SENÃO e ESCOLHA · ~10 min
SE / SENÃO
se (nota >= 7.0) entao 
   escreva("Aprovado") 
senao 
   se (nota >= 5.0) entao 
      escreva("Recuperação") 
   senao 
      escreva("Reprovado") 
   fimse 
fimse
ESCOLHA / CASO
escolha (diaSemana) 
   caso 1: escreva("Seg") 
   caso 2: escreva("Ter") 
   caso 3: escreva("Qua") 
   outrocaso 
      escreva("Inválido") 
fimescolha
⚡  Dica de uso:
Use SE/SENÃO quando a condição é uma expressão booleana complexa (intervalos, comparações).  Use ESCOLHA quando você compara uma 
variável com valores discretos e fixos (dias, meses, opções de menu).

===PAGE_BREAK===

Estruturas de Repetição
ENQUANTO, PARA e REPITA 
ENQUANTO
📌 Quando não se sabe 
o nº de repetições
enquanto (i <= 5) faca 
   escreva(i) 
   i <- i + 1 
fimenquanto
PARA
📌 Quando se conhece 
o nº de repetições
para i de 1 ate 10 faca 
   escreva(i) 
fimpara
REPITA
📌 Executa ao menos 
uma vez (pós-teste)
repita 
   leia(opcao) 
   escreva(opcao) 
ate (opcao = 0)
Comparação rápida:
▸  ENQUANTO → pré-teste (pode não executar) ▸  PARA → contador automático (pré-teste) ▸  REPITA → pós-teste (executa pelo menos 1x)

===PAGE_BREAK===

Vetores (Arrays Unidimensionais)
Coleções de dados homogêneos 
Declaração e acesso por índice
10
[1]
25
[2]
7
[3]
42
[4]
18
[5]
← índice 3 acessado: notas[3] = 7
var 
   notas: vetor[1..5] de real 
   i: inteiro 
inicio 
   para i de 1 ate 5 faca 
      leia(notas[i]) 
   fimpara 
   para i de 1 ate 5 faca 
      escreva(notas[i]) 
   fimpara 
fimalgoritmo
Matrizes (2D)
// Matriz 3x3 
tabela: vetor[1..3,1..3] de inteiro 
 
// Acesso 
tabela[2,3] <- 8 
escreva(tabela[1,1])

===PAGE_BREAK===

Funções e Procedimentos
Modularização do código 
Procedimento
Executa ações. Não retorna valor.
Função
Calcula e RETORNA um valor.
Parâmetro
Dado enviado para subalgoritmo.
Escopo
Variáveis locais vs. globais.
Procedimento
procedimento saudacao(nome: caractere) 
inicio 
   escreva("Olá, ", nome) 
fimprocedimento 
 
// Chamada: 
saudacao("Carlos")
Função com retorno
funcao maior(a, b: inteiro): inteiro 
inicio 
   se (a > b) entao 
      retorne(a) 
   senao 
      retorne(b) 
   fimse 
fimfuncao 
 
// Chamada: 
m <- maior(10, 25)

===PAGE_BREAK===

Algoritmos de Ordenação
Bubble Sort e Selection Sort
Bubble Sort — ideia: comparar pares adjacentes e trocar se necessário
Passo 1: 64 > 34 → troca 64 34 25 12 22
Passo 2: 64 > 25 → troca 34 64 25 12 22
Passo 3: 64 > 12 → troca 34 25 64 12 22
Implementação em Portugol
para i de 1 ate N-1 faca 
   para j de 1 ate N-i faca 
      se (v[j] > v[j+1]) entao  
aux <- v[j]  
v[j] <- v[j+1]  
v[j+1] <- aux  
fimse 
   fimpara 
fimpara

===PAGE_BREAK===

Algoritmos de Busca
Sequencial e Binária 
Busca Sequencial
Percorre o vetor elemento por elemento até encontrar o valor ou chegar ao 
final. O(n)
i <- 1 
achou <- falso 
enquanto (i<=N) E (NAO achou) faca 
   se (v[i] = chave) entao 
      achou <- verdadeiro 
   fimse 
   i <- i + 1 
fimenquanto
Busca Binária
Vetor deve estar ORDENADO. Divide ao meio e descarta metade. O(log n)
ini <- 1  fim <- N 
enquanto (ini <= fim) E (NAO achou) faca 
   meio <- (ini + fim) DIV 2 
   se (v[meio] = chave) entao 
      achou <- verdadeiro 
   senao se (chave < v[meio]) entao 
      fim <- meio - 1 
   senao 
      ini <- meio + 1 
   fimse 
fimenquanto
Complexidade:   Busca Sequencial  O(n) — pior caso: percorre tudo   |   Busca Binária  O(log n) — divide ao meio a cada iteração

===PAGE_BREAK===

Exercício Prático Integrador
Coloque em prática tudo que aprendeu! 
📝  Enunciado
Crie um algoritmo em Portugol que: 
1. Leia 10 notas de alunos em um vetor 
2. Calcule a média da turma (usando uma função) 
3. Ordene as notas usando Bubble Sort 
4. Exiba: maior nota, menor nota, média e situação da turma 
   (Aprovada se média >= 7, Recuperação se >= 5, Reprovada se < 5)
Conceitos utilizados:
Variáveis Vetor Para (loop) Bubble Sort Função SE/SENÃO Leia/Escreva
💡 Dica: comece declarando as variáveis, depois escreva a função calcularMedia(), depois o Bubble Sort, e por último o bloco principal.

===PAGE_BREAK===

Resumo Geral
O que vimos hoje
Algoritmos
Sequência finita de passos com entrada, processamento e saída
Variáveis/Tipos
inteiro, real, caractere, logico — cada um com seu uso
Operadores
Aritméticos (+−*/ MOD DIV), Relacionais (= <> < >) e Lógicos
Decisão
SE/SENÃO para condições; ESCOLHA para valores discretos
Repetição
PARA (contador), ENQUANTO (pré-teste), REPITA (pós-teste)
Vetores
Coleções de mesmo tipo; matrizes são vetores 2D
Funções
Retornam valores; Procedimentos executam ações sem retorno
Ordenação/Busca
Bubble Sort O(n²); Busca Sequencial O(n); Binária O(log n)

===PAGE_BREAK===

Algoritmos são a 
base de tudo!
Pratique, erre, corrija e evolua.
🧠  Leia o enunciado com atenção antes de codificar
✏   Esboce o algoritmo no papel primeiro
🔁  Trace o algoritmo manualmente com exemplos
🧪  Teste com casos extremos (0, negativos, vazios)
Bons estudos! 
🚀