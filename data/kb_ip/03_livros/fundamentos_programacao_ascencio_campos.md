---
tipo: livro_referencia_podado
etapa: 1
linguagem: pseudo_algoritmo_pascal_c_java
fonte: docs/materiais_kb/livros_referencia/Fundamentos_da_PROGRAMACAO_de.pdf
autor_original: Ana Fernanda Gomes Ascêncio, Edilene A. V. de Campos
data_processamento: 2026-07-04
status: podado_para_disciplina
capitulos_incluidos: [1, 3, 4, 5, 6, 7, 8]
capitulos_pulados_e_por_que: |
  - 2 (Paradigmas): puramente teórico/enquadramento, não usado nas aulas do Prof.
  - 9 (Strings C/C++/Java/Pascal): a disciplina UFCAT usa strings em Python (Cap 8 do Pense Python)
  - 10 (Registros/structs): não está no escopo de IP
  - 11 (Arquivos em PASCAL/C/Java): usamos arquivos em Python (Cap 14 do Pense Python)
  - 12 (POO): fora da disciplina IP
  - 13 (Desafios mistos): capítulo-exercícios misturados, conteúdo já coberto pelas listas do Prof.
observacao: |
  O livro é focado em PASCAL/C/Java, mas as seções iniciais de cada capítulo
  mostram o algoritmo em Portugol/pseudocódigo. Isso é valioso pra Etapa 1.
  Para resolver exercícios, o aluno vai recorrer mais à versão Portugol do
  que à PASCAL/C/Java — extraído mantém essas 3 linguagens por capítulo.
---

=== INTRODUÇÃO (capa + sumário + prefácio) ===

---

Fundamentos da
PROGRAMAÇÃO de
COMPUTADORES
ALGORITMOS, PASCAL, C/C++ (PADRÃO ANSI) E JAVA
3ª edição

---

Fundamentos da
PROGRAMAÇÃO de
COMPUTADORES
ALGORITMOS, PASCAL, C/C++ (PADRÃO ANSI) E JAVA
3ª edição
Ana Fernanda Gomes Ascencio
Edilene Aparecida Veneruchi de Campos
São Paulo
Brasil   Argentina   Colômbia   Costa Rica   Chile   Espanha
Guatemala   México   Peru   Porto Rico   Venezuela

---

©2012 by Ana Fernanda Gomes Ascencio e Edilene Aparecida Veneruchi.
Todos os direitos reservados. Nenhuma parte desta publicação poderá ser reproduzida ou transmitida 
de qualquer modo ou por qualquer outro meio, eletrônico ou mecânico, incluindo fotocópia, 
gravação ou qualquer outro tipo de sistema de armazenamento e transmissão de informação, 
sem prévia autorização, por escrito, da Pearson Education do Brasil.
Diretor editorial: Roger Trimer
Gerente editorial: Sabrina Cairo
Editor de aquisição: Brunno Barreto
Coordenadora de produção editorial: Thelma Babaoka
Editora de texto: Sabrina Levensteinas
Preparação: Maria Alice da Costa
Revisão: Luciane Gomide
Capa: Alexandre Mieda
Diagramação: Globaltec Editorial & Marketing
Dados Internacionais de Catalogação na Publicação (CIP)
(Câmara Brasileira do Livro, SP, Brasil)
Ascencio, Ana Fernanda Gomes
Fundamentos da programação de computadores : algoritmos, 
PASCAL , C/C++ (padrão ANSI) e J AVA / Ana Fernanda Gomes 
Ascencio e Edilene Aparecida Veneruchi de Campos . -- 3. ed. -- São 
Paulo : Pearson Education do Brasil, 2012.
Bibliografia
ISBN 978-85-64574-16-8
1. Algoritmos 2. Programação (Computadores eletrônicos) I. 
Campos, Edilene Aparecida Veneruchi de. II. Título.
11-11938 CDD-005.1
Índices para catálogo sistemático:
1. Computadores : Programação 005.1
2. Programação de computadores : 
Processamento de dados 005.1
1a reimpressão – janeiro 2013
Direitos exclusivos para a língua portuguesa cedidos à
Pearson Education do Brasil Ltda.,
uma empresa do grupo Pearson Education
Rua Nelson Francisco, 26
CEP 02712-100 – São Paulo – SP – Brasil
Fone: 11 2178-8686 – Fax: 11 2178-8688
e-mail: vendas@pearson.com
3a reimpressão – janeiro 2014
   Direitos exclusivos para a língua portuguesa cedidos à
Pearson Education do Brasil Ltda.,
uma empresa do grupo Pearson Education
Rua Nelson Francisco, 26
CEP 02712-100 – São Paulo – SP – Brasil
Fone: (11) 2178-8686 – Fax: (11) 2178-8688
vendas@pearson.com

---

Aos meus ﬁlhos, Eduardo e Pedro, amores eternos.
Ana Fernanda Gomes Ascencio
À família maravilhosa que consegui construir:  
Vanderlei, Yanko e Juliana.
Edilene A.Veneruchi de Campos

---

Capítulo 1
Conceitos básicos ..........................................................................................................................................1
1.1 Conceito de algoritmo  .............................................................................................................1
1.2 Método para a construção de algoritmos ................................................................................3
1.3 Tipos de algoritmos  .................................................................................................................3
1.4 Exemplos de algoritmos ..........................................................................................................4
1.5 Conceito de variável ................................................................................................................7
1.6 Tipos de dados ........................................................................................................................8
1.7 Formação de identiﬁcadores  ................................................................................................... 9
1.8 Exemplos de identiﬁcadores  .................................................................................................10
1.9 Linguagem PASCAL ..............................................................................................................10
1.10 Linguagem C/C++ ...............................................................................................................10
1.11 Linguagem JAVA ................................................................................................................11
Capítulo 2
Paradigmas de programação ....................................................................................................................12
Capítulo
 3
Estrutura sequencial ...................................................................................................................................19
3.1 Estrutura sequencial em algoritmos  ....................................................................................19
3.2 Estrutura sequencial em PASCAL ........................................................................................20
3.3 Estrutura sequencial em C/C++  ..........................................................................................25
3.4 Estrutura sequencial em JAVA  ............................................................................................31
Capítulo 4
Estrutura condicional ..................................................................................................................................53
4.1 Estrutura condicional em algoritmos  ...................................................................................53
4.2 Estrutura condicional em PASCAL  ......................................................................................54
4.3 Estrutura condicional em C/C++  .........................................................................................56
4.4 Estrutura condicional em JAVA  ..........................................................................................58
00010000000000010100011011000001001011000100010000000000010100011011000001001011
0001000100000000000101000110110000010010110001000100000000000101000110110000010
0101100010001000000000001010001101100000100101100010001000000000001010001101100
0001001011000100010000000000010100011011000001001011000100010000000000010100011
0110000010010110001000100000000000101000110110000010010110001000100000000000101
0001101100000100101100010001000000000001010001101100000100101100010001000000000
0010100011011000001001011000100010000000000010100011011000001001011000100010000
0000000101000110110000010010110001000100000000000101000110110000010010110001000
1000000000001010001101100000100101100010001000000000001010001101100000100101100
01000100000000000101000110110000010010110001000100000000000101000110110000010010
11000100010000000000010100011011000001001011000100010000000000010100011011000001
00101100010010110001000100000000001010001101100000100101100010010110001000100000
00000010100011011000001100010010110001000100000000000100010010110001000100000000
Sumário

---

viii | Fundamentos da programação de computadores
Capítulo 5
Estrutura de repetição ............................................................................................................................... 95
5.1 Estrutura de repetição em algoritmo.................................................................................... 95
5.2 Estrutura de repetição em PASCAL  ...................................................................................100
5.3 Estrutura de repetição em C/C++....................................................................................... 105
5.4 Estrutura de repetição em JAVA........................................................................................ 111
Capítulo 6
Vetor.............................................................................................................................................................. 151
6.1 Vetor em algoritmos  ..........................................................................................................151
6.2 Vetor em PASCAL............................................................................................................. 152
6.3 Vetor em C/C++  ................................................................................................................155
6.4 Vetor em JAVA .................................................................................................................156
Capítulo 7
Matriz ............................................................................................................................................................194
7.1 Matriz em algoritmos  ........................................................................................................194
7.2 Matriz em PASCAL  ...........................................................................................................201
7.3 Matriz em C/C++  ..............................................................................................................207
7.4 Matriz em JAVA  ...............................................................................................................212
Capítulo 8
Sub-rotina ....................................................................................................................................................252
8.1 Sub-rotinas (programação modularizada) ......................................................................... 252
8.2 Sub-rotinas em PASCAL (procedures, functions e units) ....................................................255
8.3 Sub-rotinas em C/C++ (funções) ........................................................................................262
8.4 Sub-rotinas em JAVA (métodos)........................................................................................ 271
Capítulo 9
Manipulando cadeias de caracteres .....................................................................................................301
9.1 Manipulando cadeias de caracteres em PASCAL  ...............................................................301
9.2 Manipulando cadeias de caracteres em C/C++................................................................... 304
9.3 Manipulando cadeias de caracteres em JAVA.................................................................... 311
Capítulo 10
Registro ........................................................................................................................................................333
10.1 Deﬁnição  de  registros  ......................................................................................................333
10.2 Declaração de registros em algoritmos  .............................................................................. 333
10.3 Declaração de registros em PASCAL  .................................................................................335
10.4 Declaração  de  registros  em  C/C++  .................................................................................338
10.5 Declaração de registros em JAVA  ......................................................................................342

---

Sumário | ix
Capítulo 11
Arquivo .........................................................................................................................................................418
11.1 Deﬁnição de arquivos em algoritmo  ..................................................................................418
11.2 Trabalhando com arquivos em PASCAL ...........................................................................418
11.3 Trabalhando com arquivos em C/C++  ...............................................................................422
11.4 Trabalhando com arquivos em JAVA ................................................................................434
Capítulo 12
Introdução à programação orientada a objetos ................................................................................468
12.1 Classe ..................................................................................................................................468
12.2 Objeto .................................................................................................................................471
12.3 Encapsulamento  ..................................................................................................................478
12.4 Herança  ..............................................................................................................................483
12.5 Polimorﬁsmo  .......................................................................................................................495
Capítulo 13
Desaﬁos  .......................................................................................................................................................547
13.1 Desaﬁo 1  .............................................................................................................................547
13.2 Desaﬁo 2  .............................................................................................................................548
13.3 Desaﬁo 3  .............................................................................................................................548
13.4 Desaﬁo 4  .............................................................................................................................548
13.5 Desaﬁo 5  .............................................................................................................................549
13.6 Desaﬁo 6  .............................................................................................................................549
13.7 Desaﬁo 7  ............................................................................................................................549
13.8 Desaﬁo 8  .............................................................................................................................550
13.9 Desaﬁo 9  .............................................................................................................................550
13.10 Desaﬁo 10  .........................................................................................................................550
13.11 Desaﬁo 11  .........................................................................................................................551
13.12 Desaﬁo 12  .........................................................................................................................551
13.13 Desaﬁo 13  .........................................................................................................................552
13.14 Desaﬁo 14  .........................................................................................................................552
13.15 Desaﬁo 15  .........................................................................................................................552
13.16 Desaﬁo 16  .........................................................................................................................552
13.17 Desaﬁo 17  .........................................................................................................................553
13.18 Desaﬁo 18  .........................................................................................................................553
13.19 Desaﬁo 19  .........................................................................................................................554
13.20 Desaﬁo 20  .........................................................................................................................554
13.21 Desaﬁo 21  .........................................................................................................................555
13.22 Desaﬁo 22  .........................................................................................................................557

---

x | Fundamentos da programação de computadores
13.23 Desaﬁo 23  .........................................................................................................................558
13.24 Desaﬁo 24  .........................................................................................................................559
13.25 Desaﬁo 25  ........................................................................................................................559
Bibliograﬁa  ..................................................................................................................................................562
Índice remissivo .........................................................................................................................................564

---

00010000000000010100011011000001001011000100010000000000010100011011000001001011
00010001000000000001010001101100000100101100010001000000000001010001101100000100
10110001000100000000000101000110110000010010110001000100000000000101000110110000
0100101100010001000000000001010001101100000100101100010001000000000001010001101
1000001001011000100010000000000010100011011000001001011000100010000000000010100
0110110000010010110001000100000000000101000110110000010010110001000100000000000
1010001101100000100101100010001000000000001010001101100000100101100010001000000
0000010100011011000001001011000100010000000000010100011011000001001011000100010
0000000000101000110110000010010110001000100000000000101000110110000010010110001
00010000000000010100011011000001001011000100010000000000010100011011000001001011
00010001000000000001010001101100000100101100010001000000000001010001101100000100
1011000100101100010001000000000010100011011000001001011000100101100010001000000
0000010100011011000001100010010110001000100000000000100010010110001000100000000
O livro proposto tem como objetivos:
■ apresentar técnicas para a elaboração de algoritmos;
■ apresentar comandos para a implementação de algoritmos nas linguagens P ASCAL, C/C++ e 
JA V A;
■ apresentar a solução de problemas em algoritmos e em programas escritos em PASCAL, C/C++ e 
JAVA;
■ incentivar os leitores à programação por meio da proposição de várias situações-problema ao final 
de cada capítulo.
T odos os capítulos apresentarão nas seções iniciais conceitos teóricos sobre a utilização de algum recur-
so de computação em algoritmos e nas linguagens de programação P ASCAL, C/C++ e JA V A.
A penúltima seção de cada capítulo apresenta uma série de problemas resolvidos em algoritmos, PASCAL, 
C/C++ e também em JAVA, e, na última, o leitor encontrará uma série de problemas para serem resolvidos.
Nesta edição, além da revisão completa da obra, foram acrescentados dois capítulos. O Capítulo 12, 
com uma introdução à programação orientada a objetos, e o Capítulo 13, com vários problemas desafiado-
res, envolvendo o conteúdo discutido em todo o livro.
RELEVÂNCIA, ATUALIDADE E PÚBLICO-ALVO
Durante alguns anos em que ensinamos fundamentos da programação de computadores, temos obser-
vado a grande dificuldade dos alunos em assimilar estes novos conceitos e em adquirir habilidades que lhes 
permitam resolver problemas reais relacionados à programação.
Observamos também que, através da análise aprofundada de problemas já resolvidos, os estudantes 
conseguem superar parte dessas dificuldades, além de adquirirem maior motivação para os estudos.
Esta obra será aproveitada por alunos iniciantes na programação de computadores, visto que as lingua-
gens P ASCAL, C/C++ e JA V A são muito utilizadas no início da programação por serem de fácil compre-
ensão e ótimas para despertar o raciocínio lógico nos alunos.
Esta obra se diferencia das demais por possuir uma grande quantidade de exercícios resolvidos e propos-
tos após cada capítulo, o que possibilita sua utilização em aulas de laboratório, uma prática muito comum 
nas universidades atualmente.
No Companion W ebsite deste livro (www .pearson.com.br/ascencio_campos), professores e alu-
nos obtêm a resolução dos exercícios apresentados em cada capítulo em P ASCAL, C/C++ e JA V A, 
incluindo fontes e executáveis.
000100000000000101000110110000010010110001000100000 00000010100011011000001001011
000100010000000000010100011011000001001011000100010 00000000001010001101100000100
101100010001000000000001010001101100000100101100010 00100000000000101000110110000
010010110001000100000000000101000110110000010010110 0010001000000000001010001101
100000100101100010001000000000001010001101100000100 1011000100010000000000010100
011011000001001011000100010000000000010100011011000 0010010110001000100000000000
101000110110000010010110001000100000000000101000110 1100000100101100010001000000
000001010001101100000100101100010001000000000001010 0011011000001001011000100010
000000000010100011011000001001011000100010000000000 0101000110110000010010110001
000100000000000101000110110000010010110001000100000 00000010100011011000001001011
000100010000000000010100011011000001001011000100010 00000000001010001101100000100
101100010010110001000100000000001010001101100000100 1011000100101100010001000000
000001010001101100000110001001011000100010000000000 0100010010110001000100000000
Apresentação

---

ANA FERNANDA GOMES ASCENCIO é professora universitária desde 1994 na área de informática. É 
graduada em ciência da computação pela Pontifícia Universidade Católica de São Paulo (PUC–SP), especia-
lista em sistemas de informação pela Universidade Federal de São Carlos (UFScar), especialista em educação 
pela Universidade para o Desenvolvimento do Estado e da Região do Pantanal (Uniderp), mestre em ciência 
da computação pela Universidade Federal do Rio Grande do Sul (UFRGS). Autora dos livros Lógica de 
programação com PASCAL, Fundamentos da programação de computadores, Introdução ao desenvolvi -
mento de aplicações em DELPHI, Aplicações das estruturas de dados em DELPHI, Desenvolvimento de 
um sistema usando DELPHI e POSTGRESQL e, recentemente, lançou o livro Estruturas de dados.
EDILENE APARECIDA VENERUCHI DE CAMPOS  é professora universitária desde 1997 na área 
de informática. Bacharel em ciência da computação pela Universidade Federal do Mato Grosso do Sul 
(UFMS), especialista em métodos e técnicas de ensino pela Universidade para o Desenvolvimento do Es -
tado e da Região do Pantanal (Uniderp) e mestre em ciência da computação pela Universidade Federal do 
Rio Grande do Sul (UFRGS). Atualmente é analista de TI da empresa pública DATAPREV, desenvolvendo 
projetos na área de gerenciamento de conteúdo corporativo, e professora da Universidade Anhanguera-Uni-
derp, onde ministra as disciplinas Algoritmos e programação e Linguagem de programação em cursos de 
graduação, e as disciplinas Programação orientada a objetos e Linguagens de programação JAVA em cursos 
de pós-graduação latu sensu, além de coordenar o curso de pós-graduação latu sensu em Desenvolvimento 
de aplicações utilizando tecnologia JAVA.
00010000000000010100011011000001001011000100010000000000010100011011000001001011
00010001000000000001010001101100000100101100010001000000000001010001101100000100
1011000100010000000000010100011011000001001011000100010000000000010100011011000
0010010110001000100000000000101000110110000010010110001000100000000000101000110
1100000100101100010001000000000001010001101100000100101100010001000000000001010
0011011000001001011000100010000000000010100011011000001001011000100010000000000
0101000110110000010010110001000100000000000101000110110000010010110001000100000
0000001010001101100000100101100010001000000000001010001101100000100101100010001
0000000000010100011011000001001011000100010000000000010100011011000001001011000
1000100000000000101000110110000010010110001000100000000000101000110110000010010
11000100010000000000010100011011000001001011000100010000000000010100011011000001
00101100010010110001000100000000001010001101100000100101100010010110001000100000
00000010100011011000001100010010110001000100000000000100010010110001000100000000
Sobre as autoras

---

00010000000000010100011011000001001011000100010000000000010100011011000001001011000100010000
00000001010001101100000100101100010001000000000001010001101100000100101100010001000000000001
01000110110000010010110001000100000000000101000110110000010010110001000100000000000101000110
11000001001011000100010000000000010100011011000001001011000100010000000000010100011011000001
00101100010001000000000001010001101100000100101100010001000000000001010001101100000100101100
01000100000000000101000110110000010010110001000100000000000101000110110000010010110001000100
00000000010100011011000001001011000100010000000000010100011011000001001011000100010000000000
01010001101100000100101100010001000000000001010001101100000100101100010001000000000001010001
10110000010010110001000100000000000101000110110000010010110001000100000000000101000110110000
01001011000100010000000000010100011011000001001011000100101100010001000000000010100011011000
00100101100010010110001000100000000000101000110110000011000100101100010001000000000001000100
10110001000100000000100000000000101000110110000011000100101100010001000000000001000100101100
010001000000001000000000001010001101100000110001001011000100010000000000010001001011000100010000000010000000000
0101000110001000100000000 10000000000010100011011000001100010010110001000100000000000100010010110001000100000000
CAPÍTULO
1
Conceitos 
básicos
Desde o início de sua existência, o homem procurou criar máquinas que o auxiliassem em seu trabalho, 
diminuindo o esforço e economizando tempo. Dentre essas máquinas, o computador vem se mostrando 
uma das mais versáteis, rápidas e seguras.
O computador pode auxiliá-lo em qualquer tarefa. É consciente, trabalhador, possui muita energia, 
mas não tem iniciativa, nenhuma independência, não é criativo nem inteligente, por isso, precisa receber 
instruções nos mínimos detalhes.
A finalidade de um computador é receber, manipular e armazenar dados. Visto somente como um gabi-
nete composto por circuitos eletrônicos, cabos e fontes de alimentação, certamente ele parece não ter nenhu-
ma utilidade. O computador só consegue armazenar dados em discos, imprimir relatórios, gerar gráficos, 
realizar cálculos, entre outras funções, por meio de programas, portanto, sua finalidade principal é realizar 
a tarefa de processamento de dados, isto é, receber dados por um dispositivo de entrada (por exemplo, te -
clado, mouse, scanner etc.), realizar operações com esses dados e gerar uma resposta que será expressa em 
um dispositivo de saída (por exemplo, impressora, monitor de vídeo, entre outros) (ASCENCIO, 1999). 
Logo, um computador possui duas partes diferentes que trabalham juntas: o hardware, composto pelas 
partes físicas, e o software, composto pelos programas.
Quando queremos criar ou desenvolver um software para realizar determinado tipo de processamento 
de dados, devemos escrever um programa ou vários programas interligados. No entanto, para que o com -
putador compreenda e execute esse programa, devemos escrevê-lo usando uma linguagem que tanto o com-
putador quanto o criador de software entendam. Essa linguagem é chamada linguagem de programação.
As etapas para o desenvolvimento de um programa são:
 ■ Análise: estuda-se o enunciado do problema para definir os dados de entrada, o processamento e 
os dados de saída. 
 ■ Algoritmo: ferramentas do tipo descrição narrativa, fluxograma ou português estruturado são uti-
lizadas para descrever o problema com suas soluções. 
 ■ Codificação: o algoritmo é transformado em códigos da linguagem de programação escolhida para 
se trabalhar. 
Portanto, um programa é a codificação de um algoritmo em uma linguagem de programação (ASCEN-
CIO, 1999).
1.1 Conceito de algoritmo 
A seguir, apresentamos alguns conceitos de algoritmos:
“Algoritmo é uma sequência de passos que visa atingir um objetivo bem definido” (FORBELLONE, 1999). 
“Algoritmo é a descrição de uma sequência de passos que deve ser seguida para a realização de uma 
tarefa” (ASCENCIO, 1999).
“Algoritmo é uma sequência finita de instruções ou operações cuja execução, em tempo finito, resolve 
um problema computacional, qualquer que seja sua instância” (SALVETTI, 1999).
“Algoritmos são regras formais para a obtenção de um resultado ou da solução de um problema, en -
globando fórmulas de expressões aritméticas” (MANZANO, 1997).

---

2 | Fundamentos da programação de computadores
“Ação é um acontecimento que, a partir de um estado inicial, após um período de tempo finito, produz 
um estado final previsível e bem definido. Portanto, um algoritmo é a descrição de um conjunto de coman-
dos que, obedecidos, resultam numa sucessão finita de ações” (FARRER, 1999).
Analisando as definições anteriores, podemos perceber que executamos no dia a dia vários algoritmos, 
como se pode observar nos exemplos a seguir.
Algoritmo 1 — Somar três números
Passo 1 — Receber os três números.
Passo 2 — Somar os três números.
Passo 3 — Mostrar o resultado obtido.
Algoritmo 2 — Fazer um sanduíche
Passo 1 — Pegar o pão.
Passo 2 — Cortar o pão ao meio.
Passo 3 — Pegar a maionese.
Passo 4 — Passar a maionese no pão.
Passo 5 — Pegar e cortar alface e tomate.
Passo 6 — Colocar alface e tomate no pão.
Passo 7 — Pegar o hambúrguer.
Passo 8 — Fritar o hambúrguer.
Passo 9 — Colocar o hambúrguer no pão.
Algoritmo 3 — Trocar uma lâmpada
Passo 1 — Pegar uma lâmpada nova.
Passo 2 — Pegar uma escada.
Passo 3 — Posicionar a escada embaixo da lâmpada queimada.
Passo 4 — Subir na escada com a lâmpada nova na mão.
Passo 5 — Retirar a lâmpada queimada.
Passo 6 — Colocar a lâmpada nova.
Passo 7 — Descer da escada.
Passo 8 — Testar o interruptor.
Passo 9 — Guardar a escada.
Passo 10 — Jogar a lâmpada velha no lixo.
Algoritmo 4 — Ir para a escola
Passo 1 — Acordar cedo.
Passo 2 — Ir ao banheiro.
Passo 3 — Abrir o armário para escolher uma roupa.
Passo 4 —  Se o tempo estiver quente, pegar uma camiseta e uma calça jeans; Caso contrário, 
pegar um agasalho e uma calça jeans.
Passo 5 — Vestir a roupa escolhida.
Passo 6 — Tomar café.
Passo 7 — Pegar uma condução.
Passo 8 — Descer próximo à escola.
Algoritmo 5 — Sacar dinheiro no banco 24 horas
Passo 1 — Ir até um banco 24 horas.
Passo 2 — Colocar o cartão.
Passo 3 — Digitar a senha.
Passo 4 — Solicitar a quantia desejada.
Passo 5 —  Se o saldo for maior ou igual à quantia desejada, sacar; caso contrário, mostrar 
mensagem de impossibilidade de saque.
Passo 6 — Retirar o cartão.
Passo 7 — Sair do banco 24 horas.

---

Capítulo 1 Conceitos básicos  | 3
Observação
Você pode estar pensando: “Mas eu realizo essas atividades de maneira diferente!”. Esse pensamen-
to está correto, pois, às vezes, um problema pode ser resolvido de diversas maneiras, porém, gerando a 
mesma resposta. Ou seja, podem existir vários algoritmos para solucionar o mesmo problema.
1.2 Método para a construção de algoritmos
Para a construção de qualquer tipo de algoritmo, é necessário seguir estes passos:
 ■ Compreender completamente o problema a ser resolvido, destacando os pontos mais importantes 
e os objetos que o compõem. 
 ■ Definir os dados de entrada, ou seja, quais dados serão fornecidos e quais objetos fazem parte desse 
cenário problema. 
 ■ Definir o processamento, ou seja, quais cálculos serão efetuados e quais as restrições para esses cál-
culos. O processamento é responsável pela transformação dos dados de entrada em dados de saída. 
Além disso, deve-se verificar quais objetos são responsáveis pelas atividades. 
 ■ Definir os dados de saída, ou seja, quais dados serão gerados depois do processamento. 
 ■ Construir o algoritmo utilizando um dos tipos descritos na próxima seção. 
 ■ Testar o algoritmo realizando simulações. 
1.3 Tipos de algoritmos
Os três tipos mais utilizados de algoritmos são: descrição narrativa, fluxograma e pseudocódigo ou 
portugol, que descrevemos a seguir.
1.3.1 Descrição narrativa
A descrição narrativa consiste em analisar o enunciado do problema e escrever, utilizando uma lingua-
gem natural (por exemplo, a língua portuguesa), os passos a serem seguidos para sua resolução.
Vantagem: não é necessário aprender nenhum conceito novo, pois uma língua natural, neste ponto, já 
é bem conhecida.
Desvantagem: a língua natural abre espaço para várias interpretações, o que posteriormente dificultará 
a transcrição desse algoritmo para programa.
1.3.2 Fluxograma
O fluxograma consiste em analisar o enunciado do problema e escrever, utilizando símbolos gráficos 
predefinidos (Tabela 1.1), os passos a serem seguidos para sua resolução.
Vantagem: o entendimento de elementos gráficos é mais simples que o entendimento de textos. 
Desvantagem: é necessário aprender a simbologia dos fluxogramas e, além disso, o algoritmo resultante 
não apresenta muitos detalhes, dificultando sua transcrição para um programa.
1.3.3 Pseudocódigo ou portugol
O pseudocódigo ou portugol consiste em analisar o enunciado do problema e escrever, por meio de 
regras predefinidas, os passos a serem seguidos para sua resolução.
Vantagem: a passagem do algoritmo para qualquer linguagem de programação é quase imediata, bas -
tando conhecer as palavras reservadas da linguagem que será utilizada.
Desvantagem: é necessário aprender as regras do pseudocódigo, que serão apresentadas nos próximos 
capítulos.

---

4 | Fundamentos da programação de computadores
1.4 Exemplos de algoritmos
Os exemplos a seguir mostram alguns algoritmos desenvolvidos com os três tipos citados anteriormente.
a) Faça um algoritmo para mostrar o resultado da multiplicação de dois números.
Algoritmo em descrição narrativa:
Passo 1 —  Receber dois números que serão multiplicados.
Passo 2 —  Multiplicar os números.
Passo 3 —  Mostrar o resultado obtido na multiplicação.
Algoritmo em fluxograma:
INÍCIO
N1, N2
M = N1 * N2
M FIM
Algoritmo em pseudocódigo:
ALGORITMO
DECLARE N1, N2, M NUMÉRICO
ESCREVA “Digite dois números”
LEIA N1, N2
M ← N1 * N2
ESCREVA “Multiplicação = “, M
FIM_ALGORITMO.
Tabela 1.1 Conjunto de símbolos utilizados no ﬂuxograma.
Símbolo utilizado para indicar o início e o ﬁm do algoritmo.
Símbolo que permite indicar o sentido do ﬂuxo de dados. Serve exclusivamente 
para conectar os símbolos ou blocos existentes.
Símbolo utilizado para indicar cálculos e atribuições de valores.
Símbolo utilizado para representar a entrada de dados.
Símbolo utilizado para representar a saída de dados.
Símbolo utilizado para indicar que deve ser tomada uma decisão, apontando a 
possibilidade de desvios.

---

Capítulo 1 Conceitos básicos  | 5
b) Faça um algoritmo para mostrar o resultado da divisão de dois números.
Algoritmo em descrição narrativa:
Passo 1 — Receber os dois números que serão divididos.
Passo 2 —  Se o segundo número for igual a zero, não poderá ser feita a divisão, pois não existe 
divisão por zero; caso contrário, dividir os números e mostrar o resultado da divisão.
Algoritmo em fluxograma:
INÍCIO
N1, N2
D
FIM
N2 = 0 NÃO
SIM
D = N1/N2
IMPOSSÍVEL 
DIVIDIR
Algoritmo em pseudocódigo:
ALGORITMO
DECLARE N1, N2, D NUMÉRICO
ESCREVA “Digite dois números”
LEIA N1, N2
SE N2 = 0
ENTÃO ESCREVA “Impossível dividir”
SENÃO INÍCIO
  D ← N1/N2
  ESCREVA “Divisão = “, D
      FIM
FIM_ALGORITMO.
c) Faça um algoritmo para calcular a média aritmética entre duas notas de um aluno e mostrar sua situa -
ção, que pode ser aprovado ou reprovado. 
Algoritmo em descrição narrativa:
Passo 1 — Receber as duas notas.
Passo 2 — Calcular a média aritmética.
Passo 3 — Mostrar a média aritmética.
Passo 4 —  Se a média aritmética for maior ou igual a 7, então a situação do aluno é aprovado; caso 
contrário, a situação é reprovado.

---

6 | Fundamentos da programação de computadores
Algoritmo em fluxograma:
M = (N1+N2)/2
NÃOSIM
FIM
M ≥ 7
N1, N2INÍCIO
M
APROVADO REPROVADO
Algoritmo em pseudocódigo:
ALGORITMO
DECLARE N1, N2, M NUMÉRICO
ESCREVA “Digite as duas notas”
LEIA N1, N2
M ← (N1 + N2)/2
ESCREVA “Média =”, M
SE M ≥ 7
ENTÃO ESCREVA “Aprovado”
SENÃO ESCREVA “Reprovado”
FIM_ALGORITMO.
d) Faça um algoritmo para calcular o novo salário de um funcionário. Sabe-se que os funcionários que 
recebem atualmente salário de até R$ 500 terão aumento de 20%; os demais terão aumento de 10%. 
Algoritmo em descrição narrativa:
Passo 1 — Receber o salário atual do funcionário.
Passo 2 —  Se o salário atual do funcionário for de até R$ 500, calcular o novo salário com per -
centual de aumento de 20%; caso contrário, calcular o novo salário com percentual 
de aumento de 10%.

---

Capítulo 1 Conceitos básicos  | 7
Algoritmo em fluxograma:
FIM
SAL_ATUAL
≤
500
NOVO_SAL =
SAL_ATUAL * 1,20
NOVO_SAL =
SAL_ATUAL * 1,10
NÃOSIM
SAL_ATUAL
INÍCIO
NOVO_SAL NOVO_SAL
Algoritmo em pseudocódigo:
ALGORITMO
DECLARE SAL_ATUAL, NOVO_SAL NUMÉRICO
ESCREVA “Digite o salário atual do funcionário” 
LEIA SAL_ATUAL
SE SAL_ATUAL ≤ 500
ENTÃO NOVO_SAL ← SAL_ATUAL * 1,20
SENÃO NOVO_SAL ← SAL_ATUAL * 1,10 
ESCREVA “Novo salário =”, NOVO_SAL 
FIM_ALGORITMO.
1.5 Conceito de variável
Duas pessoas estão conversando e precisam realizar uma conta. A primeira pessoa diz: “Vamos so -
mar dois números”. E continua: “O primeiro número é 5”. A segunda pessoa guarda o primeiro número 
na cabeça, ou seja, na memória. A primeira pessoa diz: “O segundo número é 3”. A segunda pessoa 
também guarda o segundo número na cabeça, sem esquecer o primeiro número, ou seja, cada número foi 
armazenado em posições diferentes da memória humana, sem sobreposição. A primeira pessoa pergunta: 
“Qual é o resultado da soma?” A segunda pessoa resgata os valores armazenados na memória, realiza a 
conta e responde dizendo que o resultado é 8.
Um algoritmo e, posteriormente, um programa recebem dados que precisam ser armazenados no com-
putador para serem utilizados no processamento. Esse armazenamento é feito na memória. Todos os com-
putadores trabalham com sistema numérico binário e, nesse sistema, os dados são transformados em 0 e 
1 (‘zeros’ e ‘uns’) para, então, serem armazenados na memória. Cada dígito binário (0 ou 1) ocupa uma 
porção de memória chamada bit, e um conjunto de 8 bits é denominado byte. Cada byte é identificado e 
acessado por meio de um endereço.
Todos os caracteres existentes possuem um correspondente numérico na tabela ASCII, transformado 
em caractere binário pelo método da divisão para, então, ser armazenado na memória. Dessa maneira, uma 
variável representa uma posição de memória, que possui nome e tipo e seu conteúdo pode variar ao longo 
do tempo, durante a execução de um programa. Embora uma variável possa assumir diferentes valores, ela 
só pode armazenar um valor a cada instante.

---

8 | Fundamentos da programação de computadores
A seguir, um pedaço da tabela ASCII:
Tabela 1.2 Amostra da tabela ASCII.
Caractere Valor decimal na tabela ASCII Valor binário
A 65 01000001
B 66 01000010
C 67 01000011
Exemplo de transformação em binário:
F = 70
70
0
35
1
17
1
8
0
4
0
2
0 1
F = 70 = 01000110
2
2
2
2
2
2
Todo computador possui uma tabela de alocação que contém o nome da variável, seu tipo (para saber 
quantos bytes ocupará) e seu endereço inicial de armazenamento. Dessa maneira, quando queremos buscar 
algum dado na memória, basta sabermos o nome da variável, que o computador, por meio da tabela de 
alocação, busca automaticamente.
1.6 Tipos de dados
Os tipos de dados mais utilizados são: numéricos, lógicos e literais ou caracteres, que descreveremos a 
seguir.
1.6.1 Numéricos
Os dados numéricos dividem-se em dois grupos: inteiros e reais.
Os números inteiros podem ser positivos ou negativos e não possuem parte fracionária. Exemplos de 
dados numéricos inteiros:
–23 
98 
0 
–357 
237 
–2

---

Capítulo 1 Conceitos básicos  | 9
Os números reais podem ser positivos ou negativos e possuem parte fracionária. Exemplos de dados 
numéricos reais:
23.45
346.89 
–34.88 
0.0 
–247.0
Observação
Os números reais seguem a notação da língua inglesa, ou seja, a parte decimal é separada da parte 
inteira por um ponto, e não por uma vírgula.
1.6.2 Lógicos
São também chamados dados booleanos (oriundos da álgebra de Boole) e podem assumir os valores 
verdadeiro ou falso.
1.6.3 Literais ou caracteres
São dados formados por um único caractere ou por uma cadeia de caracteres. Esses caracteres po -
dem ser as letras maiúsculas, as letras minúsculas, os números (não podem ser usados para cálculos) e os 
caracteres especiais (&, #, @, ?, +).
Exemplos de dados literais:
“aluno” 
“1234”
“@ internet” 
“0.34”
“1 + 2”
‘A’
‘3’
Observação
Um caractere é representado entre apóstrofos e um conjunto de caracteres é representado entre aspas.
1.7 Formação de identiﬁcadores
Os identificadores são os nomes das variáveis, dos programas, das constantes, das rotinas, das unidades 
etc. As regras básicas para a formação dos identificadores são:
 ■ Os caracteres permitidos são: os números, as letras maiúsculas, as letras minúsculas e o caractere 
sublinhado. 
 ■ O primeiro caractere deve ser sempre uma letra ou o caractere sublinhado. 
 ■ Não são permitidos espaços em branco e caracteres especiais (@, $, +, –, %, !). 
 ■ Não podemos usar as palavras reservadas nos identificadores, ou seja, palavras que pertençam à 
linguagem de programação.

---

10 | Fundamentos da programação de computadores
1.8 Exemplos de identiﬁcadores 
Exemplos de identificadores válidos:
A
a
nota
NOTA
X5
A32
NOTA1
MATRICULA
nota_1
dia
IDADE
Exemplos de identificadores inválidos:
5b — por começar com número;
e 12 — por conter espaço em branco; 
x-y — por conter o caractere especial – ; 
prova 2n — por conter espaço em branco;
nota(2) — por conter os caracteres especiais (); 
case — por ser palavra reservada;
SET — por ser palavra reservada.
1.9 Linguagem PASCAL
A linguagem PASCAL foi desenvolvida em 1968 por Niklaus Wirth, na Suíça, destinada principalmente 
à programação científica, mas sua grande evolução permitiu que, nos dias de hoje, seja utilizada para qual-
quer fim. Essa linguagem possui um ambiente integrado de desenvolvimento chamado Turbo Pascal com as 
seguintes características:
 ■ Apresenta um editor que permite ao desenvolvedor digitar, salvar e modificar o código de seus 
programas. 
 ■ Possui um compilador que converte os códigos dos programas em instruções de máquina e verifica 
a existência de erros de sintaxe.
 ■ Dispõe de um depurador que permite inspecionar um programa durante sua execução, facilitando 
a localização de erros. 
 ■ Conta com um sistema de ajuda ativo que oferece diferentes níveis de informação. 
 ■ Possui ainda o ambiente de execução propriamente dito, que permite executar os programas sem 
sair do Turbo Pascal (arquivos de extensão PAS) ou, se preferir, permite gerar arquivos a serem 
executados fora do ambiente do Turbo Pascal (arquivos de extensão EXE). 
1.10 Linguagem C/C++
Segundo Schildt (1996), Dennis Ritchie inventou a linguagem C e foi o primeiro a implementá-la usan-
do um computador DEC PDP-11, que utilizava o sistema operacional Unix. Essa linguagem é resultante 
de um processo evolutivo de linguagens, cujo marco inicial foi uma linguagem chamada BCPL, desenvol -
vida por Martin Richards, que teve forte influência em uma linguagem denominada B, inventada por Ken 
Thompson. Na década de 1970, B levou ao desenvolvimento de C.
Durante alguns anos, o padrão da linguagem C foi aquele fornecido com a versão 5 do sistema opera-
cional Unix, mas, com a popularização dos microcomputadores, várias implementações de C foram criadas,

---

Capítulo 1 Conceitos básicos  | 11
gerando, assim, muitas discrepâncias. Para resolver tal situação, o American National Standards Institute 
(Ansi) estabeleceu, em 1983, um comitê para definir um padrão que guiasse todas as implementações da 
linguagem C.
A linguagem C++ é uma extensão da linguagem C, e as instruções que fazem parte desta última re -
presentam um subconjunto da primeira. Os incrementos encontrados na linguagem C++ foram feitos para 
dar suporte à programação orientada a objetos, e a sintaxe dessa linguagem é basicamente a mesma da 
linguagem C.
1.11 Linguagem JAVA
A tecnologia JAVA é composta pela linguagem de programação JAVA e pela plataforma de desenvolvi-
mento JAVA. Essa linguagem de programação possui como principais características: simplicidade, orienta-
ção a objetos, portabilidade, alta performance e segurança.
Nessa linguagem, os programas são escritos em arquivos texto com a extensão .java e, ao serem compi-
lados com o compilador javac, são gerados os arquivos .class. Um arquivo .class é constituído por bytecodes, 
código interpretado pela Máquina Virtual Java (Java Virtual Machine).
Uma plataforma é um ambiente composto por hardware e software, ou seja, um sistema operacional 
e o hardware com o qual se comunica. A plataforma JAVA, entretanto, é composta apenas por software, 
uma vez que é a Máquina Virtual Java que faz a interface entre os programas e o sistema operacional. A 
plataforma JAVA é composta:
 ■ pela Máquina Virtual Java, responsável por fazer a interface entre seu programa e o sistema opera-
cional, transformando os bytecodes (comuns a qualquer ambiente) em código nativo reconhecido 
pelo hardware; e
 ■ pela Application Programming Interface (API) JAVA, composta por amplo conjunto de classes já im-
plementadas e testadas que fornecem variados recursos aos desenvolvedores. 
Figura 1.1 Processo de execução de um programa em JAVA.
MeuProg.java MeuProg.class
Código nativo
Compilador
javac
Máquina
Virtual Java

---

00010000000000010100011011000001001011000100010000000000010100011011000001001011000100010000
00000001010001101100000100101100010001000000000001010001101100000100101100010001000000000001
01000110110000010010110001000100000000000101000110110000010010110001000100000000000101000110
11000001001011000100010000000000010100011011000001001011000100010000000000010100011011000001
00101100010001000000000001010001101100000100101100010001000000000001010001101100000100101100
01000100000000000101000110110000010010110001000100000000000101000110110000010010110001000100
00000000010100011011000001001011000100010000000000010100011011000001001011000100010000000000
01010001101100000100101100010001000000000001010001101100000100101100010001000000000001010001
10110000010010110001000100000000000101000110110000010010110001000100000000000101000110110000
01001011000100010000000000010100011011000001001011000100101100010001000000000010100011011000
00100101100010010110001000100000000000101000110110000011000100101100010001000000000001000100
10110001000100000000100000000000101000110110000011000100101100010001000000000001000100101100
010001000000001000000000001010001101100000110001001011000100010000000000010001001011000100010000000010000000000
0101000110001000100000000 10000000000010100011011000001100010010110001000100000000000100010010110001000100000000
CAPÍTULO
2
Paradigmas de 
programação
Um paradigma de programação está intimamente relacionado à forma de pensar do programador e 
como ele busca a solução para os problemas. É o paradigma que permite ou proíbe a utilização de algumas 
técnicas de programação. Ele é capaz, ainda, de mostrar como o programador analisou e abstraiu o proble-
ma a resolver. Existem vários paradigmas de programação: estruturado, orientado a objetos, lógico, fun -
cional, dentre outros. Vamos analisar com mais detalhe os paradigmas estruturado e orientado a objetos.
Pelo paradigma estruturado (também conhecido como imperativo ou procedural), qualquer problema 
pode ser quebrado em problemas menores, de mais fácil solução, chamados de sub-rotinas ou funções. 
Cada sub-rotina ou função pode receber valores de entrada, submetê-los a um processo capaz de gerar um 
valor de saída para quem fez uso da sub-rotina ou função. O paradigma estruturado preconiza, ainda, que 
todo processamento pode ser realizado pelo uso de três tipos de estrutura: sequencial, condicional e itera -
tiva (de repetição). 
Já o paradigma orientado a objetos compreende o problema como uma coleção de objetos interagindo 
por meio de trocas de mensagem. Os objetos são estruturas de dados contendo estado (dados) e comporta-
mento (lógica). Dessa maneira, um conjunto de objetos com informações comuns e com o mesmo compor-
tamento dá origem a uma classe.
Além disso, um programador que utilize o paradigma estruturado analisa o problema tentando relacio-
nar as ações que deverão ser executadas e como poderão ser subdivididas em módulos. Um programador 
que utilize o paradigma orientado a objetos analisa o mesmo problema tentando identificar os objetos que 
compõem essa realidade e como eles interagem entre si.
É importante destacar que o paradigma de programação está ligado à forma de pensar do programador. 
É possível ver, por exemplo, que o uso de uma linguagem com suporte nativo à orientação a objetos não 
implica, necessariamente, a criação de uma aplicação orientada a objetos. Também, podem-se encontrar 
facilmente soluções não estruturadas, construídas a partir de linguagens de programação com suporte à 
estruturação.
Verificaremos, agora, por meio de um exemplo, a aplicação dos dois paradigmas na resolução de um 
mesmo problema no qual devemos calcular a área e o perímetro de um retângulo. Para isso, deverá existir 
uma interface com o usuário pela qual serão informadas as medidas dos lados do retângulo e visualizado o 
resultado de cada cálculo realizado. Trata-se de um problema simples, mas como resolvê-lo?
Segundo o paradigma estruturado, devemos detalhar as ações necessárias para chegar à resposta dese-
jada. Nesse sentido, devemos:
1. Obter o valor da altura do retângulo.
2. Obter o valor da largura do retângulo.
3. Calcular a área.
4. Calcular o perímetro.
5. Mostrar os cálculos realizados.
Posteriormente, devemos analisar a melhor forma de modularizar a solução. A ideia é que cada módulo 
realize uma tarefa bem específica, maximizando, assim, a possibilidade de ser reutilizado.

---

Capítulo 2 Paradigmas de programação  | 13
Cada módulo poderá receber valores e, também, devolver um valor a quem o solicitou. Nesse exemplo, 
nossa solução será composta por quatro módulos: o principal, pelo qual a execução começará; o calculaA-
rea, responsável por calcular e devolver o valor da área do retângulo; o calculaPerimetro, responsável por 
calcular e devolver o valor do perímetro do retângulo; e o mostrarMensagem, responsável por mandar para 
a interface com o usuário o resultado dos cálculos realizados.
Em PASCAL, usando o paradigma estruturado, a solução ficaria da seguinte forma:
program exemplo;
uses crt;
var altura, largura, area, perimetro: real;
function calculaArea(a, b:real):real;
begin
calculaArea := a * b;
end;
function calculaPerimetro(a, b:real):real;
begin
calculaPerimetro := 2*a + 2*b;
end;
procedure mostraMensagem(msg: string; vlr:real);
begin
writeln(msg, vlr:5:2);
end;
begin
clrscr;
write(‘Digite o valor da altura do retângulo: ‘);
readln(altura);
write(‘Digite o valor da largura do retângulo: ‘);
readln(largura);
area := calculaArea(altura, largura);
perimetro := calculaPerimetro(altura, largura);
mostraMensagem(‘O valor da área ‚ ‘, area);
mostraMensagem(‘O valor do perímetro ‚ ‘, perimetro);
readln;
end.
Em JAVA, usando o paradigma estruturado, a solução ficaria como se segue:
import java.io.*; 
import java.util.*;
class Retangulo {
public static void main(String[] args) {
float altura, largura, area, perimetro; 
Scanner entrada;
entrada = new Scanner(System.in);
System.out.print(“Digite o valor da altura do retângulo: “); 
altura = entrada.nextFloat();
System.out.print(“Digite o valor da largura do retângulo: “); 
largura = entrada.nextFloat();
area = calculaArea(altura, largura);
perimetro = calculaPerimeto(altura, largura);
mostraMensagem(“O valor da área é “, area);
mostraMensagem(“O valor do perímetro é “, perimetro);

---

14 | Fundamentos da programação de computadores
}
public static float calculaArea(float a, float b) {
return a * b;
}
public static float calculaPerimetro(float a, float b) {
return 2 *a + 2* b;
}
public static void mostraMensagem(String msg, float vlr) {
System.out.println(msg+vlr);
}
}
Em C++, fazendo uso do paradigma estruturado, a solução ficaria assim:
#include <stdio.h>
float calculaArea(float a, float b) 
{ return a*b;
}
float calculaPerimetro(float a, float b) 
{ return 2*a + 2*b;
}
void mostraMensagem(char *msg, float vlr)
{ printf(“%s %5.2f”, msg, vlr);
 }
int main()
{ float altura, largura, area, perimetro;
  printf(“Digite o valor da altura do retângulo: “);
  scanf(“%f%*c”, &altura); 
  printf(“Digite o valor da largura do retângulo: “);
  scanf(“%f%*c”, &largura);
  area = calculaArea(altura, largura);
  perimetro = calculaPerimetro(altura, largura);
  mostraMensagem(“O valor da área é “, area);
  mostraMensagem(“O valor do perímetro é “, perimetro);
  return 0;
 }
Mesmo sendo um exemplo bastante simples, pode-se ver que a sub-rotina mostrarMensagem, presente 
nas três versões, é posta em execução por duas vezes, variando-se os parâmetros informados. Isso repre -
senta uma das bases do paradigma estruturado, em que o problema é quebrado em pequenos módulos, 
para aumentar a capacidade de ser reutilizado (ou seja, escreve-se uma vez e utiliza-se quantas vezes forem 
necessárias). 
O paradigma orientado a objetos afirma que a solução de qualquer problema pode ser encontrada por 
meio das seguintes etapas:
1. Procurar por objetos existentes no problema. 
2. Determinar as características e responsabilidades de cada objeto.
3. Estabelecer como ocorrerá a interação entre os objetos identificados. 
Assim, pelo que foi apresentado e analisado no exemplo, observamos a existência de dois objetos: o 
retângulo e a interface com o usuário.
O objeto retângulo tem a obrigação de armazenar e manipular o valor da altura e da largura, além de 
calcular a área e o perímetro.
A janela tem a obrigação de receber os valores iniciais (altura e largura) e enviá-los para o retângulo. 
Depois disso, deve solicitar os valores da área e do perímetro ao objeto retângulo para mostrá-los.

---

Capítulo 2 Paradigmas de programação  | 15
A comunicação entre os objetos janela e retângulo é conhecida como troca de mensagens.
Em PASCAL, usando o paradigma orientado a objetos, a solução ficaria da seguinte forma:
program exemplo;
uses crt;
type retangulo = object
       altura, largura: real;
       procedure Inicializar_altura;
       procedure Inicializar_largura;
       function CalculaArea(alt, lar: real):real;
       function CalculaPerimetro(alt, lar: real):real;
       procedure MostrarMensagem(texto: string; valor:real);
       end;
procedure retangulo.Inicializar_altura;
begin
 writeln(‘Digite o valor da altura do retângulo:’);
 readln(altura);
end;
 
procedure retangulo.Inicializar_largura;
begin
 writeln(‘Digite o valor da largura do retângulo:’);
 readln(largura);
end;
function retangulo.CalculaArea(alt,lar: real):real;
begin
 CalculaArea := alt * lar;
end;
 
function retangulo.CalculaPerimetro(alt,lar: real):real;
begin
 CalculaPerimetro := 2*alt + 2*lar;
end;
 
procedure retangulo.MostrarMensagem(texto: string; valor: real);
begin
 writeln(texto,valor:5:2);
end;
var ret: retangulo; {instanciando um objeto da classe retangulo}
 
begin { programa principal}
 clrscr;
 ret.Inicializar_altura;
 ret.Inicializar_largura;
  ret.MostrarMensagem(‘O valor da área = ‘,ret.CalculaArea(ret.altura, ret.largura));
 ret.MostrarMensagem(‘O valor do perímetro = ‘,ret.CalculaPerimetro( 
  Ê ret.altura,ret.largura));
 readln;
 end.
Em C++, usando o paradigma orientado a objetos, a solução utilizaria dois arquivos: um com a ex -
tensão .hpp, correspondendo à definição da classe Retangulo, e outro correspondendo classe Janela seria 
representado por um arquivo com a extensão .cpp.

---



=== CAPÍTULO 1 ===

---

Capítulo 1 Conceitos básicos  | 3
Observação
Você pode estar pensando: “Mas eu realizo essas atividades de maneira diferente!”. Esse pensamen-
to está correto, pois, às vezes, um problema pode ser resolvido de diversas maneiras, porém, gerando a 
mesma resposta. Ou seja, podem existir vários algoritmos para solucionar o mesmo problema.
1.2 Método para a construção de algoritmos
Para a construção de qualquer tipo de algoritmo, é necessário seguir estes passos:
 ■ Compreender completamente o problema a ser resolvido, destacando os pontos mais importantes 
e os objetos que o compõem. 
 ■ Definir os dados de entrada, ou seja, quais dados serão fornecidos e quais objetos fazem parte desse 
cenário problema. 
 ■ Definir o processamento, ou seja, quais cálculos serão efetuados e quais as restrições para esses cál-
culos. O processamento é responsável pela transformação dos dados de entrada em dados de saída. 
Além disso, deve-se verificar quais objetos são responsáveis pelas atividades. 
 ■ Definir os dados de saída, ou seja, quais dados serão gerados depois do processamento. 
 ■ Construir o algoritmo utilizando um dos tipos descritos na próxima seção. 
 ■ Testar o algoritmo realizando simulações. 
1.3 Tipos de algoritmos
Os três tipos mais utilizados de algoritmos são: descrição narrativa, fluxograma e pseudocódigo ou 
portugol, que descrevemos a seguir.
1.3.1 Descrição narrativa
A descrição narrativa consiste em analisar o enunciado do problema e escrever, utilizando uma lingua-
gem natural (por exemplo, a língua portuguesa), os passos a serem seguidos para sua resolução.
Vantagem: não é necessário aprender nenhum conceito novo, pois uma língua natural, neste ponto, já 
é bem conhecida.
Desvantagem: a língua natural abre espaço para várias interpretações, o que posteriormente dificultará 
a transcrição desse algoritmo para programa.
1.3.2 Fluxograma
O fluxograma consiste em analisar o enunciado do problema e escrever, utilizando símbolos gráficos 
predefinidos (Tabela 1.1), os passos a serem seguidos para sua resolução.
Vantagem: o entendimento de elementos gráficos é mais simples que o entendimento de textos. 
Desvantagem: é necessário aprender a simbologia dos fluxogramas e, além disso, o algoritmo resultante 
não apresenta muitos detalhes, dificultando sua transcrição para um programa.
1.3.3 Pseudocódigo ou portugol
O pseudocódigo ou portugol consiste em analisar o enunciado do problema e escrever, por meio de 
regras predefinidas, os passos a serem seguidos para sua resolução.
Vantagem: a passagem do algoritmo para qualquer linguagem de programação é quase imediata, bas -
tando conhecer as palavras reservadas da linguagem que será utilizada.
Desvantagem: é necessário aprender as regras do pseudocódigo, que serão apresentadas nos próximos 
capítulos.

---

Capítulo 1 Conceitos básicos  | 5
b) Faça um algoritmo para mostrar o resultado da divisão de dois números.
Algoritmo em descrição narrativa:
Passo 1 — Receber os dois números que serão divididos.
Passo 2 —  Se o segundo número for igual a zero, não poderá ser feita a divisão, pois não existe 
divisão por zero; caso contrário, dividir os números e mostrar o resultado da divisão.
Algoritmo em fluxograma:
INÍCIO
N1, N2
D
FIM
N2 = 0 NÃO
SIM
D = N1/N2
IMPOSSÍVEL 
DIVIDIR
Algoritmo em pseudocódigo:
ALGORITMO
DECLARE N1, N2, D NUMÉRICO
ESCREVA “Digite dois números”
LEIA N1, N2
SE N2 = 0
ENTÃO ESCREVA “Impossível dividir”
SENÃO INÍCIO
  D ← N1/N2
  ESCREVA “Divisão = “, D
      FIM
FIM_ALGORITMO.
c) Faça um algoritmo para calcular a média aritmética entre duas notas de um aluno e mostrar sua situa -
ção, que pode ser aprovado ou reprovado. 
Algoritmo em descrição narrativa:
Passo 1 — Receber as duas notas.
Passo 2 — Calcular a média aritmética.
Passo 3 — Mostrar a média aritmética.
Passo 4 —  Se a média aritmética for maior ou igual a 7, então a situação do aluno é aprovado; caso 
contrário, a situação é reprovado.

---

Capítulo 1 Conceitos básicos  | 7
Algoritmo em fluxograma:
FIM
SAL_ATUAL
≤
500
NOVO_SAL =
SAL_ATUAL * 1,20
NOVO_SAL =
SAL_ATUAL * 1,10
NÃOSIM
SAL_ATUAL
INÍCIO
NOVO_SAL NOVO_SAL
Algoritmo em pseudocódigo:
ALGORITMO
DECLARE SAL_ATUAL, NOVO_SAL NUMÉRICO
ESCREVA “Digite o salário atual do funcionário” 
LEIA SAL_ATUAL
SE SAL_ATUAL ≤ 500
ENTÃO NOVO_SAL ← SAL_ATUAL * 1,20
SENÃO NOVO_SAL ← SAL_ATUAL * 1,10 
ESCREVA “Novo salário =”, NOVO_SAL 
FIM_ALGORITMO.
1.5 Conceito de variável
Duas pessoas estão conversando e precisam realizar uma conta. A primeira pessoa diz: “Vamos so -
mar dois números”. E continua: “O primeiro número é 5”. A segunda pessoa guarda o primeiro número 
na cabeça, ou seja, na memória. A primeira pessoa diz: “O segundo número é 3”. A segunda pessoa 
também guarda o segundo número na cabeça, sem esquecer o primeiro número, ou seja, cada número foi 
armazenado em posições diferentes da memória humana, sem sobreposição. A primeira pessoa pergunta: 
“Qual é o resultado da soma?” A segunda pessoa resgata os valores armazenados na memória, realiza a 
conta e responde dizendo que o resultado é 8.
Um algoritmo e, posteriormente, um programa recebem dados que precisam ser armazenados no com-
putador para serem utilizados no processamento. Esse armazenamento é feito na memória. Todos os com-
putadores trabalham com sistema numérico binário e, nesse sistema, os dados são transformados em 0 e 
1 (‘zeros’ e ‘uns’) para, então, serem armazenados na memória. Cada dígito binário (0 ou 1) ocupa uma 
porção de memória chamada bit, e um conjunto de 8 bits é denominado byte. Cada byte é identificado e 
acessado por meio de um endereço.
Todos os caracteres existentes possuem um correspondente numérico na tabela ASCII, transformado 
em caractere binário pelo método da divisão para, então, ser armazenado na memória. Dessa maneira, uma 
variável representa uma posição de memória, que possui nome e tipo e seu conteúdo pode variar ao longo 
do tempo, durante a execução de um programa. Embora uma variável possa assumir diferentes valores, ela 
só pode armazenar um valor a cada instante.

---

Capítulo 1 Conceitos básicos  | 9
Os números reais podem ser positivos ou negativos e possuem parte fracionária. Exemplos de dados 
numéricos reais:
23.45
346.89 
–34.88 
0.0 
–247.0
Observação
Os números reais seguem a notação da língua inglesa, ou seja, a parte decimal é separada da parte 
inteira por um ponto, e não por uma vírgula.
1.6.2 Lógicos
São também chamados dados booleanos (oriundos da álgebra de Boole) e podem assumir os valores 
verdadeiro ou falso.
1.6.3 Literais ou caracteres
São dados formados por um único caractere ou por uma cadeia de caracteres. Esses caracteres po -
dem ser as letras maiúsculas, as letras minúsculas, os números (não podem ser usados para cálculos) e os 
caracteres especiais (&, #, @, ?, +).
Exemplos de dados literais:
“aluno” 
“1234”
“@ internet” 
“0.34”
“1 + 2”
‘A’
‘3’
Observação
Um caractere é representado entre apóstrofos e um conjunto de caracteres é representado entre aspas.
1.7 Formação de identiﬁcadores
Os identificadores são os nomes das variáveis, dos programas, das constantes, das rotinas, das unidades 
etc. As regras básicas para a formação dos identificadores são:
 ■ Os caracteres permitidos são: os números, as letras maiúsculas, as letras minúsculas e o caractere 
sublinhado. 
 ■ O primeiro caractere deve ser sempre uma letra ou o caractere sublinhado. 
 ■ Não são permitidos espaços em branco e caracteres especiais (@, $, +, –, %, !). 
 ■ Não podemos usar as palavras reservadas nos identificadores, ou seja, palavras que pertençam à 
linguagem de programação.

---

Capítulo 1 Conceitos básicos  | 11
gerando, assim, muitas discrepâncias. Para resolver tal situação, o American National Standards Institute 
(Ansi) estabeleceu, em 1983, um comitê para definir um padrão que guiasse todas as implementações da 
linguagem C.
A linguagem C++ é uma extensão da linguagem C, e as instruções que fazem parte desta última re -
presentam um subconjunto da primeira. Os incrementos encontrados na linguagem C++ foram feitos para 
dar suporte à programação orientada a objetos, e a sintaxe dessa linguagem é basicamente a mesma da 
linguagem C.
1.11 Linguagem JAVA
A tecnologia JAVA é composta pela linguagem de programação JAVA e pela plataforma de desenvolvi-
mento JAVA. Essa linguagem de programação possui como principais características: simplicidade, orienta-
ção a objetos, portabilidade, alta performance e segurança.
Nessa linguagem, os programas são escritos em arquivos texto com a extensão .java e, ao serem compi-
lados com o compilador javac, são gerados os arquivos .class. Um arquivo .class é constituído por bytecodes, 
código interpretado pela Máquina Virtual Java (Java Virtual Machine).
Uma plataforma é um ambiente composto por hardware e software, ou seja, um sistema operacional 
e o hardware com o qual se comunica. A plataforma JAVA, entretanto, é composta apenas por software, 
uma vez que é a Máquina Virtual Java que faz a interface entre os programas e o sistema operacional. A 
plataforma JAVA é composta:
 ■ pela Máquina Virtual Java, responsável por fazer a interface entre seu programa e o sistema opera-
cional, transformando os bytecodes (comuns a qualquer ambiente) em código nativo reconhecido 
pelo hardware; e
 ■ pela Application Programming Interface (API) JAVA, composta por amplo conjunto de classes já im-
plementadas e testadas que fornecem variados recursos aos desenvolvedores. 
Figura 1.1 Processo de execução de um programa em JAVA.
MeuProg.java MeuProg.class
Código nativo
Compilador
javac
Máquina
Virtual Java

---



=== CAPÍTULO 3 ===

---

Capítulo 3 Estrutura sequencial  | 21
Palavras reservadas são nomes utilizados pelo compilador para representar comandos, operadores e nomes de 
seções de programas. As palavras reservadas da linguagem PASCAL são:
and goto program
asm if record
array implementation repeat
begin in set
case inherited shl
const inline shr
constructor interface string
destructor label then
div library to
do mod type
downto nil unit
else not until
end object uses
exports of var
file or while
for packed with
function procedure xor
Os tipos de dados mais utilizados na linguagem PASCAL estão descritos na tabela a seguir:
TIPO FAIXA DE VALORES TAMANHO
(aproximado)
shortint –128 a 127 8 bits
integer –32.768 a 32.767 16 bits
longint –2.147.483.648 a 2.147.483.647 32 bits
byte 0 a 255 8 bits
word 0 a 65.535 16 bits
real 2,9 × 10–39  a 1,7 × 1038 (11 a 12 dígitos com sinal) 6 bytes
single 1,5 × 10–45  a 3,4 × 1038 (7 a 8 dígitos com sinal) 4 bytes
double 5,0 × 10–324  a 1,7 × 10308 (15 a 16 dígitos com sinal) 8 bytes
extended 3,4 × 10–4932  a 1,1 × 104932 (19 a 20 dígitos com sinal) 10 bytes
comp –9,2 × 1018 a 9,2 × 1018 (19 a 20 dígitos com sinal) 8 bytes
boolean true ou false 8 bits
wordbool true ou false 16 bits
longbool true ou false 32 bits
bytebool true ou false 8 bits
char 1 caractere qualquer 1 byte
string cadeia de caracteres (no máximo 255) tantos bytes quantos forem os caracteres
3.2.2 Declaração de constantes em PASCAL 
As constantes são declaradas após a palavra CONST e seus valores não podem ser alterados durante a 
execução do programa.
Exemplo:
CONST X = 8;
 Y = 2.8;
 NOME = ‘MARIA’;
 SEXO = ‘m’;
 TESTE = TRUE;

---

Capítulo 3 Estrutura sequencial  | 23
Exemplo:
WRITELN(X);
WRITE(X);
Mostra o valor armazenado na variável X.
WRITELN(‘Conteúdo de Y = ’,Y);
WRITE(‘Conteúdo de Y = ’,Y);
Mostra a mensagem “ Conteúdo de Y = ” e em seguida o valor armazenado na variável Y.
A diferença entre esses comandos é que o comando WRITELN mostra seu conteúdo e passa o cursor para 
a linha de baixo, enquanto o comando WRITE mantém o cursor na mesma linha após mostrar a mensagem.
Exemplo:
WRITE(‘aula ‘);
WRITE(‘fácil‘);
Os comandos dados anteriormente geram a saída a seguir:
aula fácil
WRITELN(‘aula ‘);
WRITE(‘fácil‘);
Os comandos dados anteriormente geram a saída a seguir:
aula 
fácil
Nos comandos de saída, é possível ainda fazer a formatação de variáveis do tipo real, single, double, 
extended e comp. Após o nome da variável, coloca-se :m:n, onde m significa a quantidade de espaços da 
tela e n o número de caracteres gastos com a parte fracionária do número. O ponto, que é o separador de-
cimal, ocupará um caractere do total de caracteres. Os espaços que sobram à esquerda serão preenchidos 
com branco, e, quando faltam espaços, o compilador completa com a necessidade para mostrar o resultado.
Exemplo:
WRITE(X:5:2); 
No exemplo anterior, o conteúdo da variável X ocupará 5 espaços na tela. Dois espaços para a parte 
fracionária, um espaço para o ponto e dois espaços para a parte inteira.
WRITE(X:7:3); 
No exemplo anterior, o conteúdo da variável X ocupará 7 espaços na tela. Três espaços para a parte 
fracionária, um espaço para o ponto e três espaços para a parte inteira.
3.2.6 Comentários em PASCAL 
Os comentários não são interpretados pelo compilador, servem apenas para esclarecer o programa -
dor. Constituem excelentes instrumentos de documentação e devem sempre estar entre {........} ou entre 
(*............*).
3.2.7 Operadores e funções predeﬁnidas em PASCAL 
A linguagem PASCAL possui operadores e funções predefinidas destinados a cálculos matemáticos. 
Alguns são apresentados a seguir.

---

Capítulo 3 Estrutura sequencial  | 25
Por não existir o operador de potenciação, temos:
AB = EXP(B*LN(A))
Exemplo:
34 = exp(4*ln(3))
510 = exp(10*ln(5))
Observação
As funções SIN e COS esperam receber argumentos no formato de radianos; para receber argu-
mentos em graus, siga o próximo exemplo. Na linguagem PASCAL, não existe uma função para 
tangente; assim, utilize seno/cosseno.
Exemplo para o cálculo do seno de um ângulo fornecido em graus e utilizando uma variável 
para o valor de p:
VALORPI := 3.1415;
READLN(X); { X EM GRAUS }
Y := SIN ((VALORPI * X) / 180);
Exemplo para o cálculo do seno de um ângulo fornecido em graus e utilizando a função pi:
READLN(X); { X EM GRAUS }
Y := SIN ((PI * X) / 180);
As prioridades entre os operadores são:
1a) ( )
2a) funções
3a) *, /, DIV, MOD
4a) +, −
Quando se tem uma expressão em que os operadores possuem a mesma prioridade, a expressão 
é resolvida da esquerda para a direita.
Exemplos:
2 + 3 − 4 = 5 − 4 = 1
2 * 4/2 = 8/2 = 4
Observação
3.3 Estrutura sequencial em C/C++ 
#include <nome_da_biblioteca> 
int main()
{
bloco_de_comandos;
return 0;
}
Bibliotecas são arquivos contendo várias funções que podem ser incorporadas aos programas escritos 
em C/C++. A diretiva #include faz o texto contido na biblioteca especificada ser inserido no programa.
A biblioteca stdio.h permite a utilização de diversos comandos de entrada e saída.
É importante salientar que a linguagem C/C++ é sensível a letras maiúsculas e minúsculas, ou seja, 
considera que letras maiúsculas são diferentes de minúsculas (por exemplo, a é diferente de A). Sendo 
assim, todos os comandos devem, obrigatoriamente, ser escritos com letras minúsculas.

---

Capítulo 3 Estrutura sequencial  | 27
Define uma constante com identificador y e valor 4.5.
#define nome “MARIA”
Define uma constante com identificador nome e valor MARIA.
3.3.3 Comando de atribuição em C/C++
O comando de atribuição é utilizado para conceder valores ou operações a variáveis, sendo represen -
tado por = (sinal de igualdade).
Exemplo:
x = 4;
x = x + 2; 
y = 2.5; 
sexo = ‘F’;
Caso seja necessário armazenar uma cadeia de caracteres dentro de uma variável, deve-se utilizar uma 
função para manipulação de caracteres, conforme apresentado a seguir:
strcpy(nome, “João”);
Para que seja possível a utilização da função strcpy, deve-se inserir no programa, por meio da diretiva 
include, a biblioteca string.h. As funções de manipulação de strings serão abordadas no Capítulo 9.
Em C/C++, os caracteres são representados entre apóstrofos ( ‘ ). As cadeias de caracteres devem 
ser representadas entre aspas ( “ ).
Em C/C++, cada comando é finalizado com o sinal de ponto e vírgula.
Em C/C++, a parte inteira e a parte fracionária do número são separadas por um ponto.
Observações
3.3.4 Comando de entrada em C/C++
O comando de entrada é utilizado para receber dados digitados pelo usuário. Os dados recebidos são 
armazenados em variáveis. Um dos comandos de entrada mais utilizados na linguagem C/C++ é o scanf.
Exemplo:
scanf(“%d%*c”,&X);
Um valor inteiro, digitado pelo usuário, será armazenado na variável X.
scanf(“%f%*c”,&Z);
Um valor real, digitado pelo usuário, será armazenado na variável Z.
scanf(“%s%*c”,&NOME);
Um ou mais caracteres, digitados pelo usuário, serão armazenados na variável NOME.
scanf(“%c%*c”,&Y);
Um caractere, digitado pelo usuário, será armazenado na variável Y.
No comando scanf, é necessário indicar o tipo de variável que será lida: %f para variáveis que armaze-
nam números reais; %d para variáveis que armazenam números inteiros; %c para variáveis que armazenam um 
único caractere; e %s para variáveis que armazenam um conjunto de caracteres.

---

Capítulo 3 Estrutura sequencial  | 29
3.3.6 Comentários em C/C++
Comentários são textos que podem ser inseridos em programas com o objetivo de documentá-los. Eles 
não são analisados pelo compilador.
Os comentários podem ocupar uma ou várias linhas, devendo ser inseridos nos programas utilizando-
-se os símbolos /* ....... */ ou //.
Exemplo:
/*
linhas de comentário 
linhas de comentário
*/
A região de comentários é aberta com os símbolos /* e encerrada com os símbolos */.
// comentário 
A região de comentários é aberta com os símbolos // e encerrada automaticamente ao final da linha.
3.3.7 Operadores e funções predeﬁnidas em C/C++
A linguagem C/C++ possui operadores e funções predefinidas destinados a cálculos matemáticos. Al -
guns são apresentados a seguir.
Operador Exemplo Comentário
= x = y O conteúdo da variável Y é atribuído à variável X (A uma variável pode ser atribuído o 
conteúdo de outra, um valor constante ou, ainda, o resultado de uma função).
+ x + y Soma o conteúdo de X e de Y.
− x − y Subtrai o conteúdo de Y do conteúdo de X.
* x * y Multiplica o conteúdo de X pelo conteúdo de Y.
/ x / y
Obtém o quociente da divisão de X por Y.
Se os operandos são inteiros, o resultado da operação será o quociente inteiro da divisão.
Se os operandos são reais, o resultado da operação será a divisão.
Por exemplo:
int z = 5/2; → a variável z receberá o valor 2.
ﬂoat z = 5.0/2.0; → a variável z receberá o valor 2.5.
% x % y Obtém o resto da divisão de X por Y.
O operador % só pode ser utilizado com operandos do tipo inteiro.
Operador Exemplo Comentário
+= x += y Equivale a  X = X + Y.
–= x –= y Equivale a  X = X – Y.
*= x *= y Equivale a  X = X * Y.
/= x /= y Equivale a  X = X / Y.
%= x %= y Equivale a  X = X % Y.
++ x++ Equivale a  X = X + 1.
++ y = ++x Equivale a  X = X + 1 e depois Y = X.
++ y = x++ Equivale a Y = X e depois X = X +1.
––  –– x ––  –– Equivale a X = X – 1.
– – y = – –x Equivale a X = X – 1 e depois Y = X.
– – y = x– – Equivale a Y = X e depois X = X – 1.
Os operadores matemáticos de atribuição são utilizados para representar de maneira sintética uma 
operação aritmética e, posteriormente, uma operação de atribuição. Por exemplo, na tabela anterior o ope-
rador += está sendo usado para realizar a operação x + y  e, posteriormente, atribuir o resultado obtido 
à variável x.

---

Capítulo 3 Estrutura sequencial  | 31
3.4 Estrutura sequencial em JAVA
import nome_do_pacote_das_classes; 
public class nome
{
  public static void main (String args[])
  {
   bloco_de_comandos;
  }
}
Os pacotes de classes são arquivos contendo diferentes classes que possuem vários métodos, ou seja, 
funções, os quais podem ser utilizados nos programas escritos em JAVA. A diretiva import permite que 
o programa reconheça as classes do pacote e, consequentemente, a utilização de seus métodos.
É importante salientar que a linguagem JAVA é sensível a letras maiúsculas e minúsculas, ou seja, 
considera letras maiúsculas diferentes de minúsculas (por exemplo, a é diferente de A). Sendo assim, cada 
comando tem a própria sintaxe, que, às vezes, é somente com letras minúsculas e outras vezes com letras 
maiúsculas e minúsculas.
3.4.1 Declaração de variáveis em JAVA
As variáveis são declaradas após a especificação de seus tipos. Os tipos de dados mais utilizados são: 
int (para números inteiros), float e double (para números reais), char (para um caractere), String (para 
vários caracteres) e boolean (para verdadeiro ou falso).
Exemplo:
float X;
Declara uma variável chamada X em que pode ser armazenado um número real.
double Y, Z;
Declara duas variáveis chamadas Y e Z em que podem ser armazenados dois números reais.
char SEXO;
Declara uma variável chamada SEXO em que pode ser armazenado um caractere.
String NOME;
Declara uma variável chamada NOME em que podem ser armazenados vários caracteres.
A linguagem JAVA possui os tipos primitivos de dados listados a seguir.
Tipo Faixa de valores Tamanho (aproximado)
byte −128 a 127 8 bits
char 0 a 65.535 16 bits
short −32.768 a 32.767 16 bits
int −2.147.483.648 a 2.147.483.647 32 bits
long −9.223.372.036.854.775.808 a  
9.223.372.036.854.775.807 64 bits
float −3.4 × 10−38 a 3.4 × 1038 32 bits
double −1.7 × 10−308 a 1.7 × 10308 64 bits
boolean true ou false indeﬁnido

---

Capítulo 3 Estrutura sequencial  | 33
String nome;
Scanner dado;
dado = new Scanner(System.in);
nome = dado.next();
Um valor literal digitado pelo usuário será armazenado na variável nome.
É importante salientar que todas as entradas são recebidas pela linguagem JAVA como um conjunto 
de caracteres. Assim, esses caracteres deverão ser convertidos por funções de conversão de tipos. Seguem 
algumas dessas funções.
Função Funcionalidade
next() Aguarda uma entrada em formato String com uma única palavra.
nextLine() Aguarda uma entrada em formato String com uma ou várias palavras.
nextInt() Aguarda uma entrada em formato inteiro.
nextByte() Aguarda uma entrada em formato inteiro.
nextLong() Aguarda uma entrada em formato inteiro.
nextFloat() Aguarda uma entrada em formato número fracionário.
nextDouble() Aguarda uma entrada em formato número fracionário.
O tratamento de cadeia de caracteres será mais detalhado no Capítulo 9.
3.4.5 Comando de saída em JAVA
O comando de saída é utilizado para mostrar dados na tela ou na impressora. Os comandos de saída 
mais utilizados na linguagem JAVA são System.out.println e System.out.print.
Exemplo:
System.out.println(X);
Mostra o valor armazenado na variável X.
System.out.println(“Conteúdo de X = ”  + X);
Mostra a mensagem “ Conteúdo de X = ” e, em seguida, o valor armazenado na variável X.
A diferença entre esses comandos é que o comando System.out.println mostra seu conteúdo e passa 
o cursor para a linha de baixo, enquanto o comando System.out.print mantém o cursor na mesma linha 
após mostrar a mensagem.
Exemplo:
System.out.print(“aula “);
System.out.print(“fácil”);
Os comandos dados anteriormente geram a saída a seguir:
aula fácil
System.out.println(“aula “);
System.out.println(“fácil”);
Os comandos dados anteriormente geram a saída a seguir:
aula 
fácil
3.4.6 Comentários em JAVA
Comentários são textos que podem ser inseridos em programas com o objetivo de documentá-los. Eles 
são ignorados pelo interpretador.
Os comentários podem ocupar uma ou várias linhas, devendo ser inseridos nos programas utilizando-
-se os símbolos /* ....... */ ou //.

---

Capítulo 3 Estrutura sequencial  | 35
Funções matemáticas
Função Exemplo Comentário
ceil Math.ceil(X) Arredonda um número real para cima. Por exemplo, ceil(3.2) é 4.
cos Math.cos(X) Calcula o cosseno de X (X deve estar representado em radianos).
exp Math.exp(X) Obtém o logaritmo natural e elevado à potência X.
abs Math.abs(X) Obtém o valor absoluto de X.
floor Math.floor(X) Arredonda um número real para baixo. Por exemplo, ﬂoor(3.2) é 3.
log Math.log(X) Obtém o logaritmo natural de X.
log10 Math.log10(X) Obtém o logaritmo de base 10 de X.
pow Math.pow(X,Y) Calcula a potência de X elevado a Y.
sin Math.sin(X) Calcula o seno de X (X deve estar representado em radianos).
sqrt Math.sqrt(X) Calcula a raiz quadrada de X.
cbrt Math.cbrt(X) Calcula a raiz cúbica de X.
tan Math.tan(X) Calcula a tangente de X (X deve estar representado em radianos).
PI Math.PI Retorna o valor de π.
toDegrees Math.toDegrees(X) Converte a medida de X de radianos para graus.
toRadians Math.toRadians(X) Converte a medida de X de graus para radianos.
Os métodos sin, cos e tan esperam receber argumentos no formato de radianos; para receberem 
argumentos em graus, siga o próximo exemplo.
dado = new Scanner(System.in); 
x = dado.nextDouble();
y = Math.sin(Math.toRadians(x));
Observação
A linguagem JAVA possui muitas outras funções matemáticas que podem ser observadas detalhada -
mente na documentação da classe Math.
Palavras reservadas são nomes utilizados pela linguagem para representar comandos de controle do programa, 
operadores e diretivas.
abstract continue for new switch
assert default if package synchronized
boolean do goto private this
break double implements protected throw
byte else import public throws
case enum instanceof return transient
catch extends int short try
char final interface static void
class finally long strictfp volatile
const float native super while
Tem-se ainda em JAVA os literais reservados e que, assim como as palavras reservadas, não podem ser 
usados como identificadores, pois apresentarão erro de compilação. São eles: null, true e false.

---

Capítulo 3 Estrutura sequencial  | 37
Quando estamos trabalhando com tipos de dados reais, precisamos fazer a formatação desses números. 
Se isso não for feito, eles serão apresentados com formatação científica.
Exemplo de números com formatação científica:
1.5000000000E+04 = 15000
7.0000000000E+00 = 7
Exemplo de formatação:
X:6:2 A variável X será mostrada com seis caracteres: dois caracteres para a parte fracionária, um carac-
tere para o ponto e os outros três caracteres restantes para a parte inteira.
Y:8:3 A variável Y será mostrada com oito caracteres: três caracteres para a parte fracionária, um 
caractere para o ponto e os outros quatro caracteres restantes para a parte inteira.
Variável: número total de caracteres: número de caracteres da parte fracionária
O primeiro parâmetro da formatação corresponde ao número total de caracteres mostrados na tela; o 
segundo, ao total de caracteres ocupados pela parte fracionária. O ponto, que é o separador entre a parte 
inteira e fracionária, também ocupa um caractere.
Os caracteres à direita serão preenchidos com zeros e os caracteres à esquerda serão preenchidos com 
espaços em branco.
3a SOLUÇÃO:
\EXERC\CAP3\PASCAL\EX2_C.PAS e \EXERC\CAP3\PASCAL\EX2_C.EXE
1a SOLUÇÃO:
\EXERC\CAP3\C++\EX2_A.CPP e \EXERC\CAP3\C++\EX2_A.EXE
Quando estamos trabalhando com tipos de dados reais, precisamos fazer a formatação desses números 
para definir quantas casas decimais devem ser mostradas. Assim, no comando de saída printf, a formata-
ção é especificada imediatamente antes da letra que define o tipo da variável que será mostrada.
Exemplo:
printf(“Conteúdo de variável X é: %6.3f”,X);
No comando dado anteriormente, %f especifica que será mostrado um número real, e 6.3 significa que 
serão utilizados seis caracteres para mostrar o número, e, destes, três caracteres para a parte fracionária, um 
caractere para o ponto e os outros dois caracteres restantes para a parte inteira.
2a SOLUÇÃO:
\EXERC\CAP3\C++\EX2_B.CPP e \EXERC\CAP3\C++\EX2_B.EXE
3a SOLUÇÃO:
\EXERC\CAP3\C++\EX2_C.CPP e \EXERC\CAP3\C++\EX2_C.EXE
1a SOLUÇÃO:
\EXERC\CAP3\JAVA\EX2_A.java e \EXERC\CAP3\JAVA\EX2_A.class
Quando estamos trabalhando com tipos de dados reais, precisamos fazer a formatação desses números 
para definir a quantidade de casas decimais que devem ser mostradas.
Deve-se utilizar o método DecimalFormat, conforme apresentado a seguir:
DecimalFormat casas;
casas = new DecimalFormat(“0.00”);
System.out.println(“Média = ”+casas.format(media));
No exemplo anterior, a formatação permitirá que sejam mostradas duas casas decimais para o valor da 
variável média. Para a utilização do método DecimalFormat, deve-se incluir o pacote de classes text, ou 
seja, import java.text.*;
C/C++
JAVA

---

Capítulo 3 Estrutura sequencial  | 39
4. Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se 
que este sofreu um aumento de 25%.
1a SOLUÇÃO:
ALGORITMO
DECLARE sal, novosal NUMÉRICO 
LEIA sal
novosal ← sal + sal * 25/100
ESCREVA novosal
FIM_ALGORITMO.
2a SOLUÇÃO:
ALGORITMO
DECLARE sal, aumento, novosal NUMÉRICO
LEIA sal
aumento ← sal * 25/100 
novosal ← sal + aumento
ESCREVA novosal
FIM_ALGORITMO.
1a SOLUÇÃO:
\EXERC\CAP3\PASCAL\EX4_A.PAS e \EXERC\CAP3\PASCAL\EX4_A.EXE
2a SOLUÇÃO:
\EXERC\CAP3\PASCAL\EX4_B.PAS e \EXERC\CAP3\PASCAL\EX4_B.EXE
1a SOLUÇÃO:
\EXERC\CAP3\C++\EX4_A.CPP e \EXERC\CAP3\C++\EX4_A.EXE
2a SOLUÇÃO:
\EXERC\CAP3\C++\EX4_B.CPP e \EXERC\CAP3\C++\EX4_B.EXE
1a SOLUÇÃO:
\EXERC\CAP3\JAVA\EX4_A.java e \EXERC\CAP3\JAVA\EX4_A.class
2a SOLUÇÃO:
\EXERC\CAP3\JAVA\EX4_B.java e \EXERC\CAP3\JAVA\EX4_B.class
5. Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre 
o valor do aumento e o novo salário.
SOLUÇÃO:
ALGORITMO
DECLARE sal, perc, aumento, novosal NUMÉRICO
LEIA sal, perc
aumento ← sal * perc/100 
ESCREVA aumento
novosal ← sal + aumento 
ESCREVA novosal
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP3\PASCAL\EX5.PAS e \EXERC\CAP3\PASCAL\EX5.EXE 
SOLUÇÃO:
\EXERC\CAP3\C++\EX5.CPP e \EXERC\CAP3\C++\EX5.EXE
PASCAL
C/C++
JAVA
PASCAL
C/C++

---

Capítulo 3 Estrutura sequencial  | 41
rend ← dep * taxa/100 
total ← dep + rend 
ESCREVA rend
ESCREVA total 
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP3\PASCAL\EX8.PAS e \EXERC\CAP3\PASCAL\EX8.EXE 
SOLUÇÃO:
\EXERC\CAP3\C++\EX8.CPP e \EXERC\CAP3\C++\EX8.EXE
SOLUÇÃO:
\EXERC\CAP3\JAVA\EX8.java e \EXERC\CAP3\JAVA\EX8.class 
9. Faça um programa que calcule e mostre a área de um triângulo. Sabe-se que: Área = (base * altura)/2. 
SOLUÇÃO:
ALGORITMO
DECLARE base, altura, area NUMÉRICO 
LEIA base, altura
area ← (base * altura)/2 
ESCREVA area
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP3\PASCAL\EX9.PAS e \EXERC\CAP3\PASCAL\EX9.EXE 
SOLUÇÃO:
\EXERC\CAP3\C++\EX9.CPP e \EXERC\CAP3\C++\EX9.EXE
SOLUÇÃO:
\EXERC\CAP3\JAVA\EX9.java e \EXERC\CAP3\JAVA\EX9.class 
10. Faça um programa que calcule e mostre a área de um círculo. Sabe-se que: Área = p * R2. 
SOLUÇÃO:
ALGORITMO
DECLARE area, raio NUMÉRICO
LEIA raio
area ← 3.1415 * raio2
ESCREVA area
FIM_ALGORITMO.
1a SOLUÇÃO:
\EXERC\CAP3\PASCAL\EX10_A.PAS e \EXERC\CAP3\PASCAL\EX10_A.EXE
2a SOLUÇÃO:    
\EXERC\CAP3\PASCAL\EX10_B.PAS e \EXERC\CAP3\PASCAL\EX10_B.EXE
PASCAL
C/C++
JAVA
PASCAL
C/C++
JAVA
PASCAL

---

Capítulo 3 Estrutura sequencial  | 43
12. Faça um programa que receba dois números maiores que zero, calcule e mostre um elevado ao outro.
SOLUÇÃO:
ALGORITMO
DECLARE num1, num2, r1, r2 NUMÉRICO 
LEIA num1, num2
r1 ← num1num2
r2 ← num2num1 
ESCREVA r1, r2 
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP3\PASCAL\EX12.PAS e \EXERC\CAP3\PASCAL\EX12.EXE
Esse programa usou algumas funções predefinidas da linguagem PASCAL que estão descritas na Seção 3.2.7.
SOLUÇÃO:
\EXERC\CAP3\C++\EX12.CPP e \EXERC\CAP3\C++\EX12.EXE
Esse programa usou algumas funções predefinidas da linguagem C/C++ que estão descritas na Seção 3.3.7.
SOLUÇÃO:
\EXERC\CAP3\JAVA\EX12.java e \EXERC\CAP3\JAVA\EX12.class
Esse programa usou alguns métodos da linguagem JAVA que estão descritos na Seção 3.4.7.
13. Sabe-se que: 
pé = 12 polegadas 
1 jarda = 3 pés
1 milha = 1,760 jarda
Faça um programa que receba uma medida em pés, faça as conversões a seguir e mostre os resultados.
a) polegadas; 
b) jardas; 
c) milhas. 
SOLUÇÃO:
ALGORITMO
DECLARE pes, polegadas, jardas, milhas NUMÉRICO 
LEIA pes
polegadas ← pes * 12 
jardas ← pes / 3 
milhas ← jardas / 1760
ESCREVA polegadas, jardas, milhas 
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP3\PASCAL\EX13.PAS e \EXERC\CAP3\PASCAL\EX13.EXE
SOLUÇÃO:
\EXERC\CAP3\C++\EX13.CPP e \EXERC\CAP3\C++\EX13.EXE
SOLUÇÃO:
\EXERC\CAP3\JAVA\EX13.java e \EXERC\CAP3\JAVA\EX13.class
PASCAL
C/C++
JAVA
PASCAL
C/C++
JAVA

---

Capítulo 3 Estrutura sequencial  | 45
SOLUÇÃO:
\EXERC\CAP3\JAVA\EX15.java e \EXERC\CAP3\JAVA\EX15.class
16. Faça um programa que receba o número de horas trabalhadas e o valor do salário mínimo, calcule e  
mostre o salário a receber, seguindo estas regras:
a) a hora trabalhada vale a metade do salário mínimo. 
b) o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada. 
c) o imposto equivale a 3% do salário bruto. 
d) o salário a receber equivale ao salário bruto menos o imposto. 
SOLUÇÃO:
ALGORITMO
DECL ARE horas_t, vlr_sal_min, vlr_hora_t NUMÉRICO 
     vlr_sal_bru, imp, vlr_sal_liq NUMÉRICO
LEIA horas_t 
LEIA vlr_sal_min
vlr_hora_t ← vlr_sal_min / 2 
vlr_sal_bru ← vlr_hora_t * horas_t 
imp ← vlr_sal_bru * 3 / 100 
vlr_sal_liq ← vlr_sal_bru − imp 
ESCREVA vlr_sal_liq
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP3\PASCAL\EX16.PAS e \EXERC\CAP3\PASCAL\EX16.EXE
SOLUÇÃO:
\EXERC\CAP3\C++\EX16.CPP e \EXERC\CAP3\C++\EX16.EXE
SOLUÇÃO:
\EXERC\CAP3\JAVA\EX16.java e \EXERC\CAP3\JAVA\EX16.class
17. Um trabalhador recebeu seu salário e o depositou em sua conta bancária. Esse trabalhador emitiu dois 
cheques e agora deseja saber seu saldo atual. Sabe-se que cada operação bancária de retirada paga 
CPMF de 0,38% e o saldo inicial da conta está zerado.
SOLUÇÃO:
ALGORITMO
DECLARE salario, cheque1, cheque2, cpmf1, cpmf2, saldo NUMÉRICO 
LEIA salario
LEIA cheque1 
LEIA cheque2
cpmf1 ← cheque1 * 0.38 / 100 
cpmf2 ← cheque2 * 0.38 / 100
saldo ← salario − cheque1 − cheque2 − cpmf1 − cpmf2 
ESCREVA saldo
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP3\PASCAL\EX17.PAS e \EXERC\CAP3\PASCAL\EX17.EXE
JAVA
PASCAL
C/C++
JAVA
PASCAL

---

Capítulo 3 Estrutura sequencial  | 47
SOLUÇÃO:
\EXERC\CAP3\PASCAL\EX19.PAS e \EXERC\CAP3\PASCAL\EX19.EXE
SOLUÇÃO:
\EXERC\CAP3\C++\EX19.CPP e \EXERC\CAP3\C++\EX19.EXE
SOLUÇÃO:
\EXERC\CAP3\JAVA\EX19.java e \EXERC\CAP3\JAVA\EX19.class
20. Faça um programa que receba a medida do ângulo (em graus) formado por  uma escada apoiada no 
chão e encostada na parede e a altura da parede onde está a ponta da escada. Calcule e mostre a me -
dida dessa escada.
Observação: as funções trigonométricas implementadas nas linguagens de programação trabalham 
com medidas de ângulos em radianos.
a
parede
escada
chão
SOLUÇÃO:
ALGORITMO
DECLARE ang, alt, escada, radiano NUMÉRICO 
LEIA ang
LEIA alt
radiano ← ang * 3.14 / 180 
escada ← alt / seno(radiano) 
ESCREVA escada
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP3\PASCAL\EX20.PAS e \EXERC\CAP3\PASCAL\EX20.EXE
PASCAL
C/C++
JAVA
PASCAL
SOLUÇÃO:
\EXERC\CAP3\C++\EX20.CPP e \EXERC\CAP3\C++\EX20.EXE
SOLUÇÃO:
\EXERC\CAP3\JAVA\EX20.java e \EXERC\CAP3\JAVA\EX20.class
21. Uma pessoa deseja pregar um quadro em uma parede. Faça um programa para calcular e mostrar  a 
que distância a escada deve estar da parede. A pessoa deve fornecer o tamanho da escada e a altura em 
que deseja pregar o quadro.
Lembre-se de que o tamanho da escada deve ser maior que a altura que se deseja alcançar.
C/C++
JAVA

---

Capítulo 3 Estrutura sequencial  | 49
SOLUÇÃO:
\EXERC\CAP3\C++\EX22.CPP e \EXERC\CAP3\C++\EX22.EXE
SOLUÇÃO:
\EXERC\CAP3\JAVA\EX22.java e \EXERC\CAP3\JAVA\EX22.class
23. Faça um programa que receba um número real, encontre e mostre: 
a) a parte inteira desse número; 
b) a parte fracionária desse número; 
c) o arredondamento desse número. 
SOLUÇÃO:
ALGORITMO
DECLARE num, i, f, a NUMÉRICO 
LEIA num
i ← parte inteira de num 
f ← num − i
a ← arredonda (num)
ESCREVA i
ESCREVA f
ESCREVA a
FIM_ALGORITMO.
SOLUÇÃO (ARREDONDANDO O NÚMERO COMO NA MATEMÁTICA):
\EXERC\CAP3\PASCAL\EX23.PAS e \EXERC\CAP3\PASCAL\EX23.EXE
1a SOLUÇÃO (ARREDONDANDO O NÚMERO PARA CIMA):
\EXERC\CAP3\C++\EX23_A.CPP e \EXERC\CAP3\C++\EX23_A.EXE
2a SOLUÇÃO (ARREDONDANDO O NÚMERO PARA BAIXO):
\EXERC\CAP3\C++\EX23_B.CPP e \EXERC\CAP3\C++\EX23_B.EXE
1a SOLUÇÃO (ARREDONDANDO O NÚMERO PARA CIMA):
\EXERC\CAP3\JAVA\EX23_A.java e \EXERC\CAP3\JAVA\EX23_A.class
2a SOLUÇÃO (ARREDONDANDO O NÚMERO PARA BAIXO):
\EXERC\CAP3\JAVA\EX23_B.java e \EXERC\CAP3\JAVA\EX23_B.class
24. Faça um programa que receba uma hora formada por hora e minutos (um número real), calcule e  
mostre a hora digitada apenas em minutos. Lembre-se de que:
 ■ para quatro e meia, deve-se digitar 4.30; 
 ■ os minutos vão de 0 a 59. 
SOLUÇÃO:
ALGORITMO
DECLARE hora, h, m, conversao NUMÉRICO
LEIA hora
h ← pegar a parte inteira da variável hora 
m ← hora − h
conversao ← (h * 60) + (m * 100) 
ESCREVA conversao
FIM_ALGORITMO.
C/C++
JAVA
PASCAL
C/C++
JAVA

---

Capítulo 3 Estrutura sequencial  | 51
8. Faça um programa que receba o peso de uma pessoa em quilos, calcule e mostre esse peso em gramas. 
9. Faça um programa que calcule e mostre a área de um trapézio. 
Sabe-se que: A = ((base maior + base menor) * altura)/2
10. Faça um programa que calcule e mostre a área de um quadrado. Sabe-se que: A = lado * lado.
11. Faça um programa que calcule e mostre a área de um losango. Sabe-se que: A = (diagonal maior * dia-
gonal menor)/2. 
12. Faça um programa que receba o valor do salário mínimo e o valor do salário de um funcionário, calcule 
e mostre a quantidade de salários mínimos que esse funcionário ganha. 
13. Faça um programa que calcule e mostre a tabuada de um número digitado pelo usuário. 
Exemplo:
Digite um número: 5
5 × 0 = 0
5 × 1 = 5
5 × 2 = 10
5 × 3 = 15
5 × 4 = 20
5 × 5 = 25
5 × 6 = 30
5 × 7 = 35
5 × 8 = 40
5 × 9 = 45
5 × 10 = 50
14. Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre: 
a) a idade dessa pessoa em anos; 
b) a idade dessa pessoa em meses; 
c) a idade dessa pessoa em dias; 
d) a idade dessa pessoa em semanas. 
15. João recebeu seu salário e precisa pagar duas contas atrasadas. Em razão do atraso, ele deverá pagar 
multa de 2% sobre cada conta. Faça um programa que calcule e mostre quanto restará do salário de 
João. 
16. Faça um programa que receba o valor dos catetos de um triângulo, calcule e mostre o valor da hipo -
tenusa. 
17. Faça um programa que receba o raio, calcule e mostre: 
a) o comprimento de uma esfera; sabe-se que C = 2 * p R; 
b) a área de uma esfera; sabe-se que A = p R2; 
c) o volume de uma esfera; sabe-se que V = ¾ * p R3. 
18. Faça um programa que receba uma temperatura em Celsius, calcule e mostre essa temperatura em 
Fahrenheit. Sabe-se que F = 180*(C + 32)/100. 
19. Sabe-se que, para iluminar de maneira correta os cômodos de uma casa, para cada m2, deve-se usar 18 W 
de potência. Faça um programa que receba as duas dimensões de um cômodo (em metros), calcule e mostre 
a sua área (em m2) e a potência de iluminação que deverá ser utilizada. 
20. Faça um programa que receba a medida do ângulo formado por uma escada apoiada no chão e a dis-
tância em que a escada está da parede, calcule e mostre a medida da escada para que se possa alcançar 
sua ponta. 
a
Medida da escada
Distância que a escada está da parede
21. Faça um programa que receba o número de horas trabalhadas, o valor do salário mínimo e o número 
de horas extras trabalhadas, calcule e mostre o salário a receber, de acordo com as regras a seguir: 
a) a hora trabalhada vale 1/8 do salário mínimo; 
b) a hora extra vale 1/4 do salário mínimo;

---



=== CAPÍTULO 4 ===

---

Capítulo 4 Estrutura condicional  | 55
CASE seletor OF
lista de alvos1: comando1; 
lista de alvos2: comando2; 
alvo3: comando3;
alvo4: BEGIN
comando4;
comando5;
END;
END;
Se o seletor atingir a lista de alvos1, o comando1 será executado; se atingir a lista de alvos2, 
o comando2 será executado; se atingir o alvo3, o comando3 será executado; e, se atingir o alvo4, então, o 
comando4 e o comando5 serão executados. Se nenhum alvo for atingido, nada será executado.
CASE seletor OF
lista de alvos1: BEGIN
comando1;
comando2;
END;
lista de alvos2: comando3;
ELSE comando4;
END;
Na estrutura CASE acima, se nenhum alvo for atingido os comandos da estrutura ELSE serão executados.
Exemplo:
program teste; 
uses crt;
var i: integer; 
begin
clrscr;
writeln(‘Digite um número’); 
readln(i);
case i of
1: writeln(‘Número 1’);
 2,5,6:writeln(‘Número 2 ou número 5 ou número 6’);  
7..10:writeln(‘Número entre 7 e 10’);
else writeln(‘outro número’); 
end;
readln; 
end.
A restrição da estrutura case é que o seletor só pode ser uma variável do tipo char, integer ou boolean.
4.2.4 Operadores lógicos
Os principais operadores lógicos são: AND, OR e NOT, que significam e, ou, não e são usados para con -
junção, disjunção e negação, respectivamente.
TABELA E TABELA OU TABELA NÃO
V e V = V V ou V = V Não V = F
V e F = F V ou F = V Não F = V
F e V = F F ou V = V
F e F = F F ou F = F

---

Capítulo 4 Estrutura condicional  | 57
4.3.2 Estrutura condicional composta
if (condição) 
comando1;
else
comando2;
Se a condição for verdadeira, será executado o comando1; se for falsa, será executado o comando2.
if (condição)
 {
comando1; 
comando2;
 }
else
 {
comando3; 
comando4;
 }
Se a condição for verdadeira, o comando1 e o comando2 serão executados; caso contrário, o comando3 
e o comando4 serão executados.
4.3.3 Estrutura case
Em alguns programas, existem situações mutuamente exclusivas, isto é, se uma situação for executada, 
as demais não serão. Quando este for o caso, um comando seletivo é o mais indicado. Esse comando em C/
C++ tem a seguinte sintaxe:
switch (variável)
{
case valor1: lista de comandos; 
break;
case valor2: lista de comandos; 
break;
....
default: lista de comandos;
}
O comando switch(variável) avalia o valor de uma variável para decidir qual case será executado. 
Cada case está associado a UM possível valor da variável, que deve ser, obrigatoriamente, do tipo char, 
unsigned char, int, unsigned int, short int, long ou unsigned long.
O comando break deve ser utilizado para impedir a execução dos comandos definidos nos cases sub-
sequentes. Quando o valor da variável não coincidir com aqueles especificados nos cases, será executado 
então o default. 
Exemplo:
#include <stdio.h>
int main()
{
  int i; 
  printf(“Digite um número ”);
  scanf(“%d%*c”,&i);
  switch (i)
  {
   case 1:
     printf(“Número 1”);
     break;
   case 2:

---

Capítulo 4 Estrutura condicional  | 59
4.4.1 Estrutura condicional simples
if (condição) 
comando;
O comando só será executado se a condição for verdadeira. Uma condição é uma comparação que 
possui dois valores possíveis: verdadeiro ou falso.
if (condição)
 {
comando1; 
comando2; 
comando3;
 }
Em JAVA, torna-se obrigatória a utilização de chaves quando existe mais de um comando a executar. 
Os comandos entre chaves { } só serão executados se a condição for verdadeira.
4.4.2 Estrutura condicional composta
if (condição) 
 comando1;
else 
 comando2;
Se a condição for verdadeira, será executado o comando1; caso contrário, será executado o comando2.
if (condição)
 {
comando1;
comando2;
 }
else
 {
comando3; 
comando4;
 }
Se a condição for verdadeira, o comando1 e o comando2 serão executados; se for falsa, o comando3 
e o comando4 serão executados.
4.4.3 Estrutura case
Em alguns programas, existem situações mutuamente exclusivas, isto é, se uma situação for executada, 
as demais não serão. Quando este for o caso, um comando seletivo é o mais indicado, e esse comando, em 
JAVA, tem a seguinte sintaxe:
switch (variável)
{
case valor1: lista de comandos; 
break;
case valor2: lista de comandos; 
break;
....
default: lista de comandos;
}
O comando switch (variável) analisa o valor de uma variável para decidir qual case será executa-
do. Cada case está associado a UM possível valor da variável, que deve ser obrigatoriamente do tipo int, 
short, byte ou char.

---

Capítulo 4 Estrutura condicional  | 61
EXERCÍCIOS RESOLVIDOS
1. A nota final de um estudante é calculada a partir de três notas atribuídas, respectivamente, a um traba-
lho de laboratório, a uma avaliação semestral e a um exame final. A média das três notas mencionadas 
obedece aos pesos a seguir:
NOTA PESO
Trabalho de laboratório 2
Avaliação semestral 3
Exame ﬁnal 5
Faça um programa que receba as três notas, calcule e mostre a média ponderada e o conceito que segue 
a tabela:
MÉDIA PONDERADA CONCEITO
8,0 10,0 A
7,0 8,0 B
6,0 7,0 C
5,0 6,0 D
0,0 5,0 E
SOLUÇÃO:
ALGORITMO
 DECLARE nota_trab, aval_sem, exame, media NUMÉRICO 
ESCREVA “Digite a nota do trabalho de laboratório: “ 
LEIA nota_trab
ESCREVA “Digite a nota da avaliação semestral: “ 
LEIA aval_sem
ESCREVA “Digite a nota do exame final: “ 
LEIA exame
 media ← (nota_trab * 2 + aval_sem * 3 + exame * 5) / 10 
ESCREVA “Média ponderada: “ , media
SE media >= 8 E media <= 10
No exemplo anterior, existe mais de uma condição, as quais, obrigatoriamente, devem estar 
entre parênteses.
if ((X == 5 && Y == 2) || Y == 3)
System.out.println(“X é igual a 5 e Y é igual a 2, ou Y é igual a 3”);
No exemplo anterior, existe mais de uma condição e mais de um tipo de operador lógico, por -
tanto, além dos parênteses que envolvem todas as condições, devem existir ainda parênteses que 
indiquem a prioridade de execução das condições. Nesse exemplo, as condições com o operador &&, 
ou seja, (X == 5 && Y == 2), serão testadas, e seu resultado será testado com a condição || Y == 3.
if (X == 5 && (Y == 2 || Y == 3))
System.out.println(“X é igual a 5, e Y é igual a 2 ou Y é igual a 3”);
No exemplo anterior, existe mais de uma condição e mais de um tipo de operador lógico, por -
tanto, além dos parênteses que envolvem todas as condições, devem existir ainda parênteses que 
indiquem a prioridade de execução das condições. Nesse exemplo, as condições com o operador ||, 
ou seja, (Y == 2 || Y == 3), serão testadas, e seu resultado será testado com a condição && X == 5.

---

Capítulo 4 Estrutura condicional  | 63
ESCREVA “Deve tirar nota”, nota_exame, “para ser aprovado” 
FIM
SE media >= 7 E media <= 10 
ENTÃO ESCREVA “Aprovado”
FIM_ALGORITMO.
1a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL SIMPLES:
\EXERC\CAP4\PASCAL\EX2_A.PAS e \EXERC\CAP4\PASCAL\EX2_A.EXE
2a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL COMPOSTA:
\EXERC\CAP4\PASCAL\EX2_B.PAS e \EXERC\CAP4\PASCAL\EX2_B.EXE
1a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL SIMPLES:
\EXERC\CAP4\C++\EX2_A.CPP e \EXERC\CAP4\C++\EX2_A.EXE
2a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL COMPOSTA:
\EXERC\CAP4\C++\EX2_B.CPP e \EXERC\CAP4\C++\EX2_B.EXE
1a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL SIMPLES:
\EXERC\CAP4\JAVA\EX2_A.java e \EXERC\CAP4\JAVA\EX2_A.class
2a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL COMPOSTA:
\EXERC\CAP4\JAVA\EX2_B.java e \EXERC\CAP4\JAVA\EX2_B.class
3. Faça um programa que receba dois números e mostre o maior.
SOLUÇÃO:
ALGORITMO
DECLARE num1, num2 NUMÉRICO
ESCREVA “Digite o primeiro número: “
LEIA num1
ESCREVA “Digite o segundo número: “
LEIA num2
SE num1 > num2
ENTÃO ESCREVA “O maior número é: “, num1
SE num2 > num1
ENTÃO ESCREVA “O maior número é: “, num2
SE num1 = num2
ENTÃO ESCREVA “Os números são iguais “
FIM_ALGORITMO.
1a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL SIMPLES:
\EXERC\CAP4\PASCAL\EX3_A.PAS e \EXERC\CAP4\PASCAL\EX3_A.EXE
2a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL COMPOSTA:
\EXERC\CAP4\PASCAL\EX3_B.PAS e \EXERC\CAP4\PASCAL\EX3_B.EXE
1a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL SIMPLES:
\EXERC\CAP4\C++\EX3_A.CPP e \EXERC\CAP4\C++\EX3_A.EXE
2a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL COMPOSTA:
\EXERC\CAP4\C++\EX3_B.CPP e \EXERC\CAP4\C++\EX3_B.EXE
1a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL SIMPLES:
\EXERC\CAP4\JAVA\EX3_A.java e \EXERC\CAP4\JAVA\EX3_A.class
2a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL COMPOSTA:
\EXERC\CAP4\JAVA\EX3_B.java e \EXERC\CAP4\JAVA\EX3_B.class
PASCAL
C/C++
JAVA
PASCAL
C/C++
JAVA

---

Capítulo 4 Estrutura condicional  | 65
 ENTÃO ESCREVA “A ordem decrescente é: “,num4,“-”,num3,“-”,num2,“-”,num1 
SE num4 > num2 E num4 < num3
 ENTÃO ESCREVA “A ordem decrescente é: “,num3,“-”,num4,“-”,num2,“-”,num1 
SE num4 > num1 E num4 < num2
 ENTÃO ESCREVA “A ordem decrescente é: “,num3,“-”,num2,“-”,num4, “-”,num1 
SE num4 < num1
 ENTÃO ESCREVA “A ordem decrescente é: “,num3,“-”,num2,“-”,num1,“-”,num4
FIM_ALGORITMO.
1a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL SIMPLES:
\EXERC\CAP4\PASCAL\EX5_A.PAS e \EXERC\CAP4\PASCAL\EX5_A.EXE
2a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL COMPOSTA:
\EXERC\CAP4\PASCAL\EX5_B.PAS e \EXERC\CAP4\PASCAL\EX5_B.EXE
1a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL SIMPLES:
\EXERC\CAP4\C++\EX5_A.CPP e \EXERC\CAP4\C++\EX5_A.EXE
2a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL COMPOSTA:
\EXERC\CAP4\C++\EX5_B.CPP e \EXERC\CAP4\C++\EX5_B.EXE
1a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL SIMPLES:
\EXERC\CAP4\JAVA\EX5_A.java e \EXERC\CAP4\JAVA\EX5_A.class
2a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL COMPOSTA:
\EXERC\CAP4\JAVA\EX5_B.java e \EXERC\CAP4\JAVA\EX5_B.class
6. Faça um programa que receba um número inteiro e verifique se é par ou ímpar.
SOLUÇÃO:
ALGORITMO
DECLARE num, r NUMÉRICO 
ESCREVA “Digite um número: “ 
LEIA num
r ← RESTO(num/2) 
SE r = 0
ENTÃO ESCREVA “O número é par” 
SENÃO ESCREVA “O número é ímpar”
FIM_ALGORITMO.
1a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL SIMPLES:
\EXERC\CAP4\PASCAL\EX6_A.PAS e \EXERC\CAP4\PASCAL\EX6_A.EXE
2a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL COMPOSTA:
\EXERC\CAP4\PASCAL\EX6_B.PAS e \EXERC\CAP4\PASCAL\EX6_B.EXE
1a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL SIMPLES:
\EXERC\CAP4\C++\EX6_A.CPP e \EXERC\CAP4\C++\EX6_A.EXE
2a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL COMPOSTA:
\EXERC\CAP4\C++\EX6_B.CPP e \EXERC\CAP4\C++\EX6_B.EXE
1a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL SIMPLES:
\EXERC\CAP4\JAVA\EX6_A.java e \EXERC\CAP4\JAVA\EX6_A.class
2a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL COMPOSTA:
\EXERC\CAP4\JAVA\EX6_B.java e \EXERC\CAP4\JAVA\EX6_B.class
PASCAL
C/C++
JAVA
PASCAL
C/C++
JAVA

---

Capítulo 4 Estrutura condicional  | 67
ENTÃO INÍCIO
SE A>B E A>C
ENTÃO ESCREVA “A ordem desejada é: “,B,”-”,A,”-”,C 
SE B>A E B>C
ENTÃO ESCREVA “A ordem desejada é: “,A,”-”,B,”-”,C 
SE C>A E C>B
ENTÃO ESCREVA “A ordem desejada é: “,A,”-”,C,”-”,B 
FIM
FIM_ALGORITMO.
1a SOLUÇÃO:
\EXERC\CAP4\PASCAL\EX7_A.PAS e \EXERC\CAP4\PASCAL\EX7_A.EXE
2a SOLUÇÃO:
\EXERC\CAP4\PASCAL\EX7_B.PAS e \EXERC\CAP4\PASCAL\EX7_B.EXE
3a SOLUÇÃO:
\EXERC\CAP4\PASCAL\EX7_C.PAS e \EXERC\CAP4\PASCAL\EX7_C.EXE
1a SOLUÇÃO:
\EXERC\CAP4\C++\EX7_A.CPP e \EXERC\CAP4\C++\EX7_A.EXE
2a SOLUÇÃO:
\EXERC\CAP4\C++\EX7_B.CPP e \EXERC\CAP4\C++\EX7_B.EXE
3a SOLUÇÃO:
\EXERC\CAP4\C++\EX7_C.CPP e \EXERC\CAP4\C++\EX7_C.EXE
1a SOLUÇÃO:
\EXERC\CAP4\JAVA\EX7_A.java e \EXERC\CAP4\JAVA\EX7_A.class
2a SOLUÇÃO:
\EXERC\CAP4\JAVA\EX7_B.java e \EXERC\CAP4\JAVA\EX7_B.class
3a SOLUÇÃO:
\EXERC\CAP4\JAVA\EX7_C.java e \EXERC\CAP4\JAVA\EX7_C.class
8. Faça um programa que mostre o menu de opções a seguir, receba a opção do usuário e os dados neces-
sários para executar cada operação.
Menu de opções: 
1. Somar dois números. 
2. Raiz quadrada de um número. 
Digite a opção desejada:
SOLUÇÃO:
ALGORITMO
DECLARE num1, num2, soma, raiz, op NUMÉRICO 
ESCREVA “ MENU”
ESCREVA “1- Somar dois números” 
ESCREVA “2- Raiz quadrada de um número” 
ESCREVA “Digite sua opção: “
LEIA op 
SE op = 1
ENTÃO INÍCIO
ESCREVA “Digite um valor para o primeiro número:” 
LEIA num1
PASCAL
C/C++
JAVA

---

Capítulo 4 Estrutura condicional  | 69
SE mes = 3
ENTÃO ESCREVA “março” 
SE mes = 4
ENTÃO ESCREVA “abril” 
SE mes = 5
ENTÃO ESCREVA “maio” 
SE mes = 6
ENTÃO ESCREVA “junho” 
SE mes = 7
ENTÃO ESCREVA “julho” 
SE mes = 8
ENTÃO ESCREVA “agosto” 
SE mes = 9
ENTÃO ESCREVA “setembro” 
SE mes = 10
ENTÃO ESCREVA “outubro” 
SE mes = 11
ENTÃO ESCREVA “novembro” 
SE mes = 12
ENTÃO ESCREVA “dezembro” 
t ← OBTENHA_HORÁRIO; 
hora ← OBTENHA_HORA(t) 
min ← OBTENHA_MINUTO(t) 
ESCREVA “Hora Atual: “ 
ESCREVA hora, “:” , min
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP4\PASCAL\EX9.PAS e \EXERC\CAP4\PASCAL\EX9.EXE
Na solução com a linguagem PASCAL, foram utilizados os comandos getdate e gettime, para obter 
a data e a hora do sistema operacional, respectivamente. O comando getdate retorna os valores do ano, 
mês, dia do mês e dia da semana da data do sistema operacional; as variáveis que receberão esses valores 
devem ser do tipo word. O comando gettime retorna os valores da hora, minuto, segundo e centésimo de 
segundo da hora do sistema operacional e as variáveis que receberão esses valores devem ser do tipo word. 
Para a utilização dos comandos getdate e gettime, é necessário utilizar a biblioteca DOS, ou seja, USES DOS.
O dia da semana é um número em que domingo vale 0; segunda-feira, 1; terça-feira, 2; quarta -
-feira, 3; quinta-feira, 4; sexta-feira, 5; e sábado, 6.
Exemplo:
GETDATE(ano, mes, dia, dia_semana);
GETTIME(hora, min, seg, cen_seg);
Observação
SOLUÇÃO:
\EXERC\CAP4\C++\EX9.CPP e \EXERC\CAP4\C++\EX9.EXE
Na solução com a linguagem C/C++, foram utilizados os comandos t = time(NULL)  e data_hora = 
localtime(&t) para obter a data e a hora do sistema operacional. Para a utilização desses comandos, é 
necessário utilizar a biblioteca time.h, ou seja, #include <time.h> e a declaração do tipo time_t.
PASCAL
C/C++

---

Capítulo 4 Estrutura condicional  | 71
SOLUÇÃO:
ALGORITMO
 DECLARE d1,m1,a1,d2,m2,a2 NUMÉRICO 
ESCREVA “Digite a primeira data”
ESCREVA “ dia (dd): “
LEIA d1
ESCREVA “ mês (mm): “ 
LEIA m1
ESCREVA “ ano (aaaa): “ 
LEIA a1
ESCREVA “Digite a segunda data” 
ESCREVA “ dia (dd): “
LEIA d2
ESCREVA “ mês (mm): “ 
LEIA m2
ESCREVA “ ano (aaaa): “ 
LEIA a2
SE a1>a2
ENTÃO ESCREVA “A maior data é: “,d1,”-”,m1,”-”,a1 
SENÃO SE a2>a1
ENTÃO ESCREVA “A maior data é: “,d2,”-”,m2,”-”,a2 
SENÃO SE m1>m2
 ENTÃO ESCREVA “A maior data é: “,d1,”-”,m1,”-”,a1 
SENÃO SE m2>m1
ENTÃO ESCREVA “A maior data é: “,d2, “-”,m2,”-”,a2
SENÃO SE d1>d2
 ENTÃO ESCREVA “A maior data é: “-”,d1,”-”,m1,” -”,a1
SENÃO SE d2>d1
 ENTÃO ESCREVA “A maior data é: “,d2,” -”,m2,”-”,a2
 SENÃO ESCREVA “As datas são iguais !”
FIM_ALGORITMO. 
SOLUÇÃO:
\EXERC\CAP4\PASCAL\EX10.PAS e \EXERC\CAP4\PASCAL\EX10.EXE
SOLUÇÃO:
\EXERC\CAP4\C++\EX10.CPP e \EXERC\CAP4\C++\EX10.EXE
SOLUÇÃO:
\EXERC\CAP4\JAVA\EX10.java e \EXERC\CAP4\JAVA\EX10.class
11. Faça um programa que receba a hora do início de um jogo e a hora do término (cada hora é composta 
por duas variáveis inteiras: hora e minuto). Calcule e mostre a duração do jogo (horas e minutos), 
sabendo que o tempo máximo de duração do jogo é de 24 horas e que ele pode começar em um dia e 
terminar no dia seguinte.
SOLUÇÃO:
ALGORITMO
DECLARE hora_i, min_i, hora_f, min_f, hora_d, min_d NUMÉRICO
ESCREVA “Digite o horário inicial”
ESCREVA “hora: “
LEIA hora_i
PASCAL
C/C++
JAVA

---

Capítulo 4 Estrutura condicional  | 73
novo_sal ←  salario + aumento
ESCREVA “O novo salário é: “, novo_sal
FIM
SENÃO SE cargo = 2
ENTÃO INÍCIO
ESCREVA “O cargo é Secretário”
aumento ←  salario * 35 / 100
ESCREVA “O valor do aumento é: “, aumento
novo_sal ←  salario + aumento
ESCREVA “O novo salário é: “, novo_sal
FIM
SENÃO SE cargo = 3
ENTÃO INÍCIO
ESCREVA “O cargo é Caixa”
aumento ←  salario * 20 / 100
ESCREVA “O valor do aumento é: “, aumento
novo_sal ←  salario + aumento
ESCREVA “O novo salário é: “,novo_sal
FIM
SENÃO SE cargo = 4
ENTÃO INÍCIO
ESCREVA “O cargo é Gerente”
aumento ←  salario * 10 / 100
ESCREVA “O valor do aumento é: “, aumento
novo_sal ←  salario + aumento
ESCREVA “O novo salário é: “, novo_sal
FIM
SENÃO SE cargo = 5
ENTÃO INÍCIO
ESCREVA “O cargo é Diretor”
aumento ←  salario * 0 / 100
ESCREVA “O valor do aumento é: “, aumento
novo_sal ←  salario + aumento
ESCREVA “O novo salário é: “, novo_sal
FIM
SENÃO ESCREVA “Cargo Inexistente !”
FIM_ALGORITMO.
1a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL COMPOSTA:
\EXERC\CAP4\PASCAL\EX12_A.PAS e \EXERC\CAP4\PASCAL\EX12_A.EXE
2a SOLUÇÃO – UTILIZANDO ESTRUTURA SELETORA:
\EXERC\CAP4\PASCAL\EX12_B.PAS e \EXERC\CAP4\PASCAL\EX12_B.EXE
1a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL COMPOSTA:
\EXERC\CAP4\C++\EX12_A.CPP e \EXERC\CAP4\C++\EX12_A.EXE
2a SOLUÇÃO – UTILIZANDO ESTRUTURA SELETORA:
\EXERC\CAP4\C++\EX12_B.CPP e \EXERC\CAP4\C++\EX12_B.EXE
1a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL COMPOSTA:
\EXERC\CAP4\JAVA\EX12_A.java e \EXERC\CAP4\JAVA\EX12_A.class
2a SOLUÇÃO – UTILIZANDO ESTRUTURA SELETORA:
\EXERC\CAP4\JAVA\EX12_B.java e \EXERC\CAP4\JAVA\EX12_B.class
PASCAL
C/C++
JAVA

---

Capítulo 4 Estrutura condicional  | 75
ESCREVA imp
FIM 
SE op = 2
ENTÃO INÍCIO 
LEIA sal
SE sal > 1500 
ENTÃO aum ← 25
SE sal >= 750 E sal <= 1500 
ENTÃO aum ← 50
SE sal >= 450 E sal < 750 
ENTÃO aum ← 75
SE sal < 450
ENTÃO aum ← 100 novo_sal ← sal + aum 
ESCREVA novo_sal
FIM 
SE op = 3
ENTÃO INÍCIO 
LEIA sal
SE sal <= 700
ENTÃO ESCREVA”Mal Remunerado” 
SE sal > 700
ENTÃO ESCREVA”Bem Remunerado” 
FIM
SE op < 1 OU op > 3
ENTÃO ESCREVA “Opção Inválida” 
FIM_ALGORITMO.
1a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL SIMPLES:
EXERC\CAP4\PASCAL\EX13_A.PAS e \EXERC\CAP4\PASCAL\EX13_A.EXE
2a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL COMPOSTA:
\EXERC\CAP4\PASCAL\EX13_B.PAS e \EXERC\CAP4\PASCAL\EX13_B.EXE
3a SOLUÇÃO – UTILIZANDO ESTRUTURA SELETORA:
\EXERC\CAP4\PASCAL\EX13_C.PAS e \EXERC\CAP4\PASCAL\EX13_C.EXE
1a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL SIMPLES:
\EXERC\CAP4\C++\EX13_A.CPP e \EXERC\CAP4\C++\EX13_A.EXE
2a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL COMPOSTA:
\EXERC\CAP4\C++\EX13_B.CPP e \EXERC\CAP4\C++\EX13_B.EXE
3a SOLUÇÃO – UTILIZANDO ESTRUTURA SELETORA:
\EXERC\CAP4\C++\EX13_C.CPP e \EXERC\CAP4\C++\EX13_C.EXE
1a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL SIMPLES:
EXERC\CAP4\JAVA\EX13_A.java e \EXERC\CAP4\JAVA\EX13_A.class
2a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL COMPOSTA:
\EXERC\CAP4\JAVA\EX13_B.java e \EXERC\CAP4\JAVA\EX13_B.class
3a SOLUÇÃO – UTILIZANDO ESTRUTURA SELETORA:
\EXERC\CAP4\JAVA\EX13_C.java e \EXERC\CAP4\JAVA\EX13_C.class
PASCAL
C/C++
JAVA

---

Capítulo 4 Estrutura condicional  | 77
IRRF SALÁRIO BRUTO
Isento Inferior a R$ 200,00
10% De R$ 200,00 até R$ 500,00
20% Superior a R$ 500,00
 ■ O salário líquido é igual ao salário bruto menos IRRF.
 ■ A gratificação é de acordo com a tabela a seguir:
SALÁRIO LÍQUIDO GRATIFICAÇÃO
Até R$ 350,00 R$ 100,00
Superior a R$ 350,00 R$ 50,00
 ■ O salário a receber do funcionário é igual ao salário líquido mais a gratificação.
SOLUÇÃO:
ALGORITMO
DECLARE sal_min, nht, ndep, nhet NUMÉRICO
  sal_receber, vh, smes, vdep, vhe, imp NUMÉRICO 
  sbruto, sliq, grat NUMÉRICO
LEIA sal_min, nht, ndep, nhet 
vh ← 1/5 * sal_min
smes ← nht * vh 
vdep ← 32 * ndep
vhe ← nhet * (vh + (vh * 50/100)) 
sbruto ← smes + vdep + vhe
SE sbruto < 200 
ENTÃO imp ← 0
SE sbruto >= 200 E sbruto <= 500 
ENTÃO imp ← sbruto * 10/100
SE sbruto > 500
ENTÃO imp ← sbruto * 20/100 
sliq ← sbruto – imp
SE sliq <= 350 
ENTÃO grat ← 100
SE sliq > 350 
ENTÃO grat ← 50
sal_receber ← sliq + grat 
ESCREVA sal_receber
FIM_ALGORITMO.
1a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL SIMPLES:
\EXERC\CAP4\PASCAL\EX15_A.PAS e \EXERC\CAP4\PASCAL\EX15_A.EXE
2a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL COMPOSTA:
\EXERC\CAP4\PASCAL\EX15_B.PAS e \EXERC\CAP4\PASCAL\EX15_B.EXE
1a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL SIMPLES:
\EXERC\CAP4\C++\EX15_A.CPP e \EXERC\CAP4\C++\EX15_A.EXE
2a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL COMPOSTA:
\EXERC\CAP4\C++\EX15_B.CPP e \EXERC\CAP4\C++\EX15_B.EXE
PASCAL
C/C++

---

Capítulo 4 Estrutura condicional  | 79
SOLUÇÃO:
ALGORITMO
DECLARE a, b, c, delta, x1, x2 NUMÉRICO 
LEIA a, b, c
SE a = 0
ENTÃO ESCREVA “Estes valores não formam uma equação de segundo grau” 
SENÃO INÍCIO
delta ← (b * b) – ( 4 * a * c) 
SE delta < 0
ENTÃO ESCREVA “Não existe raiz real”
SE delta = 0
ENTÃO INÍCIO
ESCREVA “Existe uma raiz real”
x1 ← (– b) / (2 * a)
ESCREVA x1
FIM
SE delta > 0
ENTÃO INÍCIO
ESCREVA “Existem duas raízes reais”
x1 ←  (- b + 
delta) / ( 2 * a)
x2 ←  (- b - delta) / ( 2 * a)
ESCREVA x1, x2
FIM
FIM
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP4\PASCAL\EX17.PAS e \EXERC\CAP4\PASCAL\EX17.EXE
SOLUÇÃO:
\EXERC\CAP4\C++\EX17.CPP e \EXERC\CAP4\C++\EX17.EXE
SOLUÇÃO:
\EXERC\CAP4\JAVA\EX17.java e \EXERC\CAP4\JAVA\EX17.class
18. Dados três valores X, Y e Z, verifique se eles podem ser os comprimentos dos lados de um triângulo  
e, se forem, verifique se é um triângulo equilátero, isósceles ou escaleno. Se eles não formarem um 
triângulo, escreva uma mensagem. Considere que:
 ■ o comprimento de cada lado de um triângulo é menor que a soma dos outros dois lados; 
 ■ chama-se equilátero o triângulo que tem três lados iguais; 
 ■ denomina-se isósceles o triângulo que tem o comprimento de dois lados iguais; 
 ■ recebe o nome de escaleno o triângulo que tem os três lados diferentes. 
SOLUÇÃO:
ALGORITMO
DECLARE x, y, z NUMÉRICO
LEIA x, y, z
SE x < y + z E y < x + z E z < x + y
ENTÃO INÍCIO
SE x = y E y = z
ENTÃO ESCREVA “Triângulo Equilátero”
PASCAL
C/C++
JAVA

---

Capítulo 4 Estrutura condicional  | 81
ENTÃO ESCREVA “F”
SE peso > 90
ENTÃO ESCREVA “I”
FIM
FIM_ALGORITMO.
1a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL SIMPLES:
\EXERC\CAP4\PASCAL\EX19_A.PAS e \EXERC\CAP4\PASCAL\EX19_A.EXE
2a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL COMPOSTA:
\EXERC\CAP4\PASCAL\EX19_B.PAS e \EXERC\CAP4\PASCAL\EX19_B.EXE
1a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL SIMPLES:
\EXERC\CAP4\C++\EX19_A.CPP e \EXERC\CAP4\C++\EX19_A.EXE
2a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL COMPOSTA:
\EXERC\CAP4\C++\EX19_B.CPP e \EXERC\CAP4\C++\EX19_B.EXE
1a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL SIMPLES:
\EXERC\CAP4\JAVA\EX19_A.java e \EXERC\CAP4\JAVA\EX19_A.class
2a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL COMPOSTA:
\EXERC\CAP4\JAVA\EX19_B.java e \EXERC\CAP4\JAVA\EX19_B.class
20. Faça um programa que receba:
 ■ O código de um produto comprado, supondo que a digitação do código do produto seja sempre 
válida, isto é, um número inteiro entre 1 e 10. 
 ■ O peso do produto em quilos. 
 ■ O código do país de origem, supondo que a digitação do código seja sempre válida, isto é, um nú -
mero inteiro entre 1 e 3.
Tabelas:
CÓDIGO DO PAÍS
DE ORIGEM IMPOSTO
1 0%
2 15%
3 25%
CÓDIGO DO
PRODUTO
PREÇO POR
GRAMA
1 a 4 10
5 a 7 25
8 a 10 35
Calcule e mostre:
 ■ o peso do produto convertido em gramas; 
 ■ o preço total do produto comprado; 
 ■ o valor do imposto, sabendo que ele é cobrado sobre o preço total do produto comprado e depende 
do país de origem; 
 ■ o valor total, preço total do produto mais imposto. 
SOLUÇÃO:
ALGORITMO
DECLARE cod_prod, peso_quilos NUMÉRICO
 cod_pais, peso_gramas, pre_total NUMÉRICO 
 imposto, valor_total, pre_grama NUMÉRICO
LEIA cod_prod, peso_quilos, cod_pais 
peso_gramas ← peso_quilos * 1000
ESCREVA peso_gramas
SE cod_prod >= 1 E cod_prod <= 4 
PASCAL
C/C++
JAVA

---

Capítulo 4 Estrutura condicional  | 83
Tabelas:
CÓDIGO DO ESTADO IMPOSTO
1 35%
2 25%
3 15%
4 5%
5 Isento
CÓDIGO DA CARGA PREÇO POR QUILO
10 a 20 100
21 a 30 250
31 a 40 340
Calcule e mostre:
 ■ o peso da carga do caminhão convertido em quilos; 
 ■ o preço da carga do caminhão; 
 ■ o valor do imposto, sabendo que o imposto é cobrado sobre o preço da carga do caminhão e de -
pende do estado de origem; 
 ■ o valor total transportado pelo caminhão, preço da carga mais imposto. 
SOLUÇÃO:
ALGORITMO
DECLARE cod_est, cod_carga, peso_toneladas NUMÉRICO 
 peso_quilos, pre_carga, imposto, valor_total NUMÉRICO
 LEIA cod_est, peso_toneladas, cod_carga 
peso_quilos ← peso_toneladas * 1000 
ESCREVA peso_quilos
SE cod_carga >= 10 E cod_carga <= 20
ENTÃO pre_carga ←  100 * peso_quilos
SE cod_carga >= 21 E cod_carga <= 30
ENTÃO pre_carga ←  250 * peso_quilos
SE cod_carga >= 31 E cod_carga <= 40
ENTÃO pre_carga ←  340 * peso_quilos
ESCREVA pre_carga
SE cod_est = 1
ENTÃO imposto ←  35/100 * pre_carga
SE cod_est = 2
ENTÃO imposto ←  25/100 * pre_carga
SE cod_est = 3
ENTÃO imposto ←  15/100 * pre_carga
SE cod_est = 4
ENTÃO imposto ←  5/100 * pre_carga
SE cod_est = 5
ENTÃO imposto ←  0
ESCREVA imposto
valor_total ←  pre_carga + imposto
ESCREVA valor_total
FIM_ALGORITMO.
1a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL SIMPLES:
\EXERC\CAP4\PASCAL\EX21_A.PAS e \EXERC\CAP4\PASCAL\EX21_A.EXE
2a SOLUÇÃO – UTILIZANDO ESTRUTURA CONDICIONAL COMPOSTA:
\EXERC\CAP4\PASCAL\EX21_B.PAS e \EXERC\CAP4\PASCAL\EX21_B.EXE
3a SOLUÇÃO – UTILIZANDO ESTRUTURA SELETORA:
\EXERC\CAP4\PASCAL\EX21_C.PAS e \EXERC\CAP4\PASCAL\EX21_C.EXE
PASCAL

---

Capítulo 4 Estrutura condicional  | 85
ENTÃO imposto ← 0
SENÃO SE sal_base <= 450
ENTÃO imposto ← 3/100 * sal_base 
SENÃO SE sal_base < 700
ENTÃO imposto ← 8/100 * sal_base 
SENÃO imposto ← 12/100 * sal_base
ESCREVA imposto 
SE sal_base > 500 
ENTÃO INÍCIO
SE tempo <= 3 
ENTÃO grat ← 20 
SENÃO grat ← 30
FIM 
SENÃO INÍCIO
SE tempo <= 3 
ENTÃO grat ← 23
SENÃO SE tempo < 6
ENTÃO grat ←  35
SENÃO grat ←  33
FIM
ESCREVA grat
sal_liq ← sal_base – imposto + grat
ESCREVA sal_liq
SE sal_liq <= 350
ENTÃO ESCREVA “Classificação A”
SENÃO SE sal_liq < 600
ENTÃO ESCREVA “Classificação B”
SENÃO ESCREVA “Classificação C”
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP4\PASCAL\EX22.PAS e \EXERC\CAP4\PASCAL\EX22.EXE
SOLUÇÃO:
\EXERC\CAP4\C++\EX22.CPP e \EXERC\CAP4\C++\EX22.EXE
SOLUÇÃO:
\EXERC\CAP4\JAVA\EX22.java e \EXERC\CAP4\JAVA\EX22.class
23. Faça um programa que receba o valor do salário mínimo, o turno de trabalho (M — matutino;  V 
— vespertino; ou N — noturno), a categoria (O — operário; G — gerente) e o número de horas tra -
balhadas no mês de um funcionário. Suponha a digitação apenas de dados válidos e, quando houver 
digitação de letras, utilize maiúsculas. Calcule e mostre:
 ■ O coeficiente do salário, de acordo com a tabela a seguir.
TURNO DE TRABALHO VALOR DO COEFICIENTE
M — Matutino 10% do salário mínimo
V — Vespertino 15% do salário mínimo
N — Noturno 12% do salário mínimo
 ■ O valor do salário bruto, ou seja, o número de horas trabalhadas multiplicado pelo valor do coe -
ficiente do salário. 
 ■ O imposto, de acordo com a tabela a seguir. 
PASCAL
C/C++
JAVA

---

Capítulo 4 Estrutura condicional  | 87
ENTÃO auxilio ← 1/3 * sal_bruto
SENÃO auxilio ← 1/2 * sal_bruto
ESCREVA auxilio
sal_liq ← sal_bruto – imposto + grat + auxilio
ESCREVA sal_liq
SE sal_liq < 350
ENTÃO ESCREVA “Mal Remunerado”
SE sal_liq >= 350 E sal_liq <= 600
ENTÃO ESCREVA “Normal”
SE sal_liq > 600
ENTÃO ESCREVA “Bem Remunerado”
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP4\PASCAL\EX23.PAS e \EXERC\CAP4\PASCAL\EX23.EXE
SOLUÇÃO:
\EXERC\CAP4\C++\EX23.CPP e \EXERC\CAP4\C++\EX23.EXE
SOLUÇÃO:
\EXERC\CAP4\JAVA\EX23.java e \EXERC\CAP4\JAVA\EX23.class
24. Faça um programa que receba o preço, o tipo (A — alimentação; L — limpeza; e V — vestuário) e a  
refrigeração (S — produto que necessita de refrigeração; e N — produto que não necessita de refri -
geração) de um produto. Suponha que haverá apenas a digitação de dados válidos e, quando houver 
digitação de letras, utilize maiúsculas. Calcule e mostre:
 ■ O valor adicional, de acordo com a tabela a seguir:
REFRIGERAÇÃO TIPO PREÇO VALOR ADICIONAL
N
A < R$ 15,00 R$ 2,00
>= R$ 15,00 R$ 5,00
L < R$ 10,00 R$ 1,50
>= R$ 10,00 R$ 2,50
V < R$ 30,00 R$ 3,00
>= R$ 30,00 R$ 2,50
S
A R$ 8,00
L R$ 0,00
V R$ 0,00
O valor do imposto, de acordo com a regra a seguir.
PREÇO PERCENTUAL SOBRE O PREÇO
< R$ 25,00 5%
>= R$ 25,00 8%
 ■ O preço de custo, ou seja, preço mais imposto. 
 ■ O desconto, de acordo com a regra a seguir.
O produto que não preencher nenhum dos requisitos a seguir terá desconto de 3%, caso contrário, 
0 (zero).
Os requisitos são:
Tipo: A
Refrigeração: S
PASCAL
C/C++
JAVA

---

Capítulo 4 Estrutura condicional  | 89
ENTÃO ESCREVA “Barato”
SENÃO SE novo_pre < 100
ENTÃO ESCREVA “Normal”
SENÃO ESCREVA “Caro”
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP4\PASCAL\EX24.PAS e \EXERC\CAP4\PASCAL\EX24.EXE
SOLUÇÃO:
\EXERC\CAP4\C++\EX24.CPP e \EXERC\CAP4\C++\EX24.EXE
SOLUÇÃO:
\EXERC\CAP4\JAVA\EX24.java e \EXERC\CAP4\JAVA\EX24.class
25. Faça um programa que receba a medida de um ângulo em graus. Calcule e mostre o quadrante em que 
se localiza esse ângulo. Considere os quadrantes da trigonometria e, para ângulos maiores que 360º ou 
menores que −360º, reduzi-los, mostrando também o número de voltas e o sentido da volta (horário 
ou anti-horário).
SOLUÇÃO:
ALGORITMO
DECLARE angulo, voltas NUMÉRICO
LEIA angulo
SE angulo > 360 OU angulo < -360
ENTÃO INÍCIO
voltas ←  parte inteira(angulo / 360)
angulo ←  RESTO(angulo / 360)
FIM
SENÃO voltas ← 0
SE angulo = 0 OU angulo = 90 OU angulo = 180
OU angulo = 270 OU angulo = 360
OU angulo = -90 OU angulo = -180
OU angulo = -270 OU angulo = -360
ENTÃO ESCREVA “Está em cima de algum dos eixos”
SE (angulo > 0 E angulo < 90) OU (angulo < -270 E angulo > -360)
ENTÃO ESCREVA “1º Quadrante”
SE (angulo > 90 E angulo < 180) OU (angulo < -180 E angulo > -270)
ENTÃO ESCREVA “2º Quadrante”
SE (angulo > 180 E angulo < 270) OU (angulo < -90 E angulo > -180)
ENTÃO ESCREVA “3º Quadrante”
SE (angulo > 270 E angulo < 360) OU (angulo < 0 E angulo > -90)
ENTÃO ESCREVA “4º Quadrante”
ESCREVA voltas, “ volta(s) no sentido “
SE angulo < 0
ENTÃO ESCREVA “horário” 
SENÃO ESCREVA “anti-horário”
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP4\PASCAL\EX25.PAS e \EXERC\CAP4\PASCAL\EX25.EXE
SOLUÇÃO:
\EXERC\CAP4\C++\EX25.CPP e \EXERC\CAP4\C++\EX25.EXE
PASCAL
C/C++
JAVA
PASCAL
C/C++

---

Capítulo 4 Estrutura condicional  | 91
SALDO MÉDIO PERCENTUAL
Acima de R$ 400,00 30% do saldo médio
R$ 400,00 
 R$ 300,00 25% do saldo médio
R$ 300,00  R$ 200,00 20% do saldo médio
Até R$ 200,00 10% do saldo médio
10. O preço ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem do distri-
buidor e dos impostos, ambos aplicados ao custo de fábrica. As porcentagens encontram-se na tabela a 
seguir. Faça um programa que receba o custo de fábrica de um carro e mostre o preço ao consumidor.
CUSTO DE FÁBRICA % DO DISTRIBUIDOR % dos IMPOSTOS
Até R$ 12.000,00 5 isento
Entre R$ 12.000,00 e R$ 25.000,00 10 15
Acima de R$ 25.000,00 15 20
11. Faça um programa que receba o salário atual de um funcionário e, usando a tabela a seguir, calcule e 
mostre o valor do aumento e o novo salário.
SALÁRIO PERCENTUAL DE AUMENTO
Até R$ 300,00 15% 
R$ 300,00 
 R$ 600,00 10% 
R$ 600,00  R$ 900,00 5% 
Acima de R$ 900,00 0% 
12. Faça um programa que receba o salário bruto de um funcionário e, usando a tabela a seguir, calcule e 
mostre o valor a receber. Sabe-se que este é composto pelo salário bruto acrescido de gratificação e des-
contado o imposto de 7% sobre o salário.
TABELA DAS GRATIFICAÇÕES
SALÁRIO GRATIFICAÇÃO
Até R$ 350,00 R$ 100,00
R$ 350,00 
 R$ 600,00 R$ 75,00
R$ 600,00  R$ 900,00 R$ 50,00
Acima de R$ 900,00 R$ 35,00
13. Faça um programa que receba o preço de um produto, calcule e mostre, de acordo com as tabelas a se-
guir, o novo preço e a classificação.
TABELA 1 —  PERCENTUAL DE AUMENTO
PREÇO %
Até R$ 50,00 5
Entre R$ 50,00 e R$ 100,00 10
Acima de R$ 100,00 15
TABELA 2 —  CLASSIFICAÇÕES
NOVO PREÇO CLASSIFICAÇÃO
Até R$ 80,00 Barato
Entre R$ 80,00 e R$ 120,00 (inclusive) Normal
Entre R$ 120,00 e R$ 200,00 (inclusive) Caro
Maior que R$ 200,00 Muito caro

---

Capítulo 4 Estrutura condicional  | 93
CÓDIGO DE ORIGEM PROCEDÊNCIA
1 Sul
2 Norte
3 Leste
4 Oeste
5 ou 6 Nordeste
7 ou 8 ou 9 Sudeste
10 a 20 Centro-oeste
21 a 30 Nordeste
22. Faça um programa que receba a idade e o peso de uma pessoa. De acordo com a tabela a seguir, verifique 
e mostre em qual grupo de risco essa pessoa se encaixa.
IDADE
PESO
Até 60 Entre 60 e 90 (inclusive) Acima de 90
Menores que 20 9 8 7
De 20 a 50 6 5 4
Maiores que 50 3 2 1
23. Faça um programa que receba: 
 ■ o código do produto comprado; e
 ■ a quantidade comprada do produto.
Calcule e mostre: 
 ■ o preço unitário do produto comprado, seguindo a Tabela I; 
 ■ o preço total da nota; 
 ■ o valor do desconto, seguindo a Tabela II e aplicado sobre o preço total da nota; e
 ■ o preço final da nota depois do desconto. 
TABELA I
CÓDIGO PREÇO
1 a 10 R$ 10,00
11 a 20 R$ 15,00
21 a 30 R$ 20,00
31 a 40 R$ 30,00
TABELA II
PREÇO TOTAL DA NOTA % DE DESCONTO
Até R$ 250,00 5%
Entre R$ 250,00 e R$ 500,00 10%
Acima de R$ 500,00 15%
24. Faça um programa que receba o preço, a categoria (1 — limpeza; 2 — alimentação; ou 3 — vestuário) 
e a situação (R — produtos que necessitam de refrigeração; e N — produtos que não necessitam de re -
frigeração). 
Calcule e mostre:
 ■ O valor do aumento, usando as regras que se seguem.
PREÇO CATEGORIA PERCENTUAL DE AUMENTO
< = 25
1 5%
2 8%
3 10%
> 25
1 12%
2 15%
3 18%
 ■ O valor do imposto, usando as regras a seguir.

---



=== CAPÍTULO 5 ===

---

Capítulo 5 Estrutura de repetição  | 97
Exemplo de contador:
CONT ← 0  // inicialização da variável CONT com o valor zero
PARA I ← 1 ATÉ 5 FAÇA 
INÍCIO
 ESCREVA “Digite um número: “
 LEIA NUM
 SE (NUM > 5)
 ENTÃO CONT ← CONT + 1 // contando mais 1 na variável CONT
FIM
ESCREVA “Quantidade de número maiores que 5 = “,CONT
Simulação:
MEMÓRIA TELA
I NUM CONT
0
Inicialização da variável CONT com o valor 
zero
CONT ← 0
1 Digite um número: 5
1 5
1 5 0 O número digitado não é maior que 5, 
logo, o contador CONT não será alterado
2 Digite um número: 12
2 12
2 12 1
O número digitado é maior que 5, logo, 
o contador CONT será incrementado em 
1 unidade
CONT ← CONT + 1 
3 Digite um número: 8
3 8
3 8 2
O número digitado é maior que 5, logo, 
o contador CONT será incrementado em 
1 unidade
CONT ← CONT + 1 
4 Digite um número: 3
4 3
4 3 2 O número digitado não é maior que 5, 
logo, o contador CONT não será alterado
5 Digite um número: 6
5 6
5 6 3
O número digitado é maior que 5, logo, 
o contador CONT será incrementado em 
1 unidade
CONT ← CONT + 1 
Quantidade de números maiores que 5 = 3
5.1.2  Estrutura de repetição para número indeﬁnido de repetições e teste no início (estrutura  
ENQUANTO)
Essa estrutura de repetição é utilizada quando não se sabe o número de vezes que um trecho do algorit-
mo deve ser repetido, embora também possa ser utilizada quando se conhece esse número.
Essa estrutura baseia-se na análise de uma condição. A repetição será feita enquanto a condição se 
mostrar verdadeira.

---

Capítulo 5 Estrutura de repetição  | 99
No trecho do algoritmo anterior, portanto, os comandos que se localizam na estrutura de repetição são 
repetidos cinco vezes. Nesse exemplo, a estrutura ENQUANTO é utilizada para repetir o trecho do algoritmo 
em um número definido de vezes.
5.1.3  Estrutura de repetição para número indeﬁnido de repetições e teste no ﬁnal (estrutura REPITA) 
Essa estrutura de repetição é utilizada quando não se sabe o número de vezes que um trecho do algorit-
mo deve ser repetido, embora também possa ser utilizada quando se conhece esse número.
Essa estrutura baseia-se na análise de uma condição. A repetição será feita até a condição se tornar 
verdadeira.
A diferença entre a estrutura ENQUANTO e a estrutura REPITA é que, nessa última, os comandos serão 
repetidos pelo menos uma vez, já que a condição de parada se encontra no final.
REPITA
comandos
ATÉ condição
Repita os comandos até a condição se tornar verdadeira.
Exemplos:
X ← 1  // inicialização da variável X com o valor 1
Y ← 5  // inicialização da variável Y com o valor 5
REPITA
X ← X + 2 // contador incrementado em 2 unidades
Y ← Y + 1 // contador incrementado em 1 unidade
ATÉ X >= Y
Simulação:
X Y
1 5 Valores iniciais
3 6
Valores obtidos dentro da estrutura de repetição
5 7
7 8
9 9
No trecho do algoritmo anterior, portanto, os comandos escritos dentro da estrutura de repetição são 
repetidos quatro vezes.
X ← 1   // inicialização da variável X com o valor 1
Y ← 1   // inicialização da variável Y com o valor 1
REPITA
Y ← Y * X  // acumulador das multiplicações
X ← X + 1  // contador incrementado em 1 unidade
ATÉ X = 6
Simulação:
Y X
1 1 Valores iniciais
1 2
Valores obtidos dentro da estrutura de repetição
2 3
6 4
24 5
120 6

---

Capítulo 5 Estrutura de repetição  | 101
Existem duas instruções comumente usadas nos comandos internos das estruturas de repetição. São as 
instruções denominadas acumuladores e contadores.
Os acumuladores devem ser usados quando a realização de um cálculo precisa de valores obtidos a cada 
iteração, ou seja, o cálculo só estará pronto com a conclusão da repetição. É por isso que um acumulador deve 
ser inicializado com um valor neutro para a operação em que será utilizado. Por exemplo, se for usado em 
uma adição, deve ser inicializado com zero, e se for usado em uma multiplicação, deve ser inicializado com 1. 
Exemplo de acumulador:
SOMA := 0;      // inicialização da variável SOMA com o valor zero
FOR I := 1 TO 5 DO 
BEGIN
  WRITE(‘Digite um número: ‘);
  READLN(NUM);
  SOMA := SOMA + NUM; // acumulando o valor da variável NUM na variável SOMA
END;
WRITELN(‘Soma = ‘,SOMA);
Simulação:
MEMÓRIA TELA
I NUM SOMA
0 Inicialização da variável SOMA com o valor zero
SOMA := 0;
1 Digite um número: 5
1 5
1 5 5 Acumulando o valor da variável NUM na variável SOMA
SOMA := SOMA + NUM; 
2 Digite um número: 3
2 3
2 3 8 Acumulando o valor da variável NUM na variável SOMA
SOMA := SOMA + NUM;
3 Digite um número: 0
3 0
3 0 8 Acumulando o valor da variável NUM na variável SOMA
SOMA := SOMA + NUM;
4 Digite um número: 10
4 10
4 10 18 Acumulando o valor da variável NUM na variável SOMA
SOMA := SOMA + NUM;
5 Digite um número: 2
5 2
5 2 20 Acumulando o valor da variável NUM na variável SOMA
SOMA := SOMA + NUM;
Soma = 20
Exemplo de contador:
CONT := 0; // inicialização da variável CONT com o valor zero
FOR I := 1 TO 5 DO 
BEGIN

---

Capítulo 5 Estrutura de repetição  | 103
Exemplos:
X := 0;  // inicialização da variável X com o valor zero
WHILE X <> 5 DO
BEGIN
WRITELN(‘Valor de X = ‘,X);
X := X + 1; // contador incrementado em 1 unidade
END;
WRITELN(‘Valor de X depois que sair da estrutura = ‘,X);
No trecho de programa anterior, os comandos WRITELN(‘Valor de X = ‘,X)  e X := X + 1 ; foram 
executados cinco vezes. O teste condicional avalia X valendo 0, 1, 2, 3, 4 e 5.
Simulação:
TELA X
0 Valor inicial
Valor de X = 0 1
Valores obtidos dentro da estrutura de repetiçãoValor de X = 1 2
Valor de X = 2 3
Valor de X = 3 4
Valor de X = 4 5 Valor obtido dentro da estrutura de repetição, que  
torna a condição falsa e interrompe a repetição
Valor de X depois que
sair da estrutura = 5
X := 1;  // inicialização da variável X com o valor 1
Y := 10;  // inicialização da variável Y com o valor 10
WHILE Y > X DO
BEGIN
WRITELN(‘Valor de Y = ‘,Y);
Y := Y – 2; // contador decrementado em 2 unidades
END;
WRITELN(‘Valor de Y depois que sair da estrutura = ‘,Y);
No trecho de programa anterior, os comandos WRITELN(‘Valor de Y = ‘,Y) ; e Y := Y – 2 ; foram 
executados cinco vezes. O teste condicional avalia Y valendo 10, 8, 6, 4, 2 e 0.
Simulação:
TELA X Y
1 10 Valores iniciais
Valor de Y = 10 1 8
Valores obtidos dentro da estrutura de repetiçãoValor de Y = 8 1 6
Valor de Y = 6 1 4
Valor de Y = 4 1 2
Valor de Y = 2 1 0 Valor obtido dentro da estrutura de repetição, que  
torna a condição falsa e interrompe a repetição
Valor de Y depois que
sair da estrutura = 0
X := 1;  // inicialização da variável X com o valor 1
Y := 1;   // inicialização da variável Y com o valor 1
WHILE X < Y DO
BEGIN
WRITELN(‘Valor de X = ‘,X);

---

Capítulo 5 Estrutura de repetição  | 105
Simulação:
TELA X Y
1 10 Valores iniciais
Valor de Y = 10 1 8
Valores obtidos dentro da estrutura de repetiçãoValor de Y = 8 1 6
Valor de Y = 6 1 4
Valor de Y = 4 1 2
Valor de Y = 2 1 0 Valor obtido dentro da estrutura de repetição, que  
torna a condição verdadeira e interrompe a repetição
Valor de Y depois que
sair da estrutura = 0
5.3 Estrutura de repetição em C/C++
5.3.1 Estrutura de repetição FOR
Essa estrutura de repetição é utilizada quando se sabe o número de vezes que um trecho do programa 
deve ser repetido.
O formato geral do comando for é composto por três partes:
for (i = valor_inicial; condição; incremento ou decremento de i) 
comando;
A primeira parte atribui um valor_inicial à variável i, que tem como função controlar o número 
necessário de repetições.
A segunda parte corresponde a uma expressão relacional que, quando assumir o valor falso, determi -
nará o fim da repetição.
A terceira parte é responsável por alterar o valor da variável i (incremento ou decremento) com o ob-
jetivo de, em algum momento, fazer a condição assumir o valor falso.
Caso seja necessária a repetição de apenas um comando, o compilador entenderá que a estrutura de 
repetição terminará quando for encontrado o primeiro ; (ponto e vírgula).
Exemplo:
for (a = 1;a <= 20;a++)
printf(“\no valor de a é: %d”,a);
No exemplo anterior, à variável a é atribuído inicialmente o valor 1 (a = 1) que, depois, é incrementado em 
uma unidade (a++).
A cada incremento, o comando printf será executado. Esse processo se repete até o valor da variável a se 
tornar maior que 20 (quando a condição a <= 20 assumir o valor falso).
Se for necessária a repetição de mais de um comando, o compilador entenderá que a estrutura de repetição 
começará quando for encontrado o símbolo { e terminará quando for encontrado o símbolo }.
Exemplo:
for (a = 15;a >= 1;a = a-2)
{
printf(“Digite um número: “); 
scanf(“%d%*c”,&x);
}
No exemplo anterior, a variável a é inicializada com o valor 15 (a = 15) que, depois, é decrementada 
em duas unidades (a = a -2).
A cada decremento, o bloco de comando que está entre chaves { ... } é executado. Esse processo se repete 
até o valor da variável a se tornar menor que 1 (quando a condição a >= 1 assumir o valor falso).

---

Capítulo 5 Estrutura de repetição  | 107
Simulação:
MEMÓRIA TELA
I NUM SOMA
0 Inicialização da variável SOMA com o valor zero
SOMA = 0;
1 Digite um número: 5
1 5
1 5 5 Acumulando o valor da variável NUM na variável SOMA
SOMA = SOMA + NUM; 
2 Digite um número: 3
2 3
2 3 8 Acumulando o valor da variável NUM na variável SOMA
SOMA = SOMA + NUM;
3 Digite um número: 0
3 0
3 0 8 Acumulando o valor da variável NUM na variável SOMA
SOMA = SOMA + NUM;
4 Digite um número: 10
4 10
4 10 18 Acumulando o valor da variável NUM na variável SOMA
SOMA = SOMA + NUM;
5 Digite um número: 2
5 2
5 2 20 Acumulando o valor da variável NUM na variável SOMA
SOMA = SOMA + NUM;
Soma = 20
Exemplo de contador:
CONT = 0;  // inicialização da variável CONT com o valor zero
for(I = 1; I<= 5; I++) 
{
 printf(“Digite um número: “);
 scanf(“%d%*c”,&NUM);
 if (NUM > 5)
  CONT = CONT + 1; // contando mais 1 na variável CONT
}
printf(“Quantidade de número maiores que 5 = %d”,CONT);
Simulação:
MEMÓRIA TELA
I NUM CONT
0 Inicialização da variável CONT com o valor zero
CONT = 0;
1 Digite um número: 5
1 5
1 5 0 O número digitado não é maior que 5, logo, o 
contador CONT não será alterado
2 Digite um número: 12
2 12

---

Capítulo 5 Estrutura de repetição  | 109
Exemplos:
X = 0;  // inicialização da variável x com o valor 0
while (X != 5)
{
   printf(“Valor de X = %d”,X);
   X = X + 1;  // contador incrementado em 1 unidade
}
printf(“Valor de X depois que sair da estrutura = %d”,X);
No trecho de programa anterior, os comandos printf(“Valor de X = %d”,X) ; e X = X + 1 ; foram 
executados cinco vezes. O teste condicional avalia X valendo 0, 1, 2, 3, 4 e 5.
Simulação:
TELA X
0 Valor inicial
Valor de X = 0 1
Valores obtidos dentro da estrutura de repetiçãoValor de X = 1 2
Valor de X = 2 3
Valor de X = 3 4
Valor de X = 4 5 Valor obtido dentro da estrutura de repetição, que  
torna a condição falsa e interrompe a repetição
Valor de X depois que
sair da estrutura = 5
X = 1;  // inicialização da variável X com o valor 1
Y = 10;  // inicialização da variável Y com o valor 10
while (Y > X)
{
   printf(“Valor de Y = %d”,Y); 
   Y = Y – 2; // contador decrementado em 2 unidades
}
printf(“Valor de Y depois que sair da estrutura = %d”,Y);
No trecho de programa acima, os comandos printf(“Valor de Y = %d”,Y) ; e Y = Y – 2 ; foram 
executados cinco vezes. O teste condicional avalia Y valendo 10, 8, 6, 4, 2 e 0.
Simulação:
TELA X Y
1 10 Valores iniciais
Valor de Y = 10 1 8
Valores obtidos dentro da estrutura de repetiçãoValor de Y = 8 1 6
Valor de Y = 6 1 4
Valor de Y = 4 1 2
Valor de Y = 2 1 0 Valor obtido dentro da estrutura de repetição, que  torna a 
condição falsa e interrompe a repetição
Valor de Y depois que
sair da estrutura = 0
X = 1;  // inicialização da variável X com o valor 1
Y = 1;  // inicialização da variável Y com o valor 1
while (X < Y)
{

---

Capítulo 5 Estrutura de repetição  | 111
No trecho de programa anterior, os comandos printf(“Valor de Y = %d”,Y); e Y = Y – 2; são exe-
cutados cinco vezes. O teste condicional avalia Y valendo 8, 6, 4, 2 e 0.
Simulação:
TELA X Y
1 10 Valores iniciais
Valor de Y = 10 1 8
Valores obtidos dentro da estrutura de repetiçãoValor de Y = 8 1 6
Valor de Y = 6 1 4
Valor de Y = 4 1 2
Valor de Y = 2 1 0 Valor obtido dentro da estrutura de repetição, que  torna a 
condição falsa e interrompe a repetição
Valor de Y depois que
sair da estrutura = 0
5.4 Estrutura de repetição em JAVA
5.4.1 Estrutura de repetição FOR
Essa estrutura de repetição é utilizada quando se sabe o número de vezes que um trecho do programa 
deve ser repetido.
O formato geral do comando FOR é composto por três partes:
for (i=valor_inicial; condição; incremento ou decremento de i) 
comando;
A primeira parte atribui um valor_inicial à variável i, que tem como função controlar o número 
necessário de repetições.
A segunda parte corresponde a uma expressão relacional que, quando assumir o valor falso, determi -
nará o fim da repetição.
A terceira parte é responsável por alterar o valor da variável i (incremento ou decremento) com o ob-
jetivo de, em algum momento, fazer a condição assumir o valor falso.
Caso seja necessária a repetição de apenas um comando, o compilador entenderá que a estrutura de 
repetição terminará quando for encontrado o primeiro ; (ponto e vírgula).
Exemplo:
for (a=1;a<=20;a++)
System.out.println(“O valor de a é: “ +a);
No exemplo anterior, a variável a é inicializada com o valor 1 (a=1) e é incrementada em uma unidade 
(a++). A cada incremento, o comando System.out.println é executado. Esse processo se repete até o valor da 
variável a se tornar maior que 20 (quando a condição a <= 20 assumir o valor falso).
Se for necessária a repetição de mais de um comando, a linguagem entenderá que a estrutura de repeti-
ção começará quando for encontrado o símbolo { e terminará quando for encontrado o símbolo }.
Exemplo:
for (a=15;a>=1;a=a-2)
{
System.out.println(“Digite um número: “); 
dado = new Scanner(System.in);
x = dado.nextInt();
}

---

Capítulo 5 Estrutura de repetição  | 113
Simulação:
MEMÓRIA TELA
I NUM SOMA
0 Inicialização da variável SOMA com o valor zero
SOMA = 0;
1 Digite um número: 5
1 5
1 5 5 Acumulando o valor da variável NUM na variável SOMA
SOMA = SOMA + NUM; 
2 Digite um número: 3
2 3
2 3 8 Acumulando o valor da variável NUM na variável SOMA
SOMA = SOMA + NUM;
3 Digite um número: 0
3 0
3 0 8 Acumulando o valor da variável NUM na variável SOMA
SOMA = SOMA + NUM;
4 Digite um número: 10
4 10
4 10 18 Acumulando o valor da variável NUM na variável SOMA
SOMA = SOMA + NUM;
5 Digite um número: 2
5 2
5 2 20 Acumulando o valor da variável NUM na variável SOMA
SOMA = SOMA + NUM;
Soma = 20
Exemplo de contador:
CONT = 0;      // inicialização da variável CONT com o valor zero
for(I = 1; I <= 5; I++) 
{
 System.out.print(“Digite um número: “);
 NUM = dado.nextInt();
 if (NUM > 5)
  CONT = CONT + 1; // contando mais 1 na variável CONT
}
System.out.println(“Quantidade de número maiores que 5 = ”+ CONT);
Simulação:
MEMÓRIA TELA
I NUM CONT
0 Inicialização da variável CONT com o valor zero
CONT = 0;
1 Digite um número: 5
1 5
1 5 0 O número digitado não é maior que 5, logo, o contador 
CONT não será alterado
2 Digite um número: 12
2 12
2 12 1
O número digitado é maior que 5, logo, o contador 
CONT será incrementado em 1 unidade
CONT = CONT + 1;

---

Capítulo 5 Estrutura de repetição  | 115
   System.out.println(“Valor de X = “+X); 
   X = X + 1; // contador incrementado em 1 unidade
}
System.out.println(“Valor de X depois que sair da estrutura = “+X);
No trecho de programa anterior, os comandos System.out.println(“Valor de X = “+X); e X = X + 1; 
foram executados cinco vezes. O teste condicional avalia X valendo 0, 1, 2, 3, 4 e 5.
Simulação:
TELA X
0 Valor inicial
Valor de X = 0 1
Valores obtidos dentro da estrutura de repetiçãoValor de X = 1 2
Valor de X = 2 3
Valor de X = 3 4
Valor de X = 4 5 Valor obtido dentro da estrutura de repetição, que  
torna a condição falsa e interrompe a repetição
Valor de X depois que
sair da estrutura = 5
X = 1;  // inicialização da variável X com o valor 1
Y = 10;  // inicialização da variável Y com o valor 10
while (Y > X)
{
   System.out.println(“Valor de Y = “+Y);
   Y = Y – 2; // contador decrementado em 2 unidades
}
System.out.println(“Valor de Y depois que sair da estrutura = “+Y);
No trecho de programa anterior, os comandos System.out.println(“Valor de Y = “+Y); e Y = Y – 2; 
são executados cinco vezes. O teste condicional avalia Y valendo 10, 8, 6, 4, 2 e 0.
TELA X Y
1 10 Valores iniciais
Valor de Y = 10 1 8
Valores obtidos dentro da estrutura de repetiçãoValor de Y = 8 1 6
Valor de Y = 6 1 4
Valor de Y = 4 1 2
Valor de Y = 2 1 0 Valor obtido dentro da estrutura de repetição, que  torna a 
condição falsa e interrompe a repetição
Valor de Y depois que
sair da estrutura = 0
X = 1;  // inicialização da variável X com o valor 1
Y = 1;   // inicialização da variável Y com o valor 1
while (X < Y)
{
   System.out.println(“Valor de X = “+X); 
   X = X + 1;  // contador incrementado em 1 unidade
}
No trecho de programa, os comandos System.out.println(“Valor de X = “+X); e X = X + 1; não 
serão executados, pois com os valores iniciais de X e Y a condição é falsa. Logo, não ocorrerá a entrada na 
estrutura de repetição para execução dos seus comandos.

---

Capítulo 5 Estrutura de repetição  | 117
Simulação:
TELA X Y
1 10 Valores iniciais
Valor de Y = 10 1 8
Valores obtidos dentro da estrutura de repetiçãoValor de Y = 8 1 6
Valor de Y = 6 1 4
Valor de Y = 4 1 2
Valor de Y = 2 1 0 Valor obtido dentro da estrutura de repetição, que  torna a 
condição verdadeira e interrompe a repetição
Valor de Y depois que
sair da estrutura = 0
EXERCÍCIOS RESOLVIDOS
1. Um funcionário de uma empresa recebe, anualmente, aumento salarial. Sabe-se que: 
a) Esse funcionário foi contratado em 2005, com salário inicial de R$ 1.000,00. 
b) Em 2006, ele recebeu aumento de 1,5% sobre seu salário inicial. 
c) A partir de 2007 (inclusive), os aumentos salariais sempre corresponderam ao dobro do percentual do ano 
anterior. 
Faça um programa que determine o salário atual desse funcionário.
SOLUÇÃO:
ALGORITMO
DECLARE i, ano_atual, salario NUMÉRICO 
novo_salario, percentual NUMÉRICO
LEIA ano_atual 
salario ← 1000 
percentual ← 1.5/100
novo_salario ← salario + percentual * salario 
PARA i ← 2007 ATÉ ano_atual FAÇA
INÍCIO
percentual ←  2 * percentual
novo_salario ← novo_salario + percentual * novo_salario 
FIM
ESCREVA novo_salario 
FIM_ALGORITMO.
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\PASCAL\EX1_A.PAS e \EXERC\CAP5\PASCAL\EX1_A.EXE
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\PASCAL\EX1_B.PAS e \EXERC\CAP5\PASCAL\EX1_B.EXE
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\C++\EX1_A.CPP e \EXERC\CAP5\C++\EX1_A.EXE
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\C++\EX1_B.CPP e \EXERC\CAP5\C++\EX1_B.EXE
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\JAVA\EX1_A.java e \EXERC\CAP5\JAVA\EX1_A.class
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\JAVA\EX1_B.java e \EXERC\CAP5\JAVA\EX1_B.class
PASCAL
C/C++
JAVA

---

Capítulo 5 Estrutura de repetição  | 119
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\PASCAL\EX3_A.PAS e \EXERC\CAP5\PASCAL\EX3_A.EXE
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\PASCAL\EX3_B.PAS e \EXERC\CAP5\PASCAL\EX3_B.EXE
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\C++\EX3_A.CPP e \EXERC\CAP5\C++\EX3_A.EXE
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\C++\EX3_B.CPP e \EXERC\CAP5\C++\EX3_B.EXE
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\JAVA\EX3_A.java e \EXERC\CAP5\JAVA\EX3_A.class
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\JAVA\EX3_B.java e \EXERC\CAP5\JAVA\EX3_B.class
4. Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.  
Foram obtidos os seguintes dados:
a) código da cidade; 
b) número de veículos de passeio; 
c) número de acidentes de trânsito com vítimas. 
Deseja-se saber:
a) qual é o maior e qual é o menor índice de acidentes de trânsito e a que cidades pertencem; 
b) qual é a média de veículos nas cinco cidades juntas; 
c) qual é a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio. 
SOLUÇÃO:
ALGORITMO
DECLARE cont, cod, num_vei, num_acid NUMÉRICO
maior, cid_maior, menor, cid_menor NUMÉRICO
media_vei, soma_vei, media_acid NUMÉRICO
soma_acid, cont_acid NUMÉRICO
soma_vei ←  0
soma_acid ←  0
cont_acid ←  0
PARA cont ←  1 ATÉ 5 FAÇA
INÍCIO
LEIA cod, num_vei, num_acid
SE cont = 1
ENTÃO INÍCIO
maior ←  num_acid
cid_maior ←  cod
menor ←  num_acid
cid_menor ←  cod
FIM
SENÃO INÍCIO
SE num_acid > maior
ENTÃO INÍCIO
maior ←  num_acid
cid_maior ←  cod
FIM
SE num_acid < menor
ENTÃO INÍCIO
menor ←  num_acid
PASCAL
C/C++
JAVA

---

Capítulo 5 Estrutura de repetição  | 121
PARA   j ←  1 ATÉ fim FAÇA
INÍCIO
fat ← fat * j
FIM
expoente ←  i + 1 
SE RESTO (expoente/2) =0 
ENTÃO s ← s – x expoente/fat
SENÃO s ← s + x expoente/fat
SE denominador = 4
ENTÃO den ←  -1
SE denominador =1
ENTÃO den ←1 
SE den= 1 
ENTÃO denominador ←denominador + 1 
SENÃO denominador ←denominador – 1 
FIM
ESCREVA s
FIM_ALGORITMO.   
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\PASCAL\EX5_A.PAS e \EXERC\CAP5\PASCAL\EX5_A.EXE
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\PASCAL\EX5_B.PAS e \EXERC\CAP5\PASCAL\EX5_B.EXE
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\C++\EX5_A.CPP e \EXERC\CAP5\C++\EX5_A.EXE
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\C++\EX5_B.CPP e \EXERC\CAP5\C++\EX5_B.EXE
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\JAVA\EX5_A.java e \EXERC\CAP5\JAVA\EX5_A.class
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\JAVA\EX5_B.java e \EXERC\CAP5\JAVA\EX5_B.class
6. Uma empresa possui dez funcionários com as seguintes características: código, número de horas traba-
lhadas no mês, turno de trabalho (M — matutino; V — vespertino; ou N — noturno), categoria (O — 
operário; ou G — gerente), valor da hora trabalhada. Sabendo-se que essa empresa deseja informatizar 
sua folha de pagamento, faça um programa que:
a) Leia as informações dos funcionários, exceto o valor da hora trabalhada, não permitindo que sejam informa-
dos turnos e nem categorias inexistentes. Trabalhe sempre com a digitação de letras maiúsculas. 
b) Calcule o valor da hora trabalhada, conforme a tabela a seguir. Adote o valor de R$ 450,00 para o salário 
mínimo. 
CATEGORIA TURNO VALOR DA HORA TRABALHADA
G N 18% do salário mínimo
G M ou V 15% do salário mínimo
O N 13% do salário mínimo
O M ou V 10% do salário mínimo
c) Calcule o salário inicial dos funcionários com base no valor da hora trabalhada e no número de horas traba-
lhadas. 
d) Calcule o valor do auxílio alimentação recebido pelo funcionário de acordo com seu salário inicial, conforme 
a tabela a seguir. 
PASCAL
C/C++
JAVA

---

Capítulo 5 Estrutura de repetição  | 123
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\C++\EX6_A.CPP e \EXERC\CAP5\C++\EX6_A.EXE
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA DO-WHILE:
\EXERC\CAP5\C++\EX6_B.CPP e \EXERC\CAP5\C++\EX6_B.EXE
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\JAVA\EX6_A.java e \EXERC\CAP5\JAVA\EX6_A.class
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA DO-WHILE:
\EXERC\CAP5\JAVA\EX6_B.java e \EXERC\CAP5\JAVA\EX6_B.class
7. Faça um programa que monte os oito primeiros termos da sequência de Fibonacci.
0-1-1-2-3-5-8-13-21-34-55...
SOLUÇÃO:
ALGORITMO
DECLARE cont, num1, num2, res NUMÉRICO
num1 ← 0 
num2 ← 1 
ESCREVA num1 
ESCREVA num2
PARA cont ←  3 ATÉ 8 FAÇA
INÍCIO
res ←  num1 + num2
ESCREVA res
num1 ←  num2
num2 ←  res
FIM
FIM_ALGORITMO.
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\PASCAL\EX7_A.PAS e \EXERC\CAP5\PASCAL\EX7_A.EXE
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA REPEAT:
\EXERC\CAP5\PASCAL\EX7_B.PAS e \EXERC\CAP5\PASCAL\EX7_B.EXE
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\C++\EX7_A.CPP e \EXERC\CAP5\C++\EX7_A.EXE
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA DO-WHILE:
\EXERC\CAP5\C++\EX7_B.CPP e \EXERC\CAP5\C++\EX7_B.EXE
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\JAVA\EX7_A.java e \EXERC\CAP5\JAVA\EX7_A.class
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA DO-WHILE:
\EXERC\CAP5\JAVA\EX7_B.java e \EXERC\CAP5\JAVA\EX7_B.class
8. Faça um programa que leia o número de termos, determine e mostre os valores de acordo com a série 
a seguir:
Série = 2, 7, 3, 4, 21, 12, 8, 63, 48, 16, 189, 192, 32, 567, 768...
C/C++
JAVA
PASCAL
C/C++
JAVA

---

Capítulo 5 Estrutura de repetição  | 125
MÉDIA ARITMÉTICA MENSAGEM
Até 3 Reprovado
Entre 3 e 7 Exame
De 7 para cima Aprovado
 ■ o total de alunos aprovados; 
 ■ o total de alunos de exame; 
 ■ o total de alunos reprovados; 
 ■ a média da classe. 
SOLUÇÃO:
ALGORITMO
DECLARE cont, n1, n2, media, ta, te, tr NUMÉRICO 
media_classe, total_classe NUMÉRICO
total_classe ←  0
PARA cont ← 1 ATÉ 6 FAÇA 
INÍCIO
LEIA n1, n2
media ← (n1 + n2) /2 
ESCREVA media
SE media <= 3 
ENTÃO INÍCIO
tr ← tr + 1 
ESCREVA “Reprovado” 
FIM
SE media > 3 E media < 7 
ENTÃO INÍCIO
te ← te + 1 
ESCREVA “Exame” 
FIM
SE media >= 7 
ENTÃO INÍCIO
ta ← ta + 1 
ESCREVA “Aprovado” 
FIM
total_classe ← total_classe + media 
FIM
ESCREVA tr 
ESCREVA te 
ESCREVA ta
media_classe ← total_classe/6 
ESCREVA media_classe 
FIM_ALGORITMO.
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\PASCAL\EX9_A.PAS e \EXERC\CAP5\PASCAL\EX9_A.EXE
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\PASCAL\EX9_B.PAS e \EXERC\CAP5\PASCAL\EX9_B.EXE
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\C++\EX9_A.CPP e \EXERC\CAP5\C++\EX9_A.EXE
PASCAL
C/C++

---

Capítulo 5 Estrutura de repetição  | 127
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\JAVA\EX10_A.java e \EXERC\CAP5\JAVA\EX10_A.class
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\JAVA\EX10_B.java e \EXERC\CAP5\JAVA\EX10_B.class
11. Faça um programa que receba um número inteiro maior que 1, verifique se o número fornecido é pri-
mo ou não e mostre uma mensagem de número primo ou de número não primo.
Um número é primo quando é divisível apenas por 1 e por ele mesmo.
SOLUÇÃO:
ALGORITMO
DECLARE i, num, qtde NUMÉRICO
LEIA num
qtde ←  0
PARA i ← 1 ATÉ num  FAÇA
INÍCIO
SE RESTO(num/i) = 0
ENTÃO qtde ← qtde + 1
FIM
SE qtde > 2
ENTÃO ESCREVA “Número não primo”
SENÃO ESCREVA “Número primo”
FIM_ALGORITMO.
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\PASCAL\EX11_A.PAS e \EXERC\CAP5\PASCAL\EX11_A.EXE
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA REPEAT:
\EXERC\CAP5\PASCAL\EX11_B.PAS e \EXERC\CAP5\PASCAL\EX11_B.EXE
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\C++\EX11_A.CPP e \EXERC\CAP5\C++\EX11_A.EXE
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA DO-WHILE:
\EXERC\CAP5\C++\EX11_B.CPP e \EXERC\CAP5\C++\EX11_B.EXE
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\JAVA\EX11_A.java e \EXERC\CAP5\JAVA\EX11_A.class
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA DO-WHILE:
\EXERC\CAP5\JAVA\EX11_B.java e \EXERC\CAP5\JAVA\EX11_B.class
12. Em uma fábrica trabalham homens e mulheres divididos em três classes: 
 ■ trabalhadores que fazem até 30 peças por mês — classe 1; 
 ■ trabalhadores que fazem de 31 a 50 peças por mês — classe 2; 
 ■ trabalhadores que fazem mais de 50 peças por mês — classe 3. 
A classe 1 recebe salário mínimo. A classe 2 recebe salário mínimo mais 3% deste salário por peça, 
acima das 30 peças iniciais. A classe 3 recebe salário mínimo mais 5% desse salário por peça, acima das 30 
peças iniciais.
Faça um programa que receba o número do operário, o número de peças fabricadas no mês, o sexo do 
operário, e que também calcule e mostre:
 ■ o número do operário e seu salário; 
 ■ o total da folha de pagamento da fábrica; 
 ■ o número total de peças fabricadas no mês; 
JAVA
PASCAL
C/C++
JAVA

---

Capítulo 5 Estrutura de repetição  | 129
ESCREVA “Total da folha de pagamento = “, tot_folha
ESCREVA “Total de peças fabricadas no mês = “,tot_pecas
SE cont_m = 0
ENTÃO ESCREVA “NENHUM HOMEM”
SENÃO INÍCIO
media_m ←  media_m / cont_m
ESCREVA “Média de peças fabricadas por homens = “, media_m
FIM
SE cont_f = 0
ENTÃO ESCREVA “NENHUMA MULHER”
SENÃO INÍCIO
media_f ←  media_f / cont_f
ESCREVA “Média de peças fabricadas por mulheres = “,media_f 
FIM
ESCREVA “O número do operário com maior salário é “,num_maior
FIM_ALGORITMO.
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\PASCAL\EX12_A.PAS e \EXERC\CAP5\PASCAL\EX12_A.EXE
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\PASCAL\EX12_B.PAS e \EXERC\CAP5\PASCAL\EX12_B.EXE
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\C++\EX12_A.CPP e \EXERC\CAP5\C++\EX12_A.EXE
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\C++\EX12_B.CPP e \EXERC\CAP5\C++\EX12_B.EXE
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\JAVA\EX12_A.java e \EXERC\CAP5\JAVA\EX12_A.class
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\JAVA\EX12_B.java e \EXERC\CAP5\JAVA\EX12_B.class
13. Foi feita uma pesquisa para determinar o índice de mortalidade infantil em certo período. Faça um  
programa que:
 ■ leia o número de crianças nascidas no período; 
 ■ identifique o sexo (M ou F) e o tempo de vida de cada criança nascida. 
O programa deve calcular e mostrar:
 ■ a percentagem de crianças do sexo feminino mortas no período; 
 ■ a percentagem de crianças do sexo masculino mortas no período; 
 ■ a percentagem de crianças que viveram 24 meses ou menos no período. 
SOLUÇÃO:
ALGORITMO
DECLARE i, num_cri, meses, porc_f, porc_m, tot_f NUMÉRICO  
tot_m, tot_24, porc_24 NUMÉRICO
sexo LITERAL
ESCREVA “Digite o número de crianças nascidas no período “ 
LEIA num_cri
tot_m ← 0 
tot_f ← 0 
tot_24 ← 0
PARA i ← 1 ATE num_cri FAÇA  
PASCAL
C/C++
JAVA

---

Capítulo 5 Estrutura de repetição  | 131
Exemplo de saída do programa:
VALOR DA
DÍVIDA
VALOR DOS
JUROS
QUANTIDADE  
DE PARCELAS
VALOR DA  
PARCELA
R$ 1.000,00 0 1 R$ 1.000,00
R$ 1.100,00 100 3 R$ 366,67
R$ 1.150,00 150 6 R$ 191,67
SOLUÇÃO:
ALGORITMO
DECLARE valor_inicial, juros, valor_parc NUMÉRICO 
total, valor_juros, num_parc, i NUMÉRICO
ESCREVA “Digite o valor_inicial da dívida” 
LEIA valor_inicial
juros ← 0 
num_parc ← 1
total ← valor_inicial 
valor_parc ← valor_inicial 
ESCREVA total
ESCREVA juros 
ESCREVA num_parc 
ESCREVA valor_parc 
juros ← juros + 10
num_parc ← num_parc + 2 
PARA i ← 1 ATÉ 4 FAÇA
INÍCIO
valor_juros ← valor_inicial * juros / 100 
total ← valor_inicial + valor_juros
valor_parc ←  total / num_parc
ESCREVA total
ESCREVA valor_juros
ESCREVA num_parc
ESCREVA valor_parc
juros ←  juros + 5
num_parc ←  num_parc + 3
FIM
FIM_ALGORITMO.
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\PASCAL\EX14_A.PAS e \EXERC\CAP5\PASCAL\EX14_A.EXE
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\PASCAL\EX14_B.PAS e \EXERC\CAP5\PASCAL\EX14_B.EXE
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\C++\EX14_A.CPP e \EXERC\CAP5\C++\EX14_A.EXE
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\C++\EX14_B.CPP e \EXERC\CAP5\C++\EX14_B.EXE
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA FOR:
\EXERC\CAP5\JAVA\EX14_A.java e \EXERC\CAP5\JAVA\EX14_A.class
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\JAVA\EX14_B.java e \EXERC\CAP5\JAVA\EX14_B.class
PASCAL
C/C++
JAVA

---

Capítulo 5 Estrutura de repetição  | 133
LEIA preco
LEIA refri
LEIA categ
SE preco <= 20
ENTÃO INÍCIO
SE categ = “A”
ENTÃO custo_est ← 2
SE categ = “L”
ENTÃO custo_est ← 3
SE categ = “V”
ENTÃO custo_est ← 4
FIM
SE preco > 20 E preco <= 50
ENTÃO INÍCIO
SE refri = “S”
ENTÃO custo_est ← 6
SENÃO custo_est ← 0
FIM
SE preco > 50
ENTÃO INÍCIO
SE refri = “S”
ENTÃO INÍCIO
SE categ = “A”
ENTÃO custo_est ← 5
SE categ = “L”
ENTÃO custo_est ← 2
SE categ = “V”
ENTÃO custo_est ← 4
FIM
SENÃO INÍCIO
SE categ = “A” OU categ = “V”
ENTÃO custo_est ← 0
SE categ = “L”
ENTÃO custo_est ← 1
FIM
FIM
SE categ ≠ “A” E refri ≠ “S”
ENTÃO imp ← preco * 2 / 100
SENÃO imp ← preco * 4 / 100
preco_final ← preco + custo_est + imp
ESCREVA custo_est
ESCREVA imp
ESCREVA preco_final
SE preco_final <= 20
ENTÃO INÍCIO
qtd_b ← qtd_b + 1
ESCREVA “Classificação Barato”
FIM
SE preco_final > 20 E preco_final <= 100
ENTÃO INÍCIO
qtd_n ← qtd_n + 1
ESCREVA “Classificação Normal”
FIM
SE preco_final > 100
ENTÃO INÍCIO
qtd_c ← qtd_c + 1

---

Capítulo 5 Estrutura de repetição  | 135
ATÉ altura > 0
area ← base * altura / 2 
ESCREVA area 
FIM_ALGORITMO.
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\PASCAL\EX16_A.PAS e \EXERC\CAP5\PASCAL\EX16_A.EXE
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA REPEAT:
\EXERC\CAP5\PASCAL\EX16_B.PAS e \EXERC\CAP5\PASCAL\EX16_B.EXE
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\C++\EX16_A.CPP e \EXERC\CAP5\C++\EX16_A.EXE
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA DO-WHILE:
\EXERC\CAP5\C++\EX16_B.CPP e \EXERC\CAP5\C++\EX16_B.EXE
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\JAVA\EX16_A.java e \EXERC\CAP5\JAVA\EX16_A.class
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA DO-WHILE:
\EXERC\CAP5\JAVA\EX16_B.java e \EXERC\CAP5\JAVA\EX16_B.class
17. Faça um programa que receba o salário de um funcionário chamado Carlos. Sabe-se que outro fun -
cionário, João, tem salário equivalente a um terço do salário de Carlos. Carlos aplicará seu salário 
integralmente na caderneta de poupança, que rende 2% ao mês, e João aplicará seu salário inte -
gralmente no fundo de renda fixa, que rende 5% ao mês. O programa deverá calcular e mostrar a 
quantidade de meses necessários para que o valor pertencente a João iguale ou ultrapasse o valor 
pertencente a Carlos.
SOLUÇÃO:
ALGORITMO
DECLARE sal_carlos, sal_joao, meses NUMÉRICO 
LEIA sal_carlos
sal_joao ← sal_carlos / 3
meses ← 0
ENQUANTO sal_joao < sal_carlos FAÇA 
INÍCIO
sal_carlos ← sal_carlos + (sal_carlos * 2 / 100) 
sal_joao ← sal_joao + (sal_joao * 5 / 100)
meses ←  meses + 1
FIM
ESCREVA meses 
FIM_ALGORITMO.
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\PASCAL\EX17_A.PAS e \EXERC\CAP5\PASCAL\EX17_A.EXE
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA REPEAT:
\EXERC\CAP5\PASCAL\EX17_B.PAS e \EXERC\CAP5\PASCAL\EX17_B.EXE
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\C++\EX17_A.CPP e \EXERC\CAP5\C++\EX17_A.EXE
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA DO-WHILE:
\EXERC\CAP5\C++\EX17_B.CPP e \EXERC\CAP5\C++\EX17_B.EXE
PASCAL
C/C++
JAVA
PASCAL
C/C++

---

Capítulo 5 Estrutura de repetição  | 137
ESCREVA soma 
LEIA m
LEIA n
FIM 
FIM_ALGORITMO.
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\PASCAL\EX19_A.PAS e \EXERC\CAP5\PASCAL\EX19_A.EXE
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA REPEAT:
\EXERC\CAP5\PASCAL\EX19_B.PAS e \EXERC\CAP5\PASCAL\EX19_B.EXE
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\C++\EX19_A.CPP e \EXERC\CAP5\C++\EX19_A.EXE
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA DO-WHILE:
\EXERC\CAP5\C++\EX19_B.CPP e \EXERC\CAP5\C++\EX19_B.EXE
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\JAVA\EX19_A.java e \EXERC\CAP5\JAVA\EX19_A.class
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA DO-WHILE:
\EXERC\CAP5\JAVA\EX19_B.java e \EXERC\CAP5\JAVA\EX19_B.class
20. Faça um programa para ler o código, o sexo (M — masculino; F — feminino) e o número de horas/
aula dadas mensalmente pelos professores de uma universidade, sabendo-se que cada hora/aula vale 
R$ 30,00. Emita uma listagem contendo o código, o salário bruto e o salário líquido (levando em 
consideração os descontos explicados a seguir) de todos os professores. Mostre também a média dos 
salários líquidos dos professores do sexo masculino e a média dos salários líquidos dos professores do 
sexo feminino. Considere:
 ■ desconto para homens, 10%, e, para mulheres, 5%; 
 ■ as informações terminarão quando for lido o código = 99999. 
SOLUÇÃO:
ALGORITMO
DECLARE cod, num_h, sal_b, sal_l, media_m, media_f NUMÉRICO 
cont_m, cont_f NUMÉRICO
sexo LITERAL
LEIA cod  
cont_m ← 0  
cont_f ← 0  
ENQUANTO cod ≠ 99999 FAÇA  
INÍCIO      
LEIA sexo  
LEIA num_h  
sal_b ←  num_h * 30  
SE sexo = "M"  
  ENTÃO INÍCIO  
sal_l ←  sal_b – (sal_b * 10 / 100)  
media_m ←  media_m + sal_l  
cont_m ←  cont_m + 1  
FIM  
SE sexo = "F"  
ENTÃO INÍCIO  
PASCAL
C/C++
JAVA

---

Capítulo 5 Estrutura de repetição  | 139
SOLUÇÃO:
ALGORITMO
DECLARE num, soma, qtd, maior, menor, qtd_par NUMÉRICO  
media_par, soma_par, qtd_impar, media, perc NUMÉRICO
qtd ← 0 
qtd_par ← 0 
soma_par ← 0 
qtd_impar ← 0 
soma ← 0
LEIA num
ENQUANTO num ≠ 30000 FAÇA
INÍCIO
SE qtd = 0 
ENTÃO INÍCIO
maior ← num 
menor ← num
FIM 
SENÃO INÍCIO
SE num > maior
ENTÃO maior ← num 
SE num < menor
ENTÃO menor ←  num
FIM
soma ← soma + num 
qtd ← qtd + 1
SE RESTO(num/2) = 0
ENTÃO INÍCIO
soma_par ← soma_par + num 
qtd_par ← qtd_par + 1
FIM
SENÃO qtd_impar ← qtd_impar + 1 
LEIA num
FIM
SE qtd = 0
ENTÃO ESCREVA “Nenhum número digitado” 
SENÃO INÍCIO
ESCREVA soma 
ESCREVA qtd
media ← soma / qtd 
ESCREVA media 
ESCREVA maior 
ESCREVA menor
SE qtd_par = 0
ENTÃO ESCREVA “nenhum par” 
SENÃO INÍCIO
media_par ← soma_par / qtd_par 
ESCREVA media_par
FIM
perc ←  qtd_impar * 100 / qtd
ESCREVA perc
FIM
FIM_ALGORITMO.
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\PASCAL\EX21_A.PAS e \EXERC\CAP5\PASCAL\EX21_A.EXE
PASCAL

---

Capítulo 5 Estrutura de repetição  | 141
SE sexo = “M”
ENTÃO tot_m ←  tot_m + 1
SE sexo = “F”
ENTÃO tot_f ←  tot_f + 1
SE sexo = “F” E idade < 21 E exp = “S”
ENTÃO cont_f1 ←  cont_f1 + 1
SE sexo = “M” E idade > 45
ENTÃO cont_m1 ←  cont_m1 + 1
SE sexo = “M” E exp = “S”
ENTÃO INÍCIO
soma1 ←  soma1 + idade
cont_m2 ←  cont_m2 + 1
FIM
LEIA idade
FIM
ESCREVA tot_f
ESCREVA tot_m
SE cont_m2 = 0
ENTÃO ESCREVA “Nenhum homem com experiência”
SENÃO INÍCIO
media_idade ←  soma1 / cont_m2
ESCREVA media_idade
FIM
SE tot_m = 0
ENTÃO ESCREVA “Nenhum homem”
SENÃO INÍCIO
perc ←  cont_m1 * 100 / tot_m
ESCREVA perc
FIM
ESCREVA cont_f1
ESCREVA menor_idade
FIM_ALGORITMO.
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\PASCAL\EX22_A.PAS e \EXERC\CAP5\PASCAL\EX22_A.EXE
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA REPEAT:
\EXERC\CAP5\PASCAL\EX22_B.PAS e \EXERC\CAP5\PASCAL\EX22_B.EXE
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\C++\EX22_A.CPP e \EXERC\CAP5\C++\EX22_A.EXE
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA DO-WHILE:
\EXERC\CAP5\C++\EX22_B.CPP e \EXERC\CAP5\C++\EX22_B.EXE
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\JAVA\EX22_A.java e \EXERC\CAP5\JAVA\EX22_A.class
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA DO-WHILE:
\EXERC\CAP5\JAVA\EX22_B.java e \EXERC\CAP5\JAVA\EX22_B.class
23. Faça um programa que receba o valor do salário mínimo, uma lista contendo a quantidade de quilo -
watts gasta por consumidor e o tipo de consumidor (1 — residencial; 2 — comercial; ou 3 — indus -
trial) e que calcule e mostre:
 ■ o valor de cada quilowatt, sabendo que o quilowatt custa um oitavo do salário mínimo; 
 ■ o valor a ser pago por consumidor (conta final mais acréscimo). O acréscimo encontra-se na tabela 
a seguir: 
PASCAL
C/C++
JAVA

---

Capítulo 5 Estrutura de repetição  | 143
1a SOLUÇÃO – UTILIZANDO A ESTRUTURA WHILE:
\EXERC\CAP5\JAVA\EX23_A.java e \EXERC\CAP5\JAVA\EX23_A.class
2a SOLUÇÃO – UTILIZANDO A ESTRUTURA DO-WHILE:
\EXERC\CAP5\JAVA\EX23_B.java e \EXERC\CAP5\JAVA\EX23_B.class
24. Faça um programa que apresente o menu de opções a seguir, permita ao usuário escolher a opção  
desejada, receba os dados necessários para executar a operação e mostre o resultado. Verifique a pos-
sibilidade de opção inválida e não se preocupe com restrições do tipo salário inválido.
Menu de opções:
1. Imposto 
2. Novo salário 
3. Classificação 
4. Finalizar o programa 
Digite a opção desejada. 
Na opção 1: receber o salário de um funcionário, calcular e mostrar o valor do imposto usando as regras 
a seguir.
SALÁRIOS % DO IMPOSTO
Menor que R$ 500,00 5
De R$ 500,00 a R$ 850,00 10
Acima de R$ 850,00 15
Na opção 2: receber o salário de um funcionário, calcular e mostrar o valor do novo salário usando as 
regras a seguir.
SALÁRIOS AUMENTO
Maiores que R$ 1.500,00 R$ 25,00
De R$ 750,00 (inclusive) a R$ 1.500,00 (inclusive) R$ 50,00
De R$ 450,00 (inclusive) a R$ 750,00 R$ 75,00
Menores que R$ 450,00 R$ 100,00
Na opção 3: receber o salário de um funcionário e mostrar sua classificação usando esta tabela:
SALÁRIOS CLASSIFICAÇÃO
Até R$ 700,00 Mal remunerado
Maiores que R$ 700,00 Bem remunerado
SOLUÇÃO:
ALGORITMO
DECLARE op, sal, imp, aum, novo_sal NUMÉRICO 
REPITA
ESCREVA " MENU DE OPÇÕES"
ESCREVA “1- Imposto” 
ESCREVA “2- Novo Salário” 
ESCREVA “3- Classificação”
ESCREVA “4- Finalizar o programa” 
ESCREVA “Digite a opção desejada” 
LEIA op
SE op > 4 OU op < 1
ENTÃO ESCREVA “Opção inválida !” 
SE op = 1
JAVA

---

Capítulo 5 Estrutura de repetição  | 145
 ■ O valor do imposto, usando a tabela a seguir. 
PREÇO UNITÁRIO PERCENTUAL DE IMPOSTO
SOBRE O PREÇO UNITÁRIO
Até R$ 100,00 5%
Maior que R$ 100,00 10%
 ■ O valor do transporte usando a tabela a seguir.
CARGA PERIGOSA PAÍS DE ORIGEM VALOR DO TRANSPORTE
S
1 R$ 50,00
2 R$ 21,00
3 R$ 24,00
N
1 R$ 12,00
2 R$ 21,00
3 R$ 60,00
 ■ O valor do seguro, usando a regra a seguir.
Os produtos que vêm do México e os produtos que utilizam transporte aéreo pagam metade do valor 
do seu preço unitário como seguro.
 ■ O preço final, ou seja, preço unitário mais imposto mais valor do transporte mais valor do seguro. 
 ■ O total dos impostos. 
SOLUÇÃO:
ALGORITMO
DECLARE preco, imp, transp, seguro, final NUMÉRICO
total_imp, origem NUMÉRICO
meio_t, carga LITERAL 
LEIA preco
ENQUANTO preco > 0 FAÇA 
INÍCIO
LEIA origem 
LEIA meio_t 
LEIA carga
SE preco <= 100
ENTÃO imp ← preco * 5 / 100 
SENÃO imp ← preco * 10 / 100
SE carga = “S” 
ENTÃO INÍCIO
SE origem = 1 
ENTÃO transp ← 50 
SE origem = 2 
ENTÃO transp ← 21 
SE origem = 3 
ENTÃO transp ← 24
FIM 
SE carga = “N”
ENTÃO INÍCIO
SE origem = 1 
ENTÃO transp ← 12 
SE origem = 2 
ENTÃO transp ← 21 
SE origem = 3 
ENTÃO transp ← 60
FIM

---

Capítulo 5 Estrutura de repetição  | 147
4. Faça um programa que receba um número, calcule e mostre a tabuada desse número. 
Exemplo:
Digite um número: 5
5 × 0 = 0
5 × 1 = 5
5 × 2 = 10
5 × 3 = 15
5 × 4 = 20
5 × 5 = 25
5 × 6 = 30
5 × 7 = 35
5 × 8 = 40
5 × 9 = 45
5 × 10 = 50
5. Faça um programa que mostre as tabuadas dos números de 1 a 10. 
6. Uma loja utiliza o código V para transação à vista e P para transação a prazo. Faça um programa que receba 
o código e o valor de quinze transações, calcule e mostre: 
 ■ o valor total das compras à vista; 
 ■ o valor total das compras a prazo; 
 ■ o valor total das compras efetuadas; e
 ■ o valor da primeira prestação das compras a prazo juntas, sabendo-se que serão pagas em três vezes. 
7. Faça um programa que receba a idade, a altura e o peso de cinco pessoas, calcule e mostre: 
 ■ a quantidade de pessoas com idade superior a 50 anos; 
 ■ a média das alturas das pessoas com idade entre 10 e 20 anos; 
 ■ a porcentagem de pessoas com peso inferior a 40 kg entre todas as pessoas analisadas. 
8. Faça um programa que receba a idade, o peso, a altura, a cor dos olhos (A — azul; P — preto; V — verde; e 
C — castanho) e a cor dos cabelos (P — preto; C — castanho; L — louro; e R — ruivo) de seis pessoas, e que 
calcule e mostre:
 ■ a quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 kg; 
 ■ a média das idades das pessoas com altura inferior a 1,50 m; 
 ■ a porcentagem de pessoas com olhos azuis entre todas as pessoas analisadas; e
 ■ a quantidade de pessoas ruivas e que não possuem olhos azuis. 
9. Faça um programa que receba dez idades, pesos e alturas, calcule e mostre: 
 ■ a média das idades das dez pessoas; 
 ■ a quantidade de pessoas com peso superior a 90 kg e altura inferior a 1,50 metro; e
 ■ a porcentagem de pessoas com idade entre 10 e 30 anos entre as pessoas que medem mais de  
1,90 m. 
10. Faça um programa que receba dez números, calcule e mostre a soma dos números pares e a soma dos 
números primos. 
11. Faça um programa que receba o valor de um carro e mostre uma tabela com os seguintes dados: preço 
final, quantidade de parcelas e valor da parcela. Considere o seguinte: 
 ■ o preço final para compra à vista tem desconto de 20%; 
 ■ a quantidade de parcelas pode ser: 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60; e
 ■ os percentuais de acréscimo encontram-se na tabela a seguir.

---

Capítulo 5 Estrutura de repetição  | 149
19. Faça um programa que receba o tipo da ação, ou seja, uma letra a ser comercializada na bolsa de valores, 
o preço de compra e o preço de venda de cada ação e que calcule e mostre: 
 ■ o lucro de cada ação comercializada; 
 ■ a quantidade de ações com lucro superior a R$ 1.000,00; 
 ■ a quantidade de ações com lucro inferior a R$ 200,00; 
 ■ o lucro total da empresa. 
Finalize com o tipo de ação ‘F’.
20. Faça um programa que apresente o menu de opções a seguir: 
Menu de opções:
1. Média aritmética 
2. Média ponderada 
3. Sair 
Digite a opção desejada.
Na opção 1: receber duas notas, calcular e mostrar a média aritmética.
Na opção 2: receber três notas e seus respectivos pesos, calcular e mostrar a média ponderada. 
Na opção 3: sair do programa.
Verifique a possibilidade de opção inválida. Nesse caso, o programa deverá mostrar uma mensagem.
21. Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. 
Os códigos utilizados são:
1, 2, 3, 4 Votos para os respectivos candidatos
5 Voto nulo
6 Voto em branco
Faça um programa que calcule e mostre:
 ■ o total de votos para cada candidato; 
 ■ o total de votos nulos; 
 ■ o total de votos em branco; 
 ■ a porcentagem de votos nulos sobre o total de votos; e
 ■ a porcentagem de votos em branco sobre o total de votos. 
Para finalizar o conjunto de votos, tem-se o valor zero e, para códigos inválidos, o programa deverá 
mostrar uma mensagem.
22. Faça um programa que receba a idade e a altura de várias pessoas, calcule e mostre a média das alturas 
daquelas com mais de 50 anos. Para encerrar a entrada de dados, digite idade menor ou igual a zero. 
23. Faça um programa que apresente o menu de opções a seguir, que permita ao usuário escolher a opção 
desejada, receba os dados necessários para executar a operação e mostre o resultado. Verifique a possibi-
lidade de opção inválida e não se preocupe com as restrições como salário inválido. 
Menu de opções:
1. Novo salário 
2. Férias 
3. Décimo terceiro 
4. Sair 
Digite a opção desejada.
Na opção 1: receber o salário de um funcionário, calcular e mostrar o novo salário usando as regras a se -
guir:

---



=== CAPÍTULO 6 ===

---

Capítulo 6 Vetor  | 153
6.2.2 Declaração de vetor
 VAR nome_da_variável: ARRAY[índice_inicial .. índice_final] OF tipo_ dos_dados_do_vetor;
onde: 
nome_da_variável é o nome da variável do tipo vetor; 
índice_inicial é o valor correspondente ao índice da primeira posição do vetor; 
índice_final é o valor correspondente ao índice da última posição do vetor; 
tipo_dos_dados_do_vetor é o tipo básico dos dados que serão armazenados no vetor.
É importante salientar que o valor do índice_inicial deve ser maior ou igual ao valor do índice_fi-
nal. As posições são identificadas com valores dentro desse intervalo.
Exemplo 1:
VAR vetor1: ARRAY [1..10] OF INTEGER;
Nesse caso, o índice poderá assumir valores inteiros que vão de 1 a 10.
Exemplo 2:
VAR vetor1: ARRAY [5..9] OF REAL;
Nesse caso, o índice poderá assumir valores inteiros que vão de 5 a 9.
Outro ponto importante a ser destacado é que os índices também podem ser representados por valores 
alfabéticos. Com isso, é permitido o uso de caracteres para representar o valor_inicial e o valor_final. 
Obviamente, a regra que obriga o valor_final ser maior ou igual ao valor_inicial continua valendo. O 
exemplo 3, a seguir, ilustra essa possibilidade.
Exemplo 3:
VAR vetor1: ARRAY [‘C’..’G’] OF REAL;
Nesse caso, o índice poderá assumir valores que vão de C a G.
Observação
Os valores que indicam o índice_inicial e o índice_final devem representar valores fixos (lite-
rais1 ou constantes), não podendo ser substituídos por variáveis.
6.2.3 Exemplos de vetor
VAR X:ARRAY[1..10] OF REAL;
X 10.5 20 13.1 14.65 87 1.2 35.6 78.2 15 65.9
1 2 3 4 5 6 7 8 9 10
VAR VET: ARRAY[5..9] OF CHAR;
VET E * m J k
5 6 7 8 9
VAR X:ARRAY[´D´..´G´] OF INTEGER;
X 5 10 8 3
D E F G
1   Literal é um valor ﬁxo, deﬁnido quando se escreve o programa. Por exemplo: x:=10.3;onde 10.3 é um literal. vet: array [1..18] of 
char;onde 1 e 18, escritos dentro dos colchetes, são literais.

---

Capítulo 6 Vetor  | 155
O exemplo 1 apresentou uma estrutura de repetição FOR, que foi utilizada para garantir que a variável 
i assumisse todos os valores possíveis para o índice do vetor (de 1 a 10). Já no exemplo 2, a estrutura de 
repetição FOR garantiu que a variável i assumisse todos os valores possíveis entre os caracteres C e E. As-
sim, para cada execução da repetição, foi utilizada uma posição diferente do vetor e, dessa forma, todos os 
valores armazenados foram mostrados.
6.3 Vetor em C/C++
6.3.1 Deﬁnição de vetor
As variáveis compostas homogêneas unidimensionais (ou, simplesmente, vetores) são capazes de arma-
zenar diversos valores. Cada um desses valores é identificado pelo mesmo nome (o nome dado ao vetor), 
sendo diferenciados entre si apenas por um índice.
Os índices utilizados na linguagem C/C++ para identificar as posições de um vetor começam sempre em 
0 (zero) e vão até o tamanho do vetor menos uma unidade. O índice de um vetor em C/C++ deve sempre ser 
representado por um dos tipos inteiros disponíveis na linguagem. 
6.3.2 Declaração de vetor
Os vetores em C/C++ são identificados pela existência de colchetes logo após o nome da variável no 
momento da declaração. Dentro dos colchetes, deve-se colocar o número de elementos que o vetor poderá 
armazenar.
Em C/C++, a indicação do tamanho do vetor (ou seja, a quantidade de elementos que o vetor poderá 
armazenar) deve ser feita por um valor inteiro fixo (representado por um literal2 ou uma constante). Se hou-
ver necessidade de definir o tamanho do vetor em tempo de execução, deve-se fazê-lo através de ponteiros 
(o Capítulo 8 apresentará o conceito de ponteiro).
6.3.3 Exemplo de vetor
A seguir, são apresentadas algumas formas de criação de vetores.
Exemplo 1:
int vet[10];
vet 10 5 3 8 1 19 44 21 2 7
 0 1 2 3 4 5 6 7 8 9
No exemplo 1, o vetor chamado vet possui dez posições, começando pela posição 0 e indo até a po -
sição 9 (tamanho do vetor – 1). Em cada posição poderão ser armazenados números inteiros, conforme 
especificado pelo tipo int na declaração.
Exemplo 2:
char x[5];
X A * 2 @ k
0 1 2 3 4
No exemplo 2, o vetor chamado x possui cinco posições, começando pela posição 0 e indo até a posição 
4 (tamanho do vetor – 1). Em cada posição poderão ser armazenados caracteres, conforme especificado 
pelo tipo char na declaração.
2  Literal é um valor ﬁxo, deﬁnido quando se escreve o programa. Por exemplo:  double x=10.3;  onde 10.3 é um literal. char vet [18];  
onde 18, escrito dentro dos colchetes, é um literal.

---

Capítulo 6 Vetor  | 157
6.4.2 Declaração de vetor
Os vetores em JAVA são definidos pela existência de colchetes vazios antes ou depois do nome da variável, 
no momento da declaração. Logo depois, deve ser feito o dimensionamento do vetor.
Em JAVA, a indicação do tamanho do vetor (ou seja, a quantidade de elementos que o vetor poderá 
armazenar) pode ser feita por um valor inteiro fixo (representado por um literal3 ou uma constante) ou por 
uma variável cujo valor é definido em tempo de execução. 
6.4.3 Exemplo de vetor
Nos exemplos a seguir, são utilizadas duas linhas de comando: a primeira declara um vetor e a segunda 
define o seu tamanho.
Exemplo 1:
int x[];
x = new int[10];
X 10 5 3 8 1 19 44 21 2 7
0 1 2 3 4 5 6 7 8 9
Na primeira linha do exemplo 1, os colchetes vazios após o nome definem que x será um vetor. O tipo 
int determina que todas as suas posições armazenarão valores inteiros. A segunda linha estabelece que o 
vetor x terá tamanho 10 (ou seja, posições de 0 a 9).
Exemplo 2:
final int tam=6;
float []y;
y = new float[tam];
Y 1.5 8.9 3.0 4.7 15.3 16.0
0 1 2 3 4 5
Na primeira linha do exemplo 2, foi definida a constante tam, com valor igual a 6. Na segunda linha, 
os colchetes vazios antes do nome definem que y será um vetor. O tipo float determina o tipo do conteúdo 
que poderá ser armazenado em todas as suas posições. A terceira linha estabelece que o vetor y terá tama-
nho 6, exatamente o valor da constante tam (ou seja, o vetor terá posições de 0 a 5).
Exemplo 3:
double w[];
int tam;
tam = ent.nextInt();
w = new double[tam];
Y 1.5 8.9 3.0 4.7 15.3 16.0 … 16.0
0 1 2 3 4 5 … tam-1
No exemplo 3, tem-se um vetor cujo tamanho dependerá de um valor fornecido no momento da execu-
ção do programa. Na primeira linha do exemplo 3, os colchetes vazios depois do nome, definem que w será 
um vetor. O tipo double, determina o tipo do dado que poderá ser armazenado em todas as suas posições. 
Na segunda linha é declarada a variável tam, que, após receber um valor externo (terceira linha), indicará o 
tamanho do vetor w (quarta linha). 
Já, nos exemplos apresentados a seguir, utilizou-se a forma condensada, onde a declaração e o dimen-
sionamento do vetor são feitos utilizando-se uma única linha.
3  Literal é um valor ﬁxo, deﬁnido quando se escreve o programa. Por exemplo:  double x=10.3; onde 10.3 é um literal. char vet 
[]= new char[18];  onde 18, escrito dentro dos colchetes, é um literal.

---

Capítulo 6 Vetor  | 159
EXERCÍCIOS RESOLVIDOS
1. Faça um programa que preencha um vetor com nove números inteiros, calcule e mostre os números  
primos e suas respectivas posições.
SOLUÇÃO:
ALGORITMO
DECLARE num[9] NUMÉRICO
i, j, cont NUMÉRICO 
PARA i ← 1 ATÉ 9 FAÇA
INÍCIO
LEIA num[i]
FIM
PARA i ← 1 ATÉ 9 FAÇA 
INÍCIO
cont ← 0
PARA j ← 1 ATÉ num[i] FAÇA 
INÍCIO
SE RESTO(num[i]/j) = 0 
ENTÃO cont ← cont + 1
FIM
SE cont <= 2
ENTÃO INÍCIO 
ESCREVA num[i] 
ESCREVA i
FIM
FIM 
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP6\PASCAL\EX1.PAS e \EXERC\CAP6\PASCAL\EX1.EXE
SOLUÇÃO:
\EXERC\CAP6\C++\EX1.CPP e \EXERC\CAP6\C++\EX1.EXE
SOLUÇÃO:
\EXERC\CAP6\JAVA\EX1.java e \EXERC\CAP6\JAVA\EX1.class
2. Uma pequena loja de artesanato possui apenas um vendedor e comercializa dez tipos de objetos. O  
vendedor recebe, mensalmente, salário de R$ 545,00, acrescido de 5% do valor total de suas vendas. 
O valor unitário dos objetos deve ser informado e armazenado em um vetor; a quantidade vendida de 
cada peça deve ficar em outro vetor, mas na mesma posição. Crie um programa que receba os preços 
e as quantidades vendidas, armazenando-os em seus respectivos vetores (ambos com tamanho dez). 
Depois, determine e mostre:
 ■ um relatório contendo: quantidade vendida, valor unitário e valor total de cada objeto. Ao final, 
deverão ser mostrados o valor geral das vendas e o valor da comissão que será paga ao vendedor; e
 ■ o valor do objeto mais vendido e sua posição no vetor (não se preocupe com empates).
SOLUÇÃO:
ALGORITMO
DECLARE qtd[10], preco[10] NUMÉRICO
i, tot_geral, tot_vend, comissao, maio, ind NUMÉRICO
tot_geral ← 0
PARA i ← 1 ATÉ 10 FAÇA
INÍCIO
LEIA qtd[i] 
PASCAL
C/C++
JAVA

---

Capítulo 6 Vetor  | 161
j ←  j + 1
LEIA vet2[i]
vet3[j] ← vet2[i]
j ←  j + 1
FIM
PARA i ← 1 ATÉ 20 FAÇA
INÍCIO
ESCREVA vet3[i]
FIM
FIM_ALGORITMO. 
SOLUÇÃO:
\EXERC\CAP6\PASCAL\EX3.PAS e \EXERC\CAP6\PASCAL\EX3.EXE 
SOLUÇÃO:
\EXERC\CAP6\C++\EX3.CPP e \EXERC\CAP6\C++\EX3.EXE
SOLUÇÃO:
\EXERC\CAP6\JAVA\EX3.java e \EXERC\CAP6\JAVA\EX3.class
4. Faça um programa que preencha um vetor com oito números inteiros, calcule e mostre dois vetores 
resultantes. O primeiro vetor resultante deve conter os números positivos e o segundo, os números ne-
gativos. Cada vetor resultante vai ter, no máximo, oito posições, que não poderão ser completamente 
utilizadas.
SOLUÇÃO:
ALGORITMO
DECLARE num[8], pos[8], neg[8] NUMÉRICO    
cont, cont_n, cont_p, i NUMÉRICO 
cont_n ← 1
cont_p ← 1
PARA i ← 1 ATÉ 8 FAÇA 
INÍCIO
LEIA num[i]
SE num[i] >= 0 
ENTÃO INÍCIO
pos[cont_p] ← num[i]
cont_p ← cont_p + 1
FIM 
SENÃO INÍCIO
neg[cont_n] ← num[i]
cont_n ← cont_n + 1
FIM
FIM
SE  cont_n  =  1
ENTÃO ESCREVA “Vetor de negativos vazio”
SENÃO INÍCIO 
    PARA i ← 1 ATÉ cont_n – 1 FAÇA
    INÍCIO
    ESCREVA neg[i] 
    FIM
FIM
SE cont_p = 1
ENTÃO ESCREVA “Vetor de positivos vazio”
PASCAL
C/C++
JAVA

---

Capítulo 6 Vetor  | 163
y 2 1 5 12 3 0 1 4 5 6
1 2 3 4 5 6 7 8 9 10
Produto 6 8 20 24 3 0 8 28 55 54
1 2 3 4 5 6 7 8 9 10
 ■ A intersecção entre X e Y 
 (apenas os elementos que aparecem nos dois vetores, sem repetições). 
x 3 8 4 2 1 6 8 7 11 9
1 2 3 4 5 6 7 8 9 10
y 2 1 5 12 3 0 1 4 5 6
1 2 3 4 5 6 7 8 9 10
Intersecção 3 4 2 1 6
1 2 3 4 5
SOLUÇÃO:
ALGORITMO
DECLARE X[10], Y[10], U[20], D[10], S[10], P[10], IT[10] NUMÉRICO 
i, j, k, cont_u, cont_d, cont_i NUMÉRICO
PARA i ← 1 ATÉ 10 FAÇA 
INÍCIO
LEIA  X[i]
LEIA  Y[i]
FIM
cont_u ← 1 
cont_d ← 1 
cont_i ← 1
PARA  i ← 1  ATÉ 10 FAÇA
INÍCIO
j ← 1
ENQUANTO (j < cont_u E X[i] ≠ U[j]) FAÇA 
INÍCIO
j ← j +  1
FIM
SE j >= cont_u 
ENTÃO INÍCIO
U[cont_u] ← X[i] 
cont_u ← cont_u + 1
FIM
FIM
PARA i  ← 1  ATÉ 10 FAÇA
INÍCIO
j  ← 1
ENQUANTO (j < cont_u E Y[i] ≠ U[j]) FAÇA 
INÍCIO
j ← j  +  1
FIM
SE j >= cont_u 
ENTÃO INÍCIO
U[cont_u] ← Y[i] 
cont_u ← cont_u + 1
FIM
FIM
PARA i ← 1 ATÉ cont_u - 1 FAÇA

---

Capítulo 6 Vetor  | 165
cont_i ← cont_i + 1
FIM
FIM
FIM
PARA i ← 1 ATÉ cont_i – 1 FAÇA 
INÍCIO 
ESCREVA IT[i]
FIM
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP6\PASCAL\EX5.PAS e \EXERC\CAP6\PASCAL\EX5.EXE
SOLUÇÃO:
\EXERC\CAP6\C++\EX5.CPP e \EXERC\CAP6\C++\EX5.EXE
SOLUÇÃO:
\EXERC\CAP6\JAVA\EX5.java e \EXERC\CAP6\JAVA\EX5.class
6. Faça um programa que preencha um vetor com dez números inteiros, calcule e mostre o vetor resul -
tante de uma ordenação decrescente.
x 3 5 4 2 1 6 8 7 11 9
1 2 3 4 5 6 7 8 9 10
Ordenado 11 9 8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8 9 10
SOLUÇÃO:
ALGORITMO
DECLARE vet[10], i, j, aux NUMÉRICO 
PARA ← 1 ATÉ 10 FAÇA
INÍCIO
LEIA vet[i]
FIM
PARA i ← 1 ATÉ 10 FAÇA 
INÍCIO
PARA j ← 1 ATÉ 9 FAÇA 
INÍCIO
SE vet[j] < vet[j+1] 
ENTÃO INÍCIO
aux ← vet[j] 
vet[j] ← vet[j+1] 
vet[j+1] ← aux
FIM
FIM
FIM
PARA i ← 1 ATÉ 10 FAÇA 
INÍCIO
ESCREVA vet[i]
FIM
FIM_ALGORITMO.
PASCAL
C/C++
JAVA

---

Capítulo 6 Vetor  | 167
8. Faça um programa que preencha dois vetores com cinco elementos numéricos cada e, depois, ordene-
-os de maneira crescente. Deverá ser gerado um terceiro vetor com dez posições, composto pela junção 
dos elementos dos vetores anteriores, também ordenado de maneira crescente.
x 6 8 1 10 3
1 2 3 4 5
X 1 3 6 8 10
ordenado 1 2 3 4 5
y 20 0 7 2 5
1 2 3 4 5
Y 0 2 5 7 20
Ordenado 1 2 3 4 5
Resultado 0 1 2 3 5 6 7 8 10 20
1 2 3 4 5 6 7 8 9 10
SOLUÇÃO:
ALGORITMO
DECLARE X[5], Y[5], R[10], i, j, z, aux NUMÉRICO 
PARA i ← 1 ATÉ 5 FAÇA
INÍCIO
LEIA X[i] 
FIM
PARA i ← 1 ATÉ 5 FAÇA 
INÍCIO
PARA j ← 1 ATÉ 4 FAÇA 
INÍCIO
SE X[j] > X[j+1] 
ENTÃO INÍCIO
aux ← X[j] 
X[j] ← X[j+1] 
X[j+1] ← aux
FIM
FIM
FIM
PARA i ← 1 ATÉ 5 FAÇA 
INÍCIO
LEIA Y[i]
FIM
PARA i ← 1 ATÉ 5 FAÇA 
INÍCIO
PARA j ← 1 ATÉ 4 FAÇA 
INÍCIO
SE Y[j] > Y[j+1] 
ENTÃO INÍCIO
aux ← Y[j] 
Y[j] ← Y[j+1] 
Y[j+1] ← aux
FIM
FIM
FIM 
j ← 1;

---

Capítulo 6 Vetor  | 169
Quando a opção escolhida for Consultar, deverá ser disponibilizado mais um menu com as seguintes 
opções:
 ■ por número do voo; 
 ■ por origem; e 
 ■ por destino. 
Quando a opção escolhida for Efetuar reserva, deverá ser perguntado o número do voo em que a pes-
soa deseja viajar. O programa deverá dar as seguintes respostas:
 ■ reserva confirmada — caso exista o voo e lugar disponível, dando baixa nos lugares disponíveis; 
 ■ voo lotado — caso não exista lugar disponível nesse voo; 
 ■ voo inexistente — caso o código do voo não exista. 
A opção Sair é a única que permite encerrar a execução do programa. Sendo assim, após cada operação 
de consulta ou reserva, o programa volta ao menu principal.
SOLUÇÃO:
ALGORITMO
DECLARE voo[12], lugares[12], i, op, op2, num_voo NUMÉRICO origem[12], destino[12], 
local LITERAL
PARA i ← 1 ATÉ 12 FAÇA 
INÍCIO
LEIA voo[i] 
LEIA origem[i] 
LEIA destino[i] 
LEIA lugares[i]
FIM 
REPITA
ESCREVA “1- Consultar”
ESCREVA “2- Reservar”
ESCREVA “3- Finalizar” 
ESCREVA “Digite sua opção: “ 
LEIA op
SE op = 1
ENTÃO INÍCIO
ESCREVA “1- Consulta por voo” 
ESCREVA “2- Consulta por origem” 
ESCREVA “3- Consulta por destino” 
ESCREVA “Digite sua opção: “ 
LEIA op2
SE op2 = 1 
ENTÃO INÍCIO
ESCREVA “Digite o número de voo: “
LEIA num_voo 
i ← 1
ENQUANTO (i <= 12 E voo[i] ≠ num_voo) FAÇA 
INÍCIO
i ← i + 1
FIM
SE i > 12
ENTÃO ESCREVA “Voo inexistente “ 
SENÃO INÍCIO
ESCREVA “Número do voo: “, voo[i] 
ESCREVA “Local de origem: “, origem[i] ESCREVA “Local de 
destino: “, destino[i]
ESCREVA “Lugares disponíveis: “, lugares[i] 
FIM

---

Capítulo 6 Vetor  | 171
SOLUÇÃO:
\EXERC\CAP6\PASCAL\EX9.PAS e \EXERC\CAP6\PASCAL\EX9.EXE
SOLUÇÃO:
\EXERC\CAP6\C++\EX9.CPP e \EXERC\CAP6\C++\EX9.EXE
SOLUÇÃO:
\EXERC\CAP6\JAVA\EX9.java e \EXERC\CAP6\JAVA\EX9.class
10. Faça um programa para corrigir provas de múltipla escolha. Cada prova tem oito questões e cada 
questão vale um ponto. O primeiro conjunto de dados a ser lido é o gabarito da prova. Os outros da-
dos são os números dos alunos e as respostas que deram às questões. Existem dez alunos matriculados. 
Calcule e mostre:
 ■ o número e a nota de cada aluno; e
 ■ a porcentagem de aprovação, sabendo-se que a nota mínima é 6. 
PASCAL
C/C++
JAVA
Observações
A comparação de duas cadeias de caracteres (como dois nomes, por exemplo) em PASCAL 
é feita utilizando-se o sinal de = . As funções de manipulação de strings desta linguagem serão 
abordadas no Capítulo 9.
Exemplo:
{faz distinção entre maiúsculas e minúsculas}
if (nome1 = nome2)
then writeln(‘Nomes iguais’);
A comparação de duas cadeias de caracteres (como dois nomes, por exemplo) em C é feita 
utilizando-se algumas funções da biblioteca string.h. As funções de manipulação de strings 
desta linguagem serão abordadas no Capítulo 9.
Exemplos:
// faz distinção entre maiúsculas e minúsculas
if (strcmp(nome1,nome2)==0)   
 printf(“Nomes iguais”);
// NÃO faz distinção entre maiúsculas e minúsculas
if (strcmpi(nome1,nome2)==0)   
 printf(“Nomes iguais”);
A comparação de duas cadeias de caracteres (como dois nomes, por exemplo) em JAVA é 
feita utilizando-se alguns métodos da classe String. Os métodos de manipulação de strings 
desta linguagem serão abordados no Capítulo 9.
Exemplos:
// faz distinção entre maiúsculas e minúsculas
if (nome1.equals(nome2))   
 System.out.println(“Nomes iguais”);
// NÃO faz distinção entre maiúsculas e minúsculas
if (nome1.equalsIgnoreCase(nome2))   
 System.out.println(“Nomes iguais”);

---

Capítulo 6 Vetor  | 173
maior ← temp[cont] 
menor ← temp[cont] 
maior_mes ← cont 
menor_mes ← cont
FIM 
SENÃO INÍCIO
SE (temp[cont] > maior) 
ENTÃO INÍCIO
maior ← temp[cont] 
maior_mes ← cont
FIM
SE (temp[cont] < menor) 
ENTÃO INÍCIO
menor ← temp[cont] 
menor_mes ← cont
FIM
FIM
FIM 
ESCREVA maior
SE (maior_mes = 1)
ENTÃO ESCREVA “JANEIRO” 
SE (maior_mes = 2)
ENTÃO ESCREVA “FEVEREIRO” 
SE (maior_mes = 3)
ENTÃO ESCREVA “MARÇO” 
SE (maior_mes = 4)
ENTÃO ESCREVA “ABRIL” 
SE (maior_mes = 5)
ENTÃO ESCREVA “MAIO” 
SE (maior_mes = 6)
ENTÃO ESCREVA “JUNHO” 
SE (maior_mes = 7)
ENTÃO ESCREVA “JULHO” 
SE (maior_mes = 8)
ENTÃO ESCREVA “AGOSTO” 
SE (maior_mes = 9)
ENTÃO ESCREVA “SETEMBRO” 
SE (maior_mes = 10)
ENTÃO ESCREVA “OUTUBRO” 
SE (maior_mes = 11)
ENTÃO ESCREVA “NOVEMBRO” 
SE (maior_mes = 12)
ENTÃO ESCREVA “DEZEMBRO” 
ESCREVA menor
SE (menor_mes = 1)
ENTÃO ESCREVA “JANEIRO” 
SE (menor_mes = 2)
ENTÃO ESCREVA “FEVEREIRO” 
SE (menor_mes = 3)
ENTÃO ESCREVA “MARÇO” 
SE (menor_mes = 4)
ENTÃO ESCREVA “ABRIL” 
SE (menor_mes = 5)
ENTÃO ESCREVA “MAIO” 
SE (menor_mes = 6)
ENTÃO ESCREVA “JUNHO” 
SE (menor_mes = 7)

---

Capítulo 6 Vetor  | 175
ESCREVA “ O veículo “ , veiculo[i], “ consome “ , valor, “litro(s) de combustível 
Ê para percorrer 1000 Km”
FIM
ESCREVA “O veículo mais econômico é “, veiculo[menor_vei]
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP6\PASCAL\EX12.PAS e \EXERC\CAP6\PASCAL\EX12.EXE
SOLUÇÃO:
\EXERC\CAP6\C++\EX12.CPP e \EXERC\CAP6\C++\EX12.EXE
SOLUÇÃO:
\EXERC\CAP6\JAVA\EX12.java e \EXERC\CAP6\JAVA\EX12.class
13. Faça um programa que preencha um vetor com dez números inteiros, calcule e mostre os números su-
periores a cinquenta e suas respectivas posições. O programa deverá mostrar mensagem se não existir 
nenhum número nessa condição.
SOLUÇÃO:
ALGORITMO
DECLARE vet[10], achou LÓGICO
i NUMÉRICO
PARA i ← 1 ATÉ 10 FAÇA
INÍCIO 
LEIA vet[i] 
FIM
achou ← falso
PARA i ← 1 ATÉ 10 FAÇA 
INÍCIO
SE vet[i] > 50 
ENTÃO INÍCIO
ESCREVA vet[i], i 
achou ← verdadeiro
FIM
FIM
SE achou = falso
ENTÃO ESCREVA “Não existem números superiores a 50 no vetor” 
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP6\PASCAL\EX13.PAS e \EXERC\CAP6\PASCAL\EX13.EXE
SOLUÇÃO:
\EXERC\CAP6\C++\EX13.CPP e \EXERC\CAP6\C++\EX13.EXE
SOLUÇÃO:
\EXERC\CAP6\JAVA\EX13.java e \EXERC\CAP6\JAVA\EX13.class
14. Faça um programa que preencha três vetores com cinco posições cada. O primeiro vetor receberá  os 
nomes de cinco funcionários; o segundo e o terceiro vetor receberão, respectivamente, o salário e o 
tempo de serviço de cada um. Mostre um primeiro relatório apenas com os nomes dos funcionários 
que não terão aumento; mostre um segundo relatório apenas com os nomes e os novos salários dos 
PASCAL
C/C++
JAVA
PASCAL
C/C++
JAVA

---

Capítulo 6 Vetor  | 177
Número 5
Divisível por 5 na posição 3
Número 12
Divisível por 3 na posição 1
Divisível por 2 na posição 5
Número 4
Divisível por 2 na posição 5
Número 7
Não possui divisores no segundo vetor
Número 10
Divisível por 5 na posição 3
Divisível por 2 na posição 5
...
Para saber se um número é divisível por outro, deve-se testar o resto.
Exemplo: RESTO(5/5) = 0
SOLUÇÃO:
ALGORITMO
DECLARE vet1[10], vet2[5], i, j NUMÉRICO
achou LÓGICO 
PARA i ← 1 ATÉ 10 FAÇA
INÍCIO
LEIA vet1[i] 
FIM
PARA i ← 1 ATÉ 5 FAÇA 
INÍCIO
LEIA vet2[i] 
FIM
PARA i ← 1 ATÉ 10 FAÇA 
INÍCIO
 achou ← falso 
ESCREVA vet1[i]
PARA j ← 1 ATÉ 5 FAÇA 
INÍCIO
SE RESTO(vet1[i]/vet2[j]) = 0 
ENTÃO INÍCIO
ESCREVA “Divisível por “, vet2[j], “na posição “, j 
achou ← verdadeiro
FIM
FIM
SE achou = falso
ENTÃO ESCREVA “Não possui divisores no segundo vetor” 
FIM
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP6\PASCAL\EX15.PAS e \EXERC\CAP6\PASCAL\EX15.EXE
SOLUÇÃO:
\EXERC\CAP6\C++\EX15.CPP e \EXERC\CAP6\C++\EX15.EXE
SOLUÇÃO:
\EXERC\CAP6\JAVA\EX15.java e \EXERC\CAP6\JAVA\EX15.class
PASCAL
C/C++
JAVA

---

Capítulo 6 Vetor  | 179
SENÃO INÍCIO  
vet_result2[poslivre2] ← soma  
poslivre2 ← poslivre2 + 1  
FIM  
FIM      
PARA i ← 1 ATÉ (poslivre1 -1) FAÇA  
INÍCIO  
ESCREVA vet_result1[i]  
FIM      
PARA i ← 1 ATÉ (poslivre2 -1) FAÇA  
INÍCIO  
ESCREVA vet_result2[i]  
FIM      
FIM_ALGORITMO.
SOLUÇÃO:    
\EXERC\CAP6\PASCAL\EX16.PAS e \EXERC\CAP6\PASCAL\EX16.EXE
SOLUÇÃO:
\EXERC\CAP6\C++\EX16.CPP e \EXERC\CAP6\C++\EX16.EXE
SOLUÇÃO:
\EXERC\CAP6\JAVA\EX16.java e \EXERC\CAP6\JAVA\EX16.class 
17. Faça um programa que receba seis números inteiros e mostre: 
 ■ os números pares digitados; 
 ■ a soma dos números pares digitados; 
 ■ os números ímpares digitados; e
 ■ a quantidade de números ímpares digitados. 
Vetor 2 4 5 6 3 7
1 2 3 4 5 6
Relatório
Os números pares são: 
número 2 na posição 1 
número 4 na posição 2 
número 6 na posição 4
Soma dos pares = 12
Os números ímpares são: 
número 5 na posição 3 
número 3 na posição 5 
número 7 na posição 6
Quantidade de ímpares = 3
SOLUÇÃO:
ALGORITMO
DECLARE num[6], i, soma, qtde NUMÉRICO 
achou LÓGICO
PARA i ← 1 ATÉ 6 FAÇA 
INÍCIO
LEIA num[i] 
FIM
PASCAL
C/C++
JAVA

---

Capítulo 6 Vetor  | 181
PARA i ← 1 ATÉ 20 FAÇA 
INÍCIO 
ESCREVA dado[i] 
FIM 
num1 ← 0 
num2 ← 0 
num3 ← 0 
num4 ← 0 
num5 ← 0 
num6 ← 0 
PARA i ← 1 ATÉ 20 FAÇA 
 INÍCIO 
  SE dado[i] = 1 
  ENTÃO num1 ← num1 + 1 
  SE dado[i] = 2 
  ENTÃO num2 ← num2 + 1 
  SE dado[i] = 3 
  ENTÃO num3 ← num3 + 1 
  SE dado[i] = 4 
  ENTÃO num4 ← num4 + 1 
  SE dado[i] = 5 
  ENTÃO num5 ← num5 + 1 
  SE dado[i] = 6 
  ENTÃO num6 ← num6 + 1 
  FIM 
ESCREVA “O número 1 foi sorteado “, num1, “vez(es)”
ESCREVA “O número 2 foi sorteado “, num2, “vez(es)” 
ESCREVA “O número 3 foi sorteado “, num3, “vez(es)”
ESCREVA “O número 4 foi sorteado “, num4, “vez(es)”
ESCREVA “O número 5 foi sorteado “, num5, “vez(es)”
ESCREVA “O número 6 foi sorteado “, num6, “vez(es)” 
FIM_ALGORITMO.  
SOLUÇÃO: 
\EXERC\CAP6\PASCAL\EX18.PAS e \EXERC\CAP6\PASCAL\EX18.EXE
SOLUÇÃO:
\EXERC\CAP6\C++\EX18.CPP e \EXERC\CAP6\C++\EX18.EXE
SOLUÇÃO:
\EXERC\CAP6\JAVA\EX18.java e \EXERC\CAP6\JAVA\EX18.class
19. Faça um programa que preencha dois vetores, A e B, com vinte caracteres cada. A seguir, troque o 1 o 
elemento de A com o 20o de B, o 2o de A com o 19o de B, e assim por diante, até trocar o 20o de A com 
o 1o de B. Mostre os vetores antes e depois da troca.
Vetor 1 – Antes da troca
A G Y W 5 V S 8 6 J G A W 2 M C H Q 6 L
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
Vetor 2 – Antes da troca
S D 4 5 H G R U 8 9 K S A 1 2 V 4 D 5 M
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
PASCAL
C/C++
JAVA

---

Capítulo 6 Vetor  | 183
20. Faça um programa que leia um vetor com cinco posições para números reais e, depois, um código  
inteiro. Se o código for zero, finalize o programa; se for 1, mostre o vetor na ordem direta; se for 2, 
mostre o vetor na ordem inversa.
SOLUÇÃO:
ALGORITMO
DECLARE vet[5], i, cod NUMÉRICO
PARA i ← 1 ATÉ 5 FAÇA 
INÍCIO
LEIA vet[i] 
FIM
LEIA cod 
SE cod = 0
ENTÃO ESCREVA “fim” 
SE cod = 1
ENTÃO INÍCIO
PARA i ← 1 ATÉ 5 FAÇA 
INÍCIO
ESCREVA vet[i] 
FIM
FIM 
SE cod = 2
ENTÃO INÍCIO
PARA i ← 5 ATÉ 1 PASSO - 1 FAÇA 
INÍCIO
ESCREVA vet[i] 
FIM
FIM
SE (cod < 0) OU (cod > 2) 
ENTÃO ESCREVA “Código inválido” 
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP6\PASCAL\EX20.PAS e \EXERC\CAP6\PASCAL\EX20.EXE
SOLUÇÃO:
\EXERC\CAP6\C++\EX20.CPP e \EXERC\CAP6\C++\EX20.EXE
SOLUÇÃO:
\EXERC\CAP6\JAVA\EX20.java e \EXERC\CAP6\JAVA\EX20.class
21. Faça um programa que leia um conjunto de quinze valores e armazene-os em um vetor. A seguir, sepa-
re-os em dois outros vetores (P e I) com cinco posições cada. O vetor P armazena números pares e o 
vetor I, números ímpares. Como o tamanho dos vetores pode não ser suficiente para armazenar todos 
os números, deve-se sempre verificar se já estão cheios. Caso P ou I estejam cheios, deve-se mostrá-los 
e recomeçar o preenchimento da primeira posição. Terminado o processamento, mostre o conteúdo 
restante dentro dos vetores P e I.
SOLUÇÃO:
ALGORITMO
DECLARE vet[15], p[5], i[5] NUMÉRICO
cont, k, poslivre_p, poslivre_i NUMÉRICO 
PARA cont ← 1 ATÉ 15 FAÇA
INÍCIO
LEIA vet[cont] 
FIM
PASCAL
C/C++
JAVA

---

Capítulo 6 Vetor  | 185
22. Faça um programa que simule um controle bancário. Para tanto, devem ser lidos os códigos de dez  
contas e seus respectivos saldos. Os códigos devem ser armazenados em um vetor de números inteiros 
(não pode haver mais de uma conta com o mesmo código) e os saldos devem ser armazenados em um 
vetor de números reais. O saldo deverá ser cadastrado na mesma posição do código. Por exemplo, se 
a conta 504 foi armazenada na quinta posição do vetor de códigos, seu saldo deverá ficar na quinta 
posição do vetor de saldos. Depois de fazer a leitura dos valores, deverá aparecer o seguinte menu na 
tela:
1. Efetuar depósito 
2. Efetuar saque 
3. Consultar o ativo bancário, ou seja, o somatório dos saldos de todos os clientes 
4. Finalizar o programa 
 ■ para efetuar depósito, deve-se solicitar o código da conta e o valor a ser depositado. Se a conta não 
estiver cadastrada, deverá aparecer a mensagem Conta não encontrada e voltar ao menu. Se a conta 
existir, atualizar seu saldo; 
 ■ para efetuar saque, deve-se solicitar o código da conta e o valor a ser sacado. Se a conta não esti -
ver cadastrada, deverá aparecer a mensagem Conta não encontrada e voltar ao menu. Se a conta 
existir, verificar se o seu saldo é suficiente para cobrir o saque. (Estamos supondo que a conta não 
possa ficar com o saldo negativo.) Se o saldo for suficiente, realizar o saque e voltar ao menu. Caso 
contrário, mostrar a mensagem Saldo insuficiente e voltar ao menu; 
 ■ para consultar o ativo bancário, deve-se somar o saldo de todas as contas do banco. Depois de 
mostrar esse valor, voltar ao menu; 
 ■ o programa só termina quando for digitada a opção 4 — Finalizar o programa. 
SOLUÇÃO:
ALGORITMO
DECLARE conta[10], saldo[10] NUMÉRICO
i, j, codigo, valor, soma, op NUMÉRICO 
achou LÓGICO
PARA i ← 1 ATÉ 10 FAÇA
INÍCIO
achou ← falso 
REPITA
LEIA conta[i]
PARA j ← 1 ATÉ (i-1) FAÇA 
INÍCIO
SE conta[i] = conta[j]
ENTÃO achou ← verdadeiro
FIM
ATÉ achou = falso 
LEIA saldo[i]
FIM
REPITA
LEIA op
achou ← falso 
SE op = 1 
ENTÃO INÍCIO
LEIA codigo, valor
PARA i ← 1 ATÉ 10 FAÇA
 INÍCIO
SE codigo = conta[i]
ENTÃO INÍCIO
saldo[i] ← saldo[i] + valor 
achou ← verdadeiro

---

Capítulo 6 Vetor  | 187
Inicialmente, todas as poltronas estarão livres. Depois disso, o programa deverá apresentar as seguintes 
opções:
 ■ vender passagem; 
 ■ mostrar mapa de ocupação do ônibus; 
 ■ encerrar. 
Quando a opção escolhida for Vender Passagem, deverá ser perguntado se o usuário deseja janela ou 
corredor e o número da poltrona. O programa deverá, então, dar uma das seguintes mensagens:
 ■ Venda efetivada — se a poltrona solicitada estiver livre, marcando-a como ocupada. 
 ■ Poltrona ocupada — se a poltrona solicitada não estiver disponível para venda. 
 ■ Ônibus lotado — quando todas as poltronas já estiverem ocupadas. 
Quando a opção escolhida for Mostrar Mapa de Ocupação do Ônibus, deverá ser mostrada uma lis -
tagem conforme a seguir:
JANELA CORREDOR
1- Ocupada 1- Ocupada
2- Ocupada 2- Livre
3- Livre 3- Livre
4- Livre 4- Ocupada
5- Ocupada 5- Livre
...
Quando for escolhida a opção Encerrar, a execução do programa deverá ser finalizada.
SOLUÇÃO:
ALGORITMO
DECLARE corredor[24], janela[24] NUMÉRICO
 achou LÓGICO
posicao LITERAL 
i, num NUMÉRICO
PARA i ← 1 ATÉ 24 FAÇA
INÍCIO
corredor[i] ← 0
janela[i] ← 0
FIM
REPITA
ESCREVA “1- Vender passagem”
ESCREVA “2- Mostrar mapa de ocupação do ônibus”
ESCREVA “3- Encerrar”
LEIA op
SE op = 1
ENTÃO INÍCIO
 achou ← falso
 PARA i ← 1 ATÉ 24 FAÇA
 INÍCIO
 SE corredor[i] = 0 OU janela[i] = 0
ENTÃO achou ← verdadeiro
 FIM
 SE achou = falso
ENTÃO ESCREVA “Ônibus lotado”
SENÃO INÍCIO
REPITA
LEIA posicao
ATÉ posicao = “J” OU posicao = “C”
REPITA
LEIA num
ATÉ num >= 1 E num <= 24
SE posicao = “J” E janela[num] = 1

---

Capítulo 6 Vetor  | 189
FIM
cont_r ← 1
PARA i ← 1 ATÉ 10 FAÇA
INÍCIO
qtde ← 1
PARA j ← 1 ATÉ 10 FAÇA 
INÍCIO
SE i ≠ j
ENTÃO SE a[i] = a[j]
ENTÃO qtde ← qtde + 1
FIM
SE qtde > 1
ENTÃO INÍCIO
cont ← 1
 ENQUANTO (cont < cont_r E (a[i] ≠ repetidos[cont])) FAÇA 
INÍCIO
cont ← cont + 1
FIM
SE cont = cont_r
ENTÃO INÍCIO
repetidos[cont_r] ← a[i]
vezes[cont_r] ← qtde
cont_r ← cont_r + 1
FIM
FIM
FIM
PARA i ← 1 ATÉ cont_r - 1 FAÇA
ESCREVA “O número “,repetidos[i], “ apareceu “,vezes[i],” vezes” 
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP6\PASCAL\EX24.PAS e \EXERC\CAP6\PASCAL\EX24.EXE
SOLUÇÃO:
\EXERC\CAP6\C++\EX24.CPP e \EXERC\CAP6\C++\EX24.EXE
SOLUÇÃO:
\EXERC\CAP6\JAVA\EX24.java e \EXERC\CAP6\JAVA\EX24.class  
25. Faça um programa que gere os dez primeiros números primos acima de 100 e armazene-os em um  
vetor. Escreva no final o vetor resultante.
SOLUÇÃO:
ALGORITMO
DECLARE primos[10] NUMÉRICO
i, qtde, num, divisores NUMÉRICO
num ← 101
qtde ← 1
REPITA
divisores ←  0
PARA i ← 1 ATÉ num FAÇA
INÍCIO
SE RESTO(num/i) = 0
ENTÃO divisores ← divisores + 1 
PASCAL
C/C++
JAVA

---

Capítulo 6 Vetor  | 191
Coloque os números das matrículas dos alunos que cursam Linguagem de Programação em outro vetor, dez 
alunos. Mostre o número das matrículas que aparecem nos dois vetores. 
6. Faça um programa que receba o total das vendas de cada vendedor de uma loja e armazene-as em um vetor. 
Receba também o percentual de comissão a que cada vendedor tem direito e armazene-os em outro vetor. 
Receba os nomes desses vendedores e armazene-os em um terceiro vetor. Existem apenas dez vendedores na 
loja. Calcule e mostre: 
 ■ um relatório com os nomes dos vendedores e os valores a receber referentes à comissão; 
 ■ o total das vendas de todos os vendedores; 
 ■ o maior valor a receber e o nome de quem o receberá; 
 ■ o menor valor a receber e o nome de quem o receberá. 
7. Faça um programa que preencha um vetor com dez números reais, calcule e mostre a quantidade de números 
negativos e a soma dos números positivos desse vetor. 
8. Faça um programa que preencha um vetor com os nomes de sete alunos e carregue outro vetor com a média 
final desses alunos. Calcule e mostre: 
 ■ o nome do aluno com maior média (desconsiderar empates); 
 ■ para cada aluno não aprovado, isto é, com média menor que 7, mostrar quanto esse aluno precisa ti-
rar na prova de exame final para ser aprovado. Considerar que a média para aprovação no exame é 5. 
9. Faça um programa que preencha três vetores com dez posições cada um: o primeiro vetor, com os nomes de 
dez produtos; o segundo vetor, com os códigos dos dez produtos; e o terceiro vetor, com os preços dos pro-
dutos. Mostre um relatório apenas com o nome, o código, o preço e o novo preço dos produtos que sofrerão 
aumento. 
Sabe-se que os produtos que sofrerão aumento são aqueles que possuem código par ou preço superior a 
R$ 1.000,00. Sabe-se ainda que, para os produtos que satisfazem as duas condições anteriores, código e 
preço, o aumento será de 20%; para aqueles que satisfazem apenas a condição de código, o aumento será 
de 15%; e para aqueles que satisfazem apenas a condição de preço, o aumento será de 10%.
10. Faça um programa que preencha um vetor com dez números inteiros e um segundo vetor com cinco nú-
meros inteiros, calcule e mostre dois vetores resultantes. O primeiro vetor resultante será composto pela 
soma de cada número par do primeiro vetor somado a todos os números do segundo vetor. O segundo 
vetor resultante será composto pela quantidade de divisores que cada número ímpar do primeiro vetor 
tem no segundo vetor.
Primeiro
vetor 4 7 5 8 2 15 9 6 10 11
1 2 3 4 5
1 2 3 4 5
3 4 5 8 2
6 7 8 9 10
Segundo
vetor
Primeiro vetor resultante Segundo vetor resultante
26 30 …
8+3+4+5+8 + 2
4+3+4+5+8 + 2
0 1 …
7 não possui 
divisores
24 2
15 é divisível
por3e por 5
5é divisível
apenas por 5

---

Capítulo 6 Vetor  | 193
20. Faça um programa que leia um vetor com dez posições para números inteiros e mostre somente os nú-
meros positivos. 
21. Faça um programa que leia um vetor com dez posições para números inteiros. Crie um segundo vetor, 
substituindo os valores nulos por 1. Mostre os dois vetores. 
22. Faça um programa que leia um vetor A de dez posições. Em seguida, compacte o vetor, retirando os  
valores nulos e negativos. Armazene esse resultado no vetor B. Mostre o vetor B. (Lembre-se: o vetor B 
pode não ser completamente preenchido.)
23. Faça um programa que leia dois vetores (A e B) com cinco posições para números inteiros. O programa 
deve, então, subtrair o primeiro elemento de A do último de B, acumulando o valor, subtrair o segundo 
elemento de A do penúltimo de B, acumulando o valor e assim por diante. Ao final, mostre o resultado 
de todas as subtrações realizadas.
24. Faça um programa que leia um vetor com quinze posições para números inteiros. Crie, a seguir, um vetor 
resultante que contenha todos os números primos do vetor digitado. Escreva o vetor resultante. 
25. Faça um programa que leia um vetor com quinze posições para números inteiros. Depois da leitura, di-
vida todos os seus elementos pelo maior valor do vetor. Mostre o vetor após os cálculos.

---



=== CAPÍTULO 7 ===

---

Capítulo 7 Matriz  | 195
2 3 561 4
2
2
1
1
3
3
4X[4,1,1] X[3,6,2]
7.1.4 Atribuindo valores a uma matriz
Cada elemento de uma matriz pode armazenar um valor. Para fazer esse armazenamento, é necessário 
executar uma atribuição, informando o número da posição desejada em cada dimensão.
Exemplo 1:
declare mat[5,4] numérico
mat[2,4] ← 45
mat[3,1] ← -8
mat[1,3] ← 10
No exemplo 1, a declaração da matriz mat informa que ela tem 2 dimensões. A primeira dimensão, 
que representa as linhas, tem tamanho 5; a segunda dimensão de mat tem tamanho 4. Ou seja, para cada 
linha há 4 colunas, permitindo, assim, que a matriz tenha espaço para armazenar 20 valores numéricos. A 
representação gráfica da matriz mat e as três atribuições podem ser vistas a seguir.
Matriz mat
1 10
2 45
3 -8
4
5
1 2 3 4
Exemplo 2:
declare m[4,5,3] literal
m[3,4,1] ← “E”
m[4,5,3] ← “g” 
m[1,2,2] ← “A”
No exemplo 2, a declaração da matriz m informa que ela tem 3 dimensões. A primera dimensão, que 
representa as linhas, tem tamanho 4; a segunda dimensão, que representa as colunas, tem tamanho 5; e a 
terceira dimensão, que representa a profundidade, tem tamanho 3. Assim, a matriz m tem espaço para arma-
zenar 60 valores literais. A representação gráfica da matriz m e as três atribuições podem ser vistas a seguir.

---

Capítulo 7 Matriz  | 197
X 2
1
3
2
9
4
45
3
3
2
3
5
-23
-4
-3
1
12
15
3
4
7
34
0
Já no exemplo que se segue, é preenchida uma matriz tridimensional com quatro linhas, três colunas 
e profundidade dois. Observe que os valores da variável i estão dentro do intervalo de 1 a 4, ou seja, 
exatamente o número das linhas da matriz. Para cada valor assumido por i, os valores da variável j se 
movimentam de 1 a 3, ou seja, as três colunas que cada linha possui. Por fim, os valores da variável k se 
alternam entre 1 e 2, exatamente os valores da profundidade.
PARA i ← 1 ATÉ 4 FAÇA 
INÍCIO
 PARA j ← 1 ATÉ 3 FAÇA
 INÍCIO
  PARA k ← 1 ATÉ 2 FAÇA
   INÍCIO
    ESCREVA  “Digite o número da linha “,i, “ coluna “, j, “ e profundidade 
Ê “, k, “:”
    LEIA X[i,j,k]
   FIM
 FIM
FIM
Simulação:
MEMÓRIA TELA
i j k
1 1 1 Digite o número da linha 1 coluna 1 e profundidade 1: 2
2 Digite o número da linha 1 coluna 1 e profundidade 2: 5
2 1 Digite o número da linha 1 coluna 2 e profundidade 1: –1
2 Digite o número da linha 1 coluna 2 e profundidade 2: 0
3 1 Digite o número da linha 1 coluna 3 e profundidade 1: 15
2 Digite o número da linha 1 coluna 3 e profundidade 2: 8
2 1 1 Digite o número da linha 2 coluna 1 e profundidade 1: –25
2 Digite o número da linha 2 coluna 1 e profundidade 2: 3
2 1 Digite o número da linha 2 coluna 2 e profundidade 1: 6
2 Digite o número da linha 2 coluna 2 e profundidade 2: 9
3 1 Digite o número da linha 2 coluna 3 e profundidade 1: 7
2 Digite o número da linha 2 coluna 3 e profundidade 2: 11
3 1 1 Digite o número da linha 3 coluna 1 e profundidade 1: 23
2 Digite o número da linha 3 coluna 1 e profundidade 2: –2
2 1 Digite o número da linha 3 coluna 2 e profundidade 1: –5
2 Digite o número da linha 3 coluna 2 e profundidade 2: 46
3 1 Digite o número da linha 3 coluna 3 e profundidade 1: 19
2 Digite o número da linha 3 coluna 3 e profundidade 2: 1
4 1 1 Digite o número da linha 4 coluna 1 e profundidade 1: 14
2 Digite o número da linha 4 coluna 1 e profundidade 2: 27
2 1 Digite o número da linha 4 coluna 2 e profundidade 1: 5
2 Digite o número da linha 4 coluna 2 e profundidade 2: 4
3 1 Digite o número da linha 4 coluna 3 e profundidade 1: 10
2 Digite o número da linha 4 coluna 3 e profundidade 2: 65

---

Capítulo 7 Matriz  | 199
A primeira estrutura de repetição (linha 1) é controlada pela variável i, que poderá assumir valores 
dentro do intervalo de 1 a 3. Cada vez que essa estrutura PARA for executada, encontrará a segunda estru-
tura de repetição (linha 4), controlada pela variável j, que assumirá os valores dentro do intervalo de 1 a 4. 
Assim, cada valor assumido pela variável i estará associado a 4 valores da variável j. 
Esse arranjo resolve o problema de mostrar os elementos, separando-os por linhas, já que a variável i 
ficará com valor fixo, enquanto a variável j assumirá valores de 1 a 4, ou seja, formará todos os pares possí-
veis de índices. Se i estiver valendo 1, serão mostrados todos os elementos da linha 1, já que serão formados 
os seguintes pares: x[1,1], x[1,2], x[1,3] e x[1,4]. Depois, a variável i assume o valor 2 e novamente a j terá 
seus valores variando de 1 a 4. Com isso, será possível percorrer toda a linha 2 por meio da formação dos 
pares x[2,1], x[2,2], x[2,3] e x[2,4]. Esse processo se repetirá para os demais valores possíveis de i. A tabela 
a seguir mostra uma simulação de execução do algoritmo. Nessa simulação, é importante observar como as 
variáveis i e j têm seus valores alterados.
Simulação:
MEMÓRIA TELA
i j
1 Elementos da linha 1
1 1 4
1 2 5
1 3 1
1 4 10
2 Elementos da linha 2
2 1 16
2 2 11
2 3 76
2 4 8
3 Elementos da linha 3
3 1 9
3 2 54
3 3 32
3 4 89
A figura a seguir dá uma outra visão da forma utilizada para percorrer a matriz. A direção das setas indica 
a mudança no valor das variáveis i e j e o caminho utilizado para percorrer a matriz.
Matriz x
1 4 5 1 10
2 16 11 76 8
3 9 54 32 89
1 2 3 4
Forma 2: precisamos percorrer a matriz, de tal forma que seja possível mostrar todos os elementos gravados 
em cada coluna. Para isso, utilizaremos duas estruturas de repetição, conforme mostrado a seguir (a nume-
ração à esquerda não faz parte do algoritmo, servirá apenas para facilitar a explicação).
1. PARA i ←1 ATÉ 4 FAÇA
2. INÍCIO
3.   ESCREVA “Elementos da coluna “, i
4.  PARA j ← 1 ATÉ 3 FAÇA
5.  INÍCIO
6.   ESCREVA x[j, i]
7.  FIM
8. FIM

---

Capítulo 7 Matriz  | 201
7.2 Matriz em PASCAL
7.2.1 Deﬁnição de matriz
As variáveis compostas homogêneas multidimensionais (ou, simplesmente, matrizes) são conhecidas na 
linguagem PASCAL como ARRAY. Uma estrutura do tipo ARRAY é uma sequência de variáveis com o mesmo 
identificador (mesmo nome) e alocadas sequencialmente na memória. Todas as variáveis que compõem uma 
ARRAY devem ser do mesmo tipo.
Uma vez que as variáveis recebem o mesmo nome, o que as distingue são os índices que referenciam sua 
posição em cada dimensão da estrutura. Assim, se a matriz for bidimensional necessitará de dois índices, se 
for tridimensional necessitará de três índices, e assim por diante.
7.2.2 Declaração de matriz
VAR nome_da_variável:   ARRAY[inicio1..fim1, inicio2..fim2,  
inicioN..fimN] OF tipo_dos_dados;
onde:
nome_da_variável: é o nome da variável do tipo matriz; 
inicio1: é o índice inicial da primeira dimensão da matriz; 
fim1: é o índice final da primeira dimensão da matriz; 
inicio2: é o índice inicial da segunda dimensão da matriz; 
fim2: é o índice final da segunda dimensão da matriz; 
inicioN: é o índice inicial da n-ésima dimensão da matriz; 
fimN: é o índice final da n-ésima dimensão da matriz;
tipo_dos_dados: é o tipo básico dos dados que serão armazenados na matriz.
É importante salientar que o valor do índice_inicial deve ser maior ou igual ao valor do índice_fi-
nal, para cada dimensão. As posições são identificadas com valores dentro desse intervalo. 
Além disso, é importante destacar que os índices também podem ser representados por valores alfa -
béticos. Com isso, é permitido o uso de caracteres para representar o início e o fim de cada dimensão. O 
exemplo a seguir ilustra essa possibilidade. Como se pode ver, a matriz terá 5 linhas (de C a G) e 4 colunas 
(de L a O).
VAR matriz: ARRAY [‘C’..’G’, ‘L’..’O’] OF REAL;
Observação
Os valores que indicam o  índice_inicial e o índice_final devem representar valores 
fixos (literais1 ou constantes), não podendo ser substituídos por variáveis.
7.2.3 Exemplos de matriz
VAR X: ARRAY[1..2,1..6] OF REAL;
2 4 61 5
2
X 1
3
VAR MAT: ARRAY[2..5,3..6] OF CHAR;
1 Literal é um valor ﬁxo, deﬁnido quando se escreve o programa. Por exemplo: x:=10.3; onde 10.3 é um literal. vet: array 
[3..7, 4..9] of integer; onde 3, 7, 4 e 9, escritos dentro dos colchetes, são literais.

---

Capítulo 7 Matriz  | 203
MAT[4,5] :=’D’;  →  Atribui a letra D à posição identificada pelos índices 4 (linha) e 5 (coluna).
43
3
MAT
2
5
5
D
6
4
Y[1,4,2] := 12;  →  Atribui o valor 12 à posição identificada pelos índices 1 (linha), 4 (coluna) 
e 2 (profundidade).
2 31 4
12
2
2
1
1
Y
3
12
MAT[‘C’,‘H’] := 20;  →  Atribui o valor 20 à posição identificada pelos índices C (linha) e H (coluna).
MAT
A  
B
C 20
D
F G H I J
7.2.5 Preenchendo uma matriz
Preencher uma matriz significa percorrer todos os seus elementos, atribuindo-lhes um valor. Esse 
valor pode ser recebido do usuário, pelo teclado, ou pode ser gerado pelo programa.
Exemplo 1:
FOR i:= 1 TO 7 DO
 BEGIN
  FOR j:=1 TO 3 DO
  BEGIN
   READLN(X[i,j]);
  END;
 END;
 Exemplo 2:
FOR i:=’C’ TO ‘G’ DO
 BEGIN
  FOR j:= ‘L’ TO ‘O’ DO
  BEGIN
   READLN(MAT[i,j]);
  END;
END;

---

Capítulo 7 Matriz  | 205
Matriz x
1 4 5 1 10
2 16 11 76 8
3 9 54 32 89
1 2 3 4
Forma 1: precisamos percorrer a matriz, de tal forma que seja possível mostrar todos os elementos 
gravados em cada linha. Para isso, utilizaremos duas estruturas de repetição, conforme mostrado a seguir (a 
numeração à esquerda não faz parte do programa, servirá apenas para facilitar a explicação).
1. FOR i := 1 TO 3 DO
2. BEGIN
3.    WRITELN( ‘Elementos da linha ‘, i);
4.    FOR j := 1 TO 4 DO
5.    BEGIN 
6.    WRITELN(x[i,j]);
7.    END;
8. END;
A primeira estrutura de repetição (linha 1) é controlada pela variável i, que poderá assumir valores 
dentro do intervalo de 1 a 3. Cada execução da estrutura FOR encontrará a segunda estrutura de repetição 
(linha 4), controlada pela variável j, que assumirá os valores dentro do intervalo de 1 a 4. Assim, cada valor 
assumido pela variável i estará associado a 4 valores da variável j. 
Esse arranjo resolve o problema de mostrar os elementos, separando-os por linhas, já que a variável 
i ficará com valor fixo enquanto a variável  j assumirá valores de 1 a 4, ou seja, formará todos os pares 
possíveis de índices. Se i estiver valendo 1, serão mostrados todos os elementos da primeira linha, já que 
serão formados os seguintes pares: x[1,1], x[1,2], x[1,3] e x[1,4]. Depois, a variável  i assume o valor 2 e 
novamente a j terá seus valores variando de 1 a 4. Com isso, será possível percorrer toda a segunda linha, 
por meio da formação dos pares x[2,1], x[2,2], x[2,3] e x[2,4]. Esse processo se repetirá para os demais 
valores possíveis de i. A tabela a seguir mostra uma simulação de execução do programa. Nessa simulação 
é importante observar como as variá veis i e j têm seus valores alterados.
Simulação:
MEMÓRIA TELA
i j
1 Elementos da linha 1
1 1 4
1 2 5
1 3 1
1 4 10
2 Elementos da linha 2
2 1 16
2 2 11
2 3 76
2 4 8
3 Elementos da linha 3
3 1 9
3 2 54
3 3 32
3 4 89

---

Capítulo 7 Matriz  | 207
 A figura a seguir dá outra visão da forma utilizada para percorrer a matriz. A direção das setas indica 
a mudança no valor das variáveis i e j e o caminho utilizado para percorrer a matriz.
Matriz x
1 4 5 1 10
2 16 11 76 8
3 9 54 32 89
1 2 3 4
Pelas formas de percorrer uma matriz apresentadas anteriormente, podemos observar alguns pontos 
que merecem atenção: 
 ■ a mudança dos valores das varáveis i e j, que controlam as estruturas de repetição, permite a for-
mação de todos os possíveis pares de linha e coluna existentes na matriz. 
 ■ a mudança do valor da variável  i , utilizada no FOR externo, acontece mais lentamente que a 
mudança da variável j, utilizada no FOR interno. Logo, foi a variável i que indicou como seria o 
percurso: na primeira forma apresentada, i variou de 1 a 3 e foi usada na primeira posição dentro 
do colchetes, isso mostrou que o percurso seria horizontal, porque o índice da linha ficava parado 
enquanto j assumia todas as colunas possíveis para aquela linha. Já na segunda forma apresenta -
da, i variou de 1 a 4 e foi usada na segunda posição dentro dos colchetes, indicando que o percurso 
seria vertical, pois o índice da coluna ficava parado enquanto j assumia todas as linhas possíveis para 
aquela coluna.
7.3 Matriz em C/C++
7.3.1 Deﬁnição de matriz
Uma matriz pode ser definida como um conjunto de variáveis de mesmo tipo e identificadas pelo 
mesmo nome. Essas variáveis são diferenciadas por meio da especificação de suas posições dentro dessa 
estrutura.
A linguagem C/C++ permite a declaração de matrizes unidimensionais (mais conhecidas co mo vetores — 
descritos no capítulo anterior), bidimensionais e multidimensionais. O padrão ANSI prevê até 12 dimensões. 
Entretanto, o limite de dimensões fica por conta da quantidade de recursos computacionais disponíveis. 
Apesar disso, as matrizes mais utilizadas possuem duas dimensões. Para cada dimensão deve ser utilizado 
um índice.
Os índices usados na linguagem C/C++, para identificar as posições de uma matriz, começam sempre 
em 0 (zero) e vão até o tamanho da dimensão menos uma unidade. Os índices de uma matriz em C/C++ 
devem sempre ser representados por um dos tipos inteiros disponíveis na linguagem.
7.3.2 Declaração de matriz
tipo_dos_dados nome_variável [dimensão1] [dimensão2] [...] [dimensãoN];
onde:
tipo_dos_dados: é o tipo dos dados que serão armazenados na matriz; 
nome_variável: é o nome dado à variável do tipo matriz; 
[dimensão1]: representa o tamanho da 1a dimensão da matriz; 
[dimensão2]: representa o tamanho da 2a dimensão da matriz; 
[dimensãoN]: representa o tamanho da n-ésima dimensão da matriz.
Em C/C++, a indicação do tamanho das dimensões de uma matriz deve ser feita por um valor inteiro 
fixo (representado por um literal 2 ou uma constante). Se houver necessidade de definir o tamanho do ve -
tor em tempo de execução, deve-se fazê-lo por meio de ponteiros (o Capítulo 8 apresentará o conceito de 
ponteiro).
2  Literal é um valor ﬁxo, deﬁnido quando se escreve o programa. Por exemplo: double x=10.3; onde 10.3 é um literal. char mat [2][5]; 
onde 2 e 5, escritos dentro dos colchetes, são literais.

---

Capítulo 7 Matriz  | 209
MAT[3][2] = ‘D’;       →  Atribui a letra D à posição identificada pelos índices 3 (4 a linha) e 2  
(3a coluna).
01 2
0
MAT 1
2
3 D
Y[0][3][1] = 12;       →  Atribui o valor 12 à posição identificada pelos índices 0 (1 a linha), 3  
(4a coluna) e 1 (2a profundidade).
1 20 3
12
1
1
0
0
Y 2
12
7.3.5 Preenchendo uma matriz
Preencher uma matriz significa percorrer todos os seus elementos, atribuindo-lhes um valor. Esse valor 
pode ser recebido do usuário, por meio do teclado, ou pode ser gerado pelo programa.
No exemplo que se segue, todos os elementos de uma matriz bidimensional são percorridos, atribuin -
do-lhes valores digitados pelo usuário e capturados pelo comando scanf.
for (i=0;i<7;i++)
 {
  for (j=0;j<3;j++) 
   scanf(“%d%*c”, &MAT[i][j]);
 }
Como a matriz possui 7 linhas e 3 colunas, o exemplo apresentou duas estruturas de repetição for para 
garantir que a variável i assumisse todos os valores possíveis para linha (de 0 a 6) e a variável j assumisse 
todos os valores possíveis para coluna (de 0 a 2) da matriz MAT.  Assim, para cada execução das estruturas 
de repetição, uma posição diferente da matriz foi preenchida por um valor digitado pelo usuário por meio 
do comando scanf.
7.3.6 Mostrando os elementos de uma matriz
Pode-se também percorrer todos os elementos de uma matriz acessando seu conteúdo. Para mostrar os 
valores armazenados dentro de uma matriz, supondo que ela tenha sido declarada como float X[10][6], 
podem-se executar os comandos a seguir.
for (i=0;i<10;i++)
 { for (j=0;j<6;j++) 
  printf(“%f”, X[i][j]);
 }
Como a matriz possui dez linhas e seis colunas, o exemplo usou duas estruturas de repetição for para 
garantir que a variável i assumisse todos os valores possíveis para linha (de 0 a 9) e a variável j assumisse 
todos os valores possíveis para coluna (de 0 a 5) da matriz X. Assim, para cada execução das estruturas de 
repetição, uma posição diferente da matriz foi acessada e seu conteúdo mostrado por meio do comando 
printf.

---

Capítulo 7 Matriz  | 211
MEMÓRIA TELA
1 1 11
1 2 76
1 3 8
2 Elementos da linha 2
2 0 9
2 1 54
2 2 32
2 3 89
A figura a seguir dá outra visão da forma utilizada para percorrer a matriz. A direção das setas indica 
a mudança no valor das variáveis i e j e o caminho utilizado para percorrer a matriz.
Matriz x
0 4 5 1 10
1 16 11 76 8
2 9 54 32 89
0 1 2 3
Forma 2: precisamos percorrer a matriz, de tal forma que seja possível mostrar todos os elementos gra-
vados em cada coluna. Para isso, utilizaremos duas estruturas de repetição, conforme mostrado a seguir (a 
numeração à esquerda não faz parte do programa, servirá apenas para facilitar a explicação).
1. for (i=0;i<4;i++)
2. {
3.    printf(“Elementos da coluna %d“, i);
4.    for (j=0;j<3;j++) 
5.    { 
6.     printf(“%d”, x[j,  i]);
7.    }
8. }
A primeira estrutura de repetição (linha 1) é controlada pela variável i, que poderá assumir valores 
dentro do intervalo de 0 a 3. Cada execução dessa estrutura for encontrará a segunda estrutura de repetição 
(linha 4), controlada pela variável j, que assumirá os valores dentro do intervalo de 0 a 2. Assim, cada valor 
assumido pela variável i estará associado a 3 valores da variável j. Esse arranjo resolve o problema de mos-
trar os elementos, separando-os por colunas, já que a variável i ficará com valor fixo enquanto a variável j 
assumirá valores de 0 a 2, ou seja, formará todos os pares possíveis de índices. Se i estiver valendo 0, serão 
mostrados todos os elementos da primeira coluna, já que serão formados os seguintes pares: x[0,0], x[1,0] 
e x[2,0]. Depois, a variável i assumirá o valor 1 e novamente j terá seus valores variando de 0 a 2. Com 
isso, será possível percorrer toda a segunda coluna, por meio da formação dos pares x[0,1], x[1,1] e x[2,1]. 
Esse processo se repetirá para os demais valores possíveis de i. A tabela a seguir mostra uma simulação de 
execução do programa. Nessa simulação, é importante observar como as variáveis i e j têm seus valores 
alterados.
Simulação:
MEMÓRIA TELA
i j
0 Elementos da coluna 0
0 0 4
0 1 16
0 2 9
1 Elementos da coluna 1
1 0 5

---

Capítulo 7 Matriz  | 213
Para utilizar uma matriz em JAVA, é preciso seguir dois passos:
1
O
 PASSO: DECLARAR  UMA  VARIÁVEL  QUE  FARÁ  REFERÊNCIA  AOS  ELEMENTOS
tipo_dos_dados nome_variável[][][]...[];
 Os pares de colchetes vazios após o nome da variável definem que a variável será uma estrutura mul -
tidimensional.
2
O
 PASSO:  DEFINIR  O  TAMANHO  DAS  DIMENSÕES  DA  MATRIZ
nome_variável = new tipo_dos_dados [dimensão1][dimensão2][dimensão3]...[dimensãoN];
onde:
tipo_dos_dados: é o tipo de dados que poderá ser armazenado na sequência de variáveis que formam 
a matriz; 
nome_variável: é o nome dado à variável do tipo matriz;
[dimensão1]: representa o tamanho da primeira dimensão da matriz; 
[dimensão2]: representa o tamanho da segunda dimensão da matriz; 
[dimensãoN]: representa o tamanho da n-ésima dimensão da matriz.
7.4.3 Exemplos de matriz
Nos exemplos a seguir, são utilizadas duas linhas de comando: a primeira declara uma matriz, e a se -
gunda define o tamanho das dimensões.
É importante ressaltar que, em JAVA, os pares de colchetes podem aparecer todos antes do nome da 
variável ou depois do nome da variável ou, ainda, alguns antes e outros posteriormente. Assim, todos os 
exemplos a seguir são válidos.
Exemplo 1:
float X[][];
X = new float[2][6];
A declaração anterior criou uma variável chamada X contendo duas linhas (0 a 1) com seis colunas cada 
(0 a 5), capazes de armazenar números reais, como pode ser observado a seguir.
01234 5
X0
1
Exemplo 2:
char [][]MAT;
MAT = new char[4][3];        
A declaração anterior criou uma variável chamada MAT contendo quatro linhas (0 a 3) com três colunas 
cada (0 a 2), capazes de armazenar caracteres, como pode ser observado a seguir.
01 2
0
MAT 1
2
3
Exemplo 3:
int [][]Y[];
Y = new int[2][4][3];

---

Capítulo 7 Matriz  | 215
É importante lembrar, também, que o tamanho das dimensões não precisa ser feito em um mesmo mo-
mento. Os exemplos que seguem mostram essa flexibilidade.
Exemplo 7: 
Nesse exemplo (a numeração das linhas foi utilizada apenas para facilitar a explicação), foi definido 
pela linha 1 que a variável Y é uma matriz bidimensional. A linha 2 estabelece que o tamanho da primeira 
dimensão é 2, ou seja, essa matriz tem duas linhas, identificadas pelos índices 0 e 1. Na linha 3, foi definido 
o tamanho da linha 0, que passou a ter 5 colunas. Já a linha 4 define o tamanho da linha 1, que passou a 
ter 2 colunas.
1. int Y[][];
2. Y = new int[2][];
3. Y[0] = new int[5];
4. Y[1] = new int[2];
 Uma representação dessa matriz poderia ser:
Matriz Y 0
1
0 1 2 3 4
7.4.4 Atribuindo valores a uma matriz
Atribuir valor a uma matriz significa armazenar uma informação em um de seus elementos, identifica-
do de forma única por meio de seus índices.
X[1][4]=5;  →  Atribui o valor 5 à posição identificada pelos índices 1 (2a linha) e 4 (5a coluna).
012345
X0
15
MAT[3][2] = ‘D’;  →     Atribui a letra D à posição identificada pelos índices 3 (4 a linha) e 2  
(3a coluna).
01 2
0
MAT 1
2
3 D
Y[0][3][1] = 12;       →  Atribui o valor 12 à posição identificada pelos índices 0 (1 a linha), 3  
(4a coluna) e 1 (2a profundidade).
1 20 3
12
1
1
0
0
Y
2
12

---

Capítulo 7 Matriz  | 217
7.4.6 Mostrando os elementos de uma matriz
Pode-se, também, percorrer todos os elementos da matriz, acessando seu conteúdo.
Exemplo 1:
for (i=0; i<10; i++)
 {
  for (j=0; j<6; j++)
   System.out.println(X[i][j]);
 }
No exemplo 1 foram mostrados todos os elementos de uma matriz contendo dez linhas e seis colunas. 
Observe que são usados dois índices, i e j. Esses índices estão atrelados a estruturas de repetição que mantêm 
a variação de ambos dentro de intervalos permitidos. Ou seja, o índice i, que representa as linhas, varia de 0 
a 9 e o índice j, que representa as colunas, varia de 0 a 5.
Exemplo 2:
1. for (i=0;i<MAT.length;i++)
2. {
3.    for (j=0;j<MAT[i].length;j++)
4.     System.out.println(MAT[i][j]);
5. }
No exemplo 2, também foram mostrados todos os elementos de uma matriz. Contudo, em virtude do 
uso do atributo length (apresentado em detalhes na Seção 7.4.5), as linhas dessa matriz podem ter tama -
nhos diferentes.
Na linha 1, podemos ver o uso de MAT.length, que significa o tamanho da primeira dimensão de MAT, 
ou seja, a quantidade de linhas. Na linha 3, podemos ver MAT[i].length, que significa o tamanho da linha 
i de MAT. 
Com as duas estruturas de repetição for, pode-se garantir que a variável i assuma todos os valores possíveis 
para linha e a variável j assuma todos os valores possíveis para coluna, respeitando os dimensionamentos feitos. 
Assim, para cada execução das estruturas de repetição, uma posição diferente da matriz foi acessada e seu valor 
mostrado por meio do método println() da classe System.
7.4.7 Percorrendo uma matriz
Vimos anteriormente, nos tópicos 7.4.5 e 7.4.6, formas para preencher toda uma matriz e para mostrar 
todas as posições de uma matriz. Em tais operações, foi necessário passar por todas as posições, ou seja, foi 
preciso percorrer a matriz. 
Uma das formas mais simples de percorrer uma matriz pode ser por meio do uso de uma estrutura de 
repetição para cada dimensão da matriz. A ordem de disposição de tais estruturas de repetição define a 
forma como a matriz será percorrida. 
A seguir, apresentaremos duas formas para percorrer uma mesma matriz, chamada x, contendo 3 linhas 
e 4 colunas. 
Matriz x
0 4 5 1 10
1 16 11 76 8
2 9 54 32 89
0 1 2 3
Forma 1: precisamos percorrer a matriz, de tal forma que seja possível mostrar todos os elementos 
gravados em cada linha. Para isso, utilizaremos duas estruturas de repetição, conforme mostrado a seguir (a 
numeração à esquerda não faz parte do programa, servirá apenas para facilitar a explicação).

---

Capítulo 7 Matriz  | 219
1. for (i=0;i<4;i++)
2. {
3.    System.out.println(“Elementos da coluna “ + i);
4.    for (j=0;j<3;j++) 
5.    { 
6.     System.out.println(x[j,i]);
7.    }
8. }
A primeira estrutura de repetição (linha 1) é controlada pela variável i, que poderá assumir valores 
dentro do intervalo de 0 a 3. Cada execução da estrutura encontrará a segunda estrutura de repetição 
(linha 4), controlada pela variável  j, que assumirá os valores dentro do intervalo de 0 a 2. Assim, cada 
valor assumido pela variável i estará associado a 3 valores da variável j. Esse arranjo resolve o problema 
de mostrar os elementos, separando-os por colunas, já que a variável  i ficará com valor fixo enquanto 
a variável j assumirá valores de 0 a 2, ou seja, formará todos os pares possíveis de índices. Se i estiver 
valendo 0, serão mostrados todos os elementos da primeira coluna, já que serão formados os seguintes 
pares: x[0,0], x[1,0] e x[2,0]. Depois, a variável i assumirá o valor 1 e novamente j terá seus valores 
variando de 0 a 2. Com isso, será possível percorrer toda a segunda coluna, por meio da formação dos 
pares x[0,1], x[1,1] e x[2,1]. Esse processo se repetirá para os demais valores possíveis de  i. A tabela a 
seguir mostra uma simulação de execução do algoritmo. Nessa simulação é importante observar como as 
variáveis i e j têm seus valores alterados.
Simulação:
MEMÓRIA TELA
i j
0 Elementos da coluna 0
0 0 4
0 1 16
0 2 9
1 Elementos da coluna 1
1 0 5
1 1 11
1 2 54
2 Elementos da coluna 2
2 0 1
2 1 76
2 2 32
3 Elementos da coluna 3
3 0 10
3 1 8
3 2 89
A figura a seguir dá outra visão da forma utilizada para percorrer a matriz. A direção das  setas indica 
a mudança no valor das variáveis i e j e o caminho utilizado para percorrer a matriz.
Matriz x
0 4 5 1 10
1 16 11 76 8
2 9 54 32 89
0 1 2 3
Pelas formas de percorrer uma matriz apresentadas anteriormente, podemos observar alguns pontos 
que merecem atenção: 
 ■ a mudança dos valores das varáveis i e j, que controlam as estruturas de repetição, permite a for-
mação de todos os possíveis pares de linha e coluna existentes na matriz.

---

Capítulo 7 Matriz  | 221
2. Faça um programa que preencha uma matriz 10 × 3 com as notas de dez alunos em três provas. O  
programa deverá mostrar um relatório com o número dos alunos (número da linha) e a prova em que 
cada aluno obteve menor nota. Ao final do relatório, deverá mostrar quantos alunos tiveram menor 
nota em cada uma das provas: na prova 1, na prova 2 e na prova 3.
SOLUÇÃO:
ALGORITMO
DECLARE notas[10,3],q1, q2, q3, menor, p_menor, i, j NUMÉRICO 
PARA i ← 1 ATÉ 10 FAÇA
 INÍCIO
 PARA j ← 1 ATÉ 3 FAÇA 
  INÍCIO
   LEIA notas[i,j] 
  FIM
 FIM
q1 ← 0
q2 ← 0
q3 ← 0
PARA i ← 1 ATÉ 10 FAÇA 
 INÍCIO
ESCREVA i
menor ← notas[i,1] 
p_menor ← 1
PARA j ← 1 ATÉ 3 FAÇA 
  INÍCIO
   SE notas[i, j] < menor 
    ENTÃO INÍCIO
     menor ← notas[i, j] 
     p_menor ← j
          FIM
  FIM 
  ESCREVA p_menor 
  SE p_menor = 1
   ENTÃO q1 ← q1 + 1 
  SE p_menor = 2
   ENTÃO q2 ← q2 + 1 
  SE p_menor = 3
   ENTÃO q3 ← q3 + 1
 FIM 
ESCREVA q1, q2, q3 
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP7\PASCAL\EX2.PAS e \EXERC\CAP7\PASCAL\EX2.EXE
SOLUÇÃO:
\EXERC\CAP7\C++\EX2.CPP e \EXERC\CAP7\C++\EX2.EXE
SOLUÇÃO:
\EXERC\CAP7\JAVA\EX2.java e \EXERC\CAP7\JAVA\EX2.class
3. Faça um programa que preencha: 
 ■ um vetor com oito posições, contendo nomes de lojas; 
 ■ outro vetor com quatro posições, com nomes de produtos; 
 ■ uma matriz com os preços de todos os produtos em cada loja. 
PASCAL
C/C++
JAVA

---

Capítulo 7 Matriz  | 223
PARA i ← 1 ATÉ 10 FAÇA 
  INÍCIO
  soma[i]  ← 0
  PARA j ← 1 ATÉ 20 FAÇA 
   INÍCIO
    soma[i] ← soma[i] + mat[i, j] 
   FIM
  FIM
PARA i ← 1 ATÉ 10 FAÇA 
  INÍCIO
  PARA j ← 1 ATÉ 20 FAÇA 
   INÍCIO
    mat[i, j] ← mat[i, j] * soma[i] 
   FIM
  FIM
PARA i ← 1 ATÉ 10 FAÇA 
  INÍCIO
  PARA j ← 1 ATÉ 20 FAÇA 
   INÍCIO
    ESCREVA mat[i, j] 
   FIM
  FIM 
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP7\PASCAL\EX4.PAS e \EXERC\CAP7\PASCAL\EX4.EXE 
SOLUÇÃO:
\EXERC\CAP7\C++\EX4.CPP e \EXERC\CAP7\C++\EX4.EXE
SOLUÇÃO:
\EXERC\CAP7\JAVA\EX4.java e \EXERC\CAP7\JAVA\EX4.class 
5. Na teoria dos sistemas, define-se o elemento MINMAX de uma matriz como o maior elemento da  
linha em que se encontra o menor elemento da matriz. Elabore um programa que carregue uma matriz 
4  7 com números reais, calcule e mostre seu MINMAX e sua posição (linha e coluna).
SOLUÇÃO:
ALGORITMO
 DECLARE mat[4,7], menor, maior, i, j, l_menor, col NUMÉRICO
PARA i ← 1 ATÉ 4 FAÇA
 INÍCIO
 PARA j ← 1 ATÉ 7 FAÇA
   INÍCIO
    LEIA mat[i, j]
   FIM
 FIM
menor ← mat[1, 1]
l_menor ← 1
PARA i ← 1 ATÉ 4 FAÇA
  INÍCIO
  PARA j ← 1 ATÉ 7 FAÇA
   INÍCIO
    SE mat[i, j] < menor
PASCAL
C/C++
JAVA

---

Capítulo 7 Matriz  | 225
   INÍCIO
   PARA j ← 1 ATÉ 5 FAÇA
    INÍCIO
    mult ← a[i, j] * b[j, k]
    soma ← soma + mult
    FIM
   c[i, k] ← soma
   soma ← 0
   FIM
 FIM
PARA i ← 1 ATÉ 4 FAÇA
  INÍCIO
  PARA j ← 1 ATÉ 2 FAÇA
    INÍCIO
    ESCREVA c[i, j]
    FIM
  FIM
FIM_ALGORITMO.  
SOLUÇÃO:
\EXERC\CAP7\PASCAL\EX6.PAS e \EXERC\CAP7\PASCAL\EX6.EXE
SOLUÇÃO:
\EXERC\CAP7\C++\EX6.CPP e \EXERC\CAP7\C++\EX6.EXE
SOLUÇÃO:
\EXERC\CAP7\JAVA\EX6.java e \EXERC\CAP7\JAVA\EX6.class
7. Um elemento Aij de uma matriz é dito ponto de sela da matriz A se, e somente se, Aij for, ao mesmo 
tempo, o menor elemento da linha i e o maior elemento da coluna j. Faça um programa que carregue 
uma matriz de ordem 5  7, verifique se a matriz possui ponto de sela e, se possuir, mostre seu valor 
e sua localização.
SOLUÇÃO:
ALGORITMO
DECLARE mat[5,7] NUMÉRICO
 i, j, maior, menor, linha, coluna, cont NUMÉRICO 
PARA i ← 1 ATÉ 5 FAÇA
 INÍCIO
 PARA j ← 1 ATÉ 7 FAÇA
  INÍCIO
   LEIA mat[i, j]  
  FIM
 FIM
cont ← 0
PARA i ← 1 ATÉ 5 FAÇA
 INÍCIO
  menor ← mat[i, 1] 
  linha ← i
  coluna ← 0
  PARA j ← 1 ATÉ 7 FAÇA
   INÍCIO
    SE mat[i,j] < menor 
     ENTÃO INÍCIO
      menor ← mat[i, j] 
      linha ← i
PASCAL
C/C++
JAVA

---

Capítulo 7 Matriz  | 227
 INÍCIO
 PARA j  ← 1 ATÉ 4 FAÇA
  INÍCIO
   SE mat1[i, j] = 30
    ENTÃO mat2[i, j]  ← 0
    SENÃO mat2[i, j]  ← mat1[i, j]
  FIM
 FIM
ESCREVA qtde
PARA i ← 1 ATÉ 6 FAÇA
 INÍCIO
 PARA j  ← 1 ATÉ 4 FAÇA
  INÍCIO
   ESCREVA mat2[i, j]
  FIM
 FIM
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP7\PASCAL\EX8.PAS e \EXERC\CAP7\PASCAL\EX8.EXE
SOLUÇÃO:  
\EXERC\CAP7\C++\EX8.CPP e \EXERC\CAP7\C++\EX8.EXE
SOLUÇÃO:
\EXERC\CAP7\JAVA\EX8.java e \EXERC\CAP7\JAVA\EX8.class
9. Crie um programa que preencha uma matriz 15   5 com números inteiros, calcule e mostre quais  
elementos da matriz se repetem e quantas vezes cada um se repete.
SOLUÇÃO:
ALGORITMO
DECLARE mat[15,5], rep[15,5], vezes[15,5] NUMÉRICO
 i, j, k, l, lin, lin2, col, x, num, qtde, achou NUMÉRICO 
PARA i ← 1 ATÉ 15 FAÇA
 INÍCIO
 PARA j ← 1 ATÉ 5 FAÇA 
  INÍCIO
   LEIA mat[i,j]
  FIM
 FIM
lin ← 1 
col ← 1
PARA i ← 1 ATÉ 15 FAÇA
 INÍCIO
 PARA j  ← 1 ATÉ 5 FAÇA
  INÍCIO
  qtde  ← 1
  num  ← mat[i,j]
  PARA k ← 1 ATÉ 15 FAÇA
   INÍCIO
   PARA l ← 1 ATÉ 5 FAÇA
    INÍCIO
    SE i <> k OU j <> l
PASCAL
C/C++
JAVA

---

Capítulo 7 Matriz  | 229
10. Elabore um programa que preencha uma matriz 10  10 com números inteiros, execute as trocas es-
pecificadas a seguir e mostre a matriz resultante:
 ■ a linha 2 com a linha 8; 
 ■ a coluna 4 com a coluna 10; 
 ■ a diagonal principal com a diagonal secundária; 
 ■ a linha 5 com a coluna 10. 
SOLUÇÃO:
ALGORITMO
 DECLARE mat[10,10], aux, i, j NUMÉRICO 
PARA i ← 1 ATÉ 10 FAÇA
 INÍCIO
 PARA j ← 1 ATÉ 10 FAÇA 
  INÍCIO
   LEIA mat[i, j] 
  FIM
 FIM
PARA i ← 1 ATÉ 10 FAÇA 
 INÍCIO
  aux ← mat[2, i] 
  mat[2,i] ← mat[8,i]  
  mat[8, i] ← aux
 FIM
PARA i ← 1 ATÉ 10 FAÇA 
 INÍCIO
  aux ← mat[i, 4]  
  mat[i, 4] ← mat[i,10]  
  mat[i, 10] ← aux
 FIM
j ← 10
PARA i ← 1 ATÉ 10 FAÇA 
 INÍCIO
  aux  ← mat[i, i]
  mat[i, i] ← mat[i, j] 
mat[i, j] ← aux
  j ← j - 1 
 FIM
PARA j ← 1 ATÉ 10 FAÇA 
 INÍCIO
  aux ← mat[5, j] 
  mat[5, j] ← mat[j,10]  
  mat[j, 10] ← aux
 FIM
PARA i ← 1 ATÉ 10 FAÇA 
 INÍCIO
 PARA j ← 1 ATÉ 10 FAÇA 
  INÍCIO
   ESCREVA mat[i, j] 
  FIM
 FIM 
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP7\PASCAL\EX10.PAS e \EXERC\CAP7\PASCAL\EX10.EXE
SOLUÇÃO:
\EXERC\CAP7\C++\EX10.CPP e \EXERC\CAP7\C++\EX10.EXE
PASCAL
C/C++

---

Capítulo 7 Matriz  | 231
   INÍCIO
    LEIA mat[i,j]  
   FIM
  FIM
PARA i ← 1 ATÉ 4 FAÇA 
 INÍCIO 
 soma_linha[i] ← 0
 PARA j ← 1 ATÉ 4 FAÇA 
  INÍCIO
   soma_linha[i]  ← soma_linha[i] + mat[i,j]
  FIM
 FIM
PARA i ← 1 ATÉ 4 FAÇA 
 INÍCIO 
 soma_coluna[i] ← 0
 PARA j ← 1 ATÉ 4 FAÇA 
  INÍCIO
   soma_coluna[i]  ← soma_coluna[i] + mat[j,i]
  FIM
 FIM 
soma_diagp ← 0
PARA i ← 1 ATÉ 4 FAÇA 
 INÍCIO
  soma_diagp ← soma_diagp + mat[i,i] 
 FIM
soma_diags ← 0 
j ← 4
PARA i ← 1 ATÉ 4 FAÇA 
 INÍCIO
  soma_diags ← soma_diags + mat[i,j] 
  j ← j - 1
 FIM
q_magico ← verdadeiro 
PARA i ← 1 ATÉ 4 FAÇA 
INÍCIO
PARA j ← 1 ATÉ 4 FAÇA 
  INÍCIO
  SE soma_linha[i]  soma_coluna[j] 
   ENTÃO q_magico ← falso
  FIM
FIM
PARA i ← 1 ATÉ 4 FAÇA 
 INÍCIO
  SE soma_linha[i]  soma_diagp
  ENTÃO q_magico ← falso
 FIM
PARA i ← 1 ATÉ 4 FAÇA 
 INÍCIO
  SE soma_linha[i]  soma_diags
  ENTÃO q_magico ← falso
 FIM
SE q_magico = verdadeiro
 ENTÃO ESCREVA “Forma quadrado mágico”
 SENÃO ESCREVA “Não forma quadrado mágico”
FIM_ALGORITMO.

---

Capítulo 7 Matriz  | 233
    SENÃO SE preco[i,j] > 50 E preco[i,j] <= 100
         ENTÃO imp[i,j]  ← preco[i,j]*10/100
         SENÃO imp[i,j]  ← preco[i,j]*15/100
  FIM
 FIM
PARA i ← 1 ATÉ 5 FAÇA
 INÍCIO
 ESCREVA “Nome do produto “,nome[i]
 ESCREVA “Custo = “, custo[i]
 PARA j  ← 1 ATÉ 4 FAÇA
   INÍCIO
   final  ← preco[i,j] + imp[i,j] + custo[i]
   ESCREVA “Imposto na loja “, j,” = “, imp[i,j]
   ESCREVA “Preço na loja “, j, “ = “, preco[i,j]
   ESCREVA “Preço final na loja “,j, “ = “, final
   FIM
 FIM
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP7\PASCAL\EX13.PAS 
e \EXERC\CAP7\PASCAL\EX13.EXE
 SOLUÇÃO:
\EXERC\CAP7\C++\EX13.CPP e \EXERC\CAP7\C++\EX13.EXE
SOLUÇÃO:
\EXERC\CAP7\JAVA\EX13.java e \EXERC\CAP7\JAVA\EX13.class
14. Faça um programa que receba: 
 ■ um vetor com o nome de cinco cidades diferentes; 
 ■ uma matriz 5  5 com a distância entre as cidades, e na diagonal principal deve ser colocada auto-
maticamente a distância zero, ou seja, não deve ser permitida a digitação; 
 ■ o consumo de combustível de um veículo, ou seja, quantos quilômetros esse veículo percorre com 
um litro de combustível. 
O programa deverá calcular e mostrar:
 ■ os percursos que não ultrapassam 250 quilômetros (os percursos são compostos pelos nomes das 
cidades de origem e pelos nomes das cidades de destino); 
 ■ todos os percursos (nome da cidade de origem e nome da cidade de destino), junto com a quantida-
de de combustível necessária para o veículo percorrê-los.
SOLUÇÃO:
ALGORITMO
DECLARE cidade[5] LITERAL
 distancia[5,5], i, j, consumo, qtde NUMÉRICO
NUMÉRICO PARA i ← 1 ATÉ 5 FAÇA
 INÍCIO
  LEIA cidade[i] 
 FIM
PARA i ← 1 ATÉ 5 FAÇA 
 INÍCIO
  PARA j ← 1 ATÉ 5 FAÇA 
   INÍCIO
    SE i = j
PASCAL
C/C++
JAVA

---

Capítulo 7 Matriz  | 235
 INÍCIO
  LEIA vet1[i] 
 FIM
PARA i ← 1 ATÉ 10 FAÇA 
 INÍCIO
  LEIA vet2[i] 
 FIM
PARA i ← 1 ATÉ 4 FAÇA 
 INÍCIO
 PARA j ← 1 ATÉ 3 FAÇA 
  INÍCIO
   LEIA mat[i,j] 
  FIM
 FIM 
maior ← vet1[1]
PARA i ← 1 ATÉ 5 FAÇA 
 INÍCIO
  SE vet1[i] > maior
   ENTÃO maior  ← vet1[i]
 FIM 
menor ← vet2[1]
PARA i ← 1 ATÉ 10 FAÇA 
 INÍCIO
  SE vet2[i] < menor
   ENTÃO menor  ← vet2[i]
 FIM
mult ← maior * menor 
PARA i ← 1 ATÉ 4 FAÇA 
 INÍCIO
 PARA j ← 1 ATÉ 3 FAÇA 
  INÍCIO
   mat_result[i, j] ← mat[i, j] + mult 
  FIM
 FIM
ESCREVA “Matriz resultante” 
PARA i ← 1 ATÉ 4 FAÇA
 INÍCIO
 PARA j ← 1 ATÉ 3 FAÇA 
  INÍCIO
   ESCREVA mat_result[i,j]
  FIM
 FIM
PARA i ← 1 ATÉ 4 FAÇA 
 INÍCIO
  soma  ← 0
  PARA j ← 1 ATÉ 3 FAÇA 
   INÍCIO
    SE RESTO(mat_result[i,j]/2) = 0
    ENTÃO soma  ← soma + mat_result[i,j]
   FIM
   ESCREVA “Soma dos elementos pares da linha “, i, “ da matriz resultante = “, 
soma
 FIM
PARA j ← 1 ATÉ 3 FAÇA
 INÍCIO
  qtde  ← 0
  PARA i ← 1 ATÉ 4 FAÇA 
   INÍCIO

---

Capítulo 7 Matriz  | 237
PARA i ← 1 ATÉ 7 FAÇA
 INÍCIO
  ESCREVA vet1[i]
 FIM
PARA i ← 1 ATÉ 7 FAÇA
 INÍCIO
  ESCREVA vet2[i]
 FIM
FIM_ALGORITMO.
SOLUÇÃO: 
\EXERC\CAP7\PASCAL\EX16.PAS e \EXERC\CAP7\PASCAL\EX16.EXE
SOLUÇÃO:
\EXERC\CAP7\C++\EX16.CPP e \EXERC\CAP7\C++\EX16.EXE
SOLUÇÃO:
\EXERC\CAP7\JAVA\EX16.java e \EXERC\CAP7\JAVA\EX16.class
17. Faça um programa que utilize uma matriz 5   5 a qual aceite três tipos de valores: múltiplos de 5,  
múltiplos de 11 e múltiplos de 13. Devem ser lidos apenas valores maiores que zero. Após a leitura, os 
números devem ser distribuídos da seguinte maneira:
 ■ os múltiplos de 5 devem ocupar a diagonal principal; 
 ■ os múltiplos de 11 devem ficar acima da diagonal principal; 
 ■ os múltiplos de 13 devem ficar abaixo da diagonal principal. 
Como alguns números podem ser múltiplos de 5, de 11 e também de 13 (por exemplo, 55 é múltiplo de 5 e 
de 11; 65 é múltiplo de 5 e de 13), deve-se, primeiro, verificar se o número digitado é múltiplo de 5. Caso não seja, 
deve-se verificar se é múltiplo de 11. Caso não seja, deve-se verificar se é múltiplo de 13. Caso não seja, o progra-
ma deverá mostrar a mensagem Número inválido (por exemplo, o número 55 deverá ser considerado múltiplo de 
5, pois esta é a comparação que será feita primeiro).
Segue-se um exemplo.
5 44 11 33 55
26 15 77 99 88
39 13 10 121 22
52 78 65 40 132
91 117 104 143 25
Esse programa deverá observar as seguintes situações:
 ■ quando o usuário digitar um múltiplo de 5 e não houver mais espaço na diagonal principal, deverá 
mostrar a mensagem Diagonal totalmente preenchida; 
 ■ quando o usuário digitar um múltiplo de 11 e não houver mais espaço disponível na matriz, deverá 
mostrar a mensagem Não existe espaço acima da diagonal principal; 
 ■ quando o usuário digitar um múltiplo de 13 e não houver mais espaço disponível na matriz, deverá 
mostrar a mensagem Não existe espaço abaixo da diagonal principal; 
 ■ quando a matriz estiver totalmente preenchida, deverá mostrar todos os elementos da matriz, junto 
com suas posições (linha e coluna). 
PASCAL
C/C++
JAVA

---

Capítulo 7 Matriz  | 239
    cont_ab ← cont_ab + 1
    FIM
       SENÃO ESCREVA “ Não existe mais espaço para  
múltiplos de 11” 
   FIM
  SENÃO INÍCIO
         r ← RESTO (num/13) 
   SE r = 0
      ENTÃO INÍCIO
        SE cont_ab < 10 
      ENTÃO INÍCIO
       mat[lin_ab,col_ab] ← num 
       col_ab ← col_ab + 1
       SE col_ab >= lin_ab 
       ENTÃO INÍCIO
             lin_ab ← lin_ab + 1 
       col_ab ← 1
           FIM
         cont_ab ← cont_ab + 1
         FIM
    SENÃO ESCREVA “ Não existe mais espaço para 
múltiplos de 13”
    FIM
  SENÃO ESCREVA “ Digite um número múltiplo de 5 ou  
de 11 ou de 13”
    FIM
  FIM 
FIM
PARA i ← 1 ATÉ 5 FAÇA 
INÍCIO
PARA j ← 1 ATÉ 5 FAÇA 
 INÍCIO
  ESCREVA mat[i,j]
 FIM
FIM 
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP7\PASCAL\EX17.PAS e \EXERC\CAP7\PASCAL\EX17.EXE
SOLUÇÃO:
\EXERC\CAP7\C++\EX17.CPP e \EXERC\CAP7\C++\EX17.EXE
SOLUÇÃO:
\EXERC\CAP7\JAVA\EX17.java e \EXERC\CAP7\JAVA\EX17.class
18. Crie um programa que leia um vetor vet contendo 18 elementos. A seguir, o programa deverá distribuir 
esses elementos em uma matriz 3 × 6 e, no final, mostrar a matriz gerada.
Veja a seguir um exemplo do que seu programa deverá fazer.
vet 3 25 1 58 97 43 65 32 27 19 10 6 88 13 34 57 89 87
mat 3 25 1 58 97 43
65 32 27 19 10 6
88 13 34 57 89 87
PASCAL
C/C++
JAVA

---

Capítulo 7 Matriz  | 241
SOLUÇÃO:
ALGORITMO
DECLARE mat[5,4], i, j, num, r NUMÉRICO
 lin_p, col_p, lin_i, col_i, tot NUMÉRICO 
lin_p ← 2
col_p ← 1 
lin_i ← 1 
col_i ← 1 
tot ← 0 
REPITA
SE tot ≠ 20 
          ENTÃO INÍCIO
   LEIA num
   r  ← RESTO (num/2)
    SE r = 0
    ENTÃO INÍCIO
     SE lin_p > 4
       ENTÃO ESCREVA “Sem espaço para números pares”
      SENÃO INÍCIO
       mat[lin_p,col_p]  ← num
       col_p  ← col_p + 1
       SE col_p > 4
        ENTÃO INÍCIO
        lin_p ← lin_p + 2 col_p ← 1
             FIM
            FIM
           FIM
    SENÃO INÍCIO
     SE lin_i > 5
       ENTÃO ESCREVA “Sem espaço para números ímpares” 
SENÃO INÍCIO
            mat[lin_i,col_i] ← num 
            col_i ← col_i + 1
            SE col_i > 4       
            ENTÃO INÍCIO
           lin_i ← lin_i + 2 
           col_i ← 1
                  FIM
            FIM
           FIM 
tot ← tot + 1
FIM
   ATÉ tot = 20
   ESCREVA “Matriz totalmente preenchida”  
    PARA i ← 1 ATÉ 5 FAÇA
    INÍCIO
    PARA j ← 1 ATÉ 4 FAÇA   
         INÍCIO
      ESCREVA mat[i,j] 
         FIM
    FIM 
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP7\PASCAL\EX19.PAS e \EXERC\CAP7\PASCAL\EX19.EXE
SOLUÇÃO:
\EXERC\CAP7\C++\EX19.CPP e \EXERC\CAP7\C++\EX19.EXE
SOLUÇÃO:
\EXERC\CAP7\JAVA\EX19.java e \EXERC\CAP7\JAVA\EX19.class
PASCAL
C/C++
JAVA

---

Capítulo 7 Matriz  | 243
FIM
PARA i ← 1 ATÉ 5 FAÇA
INÍCIO
PARA j ← 1 ATÉ 4 FAÇA
INÍCIO
ESCREVA “Elemento da posição “, i, “-”, j, “ = “, num[i][j]
FIM
FIM
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP7\PASCAL\EX20.PAS e \EXERC\CAP7\PASCAL\EX20.EXE
SOLUÇÃO:
\EXERC\CAP7\C++\EX20.CPP e \EXERC\CAP7\C++\EX20.EXE
SOLUÇÃO:
\EXERC\CAP7\JAVA\EX20.java e \EXERC\CAP7\JAVA\EX20.class
21. Crie um programa que utilize uma matriz com as dimensões fornecidas pelo usuário e execute as  so-
licitações a seguir.
Para realizar essa tarefa, a matriz deverá ser obrigatoriamente quadrada (número igual de linhas e co -
lunas). Sendo assim, solicite que seja informada a dimensão da matriz.
Posteriormente, o programa deverá realizar a leitura dos elementos que vão compor a matriz. Por fim, 
deverá somar e mostrar os elementos que estão abaixo da diagonal secundária. 
Veja o exemplo.
Imagine que sejam informados números, conforme apresentado nesta matriz.
20 10 1 8
17 42 11 98
19 45 32 87
12 36 65 25
O resultado do problema seria: 98 + 32 + 87 + 36 + 65 + 25 = 343
SOLUÇÃO:
ALGORITMO
 DECLARE num[100,100],dim, l, c, soma, cont NUMÉRICO 
 REPITA
   ESCREVA “Digite a dimensão da matriz (quadrada) - no máximo 100” 
  LEIA dim
 ATÉ dim >= 1 E dim <= 100 
 l ← 1
 c  ← 1
 ENQUANTO l ≤ dim FAÇA 
 INÍCIO
  ENQUANTO c ≤ dim FAÇA 
  INÍCIO
   LEIA num[l,c] 
   c ← c + 1
  FIM
PASCAL
C/C++
JAVA

---

Capítulo 7 Matriz  | 245
 INÍCIO
 LEIA prod[5,i] 
 FIM
PARA i ← 1 ATÉ 4 FAÇA
 INÍCIO
 tot_arm  ← 0
 PARA j  ← 1 ATÉ 3 FAÇA
  INÍCIO
   tot_arm  ← tot_arm + prod[i,j]
  FIM
 ESCREVA “O total de itens no armazém “,i, “ = “,tot_arm
 SE i=1
   ENTÃO INÍCIO
    menor_e ← tot_arm
    ind_a ← i
    ind_a ← i
 FIM
 SENÃO INÍCIO
    SE tot_arm < menor_e
   ENTÃO INÍCIO
    menor_e ← tot_arm 
    ind_a ← i
    FIM
    FIM
 FIM
ESCREVA “Armazém com menor estoque”, ind_a 
PARA i ← 1 ATÉ 4 FAÇA
 INÍCIO
  SE i = 1
   ENTÃO INÍCIO
    maior_e ← prod[i,2] 
    ind_a ← i
    FIM
  SENÃO INÍCIO
     SE prod[i,2] > maior_e 
     ENTÃO INÍCIO  
       maior_e ← prod[i,2] 
       ind_a ← i
      FIM
  FIM
 FIM
 ESCREVA “O maior estoque do produto 2 está no armazém” ,ind_a 
PARA j ← 1 ATÉ 3 FAÇA
 INÍCIO
  custo_p  ← 0
  PARA i ← 1 ATÉ 4 FAÇA    
   INÍCIO
    custo_p  ← custo_p + prod[i,j]
   FIM
  custo_p  ← custo_p * prod[5,j]
  ESCREVA “O custo total do produto “, j , “ = “,custo_p
 FIM
PARA i ← 1 ATÉ 4 FAÇA  
INÍCIO
  custo_a  ← 0
  PARA j ← 1 ATÉ 3 FAÇA 
   INÍCIO
    custo_a  ← custo_a + (prod[i,j] * prod[5,j])
   FIM
  ESCREVA “O custo total do armazém “, i ,” = “, custo_a 
FIM
FIM_ALGORITMO.

---

Capítulo 7 Matriz  | 247
SOLUÇÃO:
\EXERC\CAP7\PASCAL\EX23.PAS e \EXERC\CAP7\PASCAL\EX23.EXE
SOLUÇÃO:
\EXERC\CAP7\C++\EX23.CPP e \EXERC\CAP7\C++\EX23.EXE
SOLUÇÃO:
\EXERC\CAP7\JAVA\EX23.java e \EXERC\CAP7\JAVA\EX23.class
24. Uma escola deseja controlar as médias das disciplinas que seus alunos cursam. Sabe-se que nessa  es-
cola existem três turmas, com oito alunos cada uma, e cada aluno cursa quatro disciplinas. Crie um 
programa que armazene essas médias em uma matriz 3  8  4. Depois da leitura, ele deverá calcular 
e mostrar:
 ■ a média geral de cada aluno; 
 ■ a média de cada turma. 
SOLUÇÃO:
ALGORITMO
DECLARE medias[3][8][4], i, j, k, media_aluno, media_turma NUMÉRICO 
PARA i ← 1 ATÉ 3 FAÇA
 INÍCIO
  PARA j ← 1 ATÉ 8 FAÇA 
   INÍCIO
    PARA k ← 1 ATÉ 4 FAÇA 
     INÍCIO
      LEIA medias[i][j][k]
     FIM
   FIM
 FIM
PARA i ← 1 ATÉ 3 FAÇA  
 INÍCIO
  PARA j ← 1 ATÉ 8 FAÇA 
     INÍCIO
   media_aluno  ← 0
    PARA k ← 1 ATÉ 4 FAÇA 
    INÍCIO
     media_aluno ← media_aluno + medias[i][j][k]
    FIM
    media_aluno  ← media_aluno / 4
     ESCREVA “A média do aluno “, j, “ na turma “, i, “ = “, media_aluno
     FIM
 FIM
PARA i ← 1 ATÉ 3 FAÇA  
 INÍCIO
  media_turma  ← 0
  PARA j ← 1 ATÉ 8 FAÇA 
     INÍCIO
   PARA k ← 1 ATÉ 4 FAÇA 
   INÍCIO
    media_turma  ← media_turma + medias[i][j][k]
   FIM
     FIM
  media_turma  ← media_turma / (8 * 4)
  ESCREVA “A média da turma “, i, “ = “, media_turma
     FIM
FIM_ALGORITMO.
PASCAL
C/C++
JAVA

---

Capítulo 7 Matriz  | 249
PARA i ← 1 ATÉ 5 FAÇA 
INÍCIO
     tot_prod ← 0
     PARA j ← 1 ATÉ 3 FAÇA 
     INÍCIO
     tot_prod ← tot_prod + bim[i,j]
     FIM 
ESCREVA tot_prod
FIM 
FIM_ALGORITMO.
SOLUÇÃO:
\EXERC\CAP7\PASCAL\EX25.PAS e \EXERC\CAP7\PASCAL\EX25.EXE
SOLUÇÃO:
\EXERC\CAP7\C++\EX25.CPP e \EXERC\CAP7\C++\EX25.EXE
SOLUÇÃO:
\EXERC\CAP7\JAVA\EX25.JAVA e \EXERC\CAP7\JAVA\EX25.class
EXERCÍCIOS PROPOSTOS
1. Faça um programa que preencha uma matriz 3  5 com números inteiros, calcule e mostre a quantidade de 
elementos entre 15 e 20. 
2. Crie um programa que preencha uma matriz 2  4 com números inteiros, calcule e mostre: 
 ■ a quantidade de elementos entre 12 e 20 em cada linha; 
 ■ a média dos elementos pares da matriz. 
3. Elabore um programa que preencha uma matriz 6  3, calcule e mostre: 
 ■ o maior elemento da matriz e sua respectiva posição, ou seja, linha e coluna; 
 ■ o menor elemento da matriz e sua respectiva posição, ou seja, linha e coluna. 
4. Faça um programa que receba: 
 ■ as notas de 15 alunos em cinco provas diferentes e armazene-as em uma matriz 15  5; 
 ■ os nomes dos 15 alunos e armazene-os em um vetor de 15 posições. 
O programa deverá calcular e mostrar:
 ■ para cada aluno, o nome, a média aritmética das cinco provas e a situação (aprovado, reprovado 
ou exame); 
 ■ a média da classe. 
5. Elabore um programa que preencha uma matriz 12  4 com os valores das vendas de uma loja, em que cada 
linha representa um mês do ano e cada coluna representa uma semana do mês. O programa deverá calcular 
e mostrar: 
 ■ o total vendido em cada mês do ano, mostrando o nome do mês por extenso; 
 ■ o total vendido em cada semana durante todo o ano; 
 ■ o total vendido pela loja no ano. 
6. Faça um programa que preencha uma matriz 20  10 com números inteiros, e some cada uma das colunas, 
armazenando o resultado da soma em um vetor. A seguir, o programa deverá multiplicar cada elemento da 
matriz pela soma da coluna e mostrar a matriz resultante. 
7. Elabore um programa que preencha uma matriz M de ordem 4  6 e uma segunda matriz N de ordem 6  
4, calcule e imprima a soma das linhas de M com as colunas de N. 
PASCAL
C/C++
JAVA

---

Capítulo 7 Matriz  | 251
23. Faça um programa que preencha uma matriz 3  4, calcule e mostre: 
 ■ a quantidade de elementos pares; 
 ■ a soma dos elementos ímpares; 
 ■ a média de todos os elementos. 
24. Elabore um programa que preencha uma matriz 4  5, calcule e mostre um vetor com cinco posições, 
onde cada posição contém a soma dos elementos de cada coluna da matriz. O programa deverá mostrar 
apenas os elementos do vetor maiores que dez. Se não existir nenhum elemento maior que dez, deverá 
mostrar uma mensagem. 
25. Crie um programa que: 
 ■ receba o preço de dez produtos e armazene-os em um vetor; 
 ■ receba a quantidade estocada de cada um desses produtos, em cinco armazéns diferentes, utilizando 
uma matriz 5  10. 
O programa deverá calcular e mostrar:
 ■ a quantidade de produtos estocados em cada um dos armazéns; 
 ■ a quantidade de cada um dos produtos estocados, em todos os armazéns juntos; 
 ■ o preço do produto que possui maior estoque em um único armazém; 
 ■ o menor estoque armazenado; 
 ■ o custo de cada armazém.

---



=== CAPÍTULO 8 ===

---

Capítulo 8 Sub-rotina  | 253
Outro ponto que precisa ser destacado é que, dentro das sub-rotinas, pode ocorrer declaração de 
variáveis, chamadas variáveis locais. Elas recebem esse nome porque podem ser utilizadas apenas dentro 
da sub-rotina. Quando a execução desta chega ao fim, essas variáveis são destruí das e seus conteúdos são 
perdidos.
Variáveis declaradas fora de qualquer sub-rotina são chamadas globais. Elas recebem esse nome porque 
qualquer ponto do programa, incluindo as sub-rotinas, pode utilizá-las. São destruí das quando a execução 
do programa chega ao fim.
Observação
Não se aconselha a utilização excessiva de variáveis globais, por tornar difícil a manutenção 
e a busca por erros nos programas.
No algoritmo usado como exemplo anteriormente, tem-se 3 variáveis globais, declaradas na linha 2 e 
denominadas sal, aum e novo_sal. Na linha 9, existe a declaração de 2 variáveis locais da sub-rotina cal-
culo. São elas: perc e valor.
É importante salientar que, na linha 4, onde a sub-rotina calculo é chamada, a variável sal está sendo 
passada como parâmetro e, na linha 8, cabeçalho da sub-rotina calculo, uma variável, que pode ou não ter 
o mesmo nome, está recebendo o valor do parâmetro.
O parâmetro pode ser passado por valor e, então, a variável do cabeçalho se comportará como uma 
variável local da sub-rotina.
O parâmetro pode ser passado por referência e, então, a variável do cabeçalho se comportará como 
uma variável global.
A passagem de parâmetros por valor ou por referência depende da sintaxe de cada linguagem e as pró-
ximas seções demonstrarão essas especificidades.
Exemplo de variáveis locais e globais:
1. ALGORITMO
2. DECLARE X, Y NUMÉRICO // variáveis globais
3. X ← 1
4. Y ← 2
5. ESCREVA “VALORES INICIAIS”
6. ESCREVA “X = “,X,” e Y = “,Y
7. S1     // chamada da sub-rotina S1, sem parâmetros
8. ESCREVA “VALORES DEPOIS DA EXECUÇÃO DA SUB-ROTINA S1”
9. ESCREVA “X = “,X,” e Y = “,Y
10. S2(X,Y) //chamada da sub-rotina S2, com parâmetros por valor
11. ESCREVA “VALORES DEPOIS DA EXECUÇÃO DA SUB-ROTINA S2”
12. ESCREVA “X = “,X,” e Y = “,Y
13. S3(X,Y)      // chamada da sub-rotina S3, com parâmetros por referência
14. ESCREVA “VALORES DEPOIS DA EXECUÇÃO DA SUB-ROTINA S3”
15. ESCREVA “X = “,X,” e Y = “,Y
16. FIM_ALGORITMO.
17. SUB_ROTINA S1 
18. // sub-rotina sem parâmetros e sem retorno
19. DECLARE X, Y, Z NUMÉRICO // variáveis locais da sub-rotina S1
20. X ← 8
21. Y ← 10
22. Z ← 5
23. ESCREVA “VALORES IMPRESSOS DENTRO DA SUB-ROTINA S1”
24. ESCREVA “X = “,X

---

Capítulo 8 Sub-rotina  | 255
VARIÁVEIS
globais
locais da
sub-rotina 
s1
locais da
sub-
-rotina s2
locais da
sub-rotina 
s3
Linha 
executada Saída na tela
35 X = 3
36 Y = 4
37 Z = 7
11 VALORES DEPOIS DA EXECUÇÃO DA SUB-ROTINA S2
12 X = 1 e Y = 2
13
1 2 39
3 42
0 0 43
0 0 44
45 VALORES IMPRESSOS DENTRO DA SUB-ROTINA S3
46 X = 0
47 Y = 0
48 A = 3
14 VALORES DEPOIS DA EXECUÇÃO DA SUB-ROTINA S3
15 X = 0 e Y = 0
8.2 Sub-rotinas em PASCAL (procedures, functions e units) 
A linguagem PASCAL possibilita a modularização por meio de procedures (procedimentos), functions 
(funções) e units (unidades). As sub-rotinas do tipo procedures (procedimentos) e functions (funções) devem 
ter seus códigos descritos antes do BEGIN do programa principal. Apenas as units (unidades) apresentam 
sintaxe diferenciada e descrita na Seção 8.2.7.
As variáveis globais, ou seja, aquelas que são reconhecidas por todas as partes do programa, devem ser 
declaradas antes do BEGIN do programa principal. As variáveis locais devem ser declaradas dentro das sub-
-rotinas e são reconhecidas apenas na sub-rotina onde foram declaradas. 
A seguir, um programa exemplo que soma dois números digitados pelo usuário será utilizado para de -
monstrar os diferentes tipos de sub-rotinas.
8.2.1 Procedures sem passagem de parâmetros
As procedures (procedimentos) são rotinas chamadas pelo programa principal para executar alguma 
operação específica, mas não retornam valor para quem as chamou. Possuem a seguinte sintaxe:
PROCEDURE nome_da_procedure; 
declaração_de_variáveis_locais; 
BEGIN
 comandos; 
END;
Quando o programa encontra uma linha contendo o nome da procedure, o fluxo da execução é desvia-
do para as linhas contidas dentro dela. Essa execução só retornará ao fluxo normal quando a execução da 
procedure chegar ao fim.
A seguir, é apresentado um exemplo de procedure sem parâmetros (a numeração das linhas não faz 
parte do programa) com a utilização de variáveis globais. 
1. PROGRAM EXEMPLO;
2. USES CRT;
3. VAR A, B, S : INTEGER; {variáveis globais}
4. PROCEDURE SOMAR;
5. BEGIN

---

Capítulo 8 Sub-rotina  | 257
A seguir, é mostrado um exemplo de procedure com passagem de parâmetros por valor, ou seja, os 
parâmetros são variáveis locais da sub-rotina (a numeração das linhas não faz parte do programa).
1. PROGRAM EXEMPLO;
2. USES CRT;
3. VAR A, B: INTEGER;  {variáveis globais}
4. PROCEDURE SOMAR(X,Y: INTEGER);
5. VAR S: INTEGER;  {variável local da sub-rotina SOMAR}
6. BEGIN
7. S := X + Y;
8. WRITELN(‘Soma = ‘,S);
9. END;
10. BEGIN  {início do programa principal}
11. CLRSCR;
12. WRITELN(‘Digite o primeiro número: ‘);
13. READLN(A);
14. WRITELN(‘Digite o segundo número: ‘);
15. READLN(B);
16. SOMAR(A,B);  {chamada da sub-rotina SOMAR}
17. READLN;
18. END.
O programa começa sua execução no BEGIN principal, representado no exemplo anterior pela linha 10. 
Posteriormente, executa as linhas 11 a 16. Na linha 16, existe a chamada a uma procedure. O programa 
principal é desviado para a procedure, denominada SOMAR, que possui as variáveis A e B como parâme-
tros. Assim, o fluxo de execução do programa vai para a linha 4, executando toda a procedure, ou seja, as 
linhas 5 a 9. O primeiro parâmetro é a variável A e será passada para a variável X. O segundo parâmetro é a 
variável B e será passada para a variável Y. Em seguida, ele retorna à linha 17, exatamente abaixo da linha 
onde ocorreu o desvio. Executa as linhas 17 e 18 e o programa é encerrado.
A linguagem PASCAL não permite a passagem de vetores e matrizes como parâmetros da mesma forma 
em que são passados parâmetros de tipos primitivos (INTEGER, REAL, STRING e CHAR). Para passar um vetor 
ou uma matriz como parâmetro é necessário definir um novo tipo.
Exemplo de vetor passado como parâmetro para uma sub-rotina:
PROGRAM VETOR;
USES CRT;
TYPE X = ARRAY[1..5] OF INTEGER; 
VAR I:INTEGER;
  W:X;
PROCEDURE MOSTRAR(Y:X);
BEGIN
 WRITELN(‘MOSTRANDO O VETOR NA SUB-ROTINA’);
 FOR I:=1 TO 5 DO
 BEGIN
 WRITELN(Y[I]);
 END;
END;
BEGIN  {BEGIN DO PROGRAMA PRINCIPAL}
CLRSCR;
WRITELN(‘DIGITANDO OS NúMEROS DO VETOR ‘);
FOR I:=1 TO 5 DO
BEGIN
 READLN(W[I]);

---

Capítulo 8 Sub-rotina  | 259
FUNCTION nome_da_function : tipo_de_dado_do_valor_retornado; 
declaração_de_variáveis_locais;
BEGIN 
 comandos;
END;
É importante ressaltar que, para que ocorra o retorno de algum valor para quem chamou a function, 
deve-se atribuir tal valor a uma variável cujo nome seja igual ao dado à function.
A chamada à function acontece atribuindo seu nome a uma variável ou a uma condição, que receberá o 
retorno produzido. A seguir, é apresentado um exemplo (a numeração das linhas não faz parte do programa).
1. PROGRAM EXEMPLO;
2. USES CRT;
3. VAR A, B, S : INTEGER; {variáveis globais}
4. FUNCTION SOMAR: INTEGER;
5. BEGIN
6. SOMAR := A + B;
7. END;
8. BEGIN  {início do programa principal}
9. CLRSCR;
10. WRITELN(‘Digite o primeiro número: ‘);
11. READLN(A);
12. WRITELN(‘Digite o segundo número: ‘);
13. READLN(B);
14. S := SOMAR;  {chamada da sub-rotina SOMAR}
15. WRITELN(‘Soma = ‘,S);
16. READLN;
17. END.
O programa começa sua execução no BEGIN principal, representado no exemplo anterior pela linha 8. 
Posteriormente, executa as linhas 9 a 14. Na linha 14, existe a chamada a uma function. O programa prin-
cipal é desviado para a function, denominada SOMAR. Assim, o fluxo de execução do programa vai para a 
linha 4, executando toda a function, ou seja, da linha 4 à 7. Em seguida, ele retorna à linha 14, atribuindo 
o valor retornado à variável S. Por fim, executa as linhas 15, 16 e 17, e o programa é encerrado.
8.2.5 Function com passagem de parâmetros por valor
Uma function pode receber parâmetros no momento em que é chamada. Os valores informados são 
copiados, sequencialmente, em variáveis descritas em seu cabeçalho. A sintaxe correta é a seguinte:
 FUNCTION nome_da_function(parâmetros:tipo_dos_dados):tipo_de_dado_do valor_retornado; 
declaração_de_variáveis_locais;
BEGIN 
 comandos;
END;
A chamada a uma function acontece atribuindo seu nome a uma variável ou a uma condição, que 
receberá o retorno ao término de sua execução. No momento da chamada, são informados, também, os 
parâmetros que deverão ser levados para a function. A seguir, é apresentado um exemplo de function com 
passagem de parâmetros por valor, ou seja, os parâmetros são variáveis locais da sub-rotina (a numeração 
das linhas não faz parte do programa).

---

Capítulo 8 Sub-rotina  | 261
10. WRITELN(‘Digite o primeiro número: ‘);
11. READLN(A);
12. WRITELN(‘Digite o segundo número: ‘);
13. READLN(B);
14. S := SOMAR(A,B);  {chamada da sub-rotina SOMAR}
15. WRITELN(‘Soma = ‘,S);
16. READLN;
17. END.
O programa começa sua execução no BEGIN principal, representado no exemplo anterior pela linha 
8. Posteriormente, executa as linhas 9 a 14. Na linha 14, existe a chamada a uma function. O programa 
principal é desviado para a function, denominada SOMAR. Assim, o fluxo de execução do programa vai para 
a linha 4, executando toda a function, ou seja, da linha 4 à 7. O primeiro parâmetro é a variável A e será 
passada para a variável X. O segundo parâmetro é a variável B e será passada para a variável Y. Como os 
parâmetros foram passados por referência e isso é identificado pela presença da palavra VAR no cabeçalho 
da function, qualquer alteração nos valores de X ou de Y será também refletida nas variáveis A e B, respec-
tivamente. Em seguida, ele retorna à linha 14, atribuindo o valor retornado à variável S. Por fim, executa 
as linhas 15, 16 e 17 e o programa é encerrado.
8.2.7 Units
Uma unit é um arquivo (.PAS), que pode conter várias procedures e functions, e, depois de compilado, 
torna-se uma biblioteca (.TPU), que pode ser chamada por outros programas por meio do comando USES. 
A sintaxe de uma unit é a seguinte.
UNIT nome_da_unit; {o nome da unit deve ser o nome do arquivo}
INTERFACE
 Cabeçalho das procedures e das functions;
IMPLEMENTATION
 Implementação das procedures e das functions;
END;
Exemplo de unit:
unit calcula;  {esse arquivo deve ser salvo como CALCULA.PAS}
interface
 procedure somar(a,b: integer);
 function multiplicar(a,b,c: integer): integer;
implementation
 procedure somar(a,b:integer);
 var s: integer;
 begin
 s := a + b;
 writeln(‘Soma = ‘,s);
 end;
 function multiplicar(a,b,c:integer):integer;
 begin
 multiplicar := a * b * c; 
 end;
end.
Para criar uma unit, ou seja, uma biblioteca, é necessário abrir um novo arquivo, digitar os códigos 
da biblioteca, como mostra o exemplo anterior, e salvar o arquivo com o mesmo nome da  unit . Esse 
arquivo será .PAS. Em seguida, no menu COMPILE, altere o destino da compilação para DISK. Assim,

---

Capítulo 8 Sub-rotina  | 263
1. #include <stdio.h>
2. int a, b, s; // variáveis globais
3. void soma()
4. { 
5.   printf(“\nDigite o primeiro número: “);
6.   scanf(“%d%*c”,&a);
7.   printf(“\nDigite o segundo número: “);
8.   scanf(“%d%*c”,&b);
9.   s = a + b;
10.   printf(“\nSoma = %d”,s); 
11. } 
12. int main() 
13. { 
14.  soma(); 
15.  getchar();
16.  return 0;
17. } 
Como já comentado na seção 8.3, a execução de programa escrito em C/C++ sempre começa pela fun-
ção main. No exemplo, a execução se inicia na linha 12. Na linha 14, existe uma chamada à função soma. 
Nesse ponto, o fluxo da execução é desviado para a linha 3. Depois, são executadas as linhas 4 até 11. 
Quando a execução atinge a linha 11, a marca de final da função é encontrada. Nesse momento, o fluxo 
da execução retorna para a linha 15, exatamente abaixo de onde ocorreu o desvio para a função soma. Na 
linha 17 está a marca de finalização da função main. Assim, a execução do programa é concluída.
Devemos destacar que, no momento em que a função soma foi chamada, na linha 14, nenhum valor 
ou variável foi colocado entre parênteses, indicando que não houve passagem de parâmetros. Além disso, 
dentro da função soma não foi utilizado o comando return, sinalizando que ela não retornou valor para 
quem a chamou. Por essa razão, seu tipo é void.
A seguir, é apresentado um exemplo de função sem parâmetros e sem retorno (a numeração das linhas 
não faz parte do programa) com a utilização de variáveis locais.
 
1.   #include <stdio.h>
2.   void soma()
3.   { 
4.     int a, b, s; // variáveis locais da sub-rotina soma
5.     printf(“\nDigite o primeiro número: “);
6.     scanf(“%d%*c”,&a);
7.     printf(“\nDigite o segundo número: “);
8.     scanf(“%d%*c”,&b);
9.     s = a + b;
10.    printf(“\nSoma = %d”,s); 
11.  }
12.  int main() 
13.  { 
14.  soma(); 
15. getchar();
16. return 0;
17.  }
No exemplo anterior, a execução se inicia na linha 12. Na linha 14, existe uma chamada à função soma. 
Nesse ponto, o fluxo da execução é desviado para a linha 2. Depois, são executadas as linhas 2 até 11. 
Quando a execução atinge a linha 11, a marca de final da função é encontrada. Nesse momento, o fluxo 
da execução retorna para a linha 15, exatamente abaixo de onde ocorreu o desvio para a função soma. Na 
linha 17 está a marca de finalização da função main. Assim, a execução do programa é concluída.

---

Capítulo 8 Sub-rotina  | 265
12. int main() 
13. { 
14.   int s;   // variável local da sub-rotina main
15.   s = soma();   // chamada da sub-rotina soma
16.   printf(“\nSoma = %d”,s); 
17.   getchar();
18.   return 0;
19. } 
No exemplo anterior, a execução se inicia na linha 12 e as linhas 13 a 15 são executadas. Na li -
nha 15, existe uma chamada à função soma. Nesse ponto, o fluxo da execução é desviado para  
a linha 2. Depois, são executadas as linhas 2 até 10. Quando a execução atinge a linha 10, a marca de 
retorno da função é encontrada. Nesse momento, o fluxo da execução retorna para a linha 15, atribuindo 
o valor retornado à variável s. Por fim, executa as linhas 16 a 19. Na linha 19 está a marca de finalização 
da função main. Assim, a execução do programa é concluída.
Devemos destacar que, no momento em que a função soma foi chamada, na linha 15, nenhum valor 
ou variável foi colocado entre parênteses, o que indica que não houve passagem de parâmetros. Além 
disso, dentro da função soma, foi utilizado o comando return s, significando que o valor da variável s 
foi devolvido a quem a chamou. Por essa razão, o tipo da função é int, exatamente igual ao tipo do valor 
retornado.
8.3.4 Funções com passagem de parâmetros e com retorno
O quarto tipo de função é representado por aquelas que recebem valores no momento em que são 
chamadas (parâmetros) e que, no final, devolvem um valor para quem as chamou (retorno). A seguir, é 
apresentado um exemplo (a numeração das linhas não faz parte do programa, servindo apenas para fa -
cilitar a explicação).
1. #include <stdio.h>
2. int soma(int a, int b)
3. { 
4.   return a + b;
5. } 
6. int main() 
7. { 
8.   int a, b, s;
9.   printf(“\nDigite o primeiro número: “);
10.   scanf(“%d%*c”,&a);
11.   printf(“\nDigite o segundo número: “);
12.   scanf(“%d%*c”,&b);
13.   s = soma(a,b); 
14.   printf(“\nSoma = %d”,s); 
15.   getchar();
16.   return 0;
17. }
No exemplo anterior, a execução iniciou na linha 6. A partir daí, são executadas sequencialmente as 
linhas 7 a 13. Nas linhas 10 e 12, dois valores são recebidos e armazenados nas variáveis a e b. Chegando 
à linha 13, o fluxo de execução é desviado para a função soma, levando para lá os valores das variáveis 
a e b. Serão, então, executadas as linhas 2 a 4. Ao chegar à linha 4, o comando  return é encontrado. 
Isso indica que a execução da função chegou ao fim e que o valor da operação a + b será devolvido para 
quem a chamou. O fluxo de execução retorna à função main, na linha 13, e o valor retornado é atribuído 
à variável s. Depois disso, as linhas 14 a 17 são executadas e o programa chega ao fim.
Devemos destacar que, no momento em que a função soma foi chamada, na linha 13, duas variáveis 
foram colocadas entre parênteses, indicando que houve passagem de parâmetros. Assim, os valores dessas 
variáveis são copiados, respectivamente, para as variáveis a e b, descritas no cabeçalho da função, na li -
nha 2. Além disso, dentro da função soma foi utilizado o comando return a + b, sinalizando que o valor

---

Capítulo 8 Sub-rotina  | 267
17.   int soma; 
18.   a = 2 * a; 
19.   b = 2 * b; 
20.   soma = a + b; 
21.   return soma; 
22. }
Na Figura 8.1 é feita uma representação gráfica de como se dá uma passagem de parâmetros por valor, 
apresentada no programa anterior. Estamos supondo que os valores armazenados nas variáveis x e y, por 
meio da execução das linhas 7 e 9, tenham sido, respectivamente, 5 e 3. Quando a linha 10 é executada, 
esses valores são copiados para as variáveis a e b (pertencentes à função soma_dobro). Depois disso, os 
valores de a e b são multiplicados por 2, nas linhas 18 e 19, e depois, na linha 20, é realizada a soma. O 
resultado dessa soma é devolvido à função main pela execução da linha 21, onde o valor calculado recai 
sobre a variável res (retorno à linha 10).
Figura 8.1 Representação gráfica da passagem de parâmetros por valor.
Função main Função soma_dobro
return soma
soma
res = soma_dobro (5,3)
a5
3
55 *2 = 10
3*2 = 63
16 16
b
x
y
res
No momento em que a função soma_dobro chega ao fim, as variáveis a, b e soma são destruídas e, 
portanto, as alterações realizadas pelas multiplicações por 2 são perdidas, ou seja, x continua valendo 5 e 
y continua valendo 3.
8.3.6 Passagem de parâmetros por referência
Passagem de parâmetros por referência significa que os parâmetros passados para uma função cor -
respondem a endereços de memória ocupados por variáveis. Dessa maneira, toda vez que for necessário 
acessar determinado valor, isso será feito por meio de referência, ou seja, apontamento ao seu endereço.
1. #include <stdio.h>
2. int soma_dobro(int *a, int *b);
3. int main()
4. {
5. int x, y, res;
6. printf(“\nDigite o primeiro número: “);
7. scanf(“%d%*c”,&x);
8. printf(“\nDigite o segundo número: “);
9. scanf(“%d%*c”,&y);
10. res = soma_dobro(&x,&y); 
11. printf(“\nA soma dos números %d e %d = %d”,x,y,res);
12. getchar(); 
13. return 0;
14. } 
15. int soma_dobro(int *a, int *b) 
16. {  
17. int soma; 
18. *a = 2*(*a);

---

Capítulo 8 Sub-rotina  | 269
A execução desse programa começa na linha 13, com a função main. Na função main, são declaradas 
algumas variáveis, dentre elas, mat e vet. A variável mat representa uma matriz bidimensional com 3 linhas e 
5 colunas para armazenar números reais. A variável vet representa um vetor com 3 posições para armazenar 
a soma dos números de cada linha da matriz mat. Da linha 17 à 25, a matriz mat é preenchida com números 
inseridos pelo usuário. Aproveitando essas estruturas de repetição, o vetor vet tem todas as suas posições 
inicializadas com zero, na linha 19.
Duas linhas merecem atenção especial: 26 e 2. A linha 26 está chamando a função soma_linhas, pas-
sando como parâmetros a matriz mat e o vetor vet. Observe, entretanto, que essas duas variáveis não estão 
acompanhadas de colchetes ([]). Assim, quando o nome de uma matriz ou vetor for utilizado sem apresen-
tar colchetes contendo um índice, isso significa que estamos usando o endereço de memória ocupado pela 
posição 0 do vetor ou pela posição 0X0 da matriz.
Como endereços de memória só podem ser atribuídos a ponteiros, observe a linha 2, onde está o ca -
beçalho da função soma_linhas. Nela, pode-se ver que a função recebe dois parâmetros: m[][5] e v[]. 
Assim, toda vez que encontrar um vetor com colchetes vazios ou uma matriz com os colchetes da primeira 
dimensão vazios, entenda que eles são variáveis ponteiros que guardam os endereços iniciais das variáveis.
A partir daí, o programa consegue percorrer o vetor e a matriz normalmente, da linha 5 à 11. Quando 
a função soma_linhas chegar ao fim, o fluxo de execução retornará para a linha 27 e o vetor vet, que 
entrou na função soma_linhas contendo zero em todas as suas posições, voltará com o somatório dos nú-
meros de cada linha da matriz mat. Esses valores serão mostrados nas linhas 27 à 29. O programa, então, 
é finalizado.
4.  int i, j;
5.  for (i = 0;i < 3;i++)
6.   { 
7.    for (j = 0;j < 5;j++)
8.    { 
9.      v[i] = v[i] + m[i][j];
10.   }
11.  } 
12.} 
13.int main() 
14.{ 
15. int i, j; 
16. float mat[3][5], vet[3]; 
17. for (i = 0;i < 3;i++) 
18.  { 
19.  vet[i] = 0; 
20.  for (j = 0;j < 5;j++) 
21.   { 
22.    printf(“\nDigite o elemento %d - %d:”,i,j);
23.    scanf(“%f%*c”,&mat[i][j]); 
24.   } 
25. } 
26.soma_linhas(mat, vet); 
27.for (i = 0;i < 3;i++) 
28.{ 
29.     printf(“\nSoma da linha %d = %f”,i,vet[i]); 
30.} 
31.getchar(); 
32.return 0;
33.}

---

Capítulo 8 Sub-rotina  | 271
8.4 Sub-rotinas em JAVA (métodos)
JAVA é uma linguagem que dá suporte ao paradigma orientado a objeto. Assim, todos os programas 
devem fazer uso de classes. Uma classe pode ser entendida como um tipo de dado capaz de armazenar di -
versas informações e também várias funções para manipular adequadamente essas informações. Seguindo o 
paradigma orientado a objetos, essas informações são chamadas atributos, e as funções, métodos.
Como acontece com todas as linguagens de programação, o usuário poderá utilizar métodos de classes 
já existentes (o Capítulo 9 abordará, por exemplo, vários métodos especificamente criados para trabalhar 
com cadeias de caracteres), como também poderá criar quantos métodos forem necessários para a resolução 
do problema. O capítulo 12 apresenta uma introdução à programação orientada a objetos.
Cada método pode receber diversos valores, os parâmetros, e pode devolver um valor, o retorno. Dessa 
maneira, quando se especifica um método, deve-se deixar claro qual será o tipo de retorno e quais são os 
parâmetros necessários para a sua execução. A chamada a um método normalmente requer que seja infor-
mado o objeto ou a classe que o executará. A sintaxe para chamada de um método é apresentada a seguir.
[retorno = ]nomeDoObjeto.nomeDoMétodo([ listaDeParametros ]);
ou
[retorno = ]nomeDaClasse.nomeDoMétodo([ listaDeParametros ]);
Observe que o retorno e a listaDeParametros aparecem entre colchetes, indicando que são opcionais.
A seguir, são apresentados vários exemplos de métodos. É importante observar que, em todos eles, apa-
recerão as palavras public e static. Essas palavras são chamadas modificadores, ou seja, definem caracte-
rísticas complementares aos métodos. Outros modificadores são: private, protected, abstract e final. 
O modificador public quer dizer que o método poderá ser chamado por qualquer classe, e o modifi -
cador static indica que esse método existirá e poderá ser executado mesmo se nenhum objeto da classe 
onde estiver inserido for criado.
Os parâmetros são representados por uma lista de variáveis colocadas dentro de parênteses, logo após 
o nome do método. Caso haja retorno, a última linha do método deverá incluir o comando return, seguido 
do valor ou variável que será devolvido a quem chamou o método. O tipo do valor retornado deverá ser 
exatamente igual ao tipo informado antes do nome do método. Caso não haja retorno, deverá ser digitada 
a palavra void. Os tipos de métodos são apresentados em detalhes a seguir.
As variáveis globais, ou seja, aquelas que são reconhecidas por todas as partes do programa, devem ser 
declaradas fora de todos os métodos, inclusive fora do método main. As variáveis locais devem ser declara-
das dentro dos métodos e são reconhecidas apenas no método onde foram declaradas. 
A seguir, um programa exemplo que soma dois números digitados pelo usuário será utilizado para 
demonstrar os diferentes tipos de métodos.
8.4.1 Métodos sem passagem de parâmetros e sem retorno
O tipo mais simples de método é aquele que não recebe nenhuma informação no momento de sua 
chamada e também não repassa nenhum valor para quem o chamou. A seguir, é apresentado um exemplo 
de método sem parâmetros e sem retorno (a numeração das linhas não faz parte do programa) com a 
utilização de variáveis globais. 
1. import java.util.Scanner;
2. public class Exemplo
3. {
4.   static int a, b, s;  // variáveis globais
5.   public static void main(String args[])
6.   {
7.    soma();   // chamada do método soma()
8.   }
9.   public static void soma()
10.   { 
11.    Scanner e = new Scanner(System.in);
12.    System.out.println(“Digite o primeiro número: “);

---

Capítulo 8 Sub-rotina  | 273
8.4.2 Métodos com passagem de parâmetros e sem retorno
O segundo tipo de método é representado por aqueles que recebem valores no momento em que são 
chamados (parâmetros), mas que, no final, não devolvem valor para quem os chamou (retorno). A seguir, é 
apresentado um exemplo (a numeração das linhas não faz parte do programa, servindo apenas para facilitar 
a explicação).
1. import java.util.Scanner;
2. public class Exemplo
3. {
4.   public static void main(String args[])
5.   {
6.    int a, b;   // variáveis locais do método main
7.    Scanner e = new Scanner(System.in);
8.    System.out.println(“Digite o primeiro número: “); 
9.    a = e.nextInt(); 
10.   System.out.println(“Digite o segundo número: “); 
11.   b = e.nextInt();    
12.   soma(a,b);   // chamada do método soma()
13.  }
14   public static void soma(int a,int b)
15.  { 
16.   int s;   // variável local do método soma()
17.   s = a + b; 
18.   System.out.println(“Soma = “ + s); 
19.  } 
20. }
Como acontece nos programas escritos na linguagem C/C++, a execução de um programa JAVA tam-
bém começa pelo método main. No exemplo, a execução teve início na linha 4. A partir daí, são executadas 
sequencialmente as linhas 5 a 12. Nas linhas 9 e 11, dois valores são recebidos e armazenados nas variáveis 
a e b. Chegando à linha 12, o fluxo de execução é desviado para o método  soma, na linha 14, levando 
para lá os valores das variáveis a e b. Serão, então, executadas as linhas 14 a 19, onde está a marca de en -
cerramento do método. O fluxo de execução retorna ao método main, na linha 13, imediatamente abaixo 
do ponto de chamada ao método soma. Desse modo, a execução do programa é concluída.
Devemos destacar que, no momento em que o método soma foi chamado, na linha 12, duas variáveis 
foram colocadas entre parênteses, o que significa que houve passagem de parâmetros. Os valores dessas 
variáveis são copiados para as variáveis a e b, descritas no cabeçalho do método, na linha 14. Além disso, 
dentro do método soma não foi utilizado o comando return, indicando que ele não retornou valor para 
quem o chamou. Por essa razão, seu tipo foi definido como void.
8.4.3 Métodos sem passagem de parâmetros e com retorno
O terceiro tipo de método é representado por aqueles que não recebem valores no momento em que são 
chamados (parâmetros), mas que, no final, devolvem um valor para quem os chamou (retorno). A seguir, é 
apresentado um exemplo (a numeração das linhas não faz parte do programa, servindo apenas para facilitar 
a explicação).
1. import java.util.Scanner;
2. public class Exemplo
3. {
4.   public static void main(String args[])
5.   {
6.    int s;    // variável local do método main
7.    s = soma();   // chamada do método soma()

---

Capítulo 8 Sub-rotina  | 275
No exemplo anterior, a execução teve início na linha 4. A partir daí, são executadas, sequencialmente, 
as linhas 5, 6, 7, 8, 9, 10 e 11. Nas linhas 9 e 11, dois valores são recebidos e armazenados nas variáveis a 
e b. Chegando à linha 12, o fluxo de execução é desviado para o método soma, levando para lá os valores 
das variáveis a e b. Serão, então, executadas as linhas 15, 16 e 17. Ao chegar à linha 17, o comando return 
é encontrado. Isso significa que a execução do método chegou ao fim e que o valor da operação a + b será 
devolvido para quem o chamou. O fluxo de execução retorna ao método main, na linha 12, e o valor retor-
nado é atribuído à variável s. Depois disso, as linhas 13 e 14 são executadas e o programa chega ao fim.
Devemos destacar que, no momento em que o método soma foi chamado, na linha 12, duas variáveis 
foram colocadas entre parênteses, indicando que houve passagem de parâmetros. Assim, os valores dessas 
variáveis são copiados, respectivamente, para as variáveis a e b, descritas no cabeçalho do método, na linha 
15. Além disso, dentro do método soma foi utilizado o comando return a + b , o que significa que um 
valor foi devolvido a quem o chamou. Por essa razão, o tipo do método é int, exatamente igual ao tipo do 
valor retornado.
8.4.5 Passagem de parâmetros por valor e por referência
Uma peculiaridade da linguagem JAVA é que todas as variáveis que não forem de tipos primitivos se -
rão consideradas referência. Isso quer dizer que a variável contém apenas o endereço de memória onde a 
informação completa foi gravada.
Assim, toda vez que um tipo primitivo for passado como parâmetro, essa passagem será feita por valor, 
ou seja, será criada uma cópia completa da informação dentro do método. Toda vez que um tipo não pri -
mitivo for passado como parâmetro, a passagem será por referência, isto é, será feita uma cópia apenas do 
endereço onde a informação está gravada. As seções 8.3.5 e 8.3.6, apresentadas anteriormente, descrevem 
em detalhe esses dois tipos de passagem de parâmetros. Os princípios lá descritos são os mesmos em todas 
as linguagens de programação.
Observação
Na linguagem JAVA, vetores e matrizes não são considerados tipos primitivos e, assim, são 
passados como parâmetros por meio de referência. Observe o exemplo (a numeração das linhas 
não faz parte do programa, servindo apenas para facilitar a explicação).
1. import java.util.Scanner;
2. public class Exemplo
3. {
4.   public static void main(String args[])
5.   { Scanner e;
6.     int i, j;
7.     float mat[][], vet[];
8.     mat = new float[3][5];
9.     vet = new float[3];
10.   e = new Scanner(System.in); 
11.   for (i=0;i<3;i++) 
12.   { vet[i] = 0; 
13.     for (j=0;j<5;j++) 
14.     { System.out.println(“Digite o elemento “ + i + “-” + j + “ : “); 
15.            mat[i][j] = e.nextFloat();
16.    }
17.   } 
18.   soma_linhas(mat, vet); 
19.   for (i=0; i<3; i++) 
20.   { System.out.println (“Soma da linha “ + i + “ =  “ + vet[i]); 
21.   } 
22.   }

---

Capítulo 8 Sub-rotina  | 277
  b = dado.nextInt();
  c = a + b;
  return c;
 } 
}
O exemplo a seguir é um programa JAVA que utiliza os métodos implementados em rotinas.java, 
por isso, na primeira linha de código, existe a importação do arquivo que tem os métodos implementados.
import sub_rotinas.rotinas;
public class principal
{
public static void main(String args[])
{
 int r;
 rotinas.mensagem();
 r = rotinas.soma();
 System.out.println(“soma = “+r);
}
}
EXERCÍCIOS  RESOLVIDOS
1. Faça um programa contendo uma sub-rotina que retorne 1 se o número digitado for positivo ou 0 se  
for negativo.
SOLUÇÃO:
ALGORITMO
DECLARE num, x NUMÉRICO 
LEIA num
x ← verifica(num) 
SE x = 0
ENTÃO ESCREVA “Número positivo” 
SENÃO ESCREVA “Número negativo” 
FIM_ALGORITMO.
SUB-ROTINA verifica(num NUMÉRICO)
 DECLARE res NUMÉRICO
 SE num >= 0
 ENTÃO res ←  1
 SENÃO res ←  0
 RETORNE res
FIM_SUB_ROTINA verifica
SOLUÇÃO:
\EXERC\CAP8\PASCAL\EX1.PAS e \EXERC\CAP8\PASCAL\EX1.EXE
1a SOLUÇÃO: FUNÇÃO  ANTES  DA  main()
\EXERC\CAP8\C++\EX1_A.CPP e \EXERC\CAP8\C++\EX1_A.EXE
2a SOLUÇÃO: FUNÇÃO  DEPOIS  DA  main()
\EXERC\CAP8\C++\EX1_B.CPP e \EXERC\CAP8\C++\EX1_B.EXE
PASCAL
C/C++

---

Capítulo 8 Sub-rotina  | 279
 PARA i ←  b ATÉ c FAÇA
  INÍCIO
   r ←  RESTO (i / a)
   SE r = 0
   ENTÃO s ←  s + i
  FIM
 RETORNE s
FIM_SUB_ROTINA divisores
SOLUÇÃO:
\EXERC\CAP8\PASCAL\EX3.PAS e \EXERC\CAP8\PASCAL\EX3.EXE 
1a SOLUÇÃO: FUNÇÃO  ANTES  DA  main()
\EXERC\CAP8\C++\EX3_A.CPP e \EXERC\CAP8\C++\EX3_A.EXE
2a SOLUÇÃO: FUNÇÃO  DEPOIS  DA  main()
\EXERC\CAP8\C++\EX3_B.CPP e \EXERC\CAP8\C++\EX3_B.EXE
SOLUÇÃO:
\EXERC\CAP8\JAVA\EX3.java e \EXERC\CAP8\JAVA\EX3.class
4. Faça uma sub-rotina que receba um único valor representando segundos. Essa sub-rotina deverá con-
vertê-lo para horas, minutos e segundos. Todas as variáveis devem ser passadas como parâmetro, não 
havendo variáveis globais.
SOLUÇÃO:
ALGORITMO
DECLARE seg NUMÉRICO 
LEIA seg 
transformacao(seg); 
FIM_ALGORITMO.
SUB-ROTINA transformacao(segundos NUMÉRICO) 
 DECLARE h, m, s, r NUMÉRICO
 h ←  segundos / 3600
 r ← RESTO(segundos / 3600) 
 m ← r / 60
 s = RESTO(r / 60) 
 ESCREVA h, m, s
FIM_SUB_ROTINA transformacao
SOLUÇÃO:
\EXERC\CAP8\PASCAL\EX4.PAS e \EXERC\CAP8\PASCAL\EX4.EXE
1a SOLUÇÃO: FUNÇÃO  ANTES  DA  main()  
\EXERC\CAP8\C++\EX4_A.CPP e \EXERC\CAP8\C++\EX4_A.EXE
2a SOLUÇÃO: FUNÇÃO  DEPOIS  DA  main()
\EXERC\CAP8\C++\EX4_B.CPP e \EXERC\CAP8\C++\EX4_B.EXE
SOLUÇÃO:
\EXERC\CAP8\JAVA\EX4.java e \EXERC\CAP8\JAVA\EX4.class
5. Crie um programa que receba os valores antigo e atual de um produto. Chame uma sub-rotina que 
determine o percentual de acréscimo entre esses valores. O resultado deverá ser mostrado no programa 
principal.
PASCAL
C/C++
JAVA
PASCAL
C/C++
JAVA

---

Capítulo 8 Sub-rotina  | 281
    FIM
  FIM
FIM_SUB_ROTINA multiplicacao
SOLUÇÃO:
\EXERC\CAP8\PASCAL\EX6.PAS e \EXERC\CAP8\PASCAL\EX6.EXE
1a SOLUÇÃO: FUNÇÃO  ANTES  DA  main()
\EXERC\CAP8\C++\EX6_A.CPP e \EXERC\CAP8\C++\EX6_A.EXE
2a SOLUÇÃO: FUNÇÃO  DEPOIS  DA  main()
\EXERC\CAP8\C++\EX6_B.CPP e \EXERC\CAP8\C++\EX6_B.EXE
SOLUÇÃO:
\EXERC\CAP8\JAVA\EX6.java e \EXERC\CAP8\JAVA\EX6.class
7. Elabore um programa contendo uma sub-rotina que receba as três notas de um aluno como parâme -
tros e uma letra. Se a letra for A, a sub-rotina deverá calcular a média aritmética das notas do aluno; se 
for P, deverá calcular a média ponderada, com pesos 5, 3 e 2. A média calculada deverá ser devolvida 
ao programa principal para, então, ser mostrada.
SOLUÇÃO:
ALGORITMO
DECLARE nota1, nota2, nota3, m NUMÉRICO 
letra LITERAL 
LEIA nota1 
LEIA nota2 
LEIA nota3 
REPITA
LEIA letra
ATÉ (letra = “A”) OU (letra = “P”)
m ← calcula_media(nota1, nota2, nota3, letra) 
SE letra = “A”
ENTÃO ESCREVA “A média aritmética “ , m 
SENÃO ESCREVA “A média ponderada “, m 
FIM_ALGORITMO.
SUB-ROTINA calcula_media(n1, n2, n3 NUMÉRICO, l LITERAL)
DECLARE media NUMÉRICO
SE l = “A”
ENTÃO media ←  (n1+n2+n3)/3
SENÃO media ←(n1*5+n2*3+n3*2)/(5+3+2)
RETORNE media
FIM_SUB_ROTINA calcula_media
SOLUÇÃO:
\EXERC\CAP8\PASCAL\EX7.PAS e \EXERC\CAP8\PASCAL\EX7.EXE
1a SOLUÇÃO  – FUNÇÃO  ANTES  DA  main()
\EXERC\CAP8\C++\EX7_A.CPP e \EXERC\CAP8\C++\EX7_A.EXE
2a SOLUÇÃO  – FUNÇÃO  DEPOIS  DA  main()
\EXERC\CAP8\C++\EX7_B.CPP e \EXERC\CAP8\C++\EX7_B.EXE
SOLUÇÃO:
\EXERC\CAP8\JAVA\EX7.java e \EXERC\CAP8\JAVA\EX7.class
PASCAL
C/C++
JAVA
PASCAL
C/C++
JAVA

---

Capítulo 8 Sub-rotina  | 283
 INÍCIO
 ESCREVA “Digite o “, i, “ o número: “ 
 LEIA num
 SE i = 1 
 ENTÃO INÍCIO
    maior ← num 
    menor ← num
       FIM 
SENÃO INÍCIO
    SE num > maior 
    ENTÃO maior ← num 
    SE num < menor 
    ENTÃO menor ← num
    FIM
 FIM
ESCREVA “O maior número digitado foi: “,maior 
ESCREVA “O menor número digitado foi: “,menor 
FIM_SUB_ROTINA maior_menor
SOLUÇÃO:
\EXERC\CAP8\PASCAL\EX9.PAS e \EXERC\CAP8\PASCAL\EX9.EXE
1a SOLUÇÃO  – FUNÇÃO  ANTES  DA  main()
\EXERC\CAP8\C++\EX9_A.CPP e \EXERC\CAP8\C++\EX9_A.EXE
2a SOLUÇÃO  – FUNÇÃO  DEPOIS  DA  main()
\EXERC\CAP8\C++\EX9_B.CPP e \EXERC\CAP8\C++\EX9_B.EXE
SOLUÇÃO:
\EXERC\CAP8\JAVA\EX9.java e \EXERC\CAP8\JAVA\EX9.class
10. Crie uma sub-rotina que receba como parâmetro um valor inteiro e positivo N e retorne o valor de S, 
obtido pelo seguinte cálculo:
S = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!
SOLUÇÃO:
ALGORITMO
DECLARE num, s NUMÉRICO 
LEIA num
s ← sequencia(num) 
ESCREVA s 
FIM_ALGORITMO.
SUB-ROTINA sequencia(n NUMÉRICO) 
DECLARE a, b, f, seq NUMÉRICO 
seq ← 1
PARA a ←  1 ATÉ n FAÇA
 INÍCIO
f ←  1
PARA b ← 1 ATÉ a FAÇA 
INÍCIO
f ←  f * b
FIM
PASCAL
C/C++
JAVA

---

Capítulo 8 Sub-rotina  | 285
 REPITA
 LEIA cabelos[x]
 ATÉ (cabelos[x] = “C” OU cabelos[x] = “L” OU cabelos[x] = “P”) 
 LEIA idade[x]
 FIM
FIM_SUB_ROTINA leitura
SUB-ROTINA media_idade (olhos[5], cabelos[5] LITERAL, 
   idade[5] NUMÉRICO)
 DECLARE i, cont, soma, media NUMÉRICO 
 soma ← 0
 cont ←  0
 PARA i ← 1 ATÉ 5 FAÇA 
 INÍCIO
  SE (olhos[i] = “C”) E (cabelos[i] = “P”) 
  ENTÃO INÍCIO
     soma ← soma + idade[i] 
     cont ← cont + 1
     FIM
 FIM
 SE cont = 0 
 ENTÃO media ← 0
 SENÃO media ← soma / cont 
 RETORNE media
FIM_SUB-ROTINA media_idade
SUB-ROTINA maior_idade (idade[5] NUMÉRICO)
DECLARE i, maior NUMÉRICO
PARA i ←  1 ATÉ 5 FAÇA
INÍCIO
SE i = 1
 ENTÃO maior ←  idade[i]
 SENÃO INÍCIO
  SE (idade[i] > maior)
  ENTÃO maior ←  idade[i]
  FIM
FIM
RETORNE maior
FIM_SUB_ROTINA maior_idade
SUB-ROTINA qt_individuos(sexo[5],olhos[5],cabelos[5] LITERAL,
idade[5] NUMÉRICO)
 DECLARE i, qtd NUMÉRICO 
qtd ← 0
 PARA i ← 1 ATÉ 5 FAÇA 
 INÍCIO
 SE sexo[i] = “F” E idade[i] >= 18 E idade[i] <= 35 E 
olhos[i] = “A” E cabelos[i] = “L”
 ENTÃO qtd ← qtd + 1 
 FIM
RETORNE qtd 
FIM_SUB_ROTINA qt_individuos
SOLUÇÃO:
\EXERC\CAP8\PASCAL\EX11.PAS e \EXERC\CAP8\PASCAL\EX11.EXE
SOLUÇÃO:
\EXERC\CAP8\C++\EX11.CPP e \EXERC\CAP8\C++\EX11.EXE
PASCAL
C/C++

---

Capítulo 8 Sub-rotina  | 287
 INÍCIO
LEIA vet1[x] 
  FIM
 fatoriais(vet1, vet2) 
 PARA x ← 1 ATÉ 10 FAÇA
INÍCIO
  ESCREVA vet2[x]
 FIM
FIM_ALGORITMO.
SUB-ROTINA fatoriais(a[10], b[10] NUMÉRICO) 
 DECLARE i, j , f NUMÉRICO
 PARA i ← 1 ATÉ 10 FAÇA 
 INÍCIO
  SE (a[i] = 0) OU (a[i] = 1) 
  ENTÃO b[i] ← 1
  SENÃO INÍCIO 
     b[i] ← 1
     PARA j ← 1 ATÉ a[i] FAÇA 
     INÍCIO
     b[i] ←  b[i] * j
     FIM 
     FIM
   FIM
FIM SUB_ROTINA fatoriais
SOLUÇÃO:
\EXERC\CAP8\PASCAL\EX13.PAS e \EXERC\CAP8\PASCAL\EX13.EXE
SOLUÇÃO:
\EXERC\CAP8\C++\EX13.CPP e \EXERC\CAP8\C++\EX13.EXE
SOLUÇÃO:
\EXERC\CAP8\JAVA\EX13.java e \EXERC\CAP8\JAVA\EX13.class
14. Crie uma sub-rotina que receba como parâmetro dois vetores de dez elementos inteiros positivos e  
mostre o vetor união dos dois primeiros.
SOLUÇÃO:
ALGORITMO
DECLARE x, vet1[10], vet2[10], vet3[20], cont NUMÉRICO 
PARA x ← 1 ATÉ 10 FAÇA
 INÍCIO 
  REPITA
   LEIA vet1[x] 
  ATÉ vet1[x] >= 0
 FIM
PARA x ← 1 ATÉ 10 FAÇA 
INÍCIO
 REPITA
  LEIA vet2[x] 
 ATÉ vet2[x] >= 0
FIM
cont ← uniao(vet1,vet2,vet3) 
x ← 1
PASCAL
C/C++
JAVA

---

Capítulo 8 Sub-rotina  | 289
PARA x ← 1 ATÉ 5 FAÇA 
 INÍCIO
  ESCREVA vet[x]
 FIM 
FIM_ALGORITMO.
SUB-ROTINA ordena(v[5] NUMÉRICO) 
DECLARE i, j, aux NUMÉRICO 
PARA i ← 1 ATÉ 5 FAÇA
 INÍCIO
PARA j ← 1 ATÉ 4 FAÇA 
INÍCIO
SE (v[j] > v[j+1]) 
ENTÃO INÍCIO
aux ← v[j] 
v[j] ← v[j+1] 
v[j+1] ← aux
        FIM
  FIM
 FIM
FIM SUB_ROTINA ordena
SOLUÇÃO:
\EXERC\CAP8\PASCAL\EX15.PAS e \EXERC\CAP8\PASCAL\EX15.EXE
SOLUÇÃO:
\EXERC\CAP8\C++\EX15.CPP e \EXERC\CAP8\C++\EX15.EXE
SOLUÇÃO:  
\EXERC\CAP8\JAVA\EX15.java e \EXERC\CAP8\JAVA\EX15.class   
16. Crie uma sub-rotina que receba dois vetores A e B de dez elementos inteiros como parâmetro. A  sub-
-rotina deverá determinar e mostrar um vetor C que contenha os elementos de A e B em ordem decres-
cente. O vetor C deverá ser mostrado no programa principal.
SOLUÇÃO:
ALGORITMO
DECLARE x, vet1[10], vet2[10], vet3[20] NUMÉRICO 
PARA x ← 1 ATÉ 10 FAÇA
 INÍCIO
  LEIA vet1[x]
 FIM
PARA x ← 1 ATÉ 10 FAÇA 
 INÍCIO
  LEIA vet2[x]
 FIM 
ordena_todos(vet1,vet2,vet3) 
PARA x ← 1 ATÉ 20 FAÇA
  INÍCIO
  ESCREVA vet3[x]
  FIM 
FIM_ALGORITMO.
PASCAL
C/C++
JAVA

---

Capítulo 8 Sub-rotina  | 291
SOLUÇÃO:
\EXERC\CAP8\PASCAL\EX16.PAS e \EXERC\CAP8\PASCAL\EX16.EXE
SOLUÇÃO:
\EXERC\CAP8\C++\EX16.CPP e \EXERC\CAP8\C++\EX16.EXE
SOLUÇÃO:
\EXERC\CAP8\JAVA\EX16.java e \EXERC\CAP8\JAVA\EX16.class
17. Faça uma sub-rotina que receba como parâmetro uma matriz A(5,5) e retorne a soma de seus elementos.
SOLUÇÃO:
ALGORITMO
DECLARE x, y, s, matriz[5,5] NUMÉRICO 
PARA x ← 1 ATÉ 5 FAÇA
INÍCIO
PARA y ← 1 ATÉ 5 FAÇA 
INÍCIO
LEIA matriz[x,y]
FIM
FIM
s ← soma_matriz(matriz) 
ESCREVA s
FIM_ALGORITMO.
SUB-ROTINA soma_matriz(m[5,5] NUMÉRICO) 
DECLARE i, j, soma NUMÉRICO
soma ←  0
PARA i ← 1 ATÉ 5 FAÇA 
INÍCIO
PARA j ← 1 ATÉ 5 FAÇA 
INÍCIO
soma ←  soma + m[i, j]
FIM
FIM 
RETORNE soma
FIM SUB-ROTINA soma_matriz
SOLUÇÃO:
\EXERC\CAP8\PASCAL\EX17.PAS e \EXERC\CAP8\PASCAL\EX17.EXE
SOLUÇÃO:
\EXERC\CAP8\C++\EX17.CPP e \EXERC\CAP8\C++\EX17.EXE
SOLUÇÃO:
\EXERC\CAP8\JAVA\EX17.java e \EXERC\CAP8\JAVA\EX17.class
18. Crie uma sub-rotina que receba como parâmetro uma matriz A(6,6) e retorne o menor elemento de  
sua diagonal secundária.
SOLUÇÃO:
ALGORITMO
DECLARE x, y, menor, matriz[6,6] NUMÉRICO 
PARA x ← 1 ATÉ 6 FAÇA
INÍCIO
PASCAL
C/C++
JAVA
PASCAL
C/C++
JAVA

---

Capítulo 8 Sub-rotina  | 293
FIM
FIM 
FIM_ALGORITMO.
SUB-ROTINA multiplica_matriz(m[6,6] NUMÉRICO)
DECLARE i, j, v NUMÉRICO
PARA i ← 1 ATÉ 6 FAÇA 
INÍCIO
v ←  m[i,i]
PARA j ← 1 ATÉ 6 FAÇA 
INÍCIO
m[i][j] ←  m[i][j] * v
FIM
 FIM
FIM_SUB_ROTINA multiplica_matriz
SOLUÇÃO:
\EXERC\CAP8\PASCAL\EX19.PAS e \EXERC\CAP8\PASCAL\EX19.EXE
SOLUÇÃO:
\EXERC\CAP8\C++\EX19.CPP e \EXERC\CAP8\C++\EX19.EXE
SOLUÇÃO:
\EXERC\CAP8\JAVA\EX19.java e \EXERC\CAP8\JAVA\EX19.class
20. Crie uma sub-rotina que receba como parâmetro uma matriz A(12,12) e retorne a média aritmética  
dos elementos abaixo da diagonal principal.
SOLUÇÃO:
ALGORITMO
DECLARE x, y, matriz[12,12], m NUMÉRICO 
PARA x ← 1 ATÉ 12 FAÇA
INÍCIO
PARA y ← 1 ATÉ 12 FAÇA 
INÍCIO
LEIA matriz[x,y]
FIM
FIM
m ← media_aritmetica(matriz) 
ESCREVA m
FIM_ALGORITMO.
SUB-ROTINA media_aritmetica(m[12,12] NUMÉRICO) 
DECLARE i, j, cont, soma, media NUMÉRICO 
soma ← 0
cont ←  0
PARA i ←  2 ATÉ 12 FAÇA
INÍCIO
PARA j ←  12 ATÉ (14 - i ) PASSO -1 FAÇA
INÍCIO
soma ←  soma + m[i,j]
cont ←  cont + 1
PASCAL
C/C++
JAVA

---

Capítulo 8 Sub-rotina  | 295
SOLUÇÃO:
\EXERC\CAP8\PASCAL\EX21.PAS e \EXERC\CAP8\PASCAL\EX21.EXE
SOLUÇÃO:
\EXERC\CAP8\C++\EX21.CPP e \EXERC\CAP8\C++\EX21.EXE
SOLUÇÃO:
\EXERC\CAP8\JAVA\EX21.java e \EXERC\CAP8\JAVA\EX21.class
22. Crie um programa que carregue um vetor com oito números inteiros, calcule e mostre dois vetores 
resultantes. O primeiro vetor resultante deverá conter os números positivos e o segundo, os números 
negativos. Cada vetor resultante terá no máximo oito posições, e nem todas serão obrigatoriamente 
utilizadas.
SOLUÇÃO:
ALGORITMO
DECLARE vet1[8], vet2[8], vet3[8], i, cont1, cont2 NUMÉRICO 
PARA i ← 1 ATÉ 8 FAÇA
 INÍCIO
  LEIA vet1[i]
 FIM
cont1 ←  pares(vet1, vet2)
SE cont1 = 1
ENTÃO ESCREVA “NENHUM PAR FOI DIGITADO” 
SENÃO
PARA i ← 1 ATÉ cont1 - 1 FAÇA 
 INÍCIO
 ESCREVA vet2[i]
 FIM
cont2 ← impares(vet1, vet3) 
SE cont2 = 1
ENTÃO ESCREVA “NENHUM ÍMPAR FOI DIGITADO” 
SENÃO
PARA i ← 1 ATÉ cont2 - 1 FAÇA 
 INÍCIO
 ESCREVA vet3[i]
 FIM 
FIM_ALGORITMO.
SUB-ROTINA pares(v1[8], v2[8] NUMÉRICO) 
 DECLARE i, r, cont NUMÉRICO
 cont ←  1
 PARA i ← 1 ATÉ 8 FAÇA 
 INÍCIO
 r ← RESTO(v1[i] / 2) 
 SE r = 0
 ENTÃO INÍCIO
 v2[cont] ← v1[i] 
 cont ← cont + 1 
 FIM
 FIM 
 RETORNE cont
FIM_SUB_ROTINA pares
PASCAL
C/C++
JAVA

---

Capítulo 8 Sub-rotina  | 297
SOLUÇÃO:
\EXERC\CAP8\PASCAL\EX23.PAS e \EXERC\CAP8\PASCAL\EX23.EXE
SOLUÇÃO:
\EXERC\CAP8\C++\EX23.CPP e \EXERC\CAP8\C++\EX23.EXE
SOLUÇÃO:
\EXERC\CAP8\JAVA\EX23.java e \EXERC\CAP8\JAVA\EX23.class
24. Faça um programa contendo uma sub-rotina que receba dois valores numéricos e um símbolo. Esse 
símbolo representará a operação que se deseja efetuar com os números. Se o símbolo for +, deverá ser re-
alizada uma adição, e, se for *, deverá ser efetuada uma multiplicação. O resultado deverá ser mostrado 
no programa principal.
SOLUÇÃO:
ALGORITMO
DECLARE num1, num2, res NUMÉRICO
 op LITERAL
LEIA num1 
LEIA num2 
REPITA
 LEIA op
ATÉ op = ‘+’ OU op = ‘*’
res ← calculo(num1, num2, op) 
ESCREVA res
FIM_ALGORITMO.
SUB-ROTINA calculo(n1, n2 NUMÉRICO, simbolo LITERAL)
DECLARE result NUMÉRICO
SE simbolo = ‘+’
ENTÃO result ←  n1 + n2
SENAO result ←  n1 * n2
RETORNE result
FIM_SUB_ROTINA calculo
SOLUÇÃO:
\EXERC\CAP8\PASCAL\EX24.PAS e \EXERC\CAP8\PASCAL\EX24.EXE
SOLUÇÃO:
\EXERC\CAP8\C++\EX24.CPP e \EXERC\CAP8\C++\EX24.EXE
SOLUÇÃO:
\EXERC\CAP8\JAVA\EX24.java e \EXERC\CAP8\JAVA\EX24.class
25. Crie uma sub-rotina que receba como parâmetro um vetor A de 25 números inteiros e substitua todos os 
valores negativos de A por zero. O vetor resultante deverá ser mostrado no programa principal.
SOLUÇÃO:
ALGORITMO
DECLARE vetor[25], i NUMÉRICO 
PARA i ← 1 ATÉ 25 FAÇA
 INÍCIO
PASCAL
C/C++
JAVA
PASCAL
C/C++
JAVA

---

Capítulo 8 Sub-rotina  | 299
Observação
A quantidade de parcelas que compõe S é igual a N.
11. Faça uma sub-rotina que receba como parâmetro um valor inteiro e positivo N, indicando a quantidade 
de parcelas de uma soma S, calculada pela fórmula:
S = 2/4  +  5/5  +  10/6  +  17/7  +  26/8  +  ...  + (n2  + 1)/(n + 3)
12. Crie uma sub-rotina que receba como parâmetro dois valores X e Z, calcule e retorne X z sem utilizar 
funções ou operadores de potência prontos. 
13. Foi realizada uma pesquisa entre 15 habitantes de uma região. Os dados coletados de cada habitante 
foram: idade, sexo, salário e número de filhos. 
 Faça uma sub-rotina que leia esses dados armazenando-os em vetores. Depois, crie sub-rotinas que 
recebam esses vetores como parâmetro e retornem a média de salário entre os habitantes, a menor e a 
maior idade do grupo e a quantidade de mulheres com três filhos que recebem até R$ 500,00 (utilize 
uma sub-rotina para cada cálculo).
14. Faça uma sub-rotina que receba um vetor X de 30 elementos inteiros como parâmetro e retorne dois 
vetores A e B. O vetor A deve conter os elementos de X que sejam maiores que zero e o vetor B, os ele-
mentos menores ou iguais a zero. 
15. Elabore uma sub-rotina que receba um vetor X de 15 números inteiros como parâmetro e retorne a 
quantidade de valores pares em X. 
16. Faça uma sub-rotina que receba um vetor X de 20 de números reais como parâmetro e retorne a soma 
dos elementos de X. 
17. Elabore uma sub-rotina que calcule o máximo divisor comum (MDC) de dois números recebidos como 
parâmetros. 
18. Crie uma sub-rotina que gere e mostre os três primeiros números primos acima de 100. 
19. Faça uma sub-rotina que receba como parâmetro dois vetores de dez números inteiros, determine e mos-
tre o vetor intersecção entre eles. 
20. A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e o 
número de filhos. Faça uma sub-rotina que leia esses dados para um número não determinado de pessoas 
e retorne a média de salário da população, a média do número de filhos, o maior salário e o percentual 
de pessoas com salário inferior a R$ 380,00.
21. Faça uma sub-rotina que receba uma matriz 10X10 e determine o maior elemento acima da diagonal 
principal. Esse valor deverá ser mostrado no programa principal. 
22. Criar um programa que: 
 ■ utilize uma sub-rotina para receber os elementos de uma matriz 10X5 de números reais; 
 ■ utilize uma sub-rotina para calcular a soma de todos os elementos localizados abaixo da sexta linha 
dessa matriz; 
Os resultados deverão ser mostrados no programa principal.
23. Crie um programa que receba três valores (obrigatoriamente maiores que zero), representando as medi-
das dos três lados de um triângulo.
Elabore sub-rotinas para:
 ■ determinar se esses lados formam um triângulo (sabe-se que, para ser triângulo, a medida de um 
lado qualquer deve ser inferior ou igual à soma das medidas dos outros dois). 
 ■ determinar e mostrar o tipo de triângulo (equilátero, isósceles ou escaleno), caso as medidas for -
mem um triângulo. 
Todas as mensagens deverão ser mostradas no programa principal.