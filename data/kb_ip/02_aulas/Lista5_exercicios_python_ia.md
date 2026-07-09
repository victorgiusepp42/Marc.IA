---
tipo: lista_exercicios
etapa: 2
topico: vetores_matrizes_listas
fonte: docs/materiais_kb/AULAS/Lista5_exercicios_python_ia.txt
data_processamento: 2026-07-04
autor_original: Prof. Dr. Márcio de Souza Dias (UFCAT/IMTec)
status: extraido_pdf_bruto
ordem_aula: '0'
observacao: Texto extraído automaticamente do PDF; revisar figuras/diagramas que não vieram.
---

# Lista5_exercicios_python_ia

🐍
 Exercicios de Python
1o Periodo  |  Graduacao em Inteligencia Artificial
Variaveis Funcoes Condicionais Iteracao Strings
15 exercicios  |  5 topicos  |  Python 3.10+

===PAGE_BREAK===

01
Variaveis, Expressoes e Instrucoes
Exercicios 1 a 3

===PAGE_BREAK===

01
Variaveis & Expressoes
Calculadora de IMC
Solicite ao usuario seu peso (kg) e altura (m). Calcule e exiba o IMC usando a formula:
   IMC = peso / altura²
Exiba com 2 casas decimais e a classificacao: Abaixo do peso (<18,5), Normal (18,5-24,9), Sobrepeso (25-29,9) ou Obeso (>=30).
💡
  Use float(input(...)) para ler numeros reais e f"{valor:.2f}" para formatar.
📥
 Entrada
Peso: 70
Altura: 1.75
📤
 Saida esperada
IMC: 22.86
Classificacao: Normal

===PAGE_BREAK===

02
Variaveis & Expressoes
Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuario informa um valor em Celsius e o programa exibe o equivalente nas outras escalas.
   F = C × 9/5 + 32     |     K = C + 273.15
💡
  Armazene o valor de entrada em uma variavel e reutilize-a nas duas expressoes.
📥
 Entrada
Temperatura (C): 100
📤
 Saida esperada
Fahrenheit: 212.00 F
Kelvin: 373.15 K

===PAGE_BREAK===

03
Variaveis & Instrucoes
Troco Inteligente
Um caixa recebe o valor da compra e o valor pago. Calcule o troco e exiba a quantidade minima de notas e moedas necessarias usando as 
denominacoes: R$100, R$50, R$20, R$10, R$5, R$2, R$1, R$0,50, R$0,25, R$0,10, R$0,05, R$0,01.
💡
  Use // (divisao inteira) e % (resto), iterando pelas denominacoes em ordem decrescente.
📥
 Entrada
Compra: 37.40
Pago: 50.00
📤
 Saida esperada
Troco: R$ 12.60
1x R$10 | 1x R$2
1x R$0.50 | 1x R$0.10

===PAGE_BREAK===

02
Funcoes em Python
Exercicios 4 a 6

===PAGE_BREAK===

04
Funcoes
Calculadora Modular
Crie um modulo com as funcoes: somar(a,b), subtrair(a,b), multiplicar(a,b), dividir(a,b) e potencia(base, exp).
Trate divisao por zero com uma mensagem de erro adequada.
Implemente um menu interativo que chame as funcoes conforme a escolha do usuario.
💡
  Use um dicionario para mapear opcoes a funcoes — evita longos if/elif e e mais Pythonico.
📥
 Entrada
Escolha: 4
Num 1: 10
Num 2: 0
📤
 Saida esperada
Erro: Divisao por
zero nao permitida!

===PAGE_BREAK===

05
Funcoes
Validador de Senha
Implemente validar_senha(senha) que retorna True se a senha atender TODOS os criterios:
  • Minimo de 8 caracteres
  • Pelo menos uma letra maiuscula e uma minuscula
  • Pelo menos um digito
  • Pelo menos um caractere especial: !@#$%^&*
Exiba qual(is) criterio(s) nao foram atendidos.
💡
  Use any(c.isupper() for c in senha) — idiomatico e eficiente. Retorne uma tupla (valido, erros).
📥
 Entrada
Senha: Python3
📤
 Saida esperada
Senha invalida:
- Caractere especial
  ausente

===PAGE_BREAK===

06
Funcoes
Funcoes de Geometria
Crie funcoes que calculem area e perimetro de figuras geometricas:
  • circulo(r)  →  area e perimetro
  • retangulo(l, a)  →  area e perimetro
  • triangulo(b, h, l1, l2, l3)  →  area e perimetro
Cada funcao deve retornar uma TUPLA (area, perimetro). Use math.pi.
💡
  math.pi fornece pi com alta precisao. Tuplas sao ideais para multiplos resultados relacionados.
📥
 Entrada
circulo(5)
📤
 Saida esperada
Area: 78.54
Perimetro: 31.42

===PAGE_BREAK===

03
Condicionais e Recursividade
Exercicios 7 a 9

===PAGE_BREAK===

07
Condicionais
Classificador de Triangulos
Dados tres lados, escreva um programa que:
  • Verifique se os lados formam um triangulo valido
  • Classifique quanto aos lados: Equilatero, Isosceles ou Escaleno
  • Classifique quanto aos angulos: Acutangulo, Retangulo ou Obtusangulo
Use a Lei dos Cossenos para classificar os angulos.
💡
  Condicao valida: a+b>c (para todos os pares). Para angulos, compare o quadrado do maior lado.
📥
 Entrada
Lado a: 3
Lado b: 4
Lado c: 5
📤
 Saida esperada
Valido: Sim
Escaleno | Retangulo

===PAGE_BREAK===

08
Recursividade
Fibonacci Recursivo
Implemente fibonacci(n) de duas formas:
  1. Recursao simples  →  O(2ⁿ)
  2. Com memorizacao (@functools.lru_cache)  →  O(n)
Compare o tempo de execucao das duas versoes para n = 35.
Sequencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
💡
  Caso base: n <= 1. O decorador @lru_cache armazena resultados ja calculados automaticamente.
📥
 Entrada
fibonacci(10)
📤
 Saida esperada
55
Simples: 0.0023s
Cache:   0.0001s

===PAGE_BREAK===

09
Recursividade
Torre de Hanoi
Implemente o classico problema da Torre de Hanoi de forma recursiva.
A funcao hanoi(n, origem, destino, auxiliar) deve exibir o passo a passo para mover n discos da torre origem para a torre destino usando a 
torre auxiliar.
Exiba tambem o numero total de movimentos realizados.
💡
  Pense no caso base (n=1) e no recursivo: mova n-1 para auxiliar, mova o maior, depois mova n-1.
📥
 Entrada
hanoi(3, A, C, B)
📤
 Saida esperada
A->C | A->B | C->B
A->C | B->A | B->C
A->C | Movs: 7

===PAGE_BREAK===

04
Funcoes com Resultado
Exercicios 10 a 12

===PAGE_BREAK===

10
Funcoes com Resultado
Calculadora de Estatisticas
Crie funcoes que recebem uma lista de numeros e retornam:
  • media(lista)         → media aritmetica
  • mediana(lista)       → valor central apos ordenacao
  • moda(lista)          → valor mais frequente
  • desvio_padrao(lista) → desvio padrao populacional
  • resumo(lista)        → dicionario com todas as metricas
Sem usar o modulo statistics.
💡
  Counter retorna um dicionario de frequencias. Mediana par = media dos dois elementos centrais.
📥
 Entrada
[4,7,13,2,7,9,4,7]
📤
 Saida esperada
media:   6.75
mediana: 7.0
moda:    [7]
desvpad: 2.99

===PAGE_BREAK===

11
Funcoes com Resultado
Verificador de Primos
Implemente as funcoes:
  • eh_primo(n)           → True se n e primo
  • primos_ate(n)         → lista de primos ate n (Crivo de Eratostenes)
  • fatoracao_prima(n)    → lista dos fatores primos de n
  • mmc(a, b) e mdc(a, b) usando o Algoritmo de Euclides
💡
  Para eh_primo, verifique divisores ate sqrt(n). O Crivo usa uma lista booleana marcando compostos.
📥
 Entrada
fatoracao_prima(360)
📤
 Saida esperada
[2, 2, 2, 3, 3, 5]
= 2³ × 3² × 5 

===PAGE_BREAK===

12
Funcoes com Resultado
Calculadora de Progressoes
Crie funcoes para trabalhar com progressoes:
  • pa_termo(a1,r,n) e pa_soma(a1,r,n)  →  Progressao Aritmetica
  • pg_termo(a1,q,n) e pg_soma(a1,q,n)  →  Progressao Geometrica
  • identificar_sequencia(lista)  →  detecta se e PA, PG ou nenhuma
💡
  PA: diferenca constante. PG: razao constante. Use all() para verificar a condicao em toda a lista.
📥
 Entrada
identificar([2,4,8,16])
📤
 Saida esperada
PG com razao q=2.0
pg_soma(1,2,10)=1023

===PAGE_BREAK===

05
Iteracao e Strings
Exercicios 13 a 15

===PAGE_BREAK===

13
Strings
Analisador de Texto
Dado um texto, crie funcoes que retornem:
  • Numero de palavras, frases e paragrafos
  • Frequencia de cada letra (ignorando maiusculas/minusculas)
  • As 5 palavras mais frequentes
  • Se o texto e um palindromo (ignorando espacos e pontuacao)
  • Versao do texto em Pig Latin
💡
  Use re.sub() para remover pontuacao. A notacao [::-1] inverte uma string (util para palindromos).
📥
 Entrada
'Arara voa alto'
📤
 Saida esperada
palavras: 3
palindromo: False
pig latin: Araraay

===PAGE_BREAK===

14
Iteracao
Padroes com Iteracao
Use lacos for e while para gerar:
  • Triangulo de Pascal — primeiras n linhas
  • Espiral numerica — preencher uma matriz n×n em espiral
  • Tabuada formatada — tabela de multiplicacao de 1 a n×n
Para o triangulo de Pascal, use listas aninhadas para armazenar cada linha.
💡
  No triangulo, cada elemento = linha_anterior[j-1] + linha_anterior[j]. Inicie e termine com 1.
📥
 Entrada
pascal(5)
📤
 Saida esperada
      1 
     1 1 
    1 2 1 
   1 3 3 1 
  1 4 6 4 1 

===PAGE_BREAK===

15
Strings & Iteracao
Cifra de Cesar Generalizada
Implemente um sistema de criptografia baseado na Cifra de Cesar:
  • cifrar(texto, chave)    → desloca cada letra chave posicoes no alfabeto
  • decifrar(texto, chave)  → reverte a cifra
  • quebrar_cifra(texto)    → testa as 26 possibilidades por analise de frequencia
Preserve maiusculas/minusculas e ignore nao-alfabeticos.
💡
  Use ord() e chr() para manipular codigos ASCII. O operador % 26 faz o wrap-around do alfabeto.
📥
 Entrada
cifrar('Python', 3)
📤
 Saida esperada
'Sbwkrq'

===PAGE_BREAK===

Bons estudos! 🚀
Programacao se aprende praticando.
Tente resolver cada exercicio antes de ver a resolucao!
15
Exercicios
5
Topicos
Python
3.10+