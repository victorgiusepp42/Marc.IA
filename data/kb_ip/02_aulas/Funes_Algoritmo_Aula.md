---
tipo: slide_ou_roteiro
etapa: 0
topico: geral
fonte: docs/materiais_kb/AULAS/Funes_Algoritmo_Aula (1).txt
data_processamento: 2026-07-04
autor_original: Prof. Dr. Márcio de Souza Dias (UFCAT/IMTec)
status: extraido_pdf_bruto
ordem_aula: '0'
observacao: Texto extraído automaticamente do PDF; revisar figuras/diagramas que não vieram.
---

# Funes_Algoritmo_Aula

Introdução à Programação - IA
Funções em
Algoritmos
Modularização · Parâmetros · Retorno · Escopo · Recursão
Definição Parâmetros Retorno Escopo Recursão Exercícios


===PAGE_BREAK===

O que é um Subprograma?
Conceito fundamental · Slide 2 de 10
Um subprograma é um programa auxiliar que executa uma sub tarefa específica. No VisuAlg existem dois tipos: procedimentos e funções.
🔍
 Legibilidade
O programa principal fica curto e fácil de ler, pois os detalhes ficam no 
subprograma.
♻
  Reusabilidade
Escreve-se o código uma vez e pode-se chamá-lo quantas vezes for necessário, 
sem duplicação de código.
🧩
  Modularização
Divide problemas complexos em partes menores e independentes, cada uma 
resolvida por um subprograma, facilitando compreensão e manutenção.
🛠
 Manutenção
Corrigir ou melhorar um subprograma não afeta os outros — basta alterar um 
único bloco.
💡
 Regra do VisuAlg
Os subprogramas devem ser declarados depois das variáveis globais e antes do inicio do programa principal. Cada subprograma pode ter suas próprias variáveis locais.


===PAGE_BREAK===

Declarando um Procedimento
Conceito fundamental · Slide 3 de 10
Procedimento é um subprograma que executa ações mas não retorna nenhum valor ao programa chamador.
✅
 Características
Usa a palavra procedimento na declaração. Termina com fimprocedimento. A 
chamada aparece como um comando isolado.
⚠
 Atenção
Procedimento não usa retorne. Se precisar devolver um resultado ao programa 
principal, use uma função ou passagem por referência.


===PAGE_BREAK===

O que é uma Função?
Conceito fundamental · Slide 4 de 10
Função é um bloco de código nomeado que executa uma tarefa específica e pode ser chamado (invocado) em qualquer ponto do programa, 
retornando ou não um resultado.
📦
  Encapsulamento
Agrupa instruções em um bloco com nome próprio, escondendo a complexidade 
interna.
♻
  Reusabilidade
Escrita uma vez, chamada quantas vezes for necessário, sem duplicação de 
código.
🧩
  Modularização
Divide problemas complexos em partes menores, facilitando compreensão e 
manutenção.
🎯
  Abstração
Permite usar uma funcionalidade sem conhecer seus detalhes de 
implementação.
💡
 ANALOGIA
Uma função é como uma receita: define-se o passo a passo uma vez e executa-se quantas vezes precisar, passando ingredientes (parâmetros) e obtendo o resultado (retorno).

===PAGE_BREAK===

Anatomia de uma Função
Estrutura · Slide 5 de 10
CHAMADA
resultado ← soma(3,5)
ENTRADA
Parâmetros: a=3, b=5
PROCESSO
s ← a + b 
RETORNO
retorne s → 8
// ① Declaração
funcao soma(a: inteiro, b: inteiro): inteiro // ② Parâmetros 
formais
var
  s:inteiro
inicio
  s <- a + b      // ③ Processamento
  retorne s          // ④ Retorno
fimfuncao
// ⑤ Chamada
resultado <- soma(3, 5)   // resultado = 8
① Declaração  (def + nome)
② Parâmetros formais
③ Processamento
④ Retorno com retorne
⑤ Chamada no programa principal

===PAGE_BREAK===

Parâmetros e Argumentos
Passagem de dados · Slide 6 de 10
Conceito Por Valor Por Referência
O que passa? Uma CÓPIA do valor O ENDEREÇO da variável
Altera original? Não — cópia isolada Sim — alterações propagam
Uso típico Apenas consultar valor Retornar múltiplos resultados


===PAGE_BREAK===

Funções vs Procedimentos
Retorno de valor · Slide 7 de 10
🔵
  FUNÇÃO  (com retorno)
funcao fatorial(n:inteiro): inteiro
var
   f,i:inteiro
  inicio
   f <- 1 
   para i de 1 ate n faca 
       f <- f * i 
   fimpara
   retorne f          // ← retorna valor 
fimfuncao
result <- fatorial(5)
escreva(result)       # 120
✅
 CARACTERÍSTICA
Devolve um valor com retorne. Pode ser usada em expressões: x <- fatorial(5) * 2.
🟠
  PROCEDIMENTO  (sem retorno)
procedimento exibir_menu()
  inicio
    escreval("1. Calcular")
    escreval("2. Relatório")
    escreval("3. Sair")
    // sem return!
  fimprocedimento
exibir_menu()    // chamada direta
// resultado <- exibir_menu() → None
⚠
 CARACTERÍSTICA
Executa ações (Calcular, Relatório, Sair). Não devolve valor útil — gera erro de 
execução em VisuAlg.

===PAGE_BREAK===

Escopo de Variáveis
Local vs Global - O escopo define onde uma variável é conhecida e pode ser usada dentro do algoritmo.                                                                    Slide 8 de 10 
🔵
  Variável LOCAL
Declarada DENTRO da função. Existe apenas enquanto a função executa. Cada 
chamada cria novas variáveis locais independentes.
🌐
  Variável GLOBAL
Declarada FORA de qualquer função. Visível em todo o programa. Evite modificá-las 
— use parâmetros e retorno.
VisuAlg — Variáveis locais e globais
algoritmo "Escopo_Global_Local" 
var total: real // GLOBAL — visível em todo o algoritmo 
funcao calcularMedia(a, b: real): real 
 var 
   soma: real // LOCAL — existe só aqui dentro 
 inicio 
   soma <- a + b 
   total <- soma // acessa a global "total" 
   retorne soma / 2 
fimfuncao 
inicio 
  escreval(calcularMedia(8.0, 6.0)) // 7.0 
  escreval(total) // 14.0 (soma foi salva na global)  
  //escreval(soma) 
fimalgoritmo
⚠
 BOAS PRÁTICAS
Prefira passar dados via parâmetros e receber via retorne. 
Variáveis globais dificultam testes e manutenção.

===PAGE_BREAK===

Exemplo Completo: Calculadora Modular
Boas práticas · Slide 9 de 10
   Vamos fazer uma Calculadora modularizada com funções
✅
 Uma responsabilidade por função ✅
 Programa principal curto e legível ✅
 Funções reutilizáveis e testáveis

===PAGE_BREAK===

Exercícios em Aula
Prática guiada · Slide 9 de 10
01
FÁCILConversor de Temperatura
Crie a função celsius_para_fahrenheit(c) que receba graus Celsius e retorne em Fahrenheit.
Fórmula: F = (C × 9/5) + 32
Teste: 0°C→32°F  |  100°C→212°F  |  37°C→98.6°F
02
FÁCILPar ou Ímpar em Lista
Crie a função eh_par(n) que retorne True/False. Em seguida crie o procedimento classificar_lista(lst) que exiba cada número com sua classificação.
Dica: use o operador % (módulo).
03
MÉDIOSistema de Notas com Classificação
Crie: calcular_media(notas) → média da lista; classificar_aluno(media) → 'Aprovado' (≥7), 'Recuperação' (≥5) ou 'Reprovado' (<5).
No principal: resultado = classificar_aluno(calcular_media([8, 6.5, 7]))