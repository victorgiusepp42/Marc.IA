---
tipo: slide_ou_roteiro
etapa: 2
topico: arquivos
fonte: docs/materiais_kb/AULAS/Aula15_Cap14_Arquivos_IP_IA.txt
data_processamento: 2026-07-04
autor_original: Prof. Dr. Márcio de Souza Dias (UFCAT/IMTec)
status: extraido_pdf_bruto
ordem_aula: '0'
observacao: Texto extraído automaticamente do PDF; revisar figuras/diagramas que não vieram.
---

# Aula15_Cap14_Arquivos_IP_IA

Capítulo 14
Arquivos
Pense em Python – Allen B. Downey
1º Período • Bacharelado em Inteligência Artificial • UFCAT
# Leitura de arquivo:
with open('dados.txt') as f:
    for linha in f:
        print(linha.strip())
# Escrita de arquivo:
with open('saida.txt','w') as f:
    f.write('Olá, IA!')
# Captura de exceção:
try:
    fin = open('arq.txt')
except FileNotFoundError:
    print('Não encontrado!')
Tópicos: Persistência · Leitura/Escrita · Formatação · Caminhos · try/except · dbm · pickle · Módulos

===PAGE_BREAK===

📋
  Roteiro da Aula
2
1 Persistência
Transitório vs. persistente — onde os dados vivem
2 Leitura e escrita
open(), modos 'r' 'w' 'a', write(), close()
3 Operador de formatação
% para formatar strings e f-strings
4 Nomes de arquivo e caminhos
Módulo os, caminhos relativos e absolutos
5 Captura de exceções
try / except — lidar com erros de arquivo
6 Bancos de dados (dbm)
Persistência tipo dicionário em disco
7 pickle e shelve
Serializar qualquer objeto Python
8 Módulos de escrita
__name__ == '__main__'
9 Exercícios práticos
Aplicar todos os conceitos

===PAGE_BREAK===

💾
  Persistência — Dados que Sobrevivem ao Programa
3
Programas transitórios perdem tudo ao fechar. Programas persistentes guardam dados em disco.
❌
  Programa TRANSITÓRIO
# Variáveis somem ao fechar!
nome = "Ana"
numeros = [1, 2, 3]
# Ao encerrar o Python:
# → nome desaparece
# → numeros desaparece
# → tudo começa do zero!
✅
  Programa PERSISTENTE
# Dados salvos em arquivo:
with open('dados.txt','w') as f:
    f.write("Ana
1 2 3
")
# Próxima execução lê de volta:
with open('dados.txt') as f:
    conteudo = f.read()
    print(conteudo)  # Ana  1 2 3
Arquivos de texto: Sequências de caracteres em disco. Simples e portável. Foco deste capítulo.
Bancos de dados: dbm, SQLite, PostgreSQL. Chave-valor ou relacional. Alta performance.
pickle / shelve: Serializa objetos Python inteiros. Conveniente para protótipos e ML.

===PAGE_BREAK===

📂
  Leitura e Escrita de Arquivos
4
open() retorna um objeto de arquivo. Segundo argumento define o modo. Sempre feche com close() ou use with.
# MODO LEITURA ('r' — padrão):
fin = open('palavras.txt')         # abre para leitura
# ou explicitamente:
fin = open('palavras.txt', 'r')
# Ler tudo de uma vez:
conteudo = fin.read()
# Ler linha por linha (eficiente para arquivos grandes):
for linha in fin:
    print(linha.strip())     # strip() remove '\n' do fim
# Ler uma linha por vez:
primeira = fin.readline()
# Ler todas as linhas numa lista:
linhas = fin.readlines()     # ['linha1\n', 'linha2\n', ...]
fin.close()   # SEMPRE fechar!
# MODO ESCRITA ('w' — cria novo ou SOBRESCREVE!):
fout = open('saida.txt', 'w')
fout.write("linha 1\n")
fout.write("linha 2\n")   # retorna nº de chars escritos
fout.close()
# MODO APPEND ('a' — adiciona ao fim):
fout = open('log.txt', 'a')
fout.write("nova entrada\n")
fout.close()
Modos de abertura
'r' Leitura (padrão). Erro se não existir.
'w' Escrita. Cria ou SOBRESCREVE!
'a' Append. Adiciona ao fim.
'r+' Leitura e escrita.
'rb' Leitura binária.
✅
  Prefira: with open()
# 'with' fecha automaticamente:
with open('arquivo.txt') as f:
    conteudo = f.read()
# arquivo fechado aqui!
# Mesmo com erro:
with open('notas.txt','w') as f:
    f.write("10 8.5 9\n")

===PAGE_BREAK===

🎨
  Formatação de Strings — %, format() e f-strings
5
write() aceita apenas strings. Para inserir outros tipos, é preciso formatar. Python oferece 3 formas.
Operador % (clássico)
camelos = 42
# %d = inteiro:
'%d camelos' % camelos
# '42 camelos'
# %g = float, %s = str:
'%d anos, %g km, %s'   % 
(3, 0.1, 'viagem')
# '3 anos, 0.1 km, viagem'
# Escrita em arquivo:
with open('saida.txt','w') 
as f:
    f.write('%d\n' % 42)
.format() (Python 3)
nome = 'Ana'
nota = 9.5
'Aluna: {}'.format(nome)
# 'Aluna: Ana'
# Posicional:
'{} tem nota {}'.format(
    nome, nota)
# 'Ana tem nota 9.5'
# Nomeado:
'{nome}: 
{nota:.1f}'.format(
    nome=nome, nota=nota)
# 'Ana: 9.5'
f-string ✅
 preferida
nome = 'Ana'
nota = 9.5
# Prefixo f antes das aspas:
f'Aluna: {nome}'
# 'Aluna: Ana'
f'{nome} nota {nota:.1f}'
# 'Ana nota 9.5'
# Expressões:
f'{2**10}'  # '1024'
f'{nota*2}' # '19.0'
# Escrever em arquivo:
with open('s.txt','w') as f:
    f.write(f'{nome}: 
{nota}')

===PAGE_BREAK===

📁
  Nomes de Arquivo, Caminhos e Módulo os
6
O módulo os fornece funções para navegar no sistema de arquivos de forma portável (Windows, Linux, Mac).
import os
import os.path
# Diretório atual:
cwd = os.getcwd()          # '/home/usuario/projeto'
# Verificar existência:
os.path.exists('memo.txt') # True ou False
os.path.isfile('memo.txt') # True se for arquivo
os.path.isdir('/home')     # True se for diretório
# Caminho absoluto:
os.path.abspath('memo.txt')  # '/home/usuario/projeto/memo.txt'
# Listar conteúdo de diretório:
os.listdir('.')              # ['dados.txt', 'script.py', ...]
os.listdir('/home/usuario')  # ['Downloads', 'Documentos', ...]
# Juntar partes de caminho (portável!):
caminho = os.path.join('/home/usuario', 'projeto', 'dados.txt')
# '/home/usuario/projeto/dados.txt'
# Separar diretório e arquivo:
os.path.split('/home/usuario/memo.txt')  # ('/home/usuario','memo.txt')
os.path.basename('/home/usuario/arq.py') # 'arq.py'
os.path.dirname('/home/usuario/arq.py')  # '/home/usuario'
Percorrer diretórios (walk)
def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(
            dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)  # recursivo!
Caminho relativo
memo.txt ou subdir/arq.py
Relativo ao diretório atual (cwd).
Caminho absoluto
/home/user/projeto/memo.txt
Começa na raiz. Independe do cwd.
os.path.join()
Use SEMPRE para construir caminhos.
Portável entre Windows ('\\') e Linux ('/').

===PAGE_BREAK===

🛡
  Captura de Exceções — try / except
7
Muitas coisas podem dar errado com arquivos. try/except captura erros e evita que o programa trave.
Erros comuns com arquivos
# Arquivo não encontrado:
open('arquivo_inexistente.txt')
# FileNotFoundError
# Sem permissão de escrita:
open('/etc/passwd', 'w')
# PermissionError
# Abrir diretório como arquivo:
open('/home')
# IsADirectoryError
Sintaxe try / except
try:
    fin = open('bad_file.txt')
    # código que pode falhar
except:
    print('Algo deu errado.')
# programa continua daqui!
# Captura específica — MELHOR PRÁTICA:
def ler_arquivo_seguro(nome):
    try:
        with open(nome, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f'Arquivo {nome!r} não encontrado.')
        return None
    except PermissionError:
        print(f'Sem permissão para ler {nome!r}.')
        return None
    except Exception as e:
        print(f'Erro inesperado: {e}')
        return None
conteudo = ler_arquivo_seguro('dados.txt')
if conteudo is not None:
    print('Lido com sucesso:', len(conteudo), 'chars')

===PAGE_BREAK===

🗄
  Bancos de Dados com dbm
8
dbm = dicionário que persiste em disco. Interface quase idêntica a dict, mas salvo em arquivo.
import dbm
# Abrir banco de dados ('c' = criar se não existir):
db = dbm.open('legendas', 'c')
# Adicionar / atualizar itens (como dicionário!):
db['cleese.png']  = 'Photo of John Cleese.'
db['palin.jpg']   = 'Photo of Michael Palin.'
# Atualizar valor existente:
db['cleese.png']  = 'John Cleese doing a silly walk.'
# Ler item (retorna bytes — prefixo b):
print(db['cleese.png'])
# b'John Cleese doing a silly walk.'
# Iterar sobre chaves (loop for funciona):
for key in db:
    print(key, db[key])
# Verificar existência:
if 'cleese.png' in db:
    print('Encontrado!')
# SEMPRE fechar ao terminar:
db.close()
dbm vs dict
Interface idêntica para acesso. Mas dados ficam 
em DISCO → persistem entre execuções!
Chaves e valores
Devem ser strings ou bytes. Para outros tipos, use 
pickle junto com dbm.
Objeto bytes (b'...')
dbm retorna bytes, não str. Use .decode() para 
converter: db['k'].decode('utf-8')
shelve — solução prática
shelve combina dbm + pickle: aceita qualquer 
tipo Python como valor!

===PAGE_BREAK===

🥒
  pickle e shelve — Serializar Objetos Python
9
pickle converte QUALQUER objeto Python em bytes e de volta. shelve = dbm + pickle automático.
pickle — serialização manual
import pickle
t1 = [1, 2, 3]
# Serializar → bytes:
s = pickle.dumps(t1)
print(s)  # b'\x80\x04\x95...'
# Desserializar → objeto:
t2 = pickle.loads(s)
print(t2)    # [1, 2, 3]
print(t1 == t2)  # True
print(t1 is t2)  # False (cópia!)
# Equivalente a copiar o objeto!
shelve — dbm + pickle automático ✅
import John Cleese doing a silly walk.
# Abrir 'prateleira':
db = shelve.open('meudb')
# Guardar qualquer tipo:
db['lista']  = [1, 2, 3]
db['modelo'] = {'acuracia': 0.95}
db['nome']   = 'IA-UFCAT'
# Ler de volta (tipo original!):
print(db['lista'])   # [1, 2, 3]
print(db['modelo'])  # {'acuracia': 0.95}
db.close()
🤖
  pickle em Inteligência Artificial — uso no dia a dia:
# Salvar modelo treinado (ex.: sklearn):
import pickle
with open('modelo_rf.pkl','wb') as f:
    pickle.dump(modelo_treinado, f)
# Carregar depois sem re-treinar:
with open('modelo_rf.pkl','rb') as f:
    modelo = pickle.load(f)
resultados = modelo.predict(X_novo)

===PAGE_BREAK===

📦
  Módulos de Escrita — __name__ == '__main__'
10
Qualquer arquivo .py pode ser importado como módulo. __name__ controla o que executa ao importar vs. rodar direto.
❌
  Problema: código executa ao importar
# wc.py (versão com problema):
def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count
print(linecount('wc.py'))  # executa!
# Ao importar: import wc → imprime 7!
✅
  Solução: if __name__ == '__main__'
# wc.py (versão correta):
def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count
if __name__ == '__main__':
    print(linecount('wc.py'))
# Agora 'import wc' não executa!
# __name__ é uma variável especial do Python:
# • Quando rodado como script: __name__ == '__main__'
# • Quando importado:          __name__ == 'wc'  (nome do módulo)
# Uso como módulo:
# >>> import wc
# >>> wc.linecount('wc.py')   # 7  ← só executa quando chamado
# Como script:
# $ python wc.py               ← executa o if __name__ == '__main__'
# Padrão recomendado para qualquer módulo Python:
def main():
    """Ponto de entrada principal."""
    resultado = linecount('wc.py')
    print(f'O arquivo tem {resultado} linhas.')
if __name__ == '__main__':
    main()

===PAGE_BREAK===

🔄
  Padrões Práticos de Leitura de Arquivo
11
Padrões fundamentais para processar arquivos de texto — usados em NLP e análise de dados.
# 1. CONTAR LINHAS:
def contar_linhas(nome):
    with open(nome) as f:
        return sum(1 for _ in f)
# 2. FILTRAR LINHAS (como grep):
def filtrar(nome, padrao):
    resultados = []
    with open(nome) as f:
        for linha in f:
            if padrao in linha:
                resultados.append(linha.strip())
    return resultados
# 3. PROCESSAR CSV SIMPLES:
def ler_csv(nome):
    dados = []
    with open(nome) as f:
        cabecalho = f.readline().strip().split(',')
        for linha in f:
            valores = linha.strip().split(',')
            dados.append(dict(zip(cabecalho, valores)))
    return dados
# ler_csv('notas.csv') → [{'aluno':'Ana','nota':'9.5'}, ...]
# 4. COPIAR / TRANSFORMAR (padrão sed):
def transformar(entrada, saida, func):
    with open(entrada) as fin, open(saida, 'w') as fout:
        for linha in fin:
            fout.write(func(linha))
# Exemplo: converter tudo para maiúsculas:
transformar('texto.txt', 'TEXTO.txt', str.upper)

===PAGE_BREAK===

🐛
  Depuração — Whitespace Invisível e repr()
12
Espaços, tabulações e quebras de linha são invisíveis — causam bugs difíceis. repr() torna tudo visível.
# O PROBLEMA — whitespace invisível:
s = '1 2\t 3\n 4'
print(s)       # imprime: 1 2    3
               #                  4
               # (tabs e newline ficam 'transparentes')
# SOLUÇÃO — repr() mostra tudo:
print(repr(s)) # '1 2\t 3\n 4'
               # agora \t e \n ficam visíveis!
# Problemas comuns ao ler arquivos:
with open('dados.txt') as f:
    for linha in f:
        # linha ainda tem '\n' no fim:
        print(repr(linha))  # 'banana\n'
        # CORRETO — remover whitespace:
        palavra = linha.strip()  # 'banana'
        # ou somente newline:
        palavra = linha.rstrip('\n')
# Diferença entre sistemas operacionais:
# Windows: '\r\n'  (CRLF)
# Linux/Mac: '\n'   (LF)
# strip() e splitlines() resolvem ambos!
# Verificar encoding:
with open('arquivo.txt', encoding='utf-8') as f:
    conteudo = f.read()
repr() é seu melhor amigo
Mostra \n, \t, \r e espaços ocultos.
print(repr(linha)) antes de processar!
strip() remove tudo
linha.strip() remove espaços, \n, \t
do início e do fim automaticamente.
splitlines() é portável
Divide em linhas corretamente em
Windows (\r\n) e Linux (\n).
encoding='utf-8'
Sempre especifique encoding ao abrir
arquivos com caracteres especiais.

===PAGE_BREAK===

📖
  Glossário — Termos do Capítulo 14
13
persistente Programa que roda por longo tempo 
mantendo dados em armazenamento 
permanente.
arquivo de texto Sequência de caracteres guardados em 
armazenamento permanente (disco, SSD...)
diretório Coleção de arquivos nomeada, também 
chamada de pasta ou folder.
caminho String que identifica um arquivo ou diretório 
no sistema de arquivos.
caminho relativo Caminho que começa no diretório atual 
(cwd). Exemplo: subdir/arq.txt
caminho absoluto Caminho que começa na raiz do sistema. 
Exemplo: /home/user/arquivo.txt
capturar Impedir que uma exceção encerre o 
programa usando try/except.
banco de dados Arquivo cujo conteúdo é organizado como 
dicionário: chaves → valores.
objeto bytes Objeto similar a string precedido de b'...'. 
Retornado por dbm e pickle.
pickle Módulo que serializa/desserializa objetos 
Python em bytes.
shell Interface de linha de comando que permite 
executar programas do sistema.
objeto pipe Objeto que representa um programa em 
execução externo, acessado pelo Python.

===PAGE_BREAK===

✏
  Exercício para os Alunos
14
Exercício 1 — linecount(), wordcount() e charcount()
📌
  Escreva três funções para analisar um arquivo de texto: contagem de linhas, palavras e caracteres.
        Use with open() e trate o caso do arquivo não existir com try/except.
# Template — complete as funções:
def linecount(filename):
    """Retorna o número de linhas do arquivo."""
    # Seu código aqui
    pass
def wordcount(filename):
    """Retorna o número de palavras do arquivo."""
    # Dica: use str.split() em cada linha
    pass
def charcount(filename):
    """Retorna o número de caracteres (sem \n)."""
    pass
# Teste com um arquivo que você criar:
# echo "Olá mundo\nIA UFCAT" > teste.txt
print(linecount('teste.txt'))    # 2
print(wordcount('teste.txt'))    # 3
print(charcount('teste.txt'))    # 12
💡
  Dicas
• Use with open(nome) as f:
• Para contar linhas: sum(1 for _ in f)
• Para palavras: len(linha.split())
• Encapsule em try/except FileNotFoundError
• Bônus: use if __name__ == '__main__':
•         para testar como script!

===PAGE_BREAK===

✏
  Exercício para os Alunos
15
Exercício 2 — sed(): Busca e Substituição em Arquivo (Exercício 14.1)
📌
  Implemente sed(padrao, substituicao, entrada, saida):
        Lê o arquivo de entrada, substitui todas as ocorrências de padrao por substituicao
        e escreve o resultado no arquivo de saída. Capture erros com try/except.
def sed(padrao, substituicao, entrada, saida):
    """Substitui padrao por substituicao no arquivo de entrada
    e escreve resultado em saida."""
    # Implemente aqui
    pass
# Testes esperados:
# Arquivo entrada.txt contém:
#   "Python é difícil."
#   "Python é complicado."
sed('difícil', 'fácil', 'entrada.txt', 'saida.txt')
# saida.txt deve conter:
#   "Python é fácil."
#   "Python é complicado."
# Captura de erros:
sed('x', 'y', 'inexistente.txt', 'saida.txt')
# deve exibir mensagem de erro e terminar graciosamente
💡
  Dicas
• Abra dois arquivos com with.
• Para cada linha, use str.replace().
• Envolva tudo em try/except.
• Capture: FileNotFoundError,
  PermissionError, Exception.
• with open(a) as fin,
•   open(b,'w') as fout:

===PAGE_BREAK===

✏
  Exercício para os Alunos
16
Exercício 3 — Anagramas com shelve e Busca de Duplicatas (Exercícios 14.2 e 14.3)
📌
  Parte A: salve e recupere anagramas usando shelve.
        Parte B: encontre arquivos duplicados em um diretório usando os.walk() e comparação de conteúdo.
import shelve
# PARTE A — store_anagrams:
def store_anagrams(anagram_dict, shelf_name):
    """Salva dicionário de anagramas em shelve."""
    db = shelve.open(shelf_name)
    for palavra, anagramas in anagram_dict.items():
        db[palavra] = anagramas
    db.close()
def read_anagrams(shelf_name, palavra):
    """Retorna lista de anagramas de uma palavra."""
    db = shelve.open(shelf_name)
    resultado = db.get(palavra, [])
    db.close()
    return resultado
import os, hashlib
# PARTE B — encontrar arquivos duplicados:
def md5_arquivo(caminho):
    """Calcula hash MD5 do arquivo."""
    h = hashlib.md5()
    with open(caminho,'rb') as f:
        h.update(f.read())
    return h.hexdigest()
def achar_duplicatas(diretorio, ext='.txt'):
    visto = {}     # hash → caminho
    duplas = []
    for root, dirs, files in os.walk(diretorio):
        for nome in files:
            if nome.endswith(ext):
                caminho = os.path.join(root, nome)
                h = md5_arquivo(caminho)
                if h in visto:
                    duplas.append((visto[h], caminho))
                else:
                    visto[h] = caminho
    return duplas
💡
  os.walk(dir) gera (raiz, subdirs, arquivos) recursivamente para toda a árvore de diretórios.

===PAGE_BREAK===

✏
  Exercício para os Alunos
17
Exercício 4 — Análise de Texto: frequência de palavras com persistência
📌
  Escreva um analisador de texto completo que: leia um arquivo, conte frequência de palavras,
        salve o resultado com shelve e permita consultas posteriores. Use o padrão if __name__ == '__main__'.
import shelve, re
from collections import Counter
def analisar_texto(nome_arquivo):
    """Lê arquivo e retorna Counter de palavras."""
    try:
        with open(nome_arquivo, encoding='utf-8') as f:
            texto = f.read().lower()
        # Extrair somente palavras (sem pontuação):
        palavras = re.findall(r"[a-záéíóúãõâêô]+", texto)
        return Counter(palavras)
    except FileNotFoundError:
        print(f'Arquivo {nome_arquivo!r} não encontrado.')
        return None
def salvar_frequencias(contador, nome_shelf):
    """Salva frequências em disco com shelve."""
    with shelve.open(nome_shelf) as db:
        db['frequencias'] = dict(contador)
        db['total'] = sum(contador.values())
    print(f'Salvo em {nome_shelf}!')
def consultar_palavra(nome_shelf, palavra):
    """Retorna frequência de uma palavra."""
    with shelve.open(nome_shelf) as db:
        freq = db.get('frequencias', {})
        return freq.get(palavra.lower(), 0)
if __name__ == '__main__':
    freq = analisar_texto('texto.txt')
    if freq:
        print('Top 10:', freq.most_common(10))
        salvar_frequencias(freq, 'freq_db')
        print('Python:', consultar_palavra('freq_db', 'python'))

===PAGE_BREAK===

📚
  Resumo do Capítulo 14 — Arquivos
Persistência
Arquivos de texto · dbm · pickle/shelve · dados sobrevivem ao 
programa
open() + with
Modos 'r','w','a' · with fecha automaticamente · sempre use 
with!
Formatação
% (clássico) · .format() · f-strings (preferido) · write() só aceita 
str
Módulo os
getcwd, listdir, path.exists, path.join, path.abspath, walk
try / except
Captura FileNotFoundError, PermissionError · EAFP — estilo 
Python
pickle / shelve
Serializa objetos Python · salva modelos de ML · shelve = dbm 
+ pickle
Próximo capítulo: Cap. 15 — Classes e Objetos — Programação Orientada a Objetos. 18