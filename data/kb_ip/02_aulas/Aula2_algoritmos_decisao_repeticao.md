---
tipo: slide_ou_roteiro
etapa: 1
topico: condicionais
fonte: docs/materiais_kb/AULAS/Aula2_algoritmos_decisao_repeticao (2).txt
data_processamento: 2026-07-04
autor_original: Prof. Dr. Márcio de Souza Dias (UFCAT/IMTec)
status: extraido_pdf_bruto
ordem_aula: '0'
observacao: Texto extraído automaticamente do PDF; revisar figuras/diagramas que não vieram.
---

# Aula2_algoritmos_decisao_repeticao

Estruturas de Decisão
e Repetição em Algoritmos
Lógica de Programação  •  Pseudocódigo  •  Exemplos Práticos  •  Exercícios
SE/ENTÃO/SENÃO CASO SELECIONE ENQUANTO/FAÇA PARA/ATÉ/FAÇA REPITA/ATÉ
Fundamentos de Programação

===PAGE_BREAK===

O que são Estruturas de Controle?
Fundamentos essenciais para criar algoritmos inteligentes
→
Sequencial
Instruções executadas 
uma após a outra, em 
ordem linear.
⿗
Decisão
O algoritmo escolhe 
caminhos diferentes 
conforme condições.
↺
Repetição
Um bloco de instruções 
é executado várias 
vezes (loop).
Todo algoritmo é formado pela combinação dessas três estruturas fundamentais.

===PAGE_BREAK===

Condições e Operadores Relacionais
A base de qualquer estrutura de decisão
O que é uma Condição?
Uma expressão que resulta em 
VERDADEIRO ou FALSO (booleano).
Operador Significado Exemplo Resultado
> maior que 5 > 3VERDADEIRO
< menor que 2 < 1 FALSO
>= maior ou 
igual 4 >= 4VERDADEIRO
<= menor ou 
igual 6 <= 5 FALSO
= igual a 3 = 3VERDADEIRO
<> diferente de5 <> 5 FALSO
Operadores Lógicos
E (AND)
Verdadeiro somente se AMBAS as condições forem verdadeiras.
idade > 18 E aprovado = V
OU (OR)
Verdadeiro se PELO MENOS UMA condição for verdadeira.
nota >= 7 OU recuperacao = V
NÃO (NOT)
Inverte o resultado lógico da condição.
NÃO (x = 0)

===PAGE_BREAK===

Estrutura SE/ENTÃO  —  Seleção Simples
Executa um bloco apenas quando a condição é verdadeira
SINTAXE
●  ●  ● pseudocódigo
SE <condição> ENTÃO 
   <bloco de instruções> 
FIM SE
FLUXO DE EXECUÇÃO
condição?
Executa bloco
V
F
Continua...
EXEMPLO PRÁTICO
●  ●  ● pseudocódigo
Algoritmo VerificaAprovacao 
  Var nota: real 
  Início 
    Leia(nota) 
    SE nota >= 7 ENTÃO 
       Escreva("Aluno APROVADO!") 
    FIM SE 
  Fim

===PAGE_BREAK===

Estrutura SE/ENTÃO/SENÃO  —  Seleção Composta
Dois caminhos alternativos conforme a condição
●  ●  ● pseudocódigo
SE <condição> ENTÃO 
   <bloco verdadeiro> 
SENÃO 
   <bloco falso> 
FIM SE
EXEMPLO: Verificar se número é positivo ou negativo
●  ●  ● pseudocódigo
Algoritmo VerificaNumero 
  Var n: inteiro 
  Inicio 
    Escreva("Digite um número: ") 
    Leia(n) 
    SE n >= 0 ENTÃO 
       Escreva("Número POSITIVO ou ZERO") 
    SENÃO 
       Escreva("Número NEGATIVO") 
    FIM SE 
  Fim
Seleção Simples vs Composta
Simples (SE/ENTÃO)
Executa o bloco apenas quando VERDADEIRO. 
Quando FALSO, simplesmente ignora e segue.
Composta (SE/ENTÃO/SENÃO)
Sempre executa um dos dois blocos. 
VERDADEIRO → bloco 1 | FALSO → bloco 2
SE encadeado (SE dentro de SE):
●  ●  ● pseudocódigoSE nota >= 7 ENTÃO 
   Escreva("Aprovado") 
SENÃO 
   SE nota >= 5 ENTÃO 
      Escreva("Recuperação") 
   SENÃO 
      Escreva("Reprovado") 
   FIM SE 
FIM SE

===PAGE_BREAK===

CASO SELECIONE  —  Seleção Múltipla Escolha
Elegante para testar muitos valores distintos de uma variável
●  ●  ● pseudocódigo
CASO <variável> SEJA 
   <valor1>: <instruções> 
   <valor2>: <instruções> 
   <valor3>: <instruções> 
   SENÃO: <instruções padrão> 
FIM CASO
💡  Quando usar?
Quando uma variável pode assumir vários 
valores distintos e cada um tem ação diferente.
EXEMPLO: Menu de Opções
●  ●  ● pseudocódigo
Algoritmo Menu 
  Var opcao: inteiro 
  Inicio 
    Escreva("1-Somar  2-Subtrair") 
    Escreva("3-Multiplicar  4-Sair") 
    Leia(opcao) 
    CASO opcao SEJA 
       1: Escreva("Operação: Soma") 
       2: Escreva("Operação: Subtração") 
       3: Escreva("Operação: Multiplicação") 
       4: Escreva("Saindo...") 
       SENÃO: Escreva("Opção inválida!") 
    FIM CASO 
  FimCASO vs SE encadeado
Ambos resolvem o mesmo problema, 
mas CASO SELECIONE torna o código 
mais legível quando há muitas opções.

===PAGE_BREAK===

Estrutura ENQUANTO/FAÇA  —  Repetição com Teste no Início
Executa enquanto a condição for verdadeira • pode não executar nenhuma vez
●  ●  ● pseudocódigo
ENQUANTO <condição> FAÇA 
   <bloco de repetição> 
FIM ENQUANTO
Teste no INÍCIO
A condição é verificada antes de executar o bloco.
Pode ser 0 vezes
Se a condição já for falsa de início, o bloco nunca roda.
Variável de controle
Deve ser atualizada dentro do bloco para evitar loop infinito.

===PAGE_BREAK===

Estrutura ENQUANTO/FAÇA  —  Repetição com Teste no Início
EXEMPLO: Tabuada do 5
i <- 1 
ENQUANTO i <= 10 FAÇA 
   Escreva(5, " x ", i, " = ", 5*i) 
   i <- i + 1 
FIM ENQUANTO
EXEMPLO COMPLETO: Somar N números
●  ●  ● pseudocódigo
Algoritmo SomaNNumeros 
  Var n, i, num, soma: inteiro 
  Inicio 
    Leia(n) 
    i <- 1 
    soma <- 0 
    ENQUANTO i <= n FAÇA 
       Leia(num) 
       soma <- soma + num 
       i <- i + 1 
    FIM ENQUANTO 
    Escreva("Soma = ", soma) 
  Fim
Teste de mesa (n=3, entradas: 4, 7, 2)
i num soma i<=n?
1 4 4 V
2 7 11 V
3 2 13 V
4 - 13 F→PARA
●  ●  ● pseudocódigo

===PAGE_BREAK===

Estrutura PARA/ATÉ/FAÇA  —  Repetição Contada
Ideal quando o número de iterações é conhecido de antemão
●  ●  ● pseudocódigo
PARA <var> DE <início> ATÉ <fim> [PASSO <inc>] FAÇA 
   <bloco de repetição> 
FIM PARA
Variável de controle
Contador que avança automaticamente a cada 
iteração.
Valor Inicial e Final
Define o intervalo: início até fim (inclusive).
PASSO (opcional)
Incremento a cada iteração. Padrão = 1. Pode 
ser negativo!
EXEMPLOS
●  ●  ● pseudocódigo
// Crescente 
PARA i DE 1 ATÉ 5 FAÇA 
   Escreva(i) 
FIM PARA 
// Saída: 1 2 3 4 5
●  ●  ● pseudocódigo
// Decrescente 
PARA i DE 10 ATÉ 1 PASSO -2 
FAÇA 
   Escreva(i) 
FIM PARA 
// Saída: 10 8 6 4 2
●  ●  ● pseudocódigo
// Fatorial de N 
fat <- 1 
PARA i DE 1 ATÉ n FAÇA 
   fat <- fat * i 
FIM PARA 
Escreva("Fatorial = ", fat)

===PAGE_BREAK===

Estrutura REPITA/ATÉ  —  Repetição com Teste no Final
O bloco executa pelo menos UMA vez antes de verificar a condição
●  ●  ● pseudocódigo
REPITA 
   <bloco de repetição> 
ATÉ <condição de parada>
Diferença chave!
ENQUANTO: testa ANTES → pode executar 0 vezes 
REPITA:   testa DEPOIS → executa PELO MENOS 1 vez 
Use REPITA quando precisa garantir que o usuário 
forneceu dados antes de verificar.
●  ●  ● pseudocódigo
// Exemplo - Tabuada com REPITA 
i <- 1 
REPITA 
   Escreva(7, " x ", i, " = ", 7*i) 
   i <- i + 1 
ATÉ i > 10

===PAGE_BREAK===

Estrutura REPITA/ATÉ  —  Repetição com Teste no Final
EXEMPLO: Validar entrada do usuário
●  ●  ● pseudocódigo
Algoritmo ValidaIdade 
  Var idade: inteiro 
  Inicio 
    REPITA 
       Escreva("Digite sua idade (0-120): ") 
       Leia(idade) 
       SE (idade < 0) OU (idade > 120) ENTÃO 
          Escreva("Idade inválida! Tente 
novamente.") 
       FIM SE 
    ATÉ (idade >= 0) E (idade <= 120) 
    Escreva("Idade válida: ", idade) 
  Fim

===PAGE_BREAK===

Comparativo dos 3 Laços
Laço Teste Min. execuções Uso ideal
ENQUANTO Início 0 Quando pode não executar
PARA Início 0 Qtd. iterações conhecida
REPITA Final 1 Validação de entrada

===PAGE_BREAK===

Exemplo Integrado  —  Decisão + Repetição
Algoritmo que calcula média e situação de múltiplos alunos
●  ●  ● pseudocódigo
Algoritmo MediaTurma 
  Var n, i: inteiro 
      nota1, nota2, media: real 
  Início 
    Escreva("Quantos alunos? ") 
    Leia(n) 
    PARA i DE 1 ATÉ n FAÇA 
       Escreva("Aluno ", i, " - Nota 1: ") 
       Leia(nota1) 
       Escreva("Aluno ", i, " - Nota 2: ") 
       Leia(nota2) 
       media <- (nota1 + nota2) / 2 
       SE media >= 7 ENTÃO 
          Escreva("Situação: APROVADO  (média=", media,")") 
       SENÃO 
          SE media >= 5 ENTÃO 
             Escreva("Situação: RECUPERAÇÃO 
(média=",media,")") 
          SENÃO 
             Escreva("Situação: REPROVADO  
(média=",media,")") 
          FIM SE 
       FIM SE 
    FIM PARA 
  Fim
Análise do Algoritmo
PARA i DE 1 ATÉ n
Laço que repete para cada aluno. n iterações conhecidas 
→ PARA é ideal.
media = (n1+n2)/2
Cálculo da média aritmética entre as duas notas.
SE encadeado
3 possibilidades: ≥7 aprovado, ≥5 recuperação, <5 
reprovado.
⾠ Estruturas de decisão e repetição podem ser combinadas e 
aninhadas em qualquer nível de profundidade.

===PAGE_BREAK===

Exercícios  —  Estruturas de Decisão
Resolva em pseudocódigo (Portugol)
1Par ou Ímpar
Leia um número inteiro. Informe se ele é par ou ímpar. 
Dica: use o operador MOD (resto da divisão).
💡 SE (n MOD 2 = 0) ENTÃO...
2Calculadora Simples
Leia dois números e um operador (+, -, *, /). Realize a operação 
correspondente e exiba o resultado. Valide divisão por zero.
💡 Use CASO SELECIONE para o operador
3Categoria por Idade
Leia a idade de uma pessoa e classifique: 
< 12 = Criança | 12-17 = Adolescente 
18-59 = Adulto | >= 60 = Idoso
💡 Use SE/ENTÃO/SENÃO encadeados
4Maior de Três Números
Leia três números distintos (A, B, C). 
Exiba qual é o maior entre os três.
💡 Compare A>B, A>C e B>C

===PAGE_BREAK===

Exercícios  —  Estruturas de Repetição
Resolva em pseudocódigo (Portugol)
5Tabuada Completa
Leia um número N. Exiba a tabuada de N de 1 até 10, no formato: 
"N x i = resultado"
💡 PARA i DE 1 ATÉ 10 FAÇA
6Números Pares
Exiba todos os números pares no intervalo de 1 a 30. 
Contabilize quantos foram exibidos.
💡 PARA i DE 2 ATÉ 30 PASSO 2 FAÇA
7Somatório com Sentinel
Leia números inteiros positivos até o usuário digitar -1 (sentinel). Ao final 
exiba a soma e a quantidade de números lidos.
💡 ENQUANTO num <> -1 FAÇA (leia dentro)
8Senha com 3 Tentativas
Defina uma senha fixa (ex: 1234). Permita ao usuário até 3 tentativas. Se 
acertar, exiba 'Acesso permitido'. Caso esgote, exiba 'Bloqueado!'.
💡 REPITA ... ATÉ (acertou OU tentativas=3)

===PAGE_BREAK===

⭐  Exercícios Desafio
Combinando decisão + repetição em problemas reais
9 Números Primos de 1 a N ˒˒
Leia N. Para cada número de 2 até N, verifique se é primo (divisível apenas por 1 e por si mesmo). Exiba todos os primos encontrados e a 
contagem total. 
Dica: use dois laços aninhados — o externo percorre 2..N, o interno testa divisores de 2 até i-1.
10Calculadora com Menu e Repetição ˒˒˒
Crie uma calculadora que: 
1) Exibe menu (+, -, *, /, sair) 
2) Lê dois números e a opção 
3) Realiza o cálculo e exibe resultado 
4) Repete até o usuário escolher 'sair' 
Valide: divisão por zero e opção inválida.
11Sequência de Fibonacci ˒˒˒
Leia N. Exiba os N primeiros termos da sequência de Fibonacci: 0, 1, 1, 2, 3, 5, 8... 
Cada termo é a soma dos dois anteriores. 
Exiba também qual é o maior número da sequência gerada.

===PAGE_BREAK===

Resumo Geral  —  Guia de Referência Rápida
Quando usar cada estrutura?
ESTRUTURAS DE DECISÃO
SE/ENTÃO
Executar bloco só quando verdadeiro
SE/ENTÃO/SENÃO
Dois caminhos alternativos (V ou F)
SE encadeado
Mais de 2 situações possíveis
CASO SELECIONE
Muitos valores distintos de 1 variável
ESTRUTURAS DE REPETIÇÃO
ENQUANTO/FAÇA
Qtd. desconhecida • pode executar 0 vezes
PARA/ATÉ/FAÇA
Qtd. de iterações conhecida antecipadamente
REPITA/ATÉ
Executa ao menos 1 vez (validação de entrada)
⾠  Armadilha: Loop Infinito
Sempre garanta que a variável de controle seja atualizada dentro do laço. Em ENQUANTO e REPITA, se a condição nunca se tornar falsa, o programa trava. 
Certifique-se de que existe uma condição de saída alcançável.