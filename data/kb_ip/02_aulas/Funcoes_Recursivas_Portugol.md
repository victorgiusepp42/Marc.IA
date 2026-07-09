---
tipo: slide_ou_roteiro
etapa: 1
topico: funcoes
fonte: docs/materiais_kb/AULAS/Funcoes_Recursivas_Portugol (2).txt
data_processamento: 2026-07-04
autor_original: Prof. Dr. Márcio de Souza Dias (UFCAT/IMTec)
status: extraido_pdf_bruto
ordem_aula: '0'
observacao: Texto extraído automaticamente do PDF; revisar figuras/diagramas que não vieram.
---

# Funcoes_Recursivas_Portugol

funcao inteiro fatorial(inteiro n)
{
  se (n == 0)
    retorne 1
  senao
    retorne n * fatorial(n-1)
}
FUNÇÕES RECURSIVAS
em Algoritmos
Portugol
Introdução à Programação

===PAGE_BREAK===

📋
  Conteúdo da Aula
01
O que é Recursão?
Conceito e analogias do mundo real
02
Anatomia de uma Função Recursiva
Caso base e caso recursivo
03
Exemplo 1 — Fatorial
Implementação passo a passo em Portugol
04
Exemplo 2 — Fibonacci
Sequência e árvore de chamadas
05
Exemplo 3 — Soma de Vetor
Percorrendo estruturas recursivamente
06
Recursão vs. Iteração
Comparação de abordagens
07
Exercícios Práticos
Atividades em Portugol

===PAGE_BREAK===

01
O que é Recursão?
Conceito fundamental e analogias

===PAGE_BREAK===

💡
  O que é Recursão?
A recursão é um mecanismo em que uma função chama a si mesma direta ou indiretamente para resolver um 
problema, dividindo-o em subproblemas menores do mesmo tipo.
🪞
 Espelhos Paralelos
A imagem refletida entre dois espelhos cria cópias de si mesma 
— uma dentro da outra — infinitamente.
🎭
 Boneca Matrioska
Cada boneca contém uma boneca menor dentro dela, até 
chegar na menor delas (o caso base).
📁
 Pastas no Computador
Uma pasta pode conter outras pastas, que contêm mais 
pastas... A navegação usa recursão.
🧩
 Dividir para Conquistar
Quebrar um grande problema em problemas menores do 
mesmo tipo até que sejam triviais de resolver.

===PAGE_BREAK===

🔁
  Como a Recursão Funciona?
Pense na recursão como resolver um problema reduzindo-o ao mesmo problema, porém menor:
Problema original
n = 5
Subproblema
n = 4
Subproblema
n = 3
Subproblema
n = 2
CASO BASE
n = 0 → 1
Fase de DESCIDA
(chamadas recursivas)
← A cada chamada, o problema fica menor até chegar ao Caso Base
⚠
  Toda função recursiva PRECISA de um caso base para não entrar em loop infinito!

===PAGE_BREAK===

02
Anatomia de uma
Função Recursiva
Caso Base e Caso Recursivo

===PAGE_BREAK===

🔬
  Partes de uma Função Recursiva
📍
 CASO BASE (Condição de Parada)
É a condição em que a função NÃO chama a si mesma. Sem o caso base a recursão nunca terminaria, causando estouro de pilha (Stack 
Overflow). Deve ser o problema mais simples possível.
🔄
 CASO RECURSIVO (Passo Recursivo)
É onde a função chama a si mesma com um argumento MENOR ou mais simples. Cada chamada deve se aproximar do caso base, 
garantindo que a recursão termine.
funcao inteiro minha_funcao(inteiro n){
  // --- CASO BASE ---
  se (n == 0)
    retorne 1          // Para aqui! Não chama a si mesmo.
  // --- CASO RECURSIVO ---
  senao
    retorne n * minha_funcao(n - 1)   // Chama com n menor
}

===PAGE_BREAK===

03
Exemplo 1
Fatorial
n! = n × (n-1) × (n-2) × ... × 1

===PAGE_BREAK===

➗
  Fatorial — Definição Matemática
Definição Matemática:
n! = 1,  se n = 0  (caso base)
n! = n × (n-1)!,  se n > 0  (caso recursivo)
Trace de execução para fatorial(4):
fatorial(4)  →  4 × fatorial(3)
fatorial(3)  →  3 × fatorial(2)
fatorial(2)  →  2 × fatorial(1)
fatorial(1)  →  1 × fatorial(0)
fatorial(0)  →  1  ✓ CASO BASE
fatorial(1)  →  1 × 1 = 1
fatorial(2)  →  2 × 1 = 2
fatorial(3)  →  3 × 2 = 6
fatorial(4)  →  4 × 6 = 24 ✓
⬇
 Descida (chamadas)
⬆
 Subida (retornos)
🎯
 BASE

===PAGE_BREAK===

💻
  Fatorial em Portugol
programa {
  funcao inteiro fatorial(inteiro n){
    se ((n == 0) ou (n == 1))        // CASO BASE
      retorne 1          
    senao
      retorne n * fatorial(n - 1)    // CASO RECURSIVO
  }
  funcao inicio() {
    
    inteiro num
    escreva("Digite um número inteiro: ")
    leia(num)
    escreva("O Fatorial de ", num,  " é ", fatorial(num))
    
  }
}
Como funciona?
1 O algoritmo lê o número N do usuário
2 Chama a função fatorial(N)
3 Se N=0 ou N=1 → retorna 1 (caso base)
4 Senão → retorna N × fatorial(N-1)
5 Continua até N chegar a 0 ou 1
6 Valores vão sendo multiplicados na volta
Teste: fatorial(5) = 120

===PAGE_BREAK===

04
Exemplo 2
Fibonacci
A sequência que aparece na natureza

===PAGE_BREAK===

🌀
  Fibonacci em Portugol
Sequência: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...   |   fib(n) = fib(n-1) + fib(n-2)
programa {
  funcao inteiro fibonacci(inteiro n){
    se (n == 0)
      retorne 0        // CASO BASE 1
    senao 
      se(n==1)         // CASO BASE 2  
        retorne 1
      senao            // CASO RECURSIVO
        retorne fibonacci(n-1) + fibonacci(n-2)
  }
  funcao inicio() {
    inteiro num, res
    escreva("Quantos termos de Fibonacci? ")
    leia(num)
    escreva("Sequência de Fibonacci: ")
    para(inteiro i = 0; i<=(num-1); i++){
      res = fibonacci(i)
      escreva(res, " ")
    }          
  }
}
Árvore de chamadas para fib(4):
fib(4)
fib(3) fib(2)
fib(2) fib(1) fib(1) fib(0)
fib(1)
=1
fib(0)
=0
⚠
  Fibonacci recursivo recalcula muitos valores 
repetidamente. fib(5) faz 15 chamadas!

===PAGE_BREAK===

05
Exemplo 3
Soma de Vetor
Percorrendo estruturas recursivamente

===PAGE_BREAK===

📊
  Soma de Vetor em Portugol
programa {
  // SOMA OS VALORES DE UM VETOR RECURSIVAMENTE
  funcao inteiro somaVetor(inteiro v[], inteiro pos, inteiro 
tamanho){
    se (pos >= tamanho)  // CASO BASE
      retorne 0
    senao // CASO RECURSIVO
      retorne v[pos] + somaVetor(v, pos + 1, tamanho)
  }
  funcao inicio() {
    inteiro vetor[5], total
    escreva("Digite 5 números inteiros: \n")
    
    para(inteiro i=0; i<5; i++){
      escreva("Número ", i+1, ": ")
      leia(vetor[i])
    }
    total = somaVetor(vetor, 0, 5)
    escreva("Soma Total = ", total)
  }            
}
Trace de execução
(vetor: [3, 7, 2, 5, 1]):
somaVetor(v, 1, 5)  →  3 + 
somaVetor(v,2,5)
somaVetor(v, 2, 5)  →  7 + 
somaVetor(v,3,5)
somaVetor(v, 3, 5)  →  2 + 
somaVetor(v,4,5)
somaVetor(v, 4, 5)  →  5 + 
somaVetor(v,5,5)
somaVetor(v, 5, 5)  →  1 + 
somaVetor(v,6,5)
somaVetor(v, 6, 5)  →  0  ✓ CASO BASE
 
↑ Retornos:  1+0=1, 5+1=6, 2+6=8,
             7+8=15, 3+15 = 18 ✓
Resultado: Soma = 18

===PAGE_BREAK===

06
Recursão vs.
Iteração
Quando usar cada abordagem?

===PAGE_BREAK===

⚖
  Recursão × Iteração — Comparação
RECURSÃO ITERAÇÃO (loops)
✅
 Código mais elegante e legível ✅
 Geralmente mais eficiente em memória
✅
 Ideal para problemas definidos
recursivamente (Fibonacci, árvores) ✅
 Mais fácil de depurar e rastrear
⚠
 Maior consumo de memória
(pilha de chamadas) ✅
 Não há risco de estouro de pilha
⚠
 Pode ser lenta se houver
muitas chamadas repetidas
⚠
 Código pode ser mais complexo
para certos algoritmos
❌
 Risco de Stack Overflow
se o caso base for errado
❌
 Pode ser difícil para problemas
naturalmente recursivos
💡
 Use recursão quando o problema se define naturalmente de forma recursiva (árvores, divide & conquer, backtracking).

===PAGE_BREAK===

07
Exercícios
Práticos
Atividades em Portugol

===PAGE_BREAK===

📝
  Exercícios — Parte 1
🏋
  Exercício 1 — Potência Recursiva
Implemente em Portugol uma função recursiva potencia(base, expoente) que calcule base^expoente.
• Caso base: qualquer número elevado a 0 é igual a 1
• Caso recursivo: base^n = base × base^(n-1)
• Teste com: potencia(2, 8) = 256  e  potencia(3, 4) = 81
funcao inteiro potencia(inteiro base, inteiro exp){
   se (exp == 0)
      retorne ___          // Complete: qual é o caso base?
   senao
      retorne ___ * potencia(___, ___ - 1)  // Complete!
}
🏋
  Exercício 2 — Contagem Regressiva
Crie uma procedure recursiva contagemRegressiva(n) que imprime números de N até 0 (sem usar laços).
• Exemplo: contagemRegressiva(5) → imprime: 5  4  3  2  1  0  🚀
 Lançamento!
• Dica: imprima N antes de chamar a função com N-1.

===PAGE_BREAK===

📝
  Exercícios — Parte 2
🔥
  Exercício 3 — Soma dos Dígitos (Intermediário)
Escreva uma função recursiva somaDigitos(n) que calcule a soma dos dígitos de um número inteiro positivo.
• Exemplo: somaDigitos(1234) = 1+2+3+4 = 10
• Dica: o último dígito é n MOD 10 e o restante é n DIV 10.
• Caso base: quando n < 10, a soma é o próprio n.
funcao inteiro somaDigitos(inteiro n ){
   se (n < 10)
      retorne ___                           // Complete: caso base
   senao
      retorne (n % 10) + somaDigitos(___ /10)   // Complete!
}
🚀
  Exercício 4 — Busca Binária Recursiva (Desafio)
Implemente a busca binária recursiva em um vetor de 10 elementos já ordenados.
• A função buscaBinaria(v, ini, fim, valor) deve retornar a posição do elemento ou -1 se não encontrado.
• Caso base 1: ini > fim → retorne -1
• Caso base 2: v[meio] = valor → retorne meio
• Recursivo: busque na metade esquerda ou direita

===PAGE_BREAK===

⚠
  Dicas e Erros Comuns
Erros Frequentes
❌
 Sem Caso Base
A função chama a si mesma sem parar → Stack Overflow 
(estouro de pilha). SEMPRE defina quando parar.
❌
 Caso Base Errado
O caso base está definido, mas a lógica está errada. Ex: usar 
n=1 no fatorial esquece que 0! = 1.
❌
 Não se Aproxima do Base
Os argumentos não diminuem a cada chamada — a função 
nunca chega ao caso base.
Boas Práticas
✅
 Identifique o Caso Base Primeiro
Antes de codificar, pense: quando o problema é trivial de 
resolver sem recursão?
✅
 Trace a Execução no Papel
Antes de rodar, simule manualmente as chamadas para n=3 
ou n=4 para validar a lógica.
✅
 Prefira Recursão para...
Árvores, grafos, divisão e conquista, backtracking e problemas 
com definição matemática recursiva.

===PAGE_BREAK===

📌
  Resumo da Aula
Recursão Uma função que chama a si mesma para resolver subproblemas menores do mesmo tipo.
Caso Base Condição obrigatória de parada. Sem ela, a recursão é infinita (Stack Overflow).
Caso Recursivo Chamada da função com argumento menor, aproximando-se sempre do caso base.
Pilha de Chamadas Cada chamada recursiva ocupa espaço na pilha de memória — tenha cuidado com recursões 
profundas.
Quando Usar Problemas naturalmente recursivos: árvores, divisão e conquista, fractais, backtracking.