---
tipo: slide_ou_roteiro
etapa: 1
topico: introducao
fonte: docs/materiais_kb/AULAS/Aula1_Fundamentos_Computacao_Algoritmos (2).txt
data_processamento: 2026-07-04
autor_original: Prof. Dr. Márcio de Souza Dias (UFCAT/IMTec)
status: extraido_pdf_bruto
ordem_aula: '0'
observacao: Texto extraído automaticamente do PDF; revisar figuras/diagramas que não vieram.
---

# Aula1_Fundamentos_Computacao_Algoritmos

🖥
💾
⚙
📟
🔢
💻
INTRODUÇÃO À PROGRAMAÇÃO
Aula 1
Fundamentos de 
Computação e 
ProgramaçãoHardware • Software • CPU • Memória • Linguagens • Resolução de Problemas
🖥
Hardware
💻
Software
🔢
Binário
🛠
Linguagens
🧩
Polya
Prof. Márcio Dias - marciodias@ufcat.edu.br

===PAGE_BREAK===

SLIDE 01
Partes de um Computador
Um computador é composto por dois grandes grupos que trabalham juntos:
🖥  HARDWARE
Dispositivos eletrônicos físicos — tudo que você pode tocar.
⌨Entrada: Teclado, Mouse, Webcam
🧠Processamento:CPU — cérebro do PC
📟Memória RAM:Armazenamento temporário
🖨Saída: Monitor, Impressora
💾Armazenamento:HD, SSD, Pen drive
💻  SOFTWARE
Instruções e programas — tudo que você não pode tocar.
🔧Sistema Operacional:Windows, Linux, macOS
📱Aplicativos: Word, Chrome, Spotify
🎮Jogos: Programas interativos
🛡Antivírus: Proteção do sistema
💻Linguagens: Python, Java, C++
💡 Analogia: O hardware é o corpo humano; o software é a mente que comanda as ações.

===PAGE_BREAK===

SLIDE 02
Hardware — Componentes Detalhados
⌨ ENTRADA
• Teclado — digitar texto e comandos
• Mouse — apontar e clicar
• Webcam — capturar imagem/vídeo
• Microfone — capturar áudio
• Scanner — digitalizar documentos
🧠 PROCESSAMENTO
• CPU — executa bilhões de instruções/seg
• Núcleos (cores) — processamento paralelo
• Clock — velocidade medida em GHz
• Cache — memória ultrarrápida da CPU
• Ex: Intel Core i9, AMD Ryzen 9
📟 MEMÓRIA RAM
• Armazenamento temporário e volátil
• Perde dados ao desligar o PC
• Medida em GB (4GB, 8GB, 16GB...)
🖨 SAÍDA
• Monitor — exibir imagens e vídeo
• Impressora — gerar saída física
• Caixas de som — reproduzir áudio
💾 ARMAZENAMENTO
• HD (HDD) — magnético, barato, lento
• SSD — flash, rápido, mais caro
• Pen Drive — USB, portátil

===PAGE_BREAK===

SLIDE 03
CPU — O Cérebro do Computador
Central Processing Unit (CPU) — recupera instruções da memória e as executa. É o componente que realiza todos os cálculos e 
toma todas as decisões.
🔄 Ciclo de Execução da CPU
1BUSCAR (Fetch) CPU busca a próxima instrução na RAM
2DECODIFICAR (Decode) Interpreta o que a instrução significa
3EXECUTAR (Execute) Realiza a operação (cálculo, movimento...)
4ARMAZENAR (Store) Guarda o resultado de volta na memória
📊 Especificações Comuns
Clock: 1 GHz a 5+ GHz
Núcleos: 2, 4, 8, 16, 32...
Cache: L1, L2, L3 (MB)
Exemplos: Intel Core, AMD Ryzen
Fun Fact: Processa bilhões de op/s
💡 Analogia: A CPU é como o cérebro humano — processa informações, toma decisões e coordena todas as ações.

===PAGE_BREAK===

SLIDE 04
Memória RAM
⚡
Volátil
Conteúdo APAGADO ao desligar ou reiniciar o computador. 
Dados devem ser salvos antes.
🚀
Rápida
Muito mais rápida que HD/SSD. CPU acessa RAM em 
nanossegundos.
📦
Temporária
Armazena programas e dados em uso. Um programa DEVE 
estar na RAM para ser executado.
🔢
Estrutura
Sequência ordenada de bytes (8 bits cada). Cada byte tem 
endereço único na memória.
📏
Capacidade
Medida em GB. Ex: 4GB, 8GB, 16GB, 32GB. Mais RAM → 
mais multitarefa.
🔄
Intermediária
Armazena também resultados intermediários e finais do 
processamento.
💡 Analogia: A RAM é como a bancada de um carpinteiro. Só cabe o que está sendo usado AGORA. Quando ele termina o dia, a bancada é limpa 
(dados perdidos). O armário (HD/SSD) guarda tudo permanentemente.

===PAGE_BREAK===

SLIDE 05
Dispositivos de Armazenamento
❌ RAM — Volátil (Temporária)
 ✅ Armazenamento — Não-Volátil (Permanente)
💽
HD (HDD)
Capacidade: 500GB–10TB | Não-Volátil
Magnético, mecânico, mais lento e barato. Boa capacidade e 
custo-benefício.
⚡
SSD
Capacidade: 128GB–4TB | Não-Volátil
Flash, sem partes móveis, muito mais rápido. Sistema 
operacional e programas.
🔌
Pen Drive
Capacidade: 4GB–1TB | Não-Volátil
USB, portátil e prático. Ideal para transferir arquivos entre 
computadores.
💿
CD / DVD
Capacidade: 700MB–17GB | Não-Volátil
Óptico, quase em desuso. CDs: 700MB. DVDs: 4,7GB–17GB.
☁
Nuvem
Capacidade: Ilimitada | Não-Volátil
Google Drive, OneDrive, Dropbox. Acessível de qualquer lugar 
com internet.

===PAGE_BREAK===

SLIDE 06
Software — A Alma do Computador
Software = conjunto de instruções que dizem ao hardware O QUE fazer. Sem software, o hardware é inútil — como um carro sem 
motorista.
🏗 Sistema Operacional
• Gerencia hardware e software
• Interface entre usuário e máquina
• Exemplos: Windows 11, Ubuntu, macOS
• Controla memória, processos, arquivos
📦 Software Aplicativo
• Realiza tarefas específicas do usuário
• Word, Excel, Photoshop, Chrome
• Jogos, apps de celular
• Depende do sistema operacional
🔧 Software de Sistema
• Drivers de hardware (impressora, GPU)
• Utilitários (antivírus, backup)
• Compiladores e interpretadores
• Bancos de dados (MySQL, Oracle)
🤔 Reflexão: "Sem os programas, o que é um computador?" → Hardware inútil! O propósito é executar o desejo humano.

===PAGE_BREAK===

SLIDE 07
Linguagem de Computador — Sistema Binário
🔢 Por que binário?
⚡ 2 estados: Dispositivos digitais têm apenas DOIS estados 
estáveis: ligado (1) e desligado (0).
0⃣
1⃣
Bit: Um único dígito binário (0 ou 1). Abreviação de 
'binary digit' — a menor unidade de informação.
📦 Byte: Grupo de 8 bits. Unidade mínima de 
armazenamento. Ex: 01000001 = letra 'A' em ASCII.
📏 Hierarquia: 1 KB = 1.024 bytes | 1 MB = 1.024 KB | 1 GB = 
1.024 MB | 1 TB = 1.024 GB
🔄 Codificação:Todo dado (texto, imagem, vídeo, áudio) é 
convertido para sequências de 0s e 1s.
📊 Exemplos de Codificação ASCII
Binário Decimal Char
01000001 65 A
01000010 66 B
01000011 67 C
01001010 74 J
01001011 75 K
01001100 76 L
00110000 48 0
00110001 49 1
00110010 50 2
00100000 32 (espaço)
00101110 46 .
00111111 63 ?
💡 A letra 'A' = 01000001 em binário = decimal 65 no ASCII

===PAGE_BREAK===

SLIDE 08
Esquemas de Codificação
Codificação é o processo de converter caracteres, imagens e outros dados em números binários que o computador entende.
ASCII — 1 byte por caractere
• American Standard Code for Information Interchange
• Criado em 1963, padronizado em 1967
• 1 byte = 8 bits → 256 caracteres possíveis
• Cobre: letras A-Z, a-z, 0-9, !@#$%...
• NÃO inclui: ç, ã, é, ñ, 漢字, ﻋﺮﺑﻲ...
Ainda usado em sistemas legados e arquivos simples
Unicode — 2+ bytes por caractere
• Padrão internacional universal de texto
• UTF-8: 1-4 bytes | UTF-16: 2-4 bytes
• +140.000 caracteres de 150+ idiomas
• Inclui: ç, ã, é, ñ, 漢字, ﻋﺮﺑﻲemojis 
😀
• Usado em HTML, Python, Java, web moderna
• Retrocompatível com ASCII (0-127 iguais)
💡 Hoje o Unicode (UTF-8) é o padrão dominante na web. O Python 3 usa Unicode por padrão — você pode usar acentos no código!

===PAGE_BREAK===

SLIDE 09
Linguagens de Programação
Humanos falam português; computadores falam binário. Linguagens de programação são a ponte entre os dois.
1) Linguagem de Máquina
Linguagem nativa do computador — instruções 
em código binário.
✓ Executada diretamente pelo hardware
✓ Extremamente rápida
✓ Nenhuma tradução necessária
Ex: 1011 0001 01100001  → move o 
valor 97 para o registrador AL
2) Linguagem Assembly
Usa abreviações mnemônicas. Assembler 
converte para código de máquina.
✓ Mais legível que binário
✓ Controle total do hardware
✓ Muito eficiente
Ex: MOV AL, 61h  → move o valor 97 
para o registrador AL
3) Linguagem de Alto Nível
Linguagem próxima ao inglês. Compilador/
Interpretador converte para binário.
✓ Fácil de aprender e usar
✓ Portátil entre sistemas
✓ Alta produtividade
Ex: total_custo = preco + imposto  ← 
Python/C/Java
Alto Nível → Assembly → Linguagem de Máquina (cada nível é traduzido para o nível abaixo)

===PAGE_BREAK===

SLIDE 10
Do Código Fonte ao Programa Executável
📝
Código Fonte
.py / .java / .c
1
▶
⚙
Compilador
tradução automática
2
▶
🔢
Prog. Objeto
.o / .obj
3
▶
📚
Bibliotecas
.lib / .dll
4
▶
🚀
Executável
.exe / .out
5
Escrito pelo programador 
em linguagem de alto 
nível. Legível por 
humanos.
Analisa e traduz todo o 
código fonte para 
linguagem de máquina de 
uma vez.
Código em linguagem de 
máquina. Ainda não 
executável — precisa de 
ligação.
Módulos de código 
reutilizável. Ex: math, 
string, I/O. Vinculados 
pelo linker.
Programa final pronto 
para ser executado pelo 
sistema operacional.
Python (alto nível): total = preco + imposto   →   Compilado para  →   10111000 01100001...

===PAGE_BREAK===

SLIDE 11
O que é Programação?
Programação é a criação de um conjunto ordenado de instruções para resolver um problema com um computador.
🔢
~100 instruções
Um computador entende apenas cerca de 100 instruções 
básicas. Programas diferentes usam essas instruções em 
ordens e combinações diferentes.
🧩
Combinação criativa
A arte da programação está em combinar essas poucas 
instruções de maneiras inteligentes para criar soluções 
complexas.
🧠
Pensar é a chave
A parte mais valiosa não é aprender a sintaxe, mas 
aprender a PENSAR: organizar a sequência de instruções 
para resolver o problema.
🎯
Linguagens diferentes
Java, Python, C, C++, FORTRAN, Pascal, Visual Basic — cada 
uma tem sua sintaxe, mas compartilham os mesmos 
conceitos fundamentais.
Exemplo em Python:  print("Olá, Mundo!")  |  area = 5 * 5 * 3.1415  |  total_custo = preco + imposto

===PAGE_BREAK===

SLIDE 12
Resolução de Problemas — George Pólya
Em 1945, o matemático húngaro George Pólya publicou o livro How to Solve It — 4 princípios universais para resolver qualquer problema 
eficientemente.
U — Compreender
🔍 Understand
• Qual é o problema? Qual é a 
incógnita?
• Identificar as ENTRADAS (inputs)
• Identificar as SAÍDAS (outputs)
• Identificar os PROCESSOS necessários
• Desenhar diagramas, introduzir 
notação
• Isolar partes do problema
D — Conceber um 
Plano
📋 Devise a Plan
• Encontrar conexões entre variáveis
• Simplificar: quebrar em sub-
problemas
• Projetar a solução — algoritmo
• Criar fluxograma ou pseudocódigo
• Fazer lista de ações para implementar
• Usar técnicas conhecidas similares
I — Implementar
💻 Implement
• Codificar em linguagem de 
programação
• Verificar resultados em cada etapa
• Testar, testar e testar!
• Depurar (debugar) erros
• Executar o plano passo a passo
• Documentar o código
E — Avaliar
✅ Evaluate
• Executar com numerosos casos de 
teste
• Usar casos esperados E inesperados
• Verificar se atende aos requisitos
• Procurar soluções mais eficientes
• Verificar se resolve outros problemas
• Revisar e otimizar o código

===PAGE_BREAK===

SLIDE 13
Aplicando Pólya — Exemplo: Salário Semanal
📋 Problema: Determinar os ganhos da semana de um empregado a partir do pagamento por hora e das horas trabalhadas. Horas 
extras (acima de 40h) pagam 1.5× o valor normal.
U — Entender
INPUT: valor_hora, horas_trabalhadas
OUTPUT: valor_total (ganhos brutos)
PROCESSO: calcular horas extras (>40h)
CONDIÇÃO: horas_extras = horas - 40
OBS: só há horas extras se trabalhou >40h
D — Plano / Algoritmo
1. Pedir horas_trabalhadas e valor_hora
2. horas_extras = horas_trabalhadas − 40
3. valor_horas_extras = 1.5 × valor_hora × horas_extras
4. valor_total = (40 × valor_hora) + valor_horas_extras
5. Imprimir valor_total
I — Implementar (Python)
horas = float(input('Horas trabalhadas: '))
valor = float(input('Valor por hora: R$'))
if horas > 40:
    extras = horas - 40
    total = (40*valor) + (1.5*valor*extras)
else:
    total = horas * valor
print(f'Ganhos: R${total:.2f}')
E — Avaliar
Teste 1: 40h × R$20 = R$800,00 
✅
Teste 2: 45h × R$20 = 40×20 + 5×30 = R$950,00 
✅
Teste 3: 0h → R$0,00 
✅
Teste 4: 40.1h → verifica cálculo de extras 
✅
Melhoria: tratar horas negativas (validação)

===PAGE_BREAK===

✅
❌ VERDADEIRO OU FALSO
Exercícios de FixaçãoAnalise cada afirmação e marque V (Verdadeiro) ou F (Falso):
1A RAM é um dispositivo de armazenamento permanente — os dados não são perdidos ao desligar o computador.
 ❌ FRAM é volátil — dados 
apagados ao desligar.
2A CPU executa o ciclo: Buscar → Decodificar → Executar → Armazenar continuamente durante o funcionamento.
 ✅ VCorreto — é o ciclo básico 
de fetch-decode-execute.
3Um programa de linguagem de alto nível pode ser executado diretamente pelo hardware sem compilação.
 ❌ FPrecisa ser compilado ou 
interpretado para binário.
4Um byte é composto por 8 bits e representa a unidade mínima de armazenamento em memória.
 ✅ V
Correto — 1 byte = 8 bits. 
Dois dados não 
compartilham o mesmo 
byte.
5O ASCII usa 2 bytes por caractere e consegue representar todos os idiomas do mundo, incluindo árabe e chinês.
 ❌ F
ASCII usa 1 byte (256 
chars). Unicode usa 2+ 
bytes e cobre 140k+ 
caracteres.
6A linguagem Assembly é mais fácil de programar que linguagens de alto nível como Python ou Java.
 ❌ F
Assembly é mais difícil — 
abreviações mnemônicas 
e dependente de 
hardware.
7O hardware sem software é inútil — os programas são a força motriz que diz ao computador o que fazer.
 ✅ V
Correto — hardware e 
software são 
interdependentes.

===PAGE_BREAK===

🎯 QUIZ — QUESTÕES
Quiz — Múltipla Escolha
1. Qual componente é responsável por executar as instruções de um programa?
A) RAM — armazena dados temporariamente
C) HD — armazena permanentemente
D) Monitor — exibe resultados
💡 A CPU (Unidade Central de Processamento) é o 'cérebro' que executa as instruções.
2. Um programador escreveu código Python e quer que o computador execute. O que é necessário?
A) Copiar o arquivo .py para o HD
B) Abrir o arquivo no Bloco de Notas
D) Renomear o arquivo para .exe
✏ Reflita: O que você acha que é mais difícil na programação — aprender a sintaxe ou aprender a pensar na solução?
  B) CPU — processa e executa instruções
✅ B) CPU — processa e executa instruções
C) Compilar/Interpretar para linguagem de máquina
✅ C) Compilar/Interpretar para linguagem de máquina
💡 Python é uma linguagem de alto nível — precisa ser interpretada para que o computador entenda.

===PAGE_BREAK===

🎯 QUIZ — QUESTÕES
Quiz — Múltipla Escolha
1. Qual componente é responsável por executar as instruções de um programa?
A) RAM — armazena dados temporariamente
✅ B) CPU — processa e executa instruções
C) HD — armazena permanentemente
D) Monitor — exibe resultados
💡 A CPU (Unidade Central de Processamento) é o 'cérebro' que executa as instruções.
2. Um programador escreveu código Python e quer que o computador execute. O que é necessário?
A) Copiar o arquivo .py para o HD
B) Abrir o arquivo no Bloco de Notas
C) Compilar/Interpretar para linguagem de máquina
D) Renomear o arquivo para .exe
💡 Python é uma linguagem de alto nível — precisa ser interpretada para que o computador entenda.
✏ Reflita: O que você acha que é mais difícil na programação — aprender a sintaxe ou aprender a pensar na solução?
✅ C) Compilar/Interpretar para linguagem de máquina
💡 Python é uma linguagem de alto nível — precisa ser interpretada para que o computador entenda.

===PAGE_BREAK===

{ }LÓGICA DE PROGRAMAÇÃO E 
ALGORITMOS Fundamentos, Conceitos e Exemplos Práticos
Lógica Pseudocódigo Fluxogramas Programação

===PAGE_BREAK===

CONCEITO 01
Lógica de Programação
"Técnica de encadear pensamentos para atingir determinado objetivo."
🧠
Pensar
Analisar o problema 
e entendê-lo bem
📋
Planejar
Organizar os passos 
da solução
💻
Executar
Transformar em 
código de computador

===PAGE_BREAK===

O que é um Algoritmo?
Definição e conceito fundamental
DEFINIÇÃO
Um algoritmo é uma sequência lógica e finita de instruções 
bem definidas que, quando executadas, resolvem um 
problema ou realizam uma tarefa específica.
Características Essenciais:
• Finitude: sempre termina 
• Precisão: passos bem definidos 
• Entrada e Saída: dados in/out 
• Eficiência: recursos adequados
ETIMOLOGIA
al-Khwārizmī
Matemático persa do séc. IX
O termo "algoritmo" deriva do nome do 
matemático Muhammad ibn Musa al-
Khwārizmī, cujas obras sobre aritmética 
foram fundamentais para a matemática 
ocidental.

===PAGE_BREAK===

O que é uma Instrução?
Instrução é cada linha/comando de um algoritmo — indica ao computador uma ação elementar a ser 
executada.
Algoritmo 1 — Fritar um Ovo
1  pegar frigideira, ovo, óleo e sal;
2  colocar óleo na frigideira;
3  acender o fogo;
4  colocar a frigideira no fogo;
5  esperar o óleo esquentar;
6  colocar o ovo;
7  retirar quando pronto;
Cada linha é 
uma instrução!
✔  Algoritmo = conjunto de instruções
✔  Cada instrução faz UMA ação simples
✔  Instruções executadas em ordem
✔  Resultado: problema resolvido!

===PAGE_BREAK===

Algoritmos no Dia a Dia
Você já usa algoritmos sem perceber!
🍰
Receita de Bolo
Lista de ingredientes + passos na ordem certa 
= resultado esperado
🚗
Trocar um Pneu
Sequência: afrouxar parafusos → levantar 
carro → trocar → apertar
📱
GPS de Navegação
Origem + destino → calcula melhor rota passo 
a passo
🔍
Pesquisa no Google
Sua busca → algoritmo de relevância → 
resultados ordenados
💳
Caixa Eletrônico
Cartão + senha → verifica saldo → entrega 
dinheiro
🧹
Varrer a Casa
Início → varrer cômodo por cômodo → juntar 
lixo → fim

===PAGE_BREAK===

Estrutura de um Algoritmo
Todo algoritmo tem três partes fundamentais
📥
ENTRADA
Dados fornecidos ao algoritmo para 
serem processados
Ex: notas do aluno, temperatura, senha do 
usuário
⚙
PROCESSAMENTO
Operações realizadas sobre os dados 
de entrada
Ex: calcular média, converter unidades, 
verificar senha
📤
SAÍDA
Resultado produzido após o 
processamento
Ex: situação do aluno, temperatura em °F, 
acesso liberado

===PAGE_BREAK===

Exemplo Prático: Trocar uma Lâmpada
Algoritmo cotidiano descrito passo a passo
1 Verificar se a lâmpada está queimada
2 Desligar o interruptor de energia
3 Buscar uma escada e uma lâmpada nova
4 Subir na escada com cuidado
5 Remover a lâmpada queimada girando no sentido anti-
horário
6 Encaixar a lâmpada nova girando no sentido horário
7 Descer da escada e ligar o interruptor
8 Verificar se a lâmpada acendeu → FIM
💡  Perceba: sequência lógica, passos definidos, início e fim claros — isso é um algoritmo!

===PAGE_BREAK===

Formas de Representação
Como escrever e visualizar algoritmos
📝  Linguagem Natural
✔ Vantagens
• Fácil de entender
• Sem regras formais
• Ótimo para inicio
✘ Desvantagens
• Ambígua
• Imprecisa
Para calcular a média: 
Some as notas e divida pela 
quantidade.
💻  Pseudocódigo
✔ Vantagens
• Semi-formal
• Próximo ao código real
• Independente de linguagem
✘ Desvantagens
• Requer conhecimento básico
• Não padronizado
LEIA nota1, nota2 
media ← (nota1 + nota2) / 2 
ESCREVA media
🔷  Fluxograma ou Blocos
✔ Vantagens
• Visual e intuitivo
• Mostra fluxo claramente
• Fácil de seguir
✘ Desvantagens
• Complexo em algoritmos grandes
• Trabalhoso de desenhar
Usa formas geométricas: 
◯ Início/Fim 
□ Processo 
◇ Decisão

===PAGE_BREAK===

Linguagem Natural — Exemplos Práticos
Problemas comuns descritos em linguagem narrativa
📝 Linguagem Natural
Exemplo 1 — Somar dois números
Passo 1: Leia o primeiro número. 
Passo 2: Leia o segundo número. 
Passo 3: Some os dois números. 
Passo 4: Mostre o resultado.
Exemplo 2 — Verificar maioridade
Passo 1: Pergunte a idade da pessoa. 
Passo 2: Se a idade for maior ou igual a 18, 
            informe que é maior de idade. 
Passo 3: Caso contrário, informe que é menor.
Exemplo 3 — Média de três notas
Passo 1: Obtenha as três notas do aluno. 
Passo 2: Some as três notas. 
Passo 3: Divida o resultado por 3. 
Passo 4: Se a média for maior ou igual a 6, 
            escreva 'Aprovado'. Senão, escreva 
            'Reprovado'.
Exemplo 4 — Saque no caixa eletrônico
Passo 1: Insira o cartão. 
Passo 2: Digite a senha. 
Passo 3: Se a senha estiver correta, informe 
            o saldo disponível. 
Passo 4: Digite o valor do saque. 
Passo 5: Se houver saldo, entregue o dinheiro. 
Passo 6: Caso contrário, mostre 'Saldo insuficiente'.

===PAGE_BREAK===

Pseudocódigo (Portugol)
Linguagem estruturada semi-formal — ponte entre o português e o código
O pseudocódigo é uma forma de representação que combina o melhor da linguagem natural (clareza) com o melhor do 
fluxograma (estrutura), usando regras predefinidas de escrita que se assemelham a uma linguagem de programação 
real.
ANATOMIA DO PSEUDOCÓDIGO
ALGORITMO →  Nome do algoritmo
VAR →  Declaração de variáveis
INÍCIO →  Início do bloco principal
LEIA →  Entrada de dados
ESCREVA →  Saída de dados
SE...ENTÃO →  Estrutura de decisão
ENQUANTO →  Estrutura de repetição
FIM_ALGORITMO →  Fim do bloco
TAMBÉM CONHECIDO COMO...
Portugol Mais comum no Brasil
Linguagem EstruturadaTermo formal acadêmico
Pseudolinguagem Termo genérico
Português EstruturadoUsado em apostilas
VisuAlg / Visualg Ferramenta popular no ensino
Disponível em: https://visualg.com.br

===PAGE_BREAK===

Pseudocódigo — Estrutura e Primeiro ExemploAnatomia completa com exemplo de soma de dois números
💻 Pseudocódigo
ALGORITMO SomaDoisNumeros
VAR
  num1, num2, soma : Inteiro
INÍCIO
  ESCREVA("Digite o 1º número: ")
  LEIA(num1)
  ESCREVA("Digite o 2º número: ")
  LEIA(num2)
  soma ← num1 + num2
  ESCREVA("Soma = ", soma)
Linha por linha:
ALGORITMO ... →  Define o nome do algoritmo
VAR →  Seção de declaração de variáveis
num1, num2, soma →  Três variáveis do tipo Inteiro
INÍCIO →  Bloco de comandos começa aqui
ESCREVA(...) →  Exibe texto na tela (saída)
LEIA(...) →  Lê valor digitado pelo usuário
soma ← ... →  Atribuição: calcula e guarda o resultado
FIM_ALGORITMO →  Fim do programa
💡  O símbolo ← significa atribuição (guarda o valor da direita na variável da esquerda).

===PAGE_BREAK===

Pseudocódigo — Decisão e RepetiçãoExemplos com estruturas SE...ENTÃO e ENQUANTO...FAÇA
💻 Pseudocódigo
// Verificar aprovação do aluno
ALGORITMO VerificaAprovacao
VAR
  nota1, nota2, media : Real
INÍCIO
  ESCREVA("Nota 1: ") ; LEIA(nota1)
  ESCREVA("Nota 2: ") ; LEIA(nota2)
  media ← (nota1 + nota2) / 2
  SE media >= 6 ENTÃO
    ESCREVA("APROVADO ✓")
  SENÃO
    ESCREVA("REPROVADO ✗")
  FIM_SE
FIM_ALGORITMO
// Contar de 1 a 5
ALGORITMO ContadorSimples
VAR
  contador : Inteiro
INÍCIO
  contador ← 1
  ENQUANTO contador <= 5 FAÇA
    ESCREVA("Número: ", contador)
    contador ← contador + 1
  FIM_ENQUANTO
  ESCREVA("Fim da contagem!")
FIM_ALGORITMO
// Saída: 1  2  3  4  5

===PAGE_BREAK===

Pseudocódigo — 
Exemplo Completo: 
Cálculo de IMC
Algoritmo com leitura, cálculo e múltiplas decisões
ALGORITMO CalculaIMC
VAR
  peso, altura, imc : Real
INÍCIO
  ESCREVA("Peso (kg): ") ; LEIA(peso)
  ESCREVA("Altura (m): ") ; LEIA(altura)
  imc ← peso / (altura * altura)
  ESCREVA("IMC = ", imc)
  SE imc < 18.5 ENTÃO
    ESCREVA("Abaixo do peso")
  SENÃO SE imc <= 24.9 ENTÃO
    ESCREVA("Peso normal")
  SENÃO SE imc <= 29.9 ENTÃO
    ESCREVA("Sobrepeso")
  SENÃO
Classificação do IMC
< 18,5 Abaixo do peso
18,5 – 24,9Peso normal
25,0 – 29,9Sobrepeso
≥ 30,0 Obesidade
🧪  Teste: peso=70, altura=1.75 → IMC ≈ 22.9 (Peso normal)
    ESCREVA(“Obesidade")
  FIM_SE
  FIM_ALGORITMO

===PAGE_BREAK===

Fluxograma: Representação Visual
Símbolos e exemplo prático
LEGENDA
Início / Fim
Processo / Ação
Decisão (SE)
Entrada / Saída
Exemplo: Aluno aprovado ou reprovado?
INÍCIO
média ≥ 6?
SIM
APROVADO
NÃO
REPROVADO
FIM
media >= 6,0
media = (nota1 + nota2)/2
LEIA nota1, nota2

===PAGE_BREAK===

Variáveis e Tipos de Dados
Os recipientes onde guardamos informações
🗄  Variável = uma 'caixinha' na memória 
com nome e tipo
123
Inteiro
Números sem casas decimais
idade: Inteiro 
idade ← 25
1.5
Real
Números com casas decimais
preco: Real 
preco ← 49.99
Aa
Texto
Cadeia de caracteres (string)
nome: Texto 
nome ← 'João'
T/F
Lógico
Verdadeiro ou Falso (booleano)
ativo: Lógico 
ativo ← VERDADEIRO
💡  Atribuição: use o símbolo ← para guardar um valor em uma 
variável

===PAGE_BREAK===

Estruturas de Controle
Tomando decisões e repetindo ações
🔀  Estrutura de Decisão (SE...ENTÃO)
SE temperatura > 30 ENTÃO
  ESCREVA "Está muito quente!"
  ESCREVA "Use protetor solar"
SENÃO SE temperatura > 20 ENTÃO
  ESCREVA "Temperatura agradável"
SENÃO
  ESCREVA "Está frio! Vista um casaco"
FIM_SE
🔁  Estrutura de Repetição (ENQUANTO)
contador ← 1
ENQUANTO contador <= 5 FAÇA
  ESCREVA 'Número: ', contador
  contador ← contador + 1
FIM_ENQUANTO
// Saída:
// Número: 1
// Número: 2  ... até 5

===PAGE_BREAK===

Boas Práticas ao Criar Algoritmos
Dicas para escrever algoritmos claros e eficientes
01
Entenda o problema antes de codificar
Leia o enunciado com atenção. Identifique entradas, saídas 
e restrições.
02
Divida em partes menores
Problemas grandes ficam simples quando decompostos em 
subproblemas.
03
Use nomes descritivos
Prefira 'mediaAluno' em vez de 'x'. Código legível = 
algoritmo claro.
04
Teste com exemplos simples
Simule seu algoritmo manualmente antes de programar. 
Previne erros.
05
Sempre valide as entradas
Verifique se os dados recebidos estão no formato e 
intervalo esperados.
06
Revise e otimize
Um algoritmo correto pode ser melhorado para ser mais 
rápido ou simples.

===PAGE_BREAK===

Exercício Proposto
Pratique criando seu próprio algoritmo
🏆  Leia três números e informe o maior
• Leia três números inteiros do usuário 
• Verificar qual o maior deles 
• Exiba o maior na tela
💡  Dicas para resolver:
1.Uitliza uma variável auxiliar chamada maior, onde está será utilizada para armazenar o maior valor

===PAGE_BREAK===

📝 ATIVIDADE PRÁTICA
Homework — Escrevendo Algoritmos
📌 Tarefa: Escreva um algoritmo para servir como manual de instruções de alguma tarefa relativamente simples. Deve ter 10-20 
passos. Suponha que está escrevendo para alguém que NUNCA realizou a tarefa.
💡 Sugestões de tarefas:
🍳Fritar um ovo
Descrição passo a passo desde pegar a 
frigideira
🦷Escovar os dentes
Detalhe cada movimento e quanto 
tempo cada etapa
🚌Pegar um ônibus
Do ponto de parada até chegar ao 
destino
�
�
Enviar um email
Abrir o app, escrever, destinatário, enviar
 🛒Fazer compras
Lista, supermercado, escolha dos 
produtos, caixa
🎮Ligar um videogame
TV, cabo, controle, jogo, menu inicial
📋 Critérios de avaliação:
✓ 10-20 passos claros ✓ Ordem lógica e correta ✓ Passos específicos e executáveis ✓ Alguém sem experiência consegue 
seguir