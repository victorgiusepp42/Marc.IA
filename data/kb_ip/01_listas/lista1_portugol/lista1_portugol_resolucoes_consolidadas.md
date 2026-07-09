---
tipo: resolucao_aluno
etapa: 1
lista: lista1_portugol
autor_original: Victor Giusepp Almeida
fonte_dir: 01_listas/lista1_portugol/resolucoes_aluno
data_processamento: 2026-07-05
status: consolidado
observacao: Resolucoes de Victor consolidadas para melhor retrieval (cada uma era 1 chunk de ~500 tokens).
---

# Resolucoes — lista1_portugol

> Consolidado de 11 resolucoes do aluno. Cada resolucao e separada por `=== EX NN ===`.

## === EX 01: 10_menu_operacoes (Visualg) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista1_portugol
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_lista1_algoritmos_IA_IP/10_menu_operacoes.visualg
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

algoritmo "menu_operacoes"

var operacao,n1,n2:inteiro
    retorno:caracter

inicio
  escreval("Escolha a operação desejada")
  escreval("1-soma")
  escreval("2-subtração")
  escreval("3-sair")
  escreval("Digite o código da operação escolhida: ")
  leia(operacao)
  enquanto operacao <> 3 faca
    enquanto operacao>3 ou operacao<1 faca
      escreval("Opção inválida, digite um número de 0 a 3")
      escreva("Digite o código da operação escolhida: ")
      leia(operacao)
      escreval(operacao)
    fimenquanto
    se operacao<>3 entao 
      escreva("Digite o primeiro número: ")
      leia(n1)
      escreval(n1)
      escreva("Digite o segundo número: ")
      leia(n2)
      escreval(n2)
        se operacao = 1 entao 
          escreval("A soma é ",n1+n2)
          senao escreval("A subtração é ",n1-n2)
        fimse
      escreval("Deseja fazer uma nova operacao?(Y/N)")
      leia (retorno)
      se retorno="Y" entao
        escreval("Escolha a operação desejada")
        escreval("1-soma")
        escreval("2-subtração")
        escreval("3-sair")
        escreval("Digite o código da operação escolhida: ")
        leia(operacao)
        senao operacao<-3
      fimse 
    fimse
  fimenquanto
  escreval("Encerrando...")
fimalgoritmo
```

## === EX 02: 11_maior_menor (Visualg) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista1_portugol
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_lista1_algoritmos_IA_IP/11_maior_menor.visualg
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

algoritmo "maior_menor"

var n, i, num, maior, menor: inteiro

inicio 
  escreva("Quantos números você deseja classificar? ")
  leia(n)
  escreval(n)
  enquanto n<1 faca
    escreval("Digite apenas números naturais!")
    escreva("Quantos números você deseja classificar? ")
    leia(n)
    escreval(n)
  fimenquanto
    escreva("Digite o número 1: ")
    leia(num)
    escreval(num)
    enquanto num<1 faca
      escreval("Digite apenas números naturais!")
      escreva("Digite o número 1: ")
      leia(num)
      escreval(num)
    fimenquanto
  maior<-num
  menor<-num
  para i de 2 ate n faca
    escreva("Digite o número ",i," :")
    leia(num)
    escreval(num)
    enquanto num<1 faca
      escreval("Digite apenas números naturais!")
      escreva("Digite o número ", i, ": ")
      leia(num)
    fimenquanto
    se num>maior entao
      maior<-num
    fimse
    se num<menor entao
      menor<-num
    fimse
  fimpara
  escreval("O menor é ",menor)
  escreval("O maior é ",maior)
fimalgoritmo
```

## === EX 03: 1_antecessor_sucessor (Visualg) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista1_portugol
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_lista1_algoritmos_IA_IP/1_antecessor_sucessor.visualg
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

algoritmo "antecessor_sucessor"


var n: inteiro

inicio
escreva("Digite um numero inteiro: ")
leia (n)
escreval(n)
escreval("O antecessor é ",(n-1))
escreval("O sucessor é ",(n+1))
fimalgoritmo
```

## === EX 04: 2_area_retangulo (Visualg) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista1_portugol
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_lista1_algoritmos_IA_IP/2_area_retangulo.visualg
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

algoritmo "area_retangulo"

var l1,l2,area: real

inicio

escreva("Digite o tamanho do lado maior: ")
leia(l1)
escreval(l1)

escreva("Digite o tamanho do lado menor: ")
leia(l2)
escreval(l2)

area<-l1*l2

escreva("A área do retângulo é ",area)

fimalgoritmo
```

## === EX 05: 3_conversor_idade (Visualg) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista1_portugol
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_lista1_algoritmos_IA_IP/3_conversor_idade.visualg
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

algoritmo "conversor_idade"

var idade: inteiro

inicio

escreva("Digite sua idade em anos: ")
leia(idade)
escreval(idade)

escreva("Sua idade em meses é ",idade*12)

fimalgoritmo
```

## === EX 06: 4_media_aprov (Visualg) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista1_portugol
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_lista1_algoritmos_IA_IP/4_media_aprov.visualg
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

algoritmo "media_aprov"

var nota1,nota2,media:real

inicio

escreva("Digite a primeira nota: ")
leia(nota1)
se ((nota1<=10) e (nota1>=0))
entao escreval(nota1)
senao enquanto ((nota1>10) ou (nota1<0)) faca
escreval("")
escreva("Nota Inválida! Digite uma nota entre 0 e 10: ")
leia(nota1)
escreval(nota1)
fimenquanto
fimse

escreva("Digite a segunda nota: ")
leia(nota2)
se ((nota2<=10) e (nota2>=0))
entao escreval(nota2)
senao enquanto ((nota2>10) ou (nota2<0)) faca
escreval("")
escreva("Nota Inválida! Digite uma nota entre 0 e 10: ")
leia(nota2)
escreval(nota2)
fimenquanto
fimse

media<-((nota1+nota2)/2)

se media>=7 
entao escreva("Media = ",media," - Aprovado")
senao escreva("Media = ",media," - Reprovado")
fimse

fimalgoritmo
```

## === EX 07: 5_soma_1_ate_n (Visualg) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista1_portugol
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_lista1_algoritmos_IA_IP/5_soma_1_ate_n.visualg
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

algoritmo "soma_1_ate_n"

var n,c,soma:inteiro

inicio

escreva("Digite N: ")
leia(n)
escreval(n)

para c de 1 ate n faca
soma<-soma+c
fimpara

escreva("Soma: ",soma)

fimalgoritmo
```

## === EX 08: 6_conta_pares (Visualg) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista1_portugol
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_lista1_algoritmos_IA_IP/6_conta_pares.visualg
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

algoritmo "conta_pares"

var i, n, cont:inteiro

inicio
  cont <- 0
  para i de 1 ate 10 faca
    escreva("Digite o numero ", i, ": ")
    leia(n)
    escreval(n)
    se n mod 2 = 0 entao
    cont<- cont+1
    fimse
  fimpara
  escreval("Quantidade de pares: ", cont)

fimalgoritmo
```

## === EX 09: 7_media_ate_0 (Visualg) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista1_portugol
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_lista1_algoritmos_IA_IP/7_media_ate_0.visualg
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

algoritmo "media_ate_0"

var cont, n, soma: real

inicio
  cont<-0
  soma<-0
  escreval("Quando digitar 0 será calculada a média")
  escreva("Digite um numero: ")
  leia(n)
  escreval(n)

    enquanto n <> 0 faca
     soma<-soma+n
     cont<-cont+1
      escreva("Digite outro numero: ")
      leia(n)
      escreval(n)
    fimenquanto
  escreval("Média: ",soma/cont:0:1)

fimalgoritmo
```

## === EX 10: 8_num_se_primo (Visualg) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista1_portugol
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_lista1_algoritmos_IA_IP/8_num_se_primo.visualg
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

algoritmo "num_se_primo_nao_trava"

var
  n, i: inteiro
  primo: logico

inicio
  primo <- verdadeiro
  escreval("Bem vindo ao validador de números primos!")
  escreva("Digite um numero: ")
  leia(n)
  se n < 2 entao
    primo <- falso
  fimse
  para i de 2 ate int(raizq(n)) faca
    se n mod i = 0 entao
      primo <- falso
    fimse
  fimpara
  se primo entao
    escreval(n, " é primo.")
  senao
    escreval(n, " não é primo.")
  fimse

fimalgoritmo
```

## === EX 11: 9_ordenador_crescente (Visualg) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista1_portugol
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_lista1_algoritmos_IA_IP/9_ordenador_crescente.visualg
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

algoritmo "ordenador_crescente"

var
  a,b:real

inicio
  escreva("Digite um número: ")
  leia(a)
  escreval(a)
  escreva("Digite outro número: ")
  leia(b)
  escreval(b)
  se a>b entao
    escreval("Ordem crescente: ", b, " < ", a)
    senao 
    escreval("Ordem crescente: ", a, " < ", b)
  fimse
fimalgoritmo
```
