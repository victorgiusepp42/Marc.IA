---
tipo: resolucao_aluno
etapa: 1
lista: lista2_portugol
autor_original: Victor Giusepp Almeida
fonte_dir: 01_listas/lista2_portugol/resolucoes_aluno
data_processamento: 2026-07-05
status: consolidado
observacao: Resolucoes de Victor consolidadas para melhor retrieval (cada uma era 1 chunk de ~500 tokens).
---

# Resolucoes — lista2_portugol

> Consolidado de 11 resolucoes do aluno. Cada resolucao e separada por `=== EX NN ===`.

## === EX 01: 10_Conversao_Decimal_Binario (Visualg) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista2_portugol
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_lista2_algoritmos_IA_IP/10_Conversao_Decimal_Binario.visualg
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

algoritmo "Conversão de Base Decimal para Binária"

var
  n,r:inteiro
  b:caractere
  
inicio

  r<-0
  b<-""

  escreval("Conversor de Base Decimal para Binária ")
  escreva("Digite um número inteiro: ")
  leia(n)
  escreval(n)

  enquanto n>0 faca
    
    r<-n mod 2

    b<-r+b

    n<-n div 2
  
  fimenquanto

  escreval(b)

fimalgoritmo
```

## === EX 02: 11_Analise_Estatistica_Sequencia (Visualg) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista2_portugol
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_lista2_algoritmos_IA_IP/11_Analise_Estatistica_Sequencia.visualg
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

algoritmo "Análise Estatística de Sequência"

var
  seq: vetor[1..50] de real
  i,qtd,acimaMedia: inteiro
  n,soma,media,maior,menor: real
  
inicio
  qtd<-0
  soma<-0

  escreval("Análise Estatística de Sequência - digite 0 para finalizar a sequência")
  escreva("Digite um número: ")
  leia(n)
  escreval(n)
  
   se n=0 entao
      escreval("Nenhum número foi informado")
        senao

      //Leitura das entradas
      enquanto n<>0 faca
      //Quantidade
      qtd<-qtd+1
      //Soma
      soma<-soma+n
      //Salva as entradas no vetor
      seq[qtd]<-n

      //Maior e menor
      se qtd=1 entao
          maior<-n
          menor<-n
          senao

          se n>maior entao
            maior<-n
          fimse

          se n<menor entao
            menor<-n
          fimse
        fimse

        //Solicita a próxima entrada para o usuário dentro do enquanto  
        escreva("Digite o próximo número (digite 0 para encerrar): ")
        leia(n)
        escreval(n)

        //Cria uma quebra entre as entradas e saídas
        se n=0 entao
          escreval("Processando...")
          escreval("")
        fimse

      fimenquanto

      //Média
      media<-soma/qtd

      //Quantidade de valores acima da média
      acimaMedia<-0
      
      para i de 1 ate qtd faca
        se seq[i]>media entao
          acimaMedia<-acimaMedia+1
        fimse
      fimpara

      //Saídas
      escreva("Análise da Sequência: [  ")
        para i de 1 ate 50 faca
          se seq[i]<>0 entao
            escreva(seq[i],"  ")
          fimse
        fimpara
        escreval("]")
      escreval("Quantidade de números lidos: ",qtd)
      escreval("Soma total: ",soma)
      escreval("Média aritmética: ",media:0:2)
      escreval("O maior número da sequência é o ",maior," e o menor número é o ",menor)
      escreval("Quantidade de valores acima da média: ",acimaMedia) 
    fimse

fimalgoritmo
```

## === EX 03: 1_triangulo_ou_nao_triangulo (Visualg) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista2_portugol
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_lista2_algoritmos_IA_IP/1_triangulo_ou_nao_triangulo.visualg
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

algoritmo "Triangulo ou nao triangulo"

var
  a,b,c: real

inicio

 escreva("Digite o primeiro lado: ")
 leia(a)
 escreval(a)
 escreva("Digite o segundo lado: ")
 leia(b)
 escreval(b)
 escreva("Digite o terceiro lado: ")
 leia(c)
 escreval(c)
  se (a<= 0) ou (b<= 0) ou (c<= 0)
   entao escreval("Lado menor que 0, não é triângulo!")
   senao 
    se nao((a<b+c) e (b<a+c) e (c<a+b))
      entao escreval("Não é triângulo")
      senao
        se (a=b) e (a=c)
          entao escreval ("É um triângulo equilátero!")
          senao 
            se (a=b) ou (a=c) ou (b=c)
              entao escreval ("É um triângulo isóceles!")
               senao escreval escreval ("É um triângulo escaleno!")
            fimse
        fimse
    fimse 
  fimse

fimalgoritmo


   



fimalgoritmo
```

## === EX 04: 2_dia_da_semana_por_extenso (Visualg) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista2_portugol
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_lista2_algoritmos_IA_IP/2_dia_da_semana_por_extenso.visualg
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

algoritmo "Dia da semana por extenso"

var
  d: inteiro

inicio

 escreval("Tabela de conversão")
 escreval("1 -> Segunda-feira")
 escreval("2 -> Terça-feira")
 escreval("3 -> Quarta-feira")
 escreval("4 -> Quinta-feira")
 escreval("5 -> Sexta-feira")
 escreval("6 -> Sábado")
 escreval("7 -> Domingo")
 escreva("Digite o número correspondente ao dia da semana: ")
 leia(d)
 escreval (d)

  escolha d 
    caso 1 
      escreval ("Segunda-feira")
    caso 2 
      escreval ("Terça-feira")
    caso 3 
      escreval ("Quarta-feira")
    caso 4 
      escreval ("Quinta-feira")
    caso 5 
      escreval ("Sexta-feira")
    caso 6 
      escreval ("Sábado")
    caso 7 
      escreval ("Domingo")
    outrocaso
      escreval ("Dia inválido!")
  fimescolha

fimalgoritmo
```

## === EX 05: 3_reajuste_salarial (Visualg) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista2_portugol
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_lista2_algoritmos_IA_IP/3_reajuste_salarial.visualg
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

algoritmo "Dia da semana por extenso"

var
  s,ns: inteiro

inicio
  
  escreva("Digite o salário atual do funcionário: ")
  leia(s)
  escreval (s)
  se s<0 
    entao escreval ("Salário inválido")
    senao
      se (s<=1000)
        entao ns<-s*1.15
        senao 
          se (s>1000) e (s<=2500)
            entao ns<-s*1.1
            senao
              se s>2500
                entao ns<-s*1.05
              fimse
          fimse
      fimse
  fimse
  escreval("O novo salário é R$",ns)

fimalgoritmo
```

## === EX 06: 4_potenciacao_sem_operador (Visualg) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista2_portugol
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_lista2_algoritmos_IA_IP/4_potenciacao_sem_operador.visualg
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

algoritmo "Potenciação sem Operador"

var
  r,i,x,y: inteiro
  

inicio

  r<-1
  
  Repita 
    escreva("Digite o valor da base: ")
    leia(x)
    se x<0 
      entao escreval("Apenas número inteiros não negativos!")
    fimse
    ate x>=0
    escreval(x)
  
  
 Repita 
    escreva("Digite o valor do expoente: ")
    leia(y)
    se y<0 
      entao escreval("Apenas número inteiros não negativos!")
    fimse
    ate y>=0
    escreval(x) 

  para i de 1 ate y 
    faca 
    r<-r*x
    i<-i+1
  fimpara

  escreval("Resultado final: " r)


fimalgoritmo
```

## === EX 07: 5_MDC_por_subtracpes (Visualg) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista2_portugol
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_lista2_algoritmos_IA_IP/5_MDC_por_subtracpes.visualg
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

algoritmo "Potenciação sem Operador"

var
  a,b,i: inteiro
  

inicio

 Repita 
    escreva("Digite o primeiro número: ")
    leia(a)
    se a<=0 
      entao escreval("Apenas número inteiros positivos!")
    fimse
    ate a>0
    escreval(a)
  
  
 Repita 
    escreva("Digite o segundo número: ")
    leia(b)
    se b<=0 
      entao escreval("Apenas número inteiros positivos!")
    fimse
    ate b>0
    escreval(b)
  
  se b>a 
    entao 
      i<-a
      a<-b
      b<-i
  fimse

  enquanto a<>b 
    faca 
    i<-a-b
    a<-b
    b<-i
      se b>a 
        entao 
          i<-a
          a<-b
          b<-i
      fimse
  fimenquanto

  escreval("O MDC é ", a)

fimalgoritmo
```

## === EX 08: 6_Relatorio_Vendas_Mensais (Visualg) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista2_portugol
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_lista2_algoritmos_IA_IP/6_Relatorio_Vendas_Mensais.visualg
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

algoritmo "Relatório de Vendas Mensais"

var
   nome: vetor[1..6] de caractere
   vendas: vetor[1..6] de real
   i,abaixoMedia: inteiro
   total, media,maiorVenda: real
   nomeMaior: caractere

inicio

  //total<-0

  para i de 1 ate 6 faca
    escreva("Digite o nome do vendedor ",i,": ")
    leia(nome[i])
    escreval(nome[i])
    escreva("Digite o valor vendido: ")
    leia(vendas[i])
    escreval("R$"vendas[i])

    total<-total+vendas[i]

  fimpara

  media<-total/6

  //abaixoMedia<-0
  maiorVenda<-vendas[1]
  nomeMaior<- nome[1]

  para i de 1 ate 6 faca
    se vendas[i]<media entao 
      abaixoMedia<-abaixoMedia+1
    fimse

    se vendas[i]>maiorVenda entao
      maiorVenda<-vendas[i]
      nomeMaior<-nome[i]
    fimse
  
  fimpara

  escreval(" ")
  escreval("Total de vendas: R$",total)
  escreval("Média de vendas por vendedor: R$",media:8:2)
  escreval(abaixoMedia," Vendedores ficaram abaixo da média")
  escreval("O vendedor que mais vendeu foi ", nomeMaior, " com R$", maiorVenda, " em vendas")


fimalgoritmo
```

## === EX 09: 7_Adivinhe_Numero_Secreto (Visualg) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista2_portugol
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_lista2_algoritmos_IA_IP/7_Adivinhe_Numero_Secreto.visualg
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

algoritmo "Adivinhe o número secreto"

var
   numsecreto,num,tentativas:inteiro
   acertou: logico

inicio
  
  numsecreto<-RandI(100)+1
  escreval("Adivinhe o número secreto!")
  acertou<-falso

  repita
  escreva("Digite um número para tentar adivinhar: ")
  leia(num)
  escreval(num)
    se num=numsecreto entao
      acertou<-verdadeiro
      escreval("Acertou !!!") senao 
      se num>numsecreto entao
        escreval("Muito alto !!!") senao 
        se num<numsecreto entao
          escreval("Muito baixo !!!")
        fimse
      fimse
    fimse
    tentativas<-tentativas+1
  ate (acertou=verdadeiro) ou (tentativas=5)

  se acertou=falso entao
    escreval("O número secreto era: ",numsecreto)
  fimse

fimalgoritmo
```

## === EX 10: 8_Contador_Notas (Visualg) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista2_portugol
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_lista2_algoritmos_IA_IP/8_Contador_Notas.visualg
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

algoritmo "Contador de Notas"

var
  nota,nota2,nota5,nota10,nota20,nota50,nota100:inteiro
   
inicio

  escreval("Contador de notas - digite 0 para finalizar")
  nota<-1

  enquanto nota<>0 faca
    escreva("Digite o valor da nota: ")
    leia(nota)
    escreval(nota)

    escolha nota
      caso 2 
      nota2<-nota2+1
      caso 5 
      nota5<-nota5+1
      caso 10 
      nota10<-nota10+1
      caso 20 
      nota20<-nota20+1
      caso 50 
      nota50<-nota50+1
      caso 100 
      nota100<-nota100+1
      outrocaso 
        se nota=0 entao
          escreval("Processando...")
          senao escreval("Valor inválido!")
        fimse
    fimescolha

  fimenquanto

  escreval(" ")
  escreval("Tabela de notas")
  escreval("Notas R$2,00: ", nota2)
  escreval("Notas R$5,00: ", nota5)
  escreval("Notas R$10,00: ", nota10)
  escreval("Notas R$20,00: ", nota20)
  escreval("Notas R$50,00: ", nota50)
  escreval("Notas R$100,00: ", nota100)
  escreval("Total em caixa: R$",((2*nota2)+(5*nota5)+(10*nota10)+(20*nota20)+(50*nota50)+(100*nota100)))

fimalgoritmo
```

## === EX 11: 9_Verificador_Numero_Perfeito (Visualg) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista2_portugol
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_lista2_algoritmos_IA_IP/9_Verificador_Numero_Perfeito.visualg
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

algoritmo "Verificador de Núemro Perfeito"

var
  n,i,j,soma,qtd:inteiro
  
inicio
  
  escreva("Digite um número inteiro maior que 1: ")
  leia(n)
  escreval(n)

  //Garante que o código não trava
  se n>8129 entao
    n<-8129
  fimse

  qtd<-0

  //repetição para todos os números menores que n
  para i de 2 ate n faca
    
    soma<-0

    //Soma dos divisores
    para j de 1 ate (i-1) faca
      se (i mod j)=0 entao
        soma<-soma+j
      fimse
    fimpara
    
    //Validação se é perfeito
    se soma=i entao 
      escreval(i," é um número perfeito")
      qtd<-qtd+1
    fimse

  fimpara

  escreval("A quantidade de números perfeitos é ",qtd)

fimalgoritmo
```
