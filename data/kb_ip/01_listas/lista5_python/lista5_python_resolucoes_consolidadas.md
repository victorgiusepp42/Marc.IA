---
tipo: resolucao_aluno
etapa: 2
lista: lista5_python
autor_original: Victor Giusepp Almeida
fonte_dir: 01_listas/lista5_python/resolucoes_aluno
data_processamento: 2026-07-05
status: consolidado
observacao: Resolucoes de Victor consolidadas para melhor retrieval (cada uma era 1 chunk de ~500 tokens).
---

# Resolucoes — lista5_python

> Consolidado de 15 resolucoes do aluno. Cada resolucao e separada por `=== EX NN ===`.

## === EX 01: 10_estatisticas (Python) ===

```
---
tipo: resolucao_aluno
etapa: 2
lista: lista5_python
linguagem: python
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista5_python/10_estatisticas.py
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

# Funcoes estatisticas
from collections import Counter

def media(lista):
    return sum(lista) / len(lista)

def mediana(lista):
    ordenada = sorted(lista)
    n = len(ordenada)
    meio = n // 2
    if n % 2 == 0:
        return (ordenada[meio - 1] + ordenada[meio]) / 2
    else:
        return ordenada[meio]

def moda(lista):
    contagem = Counter(lista)
    freq_maxima = max(contagem.values())
    return [valor for valor, freq in contagem.items() if freq == freq_maxima]

def desvio_padrao(lista):
    # Desvio padrao 
    m = media(lista)
    variancia = sum((x - m) ** 2 for x in lista) / len(lista)
    return variancia ** 0.5

def resumo(lista):
    return {
        "media": media(lista),
        "mediana": mediana(lista),
        "moda": moda(lista),
        "desvpad": desvio_padrao(lista)
    }


entrada = input("Digite os numeros separados por espaco: ")
numeros = [float(x) for x in entrada.split()]

print(f"media:   {media(numeros):.2f}")
print(f"mediana: {mediana(numeros)}")
print(f"moda:    {moda(numeros)}")
print(f"desvpad: {desvio_padrao(numeros):.2f}")
```

## === EX 02: 11_verificador_primo (Python) ===

```
---
tipo: resolucao_aluno
etapa: 2
lista: lista5_python
linguagem: python
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista5_python/11_verificador_primo.py
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

# Verificador de numeros primos 
import math

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def primos_ate(n):
    # Crivo de Eratostenes
    crivo = [True] * (n + 1)
    crivo[0] = crivo[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if crivo[i]:
            for j in range(i * i, n + 1, i):
                crivo[j] = False
    return [i for i in range(n + 1) if crivo[i]]

def fatoracao_prima(n):
    fatores = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            fatores.append(divisor)
            n //= divisor
        divisor += 1
    return fatores

def mdc(a, b):
    # Algoritmo de Euclides
    while b != 0:
        a, b = b, a % b
    return a

def mmc(a, b):
    return a * b // mdc(a, b)


n = int(input("Digite um numero: "))

print(f"eh_primo({n}): {eh_primo(n)}")
print(f"Primos ate {n}: {primos_ate(n)}")
print(f"Fatoracao prima de {n}: {fatoracao_prima(n)}")

a = int(input("Digite o primeiro numero para MDC/MMC: "))
b = int(input("Digite o segundo numero para MDC/MMC: "))
print(f"MDC({a}, {b}): {mdc(a, b)}")
print(f"MMC({a}, {b}): {mmc(a, b)}")
```

## === EX 03: 12_progressoes (Python) ===

```
---
tipo: resolucao_aluno
etapa: 2
lista: lista5_python
linguagem: python
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista5_python/12_progressoes.py
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

# Progressoes Aritmeticas e Geometricas

def pa_termo(a1, r, n):
    return a1 + (n - 1) * r

def pa_soma(a1, r, n):
    an = pa_termo(a1, r, n)
    return n * (a1 + an) / 2

def pg_termo(a1, q, n):
    return a1 * q ** (n - 1)

def pg_soma(a1, q, n):
    if q == 1:
        return a1 * n
    return a1 * (q ** n - 1) / (q - 1)

def identificar_sequencia(lista):
    if len(lista) < 2:
        return "Sequencia muito curta"

    # Verifica se e PA 
    diferencas = [lista[i+1] - lista[i] for i in range(len(lista) - 1)]
    if all(d == diferencas[0] for d in diferencas):
        print(f"PA com razao r={diferencas[0]}")
        return

    # Verifica se e PG 
    if all(lista[i] != 0 for i in range(len(lista) - 1)):
        razoes = [lista[i+1] / lista[i] for i in range(len(lista) - 1)]
        if all(q == razoes[0] for q in razoes):
            print(f"PG com razao q={razoes[0]}")
            return

    print("Nao e PA nem PG")



entrada = input("Digite os termos da sequencia separados por espaco: ")
sequencia = [float(x) for x in entrada.split()]
identificar_sequencia(sequencia)

a1 = float(input("Digite a1 da PG: "))
q = float(input("Digite a razao q: "))
n = int(input("Digite n: "))
print(f"pg_soma({int(a1)},{int(q)},{n})={int(pg_soma(a1, q, n))}")
```

## === EX 04: 13_analisador_texto (Python) ===

```
---
tipo: resolucao_aluno
etapa: 2
lista: lista5_python
linguagem: python
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista5_python/13_analisador_texto.py
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

# Analisador de Texto
import re

def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

def contar_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    sentencas = [s for s in sentencas if s.strip()]
    return len(sentencas)

def contar_paragrafos(texto):
    paragrafos = texto.split('\n\n')
    paragrafos = [p for p in paragrafos if p.strip()]
    return len(paragrafos)

def frequencia_letras(texto):
    texto_lower = texto.lower()
    frequencias = {}
    for char in texto_lower:
        if char.isalpha():
            frequencias[char] = frequencias.get(char, 0) + 1
    return frequencias

def palavras_mais_frequentes(texto, n=5):
    # Remove pontuacao e converte para minusculo
    texto_limpo = re.sub(r'[^\w\s]', '', texto.lower())
    palavras = texto_limpo.split()
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    ordenadas = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
    return ordenadas[:n]

def eh_palindromo(texto):
    # Remove tudo que nao e letra
    texto_limpo = re.sub(r'[^a-zA-Z]', '', texto.lower())
    return texto_limpo == texto_limpo[::-1]

def pig_latin(texto):
    palavras = texto.split()
    resultado = []
    for palavra in palavras:
        resultado.append(palavra + 'ay')
    return ' '.join(resultado)



texto = input("Digite um texto: ")

print(f"palavras: {contar_palavras(texto)}")
print(f"sentencas: {contar_sentencas(texto)}")
print(f"paragrafos: {contar_paragrafos(texto)}")
print(f"frequencia de letras: {frequencia_letras(texto)}")
print(f"5 mais frequentes: {palavras_mais_frequentes(texto)}")
print(f"palindromo: {eh_palindromo(texto)}")
print(f"pig latin: {pig_latin(texto)}")
```

## === EX 05: 14_padroes_iteracao (Python) ===

```
---
tipo: resolucao_aluno
etapa: 2
lista: lista5_python
linguagem: python
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista5_python/14_padroes_iteracao.py
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

# Padroes de Iteracao

def triangulo_pascal(n):
    triangulo = []
    for i in range(n):
        if i == 0:
            linha = [1]
        else:
            linha_anterior = triangulo[i - 1]
            linha = [1]
            for j in range(1, i):
                linha.append(linha_anterior[j-1] + linha_anterior[j])
            linha.append(1)
        triangulo.append(linha)
    return triangulo

def imprimir_pascal(n):
    triangulo = triangulo_pascal(n)
    largura = len(' '.join(str(x) for x in triangulo[-1]))
    for linha in triangulo:
        texto = ' '.join(str(x) for x in linha)
        print(texto.center(largura))

def espiral(n):
    # Preenche matriz n x n em ordem espiral
    matriz = [[0] * n for _ in range(n)]
    num = 1
    topo, baixo, esquerda, direita = 0, n - 1, 0, n - 1

    while topo <= baixo and esquerda <= direita:
        for j in range(esquerda, direita + 1):
            matriz[topo][j] = num
            num += 1
        topo += 1
        for i in range(topo, baixo + 1):
            matriz[i][direita] = num
            num += 1
        direita -= 1
        for j in range(direita, esquerda - 1, -1):
            matriz[baixo][j] = num
            num += 1
        baixo -= 1
        for i in range(baixo, topo - 1, -1):
            matriz[i][esquerda] = num
            num += 1
        esquerda += 1
    return matriz

def imprimir_matriz(matriz):
    n = len(matriz)
    largura = len(str(n * n))
    for linha in matriz:
        print(' '.join(str(x).rjust(largura) for x in linha))

def tabuada(n):
    # Cabecalho
    print(f"{'':>4}", end='')
    for j in range(1, n + 1):
        print(f"{j:>4}", end='')
    print()
    print("-" * (4 * (n + 1)))
    # Corpo
    for i in range(1, n + 1):
        print(f"{i:>3}|", end='')
        for j in range(1, n + 1):
            print(f"{i*j:>4}", end='')
        print()



n = int(input("Quantas linhas do Triangulo de Pascal? "))
imprimir_pascal(n)

print()
n2 = int(input("Tamanho da espiral (n x n): "))
imprimir_matriz(espiral(n2))

print()
n3 = int(input("Tabuada ate quanto? "))
tabuada(n3)
```

## === EX 06: 15_cifra_cesar (Python) ===

```
---
tipo: resolucao_aluno
etapa: 2
lista: lista5_python
linguagem: python
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista5_python/15_cifra_cesar.py
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

# Cifra de Cesar Generalizada

def cifrar(texto, chave):
    resultado = ''
    for char in texto:
        if char.isupper():
            novo = (ord(char) - ord('A') + chave) % 26
            resultado += chr(novo + ord('A'))
        elif char.islower():
            novo = (ord(char) - ord('a') + chave) % 26
            resultado += chr(novo + ord('a'))
        else:
            resultado += char
    return resultado

def decifrar(texto, chave):
    return cifrar(texto, -chave)

def quebrar_cifra(texto):
    # Testa todas as 26 chaves possiveis 
    print("Tentando todas as chaves:")
    for chave in range(26):
        tentativa = decifrar(texto, chave)
        print(f"  Chave {chave:>2}: {tentativa}")



texto = input("Digite o texto: ")
chave = int(input("Digite a chave: "))

texto_cifrado = cifrar(texto, chave)
texto_decifrado = decifrar(texto_cifrado, chave)

print(f"Cifrado: {texto_cifrado}")
print(f"Decifrado: {texto_decifrado}")

print()
quebrar_cifra(texto_cifrado)
```

## === EX 07: 1_imc (Python) ===

```
---
tipo: resolucao_aluno
etapa: 2
lista: lista5_python
linguagem: python
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista5_python/1_imc.py
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

# Calculadora de IMC (Indice de Massa Corporal)

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Calculo do IMC
imc = peso / (altura ** 2)

# Classificacao do IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc <= 24.9:
    classificacao = "Normal"
elif imc <= 29.9:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print(f"IMC: {imc:.2f}")
print(f"Classificacao: {classificacao}")
```

## === EX 08: 2_conversor_temperatura (Python) ===

```
---
tipo: resolucao_aluno
etapa: 2
lista: lista5_python
linguagem: python
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista5_python/2_conversor_temperatura.py
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

# Conversor de temperatura (Celsius para Fahrenheit e Kelvin)

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = celsius * 9/5 + 32
kelvin = celsius + 273.15

print(f"Fahrenheit: {fahrenheit:.2f} F")
print(f"Kelvin: {kelvin:.2f} K")
```

## === EX 09: 3_troco_inteligente (Python) ===

```
---
tipo: resolucao_aluno
etapa: 2
lista: lista5_python
linguagem: python
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista5_python/3_troco_inteligente.py
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

# Calculadora de troco inteligente

valor_compra = float(input("Digite o valor da compra: R$ "))
valor_pago = float(input("Digite o valor pago: R$ "))

# Converte para centavos
troco_centavos = round((valor_pago - valor_compra) * 100)

print(f"Troco: R$ {troco_centavos / 100:.2f}")

# Denominacoes em centavos
denominacoes = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
nomes = ["R$100", "R$50", "R$20", "R$10", "R$5", "R$2",
         "R$1", "R$0.50", "R$0.25", "R$0.10", "R$0.05", "R$0.01"]

# Calcula quantidade de cada nota/moeda
notas = []
moedas = []

for i in range(len(denominacoes)):
    quantidade = troco_centavos // denominacoes[i]
    troco_centavos = troco_centavos % denominacoes[i]
    if quantidade > 0:
        item = f"{quantidade}x {nomes[i]}"
        if denominacoes[i] >= 100:
            notas.append(item)
        else:
            moedas.append(item)

# Exibe notas e moedas separadamente
if notas:
    print(" | ".join(notas))
if moedas:
    print(" | ".join(moedas))
```

## === EX 10: 4_calculadora_modular (Python) ===

```
---
tipo: resolucao_aluno
etapa: 2
lista: lista5_python
linguagem: python
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista5_python/4_calculadora_modular.py
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

# Calculadora modular com funcoes

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        print("Erro: Divisao por zero nao permitida!")
        return None
    return a / b

def potencia(base, exp):
    return base ** exp


# Menu interativo
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
print("5 - Potencia")

# Dicionario mapeia opcao
opcoes = {1: somar, 2: subtrair, 3: multiplicar, 4: dividir, 5: potencia}

escolha = int(input("Escolha: "))
a = float(input("Num 1: "))
b = float(input("Num 2: "))

resultado = opcoes[escolha](a, b)
if resultado is not None:
    print(f"Resultado: {resultado}")
```

## === EX 11: 5_validar_senha (Python) ===

```
---
tipo: resolucao_aluno
etapa: 2
lista: lista5_python
linguagem: python
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista5_python/5_validar_senha.py
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

# Validador de senha com criterios multiplos

def validar_senha(senha):
    erros = []
    especiais = "!@#$%^&*"

    # Verifica cada criterio
    if len(senha) < 8:
        erros.append("Minimo de 8 caracteres")
    if not any(c.isupper() for c in senha):
        erros.append("Letra maiuscula ausente")
    if not any(c.islower() for c in senha):
        erros.append("Letra minuscula ausente")
    if not any(c.isdigit() for c in senha):
        erros.append("Digito ausente")
    if not any(c in especiais for c in senha):
        erros.append("Caractere especial ausente")

    valido = len(erros) == 0
    return (valido, erros)

# Programa principal
senha = input("Digite uma senha para validar: ")
valido, erros = validar_senha(senha)

if valido:
    print("Senha valida!")
else:
    print("Senha invalida:")
    for erro in erros:
        print(f"- {erro}")
```

## === EX 12: 6_geometria (Python) ===

```
---
tipo: resolucao_aluno
etapa: 2
lista: lista5_python
linguagem: python
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista5_python/6_geometria.py
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

# Calculo de area e perimetro de figuras geometricas
import math

def circulo(r):
    area = math.pi * r ** 2
    perimetro = 2 * math.pi * r
    return (area, perimetro)

def retangulo(l, a):
    area = l * a
    perimetro = 2 * (l + a)
    return (area, perimetro)

def triangulo(b, h, l1, l2, l3):
    area = (b * h) / 2
    perimetro = l1 + l2 + l3
    return (area, perimetro)


# Programa principal
print("Escolha a figura geometrica:")
print("1 - Circulo")
print("2 - Retangulo")
print("3 - Triangulo")
opcao = int(input("Opcao: "))

if opcao == 1:
    raio = float(input("Raio: "))
    area, perimetro = circulo(raio)
    print(f"Area: {area:.2f}")
    print(f"Perimetro: {perimetro:.2f}")

elif opcao == 2:
    largura = float(input("Largura: "))
    altura = float(input("Altura: "))
    area, perimetro = retangulo(largura, altura)
    print(f"Area: {area:.2f}")
    print(f"Perimetro: {perimetro:.2f}")

elif opcao == 3:
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    lado1 = float(input("Lado 1: "))
    lado2 = float(input("Lado 2: "))
    lado3 = float(input("Lado 3: "))
    area, perimetro = triangulo(base, altura, lado1, lado2, lado3)
    print(f"Area: {area:.2f}")
    print(f"Perimetro: {perimetro:.2f}")

else:
    print("Opcao invalida!")
```

## === EX 13: 7_classificar_triangulos (Python) ===

```
---
tipo: resolucao_aluno
etapa: 2
lista: lista5_python
linguagem: python
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista5_python/7_classificar_triangulos.py
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

# Classificacao de triangulos por lados e angulos

def verificar_triangulo(a, b, c):
    # Condicao: soma de dois lados sempre maior que o terceiro
    return a + b > c and a + c > b and b + c > a

def classificar_lados(a, b, c):
    if a == b == c:
        return "Equilatero"
    elif a == b or a == c or b == c:
        return "Isosceles"
    else:
        return "Escaleno"

def classificar_angulos(a, b, c):
    # Ordena os lados para que c seja o maior
    lados = sorted([a, b, c])
    a, b, c = lados[0], lados[1], lados[2]

    # Compara o quadrado do maior lado com a soma dos quadrados dos outros
    if c ** 2 == a ** 2 + b ** 2:
        return "Retangulo"
    elif c ** 2 > a ** 2 + b ** 2:
        return "Obtusangulo"
    else:
        return "Acutangulo"


# Programa principal
lado_a = float(input("Lado a: "))
lado_b = float(input("Lado b: "))
lado_c = float(input("Lado c: "))

if verificar_triangulo(lado_a, lado_b, lado_c):
    print("Valido: Sim")
    tipo_lados = classificar_lados(lado_a, lado_b, lado_c)
    tipo_angulos = classificar_angulos(lado_a, lado_b, lado_c)
    print(f"{tipo_lados} | {tipo_angulos}")
else:
    print("Valido: Nao")
    print("Os lados informados nao formam um triangulo.")
```

## === EX 14: 8_fibonacci (Python) ===

```
---
tipo: resolucao_aluno
etapa: 2
lista: lista5_python
linguagem: python
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista5_python/8_fibonacci.py
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

# Fibonacci recursivo 
import functools
import time

def fibonacci_simples(n):
    # Recursao simples 
    if n <= 1:
        return n
    return fibonacci_simples(n - 1) + fibonacci_simples(n - 2)

@functools.lru_cache(maxsize=None)
def fibonacci_cache(n):
    # Com memorizacao 
    if n <= 1:
        return n
    return fibonacci_cache(n - 1) + fibonacci_cache(n - 2)


# Programa principal
n = int(input("Digite n: "))

# Fibonacci simples com medicao de tempo
inicio = time.time()
resultado_simples = fibonacci_simples(n)
tempo_simples = time.time() - inicio

# Fibonacci com cache e medicao de tempo
inicio = time.time()
resultado_cache = fibonacci_cache(n)
tempo_cache = time.time() - inicio

# Resultados
print(f"{resultado_simples}")
print(f"Simples: {tempo_simples:.4f}s")
print(f"Cache: {tempo_cache:.4f}s")
```

## === EX 15: 9_torre_hanoi (Python) ===

```
---
tipo: resolucao_aluno
etapa: 2
lista: lista5_python
linguagem: python
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista5_python/9_torre_hanoi.py
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

# Torre de Hanoi 

movimentos = []

def hanoi(n, origem, destino, auxiliar):
    if n == 1:
        movimentos.append(f"{origem}->{destino}")
        return
    hanoi(n - 1, origem, auxiliar, destino)
    movimentos.append(f"{origem}->{destino}")
    hanoi(n - 1, auxiliar, destino, origem)


# Programa principal
n = int(input("Numero de discos: "))

hanoi(n, "A", "C", "B")

# Exibe movimentos em grupos de 3, com total no final da ultima linha
for i in range(0, len(movimentos), 3):
    grupo = movimentos[i:i+3]
    linha = " | ".join(grupo)
    # Se e o ultimo grupo, coloca o total de movimentos junto
    if i + 3 >= len(movimentos):
        print(f"{linha} | Movs: {len(movimentos)}")
    else:
        print(linha)
```
