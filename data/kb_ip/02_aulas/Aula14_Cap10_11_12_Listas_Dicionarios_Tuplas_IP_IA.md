---
tipo: lista_exercicios
etapa: 2
topico: vetores_matrizes_listas
fonte: docs/materiais_kb/AULAS/Aula14_Cap10_11_12_Listas_Dicionarios_Tuplas_IP_IA.txt
data_processamento: 2026-07-04
autor_original: Prof. Dr. Márcio de Souza Dias (UFCAT/IMTec)
status: extraido_pdf_bruto
ordem_aula: '0'
observacao: Texto extraído automaticamente do PDF; revisar figuras/diagramas que não vieram.
---

# Aula14_Cap10_11_12_Listas_Dicionarios_Tuplas_IP_IA

Capítulos 10 · 11 · 12
Estruturas
de Dados
Pense em Python – Allen B. Downey
1º Período • Bacharelado em Inteligência Artificial • UFCAT
Cap. 10
Listas
Mutabilidade, métodos, alias
Cap. 11
Dicionários
Chave-valor, hashtable, memos
Cap. 12
Tuplas
Imutáveis, gather/scatter, zip

===PAGE_BREAK===

Capítulo 10
Listas
Sequências mutáveis · Métodos · Alias · Mapeamento, Filtragem e Redução
Pense em Python – Allen B. Downey  |  1º Período IA/UFCAT

===PAGE_BREAK===

📋
  Listas — Criação, Acesso e Mutabilidade
3
Listas são sequências ordenadas de valores de qualquer tipo. Diferente de strings, são MUTÁVEIS.
# Criando listas:
numeros = [10, 20, 30, 40]
misturada = ['spam', 2.0, 5, [10, 20]]  # lista 
aninhada
vazia = []
# Acesso por índice (igual a strings):
frutas = ['Cheddar', 'Edam', 'Gouda']
print(frutas[0])   # 'Cheddar'
print(frutas[-1])  # 'Gouda'
# MUTABILIDADE — diferente de strings:
numeros = [42, 123]
numeros[1] = 5     # OK! strings não permitem isso
print(numeros)     # [42, 5]
# Operador in:
print('Edam' in frutas)  # True
print('Brie' in frutas)  # False
Índices como strings
Começam em 0, negativos contam do fim, 
expressões int são OK.
Mutável!
Você PODE alterar elementos: lista[0] = 'novo'. 
Strings não permitem.
Lista aninhada
Uma lista dentro de outra conta como UM elemento.
Lista vazia
[] tem comprimento 0 e é válida em qualquer 
contexto.

===PAGE_BREAK===

🔁
  Traversal, Operações e Fatiamento
4
Três formas de percorrer listas. Operadores + e * funcionam como em strings.
# TRAVERSAL:
# 1. for direto (só leitura):
for queijo in ['Edam','Gouda','Brie']:
    print(queijo)
# 2. for com índice (leitura/escrita):
nums = [1, 2, 3, 4]
for i in range(len(nums)):
    nums[i] = nums[i] * 2  # [2, 4, 6, 8]
# 3. enumerate (índice + valor):
for i, val in enumerate(nums):
    print(i, val)
# OPERAÇÕES:
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)      # [1, 2, 3, 4, 5, 6]
print([0] * 4)    # [0, 0, 0, 0]
print([1,2] * 3)  # [1, 2, 1, 2, 1, 2]
# FATIAMENTO:
t = ['a','b','c','d','e','f']
print(t[1:3])   # ['b', 'c']
print(t[:4])    # ['a', 'b', 'c', 'd']
t[1:3] = ['x','y']  # atualiza múltiplos!
for item in lista
Mais simples. Só para ler.
range(len(lista))
Quando precisa do índice.
enumerate(lista)
Índice + valor juntos.
t[1:3] = [...]
Fatiamento à esquerda substitui múltiplos.

===PAGE_BREAK===

🛠
  Métodos de Listas
5
Métodos que MODIFICAM a lista no lugar (retornam None) vs. funções que criam novas listas.
t = ['a', 'b', 'c']
# ADICIONAR:
t.append('d')        # ['a','b','c','d']  — retorna None!
t.extend(['e','f'])  # ['a','b','c','d','e','f']
t2 = t + ['g']       # cria NOVA lista, t inalterada
# REMOVER:
x = t.pop(1)   # remove índice 1, retorna 'b'
t.remove('c')  # remove primeira ocorrência de 'c'
del t[0]       # remove índice 0, sem retorno
del t[0:2]     # remove fatia
# ORGANIZAR:
t.sort()           # modifica in-place, retorna None
t2 = sorted(t)     # cria nova lista ordenada (t inalterado)
t.reverse()        # modifica in-place
# ARMADILHA CLÁSSICA:
t = ['d','c','b','a']
t = t.sort()   # ERRADO! t vira None
# Correto:
t.sort()       # modifica t e retorna None
⚠
  Métodos retornam None
t = t.sort()  →  t = None!
Sempre use t.sort() sem reatribuir.
append(x)
Adiciona x ao fim. 
In-place.
extend(lista)
Adiciona todos 
elementos. In-place.
pop(i)
Remove índice i, retorna 
valor.
remove(x)
Remove 1ª ocorrência de 
x.
sort()
Ordena in-place (retorna 
None!).
sorted(t)
Retorna NOVA lista 
ordenada.

===PAGE_BREAK===

🗺
  Mapeamento, Filtragem e Redução
6
Três padrões fundamentais que aparecem em todo processamento de listas — e na base do ML!
# REDUÇÃO — combina sequência num único valor:
def somar(t):
    total = 0
    for x in t: total += x
    return total
# Python já tem: sum([1,2,3]) → 6
# MAPEAMENTO — aplica função a cada elemento:
def capitalize_all(t):
    return [s.capitalize() for s in t]
# ['ana','bob'] → ['Ana','Bob']
# FILTRAGEM — seleciona elementos:
def only_upper(t):
    return [s for s in t if s.isupper()]
# ['A','b','C'] → ['A','C']
# Listas e strings — split/join:
s = 'pining for the fjords'
t = s.split()           # ['pining','for','the','fjords']
' '.join(t)             # 'pining for the fjords'
'-'.join(['a','b','c']) # 'a-b-c'
list('spam')            # ['s','p','a','m']
Redução
sum(), produto, concatenação.
Acumula tudo num só valor.
Mapeamento
Transforma cada elemento.
map(), list comprehension.
Filtragem
Seleciona um subconjunto.
filter(), list comprehension.
🤖
 Em ML: sum→loss, map→transformação de 
features, filter→pré-processamento

===PAGE_BREAK===

🪞
  Objetos, Valores e Alias
7
Dois nomes para o mesmo objeto mutável: mudança em um afeta o outro! Perigo com listas.
# == verifica equivalência (mesmo valor):
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True  (mesmos valores)
print(a is b)  # False (objetos diferentes)
# ALIAS — dois nomes, UM objeto:
a = [1, 2, 3]
b = a          # b aponta para o MESMO objeto!
print(b is a)  # True
b[0] = 42
print(a)       # [42, 2, 3] ← a foi afetado!
# EVITAR ALIAS — fazer cópia:
a = [1, 2, 3]
b = a[:]       # fatia cria NOVA lista
b[0] = 99
print(a)       # [1, 2, 3]  ← a intacto
print(b)       # [99, 2, 3]
# Outro jeito de copiar:
b = list(a)    # também cria cópia
⚠
  Alias — PERIGO com mutáveis
b = a  →  MESMO objeto!
b[0]=99 muda a também.
Use b = a[:] para cópia segura.
✅
 Copiar antes de modificar
a = [3,1,2]
b = a[:]  # cópia
b.sort()
print(a)  # [3,1,2] ✓
print(b)  # [1,2,3]
💡
  Strings são imutáveis → alias é inofensivo. Listas são mutáveis → alias pode causar bugs difíceis!

===PAGE_BREAK===

✏
  Exercício para os Alunos
8
Exercícios — Capítulo 10: Listas
Ex. 10.1 — nested_sum
def nested_sum(t):
    # t = [[1,2],[3],[4,5,6]]
    # retorna 21
    pass
Ex. 10.2 — cumsum
def cumsum(t):
    # t=[1,2,3] → [1,3,6]
    pass
Ex. 10.3 — middle
def middle(t):
    # t=[1,2,3,4] → [2,3]
    pass
Ex. 10.5 — is_sorted
def is_sorted(t):
    # [1,2,2]→True
    # ['b','a']→False
    pass
Ex. 10.6 — is_anagram
def is_anagram(s1, s2):
    # 'listen','silent'→True
    pass
Ex. 10.7 — has_duplicates
def has_duplicates(t):
    # retorna True se houver
    # elementos repetidos
    pass

===PAGE_BREAK===

Capítulo 11
Dicionários
Chave-valor · Hashtable · Contadores · Memos · Variáveis Globais
Pense em Python – Allen B. Downey  |  1º Período IA/UFCAT

===PAGE_BREAK===

📚
  Dicionários — Criação e Acesso
10
Dicionário: mapeamento de chaves a valores. Chaves podem ser de (quase) qualquer tipo imutável.
# Criar dicionário vazio:
eng2sp = dict()   # ou eng2sp = {}
# Adicionar itens:
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
# Forma direta:
eng2sp = {'one':'uno', 'two':'dos', 'three':'tres'}
# Acessar valor por chave:
print(eng2sp['two'])   # 'dos'
# eng2sp['four']       # KeyError!
# len e in (verifica CHAVES):
print(len(eng2sp))          # 3
print('one' in eng2sp)      # True
print('uno' in eng2sp)      # False ← valor, não chave!
# Para verificar valores:
print('uno' in eng2sp.values())  # True
# get — acesso seguro com padrão:
print(eng2sp.get('four', 'N/A')) # 'N/A'
print(eng2sp.get('one', 'N/A'))  # 'uno'
Chaves únicas
Cada chave aparece apenas uma vez. Atribuir 
novamente sobrescreve.
Ordem (Python 3.7+)
Dicionários mantêm ordem de inserção. Mas não 
conte com isso para algoritmos.
KeyError
Acessar chave inexistente gera KeyError. Use 
.get(k, padrão) para evitar.
in verifica chaves
'x' in d verifica chaves, não valores. Use 'x' in 
d.values() para valores.

===PAGE_BREAK===

📊
  Dicionário como Coleção de Contadores
11
Padrão fundamental: usar dicionário para contar frequências — histograma.
# Versão manual:
def histogram(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
h = histogram('brontossauro')
print(h)  # {'b':1,'r':2,'o':3,...}
# Versão com get (mais concisa):
def histogram_v2(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d
# Versão pythônica com Counter:
from collections import Counter
h = Counter('brontossauro')
# Loop em dicionário — percorre CHAVES:
for chave in h:
    print(chave, h[chave])
# Ordem crescente de chave:
for chave in sorted(h):
    print(chave, h[chave])
Por que dicionário?
Não precisa saber quais letras aparecerão.
Cria espaço só para as que aparecem.
Busca O(1) vs O(n) de lista!
d.get(chave, padrão)
Se chave existe → retorna valor.
Se não existe → retorna padrão.
Evita if c not in d + else.
Counter do módulo collections
Subclasse de dict otimizada.
Counter('abca') → {'a':2,'b':1,'c':1}
Já existe pronto em Python!

===PAGE_BREAK===

🔄
  Busca Reversa e Inversão de Dicionário
12
Busca normal: chave → valor (O(1)). Busca reversa: valor → chave (O(n)). Muito mais lenta!
# Busca reversa — O(n):
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('valor não encontrado')
h = histogram('parrot')  # {'p':1,'a':1,'r':2,'o':1,'t':1}
print(reverse_lookup(h, 2))  # 'r'
# reverse_lookup(h, 3) → LookupError
# Inversão completa do dicionário:
def invert_dict(d):
    inverse = {}
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse
hist = histogram('parrot')
inv = invert_dict(hist)
# {1: ['p','a','o','t'], 2: ['r']}
# Versão com setdefault:
def invert_dict_v2(d):
    inverse = {}
    for key, val in d.items():
        inverse.setdefault(val, []).append(key)
    return inverse
raise LookupError
raise causa exceção deliberada.
Usar quando função não encontra o resultado 
esperado.
setdefault(k, padrão)
Se k existe → retorna valor atual.
Se não → cria d[k]=padrão e retorna.
Evita if/else na inversão.
Listas como valores (não chaves!)
Valores de dict podem ser listas.
Mas chaves devem ser hashable.
Listas são mutáveis → não podem ser chaves!

===PAGE_BREAK===

⚡
  Memos e Variáveis Globais
13
Memoização: guardar resultados já calculados para evitar reprocessamento — essencial em IA/otimização.
# Fibonacci SEM memo — O(2^n), muito lento!
def fib_lento(n):
    if n <= 1: return n
    return fib_lento(n-1) + fib_lento(n-2)
# Fibonacci COM memo — O(n), muito rápido!
known = {0:0, 1:1}   # variável global
def fibonacci(n):
    if n in known:
        return known[n]   # já calculado!
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res        # guarda para reusar
    return res
# Variáveis globais:
contador = 0
def incrementar():
    global contador    # declarar antes de reatribuir
    contador += 1
# Mutável global — sem 'global':
known = {0:0, 1:1}
def example():
    known[2] = 1       # OK sem 'global'
    # known = {}       # isso precisaria de global
O que é um memo?
Valor calculado guardado para uso futuro.
fib(30) sem memo: 2^30≈10^9 chamadas.
fib(30) com memo: 30 chamadas!
Declaração global
Reatribuir variável global dentro de função 
exige:
  global nome_var
Ler ou modificar mutável (dict/lista) não exige.
🤖
  Memoização em IA:
• Cache de embeddings
• Dynamic Programming
• Tabelas de busca em jogos
• Beam search com histórico

===PAGE_BREAK===

✏
  Exercício para os Alunos
14
Exercícios — Capítulo 11: Dicionários
📌
  Implemente as funções abaixo usando dicionários. Compare a eficiência com as versões com listas.
# Ex 11.1 — histogram com get:
def histogram(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d
print(histogram('banana'))
# {'b':1,'a':3,'n':2}
# Ex 11.4 — has_duplicates com dicionário:
def has_duplicates(t):
    # Use dicionário para contar
    # retorna True se algum conta > 1
    pass
print(has_duplicates([1,2,3]))    # False
print(has_duplicates([1,2,1]))    # True
# Desafio — frequência de letras:
def freq_letras(texto):
    """Retorna dicionário de frequência das letras
    (ignora espaços, pontuação, case-insensitive)"""
    pass
texto = "Inteligência Artificial"
freq = freq_letras(texto)
# Mostre em ordem decrescente de frequência

===PAGE_BREAK===

Capítulo 12
Tuplas
Imutáveis · Atribuição múltipla · Gather/Scatter · zip · enumerate
Pense em Python – Allen B. Downey  |  1º Período IA/UFCAT

===PAGE_BREAK===

📦
  Tuplas — Criação e Características
16
Tuplas são como listas, mas IMUTÁVEIS. Úteis como chaves de dicionário e para retornar múltiplos valores.
# Criando tuplas:
t = 'a', 'b', 'c'          # sem parênteses
t = ('a', 'b', 'c')        # com parênteses (preferido)
t1 = 'a',                  # tupla com 1 elemento (vírgula!)
t2 = ('a')                 # NÃO é tupla → str!
t3 = tuple()               # tupla vazia
t4 = tuple('lupins')       # ('l','u','p','i','n','s')
# Acesso (igual a listas):
print(t[0])    # 'a'
print(t[1:3])  # ('b', 'c')
# Imutável → não pode alterar:
# t[0] = 'A'  ← TypeError!
# Mas pode substituir a tupla toda:
t = ('A',) + t[1:]  # ('A', 'b', 'c')
# Comparação lexicográfica:
print((0,1,2) < (0,3,4))       # True
print((0,1,2000000) < (0,3,4)) # True — só compara até 
diferença
Vírgula faz a tupla
('a') é str. ('a',) é tupla. A vírgula é o que importa!
Imutável → hashable
Pode ser chave de dicionário. Listas não podem!
Acesso igual a lista
Índice, fatia, in, len: tudo funciona igual.
Substituição total
t = ('novo',) + t[1:] cria NOVA tupla — não 
modifica.

===PAGE_BREAK===

🔀
  Atribuição de Tuplas — Desempacotamento
17
Recurso elegante do Python: atribuir múltiplos valores de uma vez. Lado direito avaliado antes de qualquer atribuição.
# Swap clássico — sem variável temporária!
a, b = 10, 20
a, b = b, a      # Python avalia b,a ANTES de atribuir
print(a, b)      # 20 10
# Desempacotar sequências:
addr = 'monty@python.org'
uname, domain = addr.split('@')
print(uname)   # 'monty'
print(domain)  # 'python.org'
# Desempacotar listas e tuplas:
t = (1, 2, 3)
x, y, z = t       # x=1, y=2, z=3
# Retornar múltiplos valores de uma função:
def min_max(t):
    return min(t), max(t)  # retorna tupla!
lo, hi = min_max([3, 1, 4, 1, 5, 9])
print(lo, hi)  # 1 9
# divmod — quociente e resto:
quot, rem = divmod(17, 5)
print(quot, rem)  # 3 2
# Erro se números não batem:
# a, b = 1, 2, 3  ← ValueError!
Lado direito primeiro
a, b = b, a funciona pois Python
avalia (b, a) ANTES de atribuir.
Temporária é desnecessária!
split + desempacotamento
Padrão muito usado:
  nome, ext = arquivo.split('.')
  user, host = email.split('@')
Funções retornando tuplas
Permite retorno de múltiplos valores.
quot, rem = divmod(7, 3)
lo, hi = min_max(lista)

===PAGE_BREAK===

⚡
  *args (gather/scatter), zip e enumerate
18
Funções com número variável de argumentos + iteração simultânea sobre múltiplas sequências.
# *args — GATHER: reúne argumentos em tupla:
def printall(*args):
    print(args)
printall(1, 2.0, '3')  # (1, 2.0, '3')
def sumall(*args):
    return sum(args)
sumall(1, 2, 3, 4, 5)  # 15
# SCATTER: expandir tupla como argumentos:
t = (7, 3)
divmod(*t)        # equivale a divmod(7, 3) → (2, 1)
# zip — pares de elementos:
s = 'abc'
nums = [0, 1, 2]
for par in zip(s, nums):
    print(par)    # ('a',0) ('b',1) ('c',2)
list(zip('Anne', 'Elk'))  # [('A','E'),('n','l'),('n','k')]
# enumerate — índice + valor:
for i, letra in enumerate('abc'):
    print(i, letra)  # 0 a   1 b   2 c
# Desempacotamento em for:
pares = [('a',0), ('b',1), ('c',2)]
for letra, numero in pares:
    print(numero, letra)
*args — gather
def f(*args): → reúne tudo numa tupla.
Convenção: use *args.
Permite número variável de argumentos.
*t — scatter
divmod(*t) expande tupla como args.
Equivale a divmod(t[0], t[1]).
Útil ao chamar funções existentes.
zip — iteração paralela
Combina duas sequências em pares.
Para na menor sequência.
list(zip(a,b)) para materializar.
zip para criar dict:
d = dict(zip('abc', range(3)))
→ {'a':0,'b':1,'c':2}

===PAGE_BREAK===

🗂
  Dicionários + Tuplas e Escolha de Estrutura
19
Combinando as três estruturas. Quando usar cada tipo de sequência?
# Tuplas como CHAVES de dicionário:
lista_tel = {}
lista_tel['Palin','Michael'] = '555-1234'
lista_tel['Jones','Terry']   = '555-5678'
for sobrenome, nome in lista_tel:
    print(nome, sobrenome, lista_tel[sobrenome,nome])
# d.items() → sequência de (chave, valor):
d = {'a':0, 'b':1, 'c':2}
for chave, valor in d.items():
    print(chave, valor)
# Criar dict de lista de tuplas:
t = [('a',0), ('c',2), ('b',1)]
d = dict(t)         # {'a':0,'c':2,'b':1}
# Criar dict com zip:
d = dict(zip('abc', range(3)))  # {'a':0,'b':1,'c':2}
# Ordenar dict por valor:
for k in sorted(d, key=d.get):
    print(k, d[k])
Use lista quando...
Precisa de mutabilidade
Ordem importa
Operações frequentes de append/remove
Use tupla quando...
Imutabilidade é desejada
Chave de dicionário
Retorno de múltiplos valores
Menos overhead de memória
Use dict quando...
Acesso por chave (O(1))
Contagem / frequência
Mapeamento bidirecional
Memoização
Strings → imutável + chars | Listas → mutável + qualquer 
tipo | Tuplas → imutável + qualquer tipo

===PAGE_BREAK===

✏
  Exercício para os Alunos
20
Exercícios — Capítulo 12: Tuplas
📌
  Exercícios que combinam tuplas, dicionários e listas — estruturas compostas.
# Ex 12.1 — most_frequent:
def most_frequent(s):
    """Exibe letras de 's' em ordem
    decrescente de frequência."""
    pass
most_frequent('banana')
# a a a n n b
# Ex — sumall com *args:
def sumall(*args):
    """Recebe qualquer número de
    argumentos e retorna a soma."""
    pass
print(sumall(1, 2, 3))      # 6
print(sumall(10, 20, 30))   # 60
# Desafio — anagramas com dict + tuple:
def agrupar_anagramas(palavras):
    """Retorna dict onde chave é tuple de letras
    ordenadas e valor é lista de anagramas."""
    pass
palavras = ['ate','eat','tea','tan','nat','bat']
grupos = agrupar_anagramas(palavras)
# {('a','e','t'): ['ate','eat','tea'],
#  ('a','n','t'): ['tan','nat'], ('a','b','t'): ['bat']}

===PAGE_BREAK===

📚
  Resumo — Caps. 10, 11 e 12
Listas []
Mutáveis · append, extend, sort, pop, remove · alias perigoso 
· copiar com [:]
Mapeamento/Filtro/Redução
sum(), capitalize_all(), only_upper() · base de list 
comprehensions
Dicionários {}
Chave→valor · O(1) busca · .get() · .items() · Chaves hashable 
(não lista!)
Memos
Guardar resultados calculados · fibonacci c/ dict → O(n) vs 
O(2^n)
Tuplas ()
Imutáveis · hashable → chave de dict · Atribuição múltipla: 
a,b = b,a
*args / zip / enumerate
gather/scatter · zip para iteração paralela · enumerate para 
índice+valor
21