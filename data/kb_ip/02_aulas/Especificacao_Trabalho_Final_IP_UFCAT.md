---
tipo: especificacao_trabalho
etapa: 0
topico: geral
fonte: docs/materiais_kb/AULAS/Especificacao_Trabalho_Final_IP_UFCAT (1).txt
data_processamento: 2026-07-04
autor_original: Prof. Dr. Márcio de Souza Dias (UFCAT/IMTec)
status: extraido_pdf_bruto
ordem_aula: '0'
observacao: Texto extraído automaticamente do PDF; revisar figuras/diagramas que não vieram.
---

# Especificacao_Trabalho_Final_IP_UFCAT

Trabalho  Final  |  Introducao  a  Programacao  |  UFCAT  -  IA
 
   UNIVERSIDADE  FEDERAL  DE  CATALAO Bacharelado  em  Inteligência  Artificial Disciplina:  Introducao  a  Programacao  (Python)    
 
TRABALHO  FINAL  EM  GRUPO 
Aplicação  Interativa  para  a  Mostra  UFCAT 
 
  
Turma:  2024/2  -  Introducao  a  Programacao  Total  de  Alunos:  39  alunos  Modalidade:  Trabalho  em  Grupo  (3  a  4  integrantes)  Duração:  4  semanas  (1  mês)  Apresentação:  Mostra  UFCAT  -  Data  a  definir  pelo  professor  Valor:  40  pontos  (40%  da  nota  final)     Catalao  -  Goiás 2026  
Página  1  de  16
 

===PAGE_BREAK===

Trabalho  Final  |  Introducao  a  Programacao  |  UFCAT  -  IA
 
1.  APRESENTAÇÃO  
 
Este  documento  descreve  a  especificação  completa  do  Trabalho  Final  da  disciplina  de  
Introdução
 
a
 
Programação
 
com
 
Python,
 
ofertada
 
no
 
Bacharelado
 
em
 
Inteligência
 
Artificial
 
da
 
Universidade
 
Federal
 
de
 
Catalao
 
(UFCAT).
  O  trabalho  tem  como  objetivo  culminar  o  aprendizado  do  semestre,  integrando  conceitos  
fundamentais
 
de
 
programação
 
por
 
meio
 
do
 
desenvolvimento
 
de
 
uma
 
aplicação
 
interativa
 
que
 
será
 
exposta
 
e
 
demonstrada
 
ao
 
público
 
na
 
Mostra
 
UFCAT.
  A  Mostra  UFCA  é  um  evento  de  extensão  que  reúne  trabalhos  de  diversos  cursos  e  
possui
 
grande
 
visibilidade
 
dentro
 
e
 
fora
 
da
 
comunidade
 
acadêmica.
 
Portanto,
 
espera-se
 
que
 
os
 
projetos
 
desenvolvidos
 
sejam
 
funcionais,
 
bem
 
documentados,
 
visualmente
 
apresentáveis
 
e
 
relevantes
 
para
 
o
 
contexto
 
de
 
Inteligência
 
Artificial.
   
Página  2  de  16
 

===PAGE_BREAK===

Trabalho  Final  |  Introducao  a  Programacao  |  UFCAT  -  IA
 
2.  OBJETIVOS  
 
2.1  Objetivo  Geral  Desenvolver,  em  grupo,  uma  aplicação  em  Python  que  demonstre  conhecimentos  
adquiridos
 
ao
 
longo
 
da
 
disciplina
 
e
 
que
 
possa
 
ser
 
apresentada
 
de
 
forma
 
clara
 
e
 
interativa
 
ao
 
público
 
da
 
Mostra
 
UFCAT.
  
2.2  Objetivos  Específicos  •  Aplicar  conceitos  de  lógica  de  programação,  estruturas  de  dados  e  controle  de  
fluxo
 
em
 
um
 
projeto
 
prático.
 •  Trabalhar  de  forma  colaborativa,  exercitando  divisão  de  tarefas,  comunicação  e  
integração
 
de
 
código.
 •  Desenvolver  habilidades  de  documentação  técnica  e  apresentação  de  projetos.  •  Explorar  pelo  menos  uma  biblioteca  Python  relacionada  a  algum  dos  temas:  
interface
 
gráfica,
 
manipulação
 
de
 
dados,
 
visualização,
 
processamento
 
de
 
linguagem
 
natural
 
ou
 
machine
 
learning
 
básico.
 •  Produzir  um  produto  final  que  seja  atraente,  funcional  e  acessível  para  o  público  
geral.
   
Página  3  de  16
 

===PAGE_BREAK===

Trabalho  Final  |  Introducao  a  Programacao  |  UFCAT  -  IA
 
3.  TEMAS  SUGERIDOS  
 
Os  grupos  devem  escolher  um  dos  temas  abaixo  ou  propor  um  tema  alternativo,  sujeito  
à
 
aprovação
 
prévia
 
do
 
professor
 
até
 
o
 
final
 
da
 
Semana
 
1
 
(17/06/2026).
 
Os
 
temas
 
foram
 
pensados
 
para
 
serem
 
acessíveis
 
aos
 
alunos
 
do
 
primeiro
 
período
 
de
 
IA,
 
ao
 
mesmo
 
tempo
 
em
 
que
 
dialogam
 
com
 
áreas
 
fundamentais
 
de
 
Inteligência
 
Artificial.
  
# Tema Descrição  Resumida 
Bibliotecas  Sugeridas 
1  Chatbot  Interativo  
Bot  de  perguntas  e  respostas  sobre  um  tema  livre  (curiosidades,  FAQ,  jogos  de  adivinhação  etc.)  
NLTK,  re,  tkinter  
2  Visualizador  de  Dados  
Painel  que  carrega  um  dataset  (CSV/JSON)  e  exibe  gráficos  e  estatísticas  de  forma  interativa.  
pandas,  matplotlib,  seaborn  
3  Jogo  com  IA  simples  
Jogo  (da  velha,  snake,  labirinto  etc.)  com  oponente  controlado  por  lógica/IA  básica.  
pygame,  random,  minimax  
4  Classificador  Visual  
App  que  recebe  uma  imagem  ou  texto  e  exibe  uma  classificação/resultado  com  explicação.  
scikit-learn,  PIL,  tkinter  
5  
Simulador  /  Calculadora  Inteligente  
Simulador  de  fenômenos  (ex:  epidemias,  mercado,  clima)  com  gráficos  em  tempo  real.  
numpy,  matplotlib,  tkinter  
6  
Assistente  de  Quiz  com  NLP  basico  
Quiz  interativo  que  usa  NLP  simples  para  interpretar  respostas  abertas  do  usuário.  
NLTK,  tkinter,  json  
7  
Tema  Livre  (IA-relacionado)  
Proposta  original,  desde  que  envolva  Python,  interatividade  e  relação  com  IA.  
A  definir  com  o  professor   Observação:  independentemente  do  tema,  o  projeto  DEVE  possuir  uma  interface  de  
interação
 
com
 
o
 
usuário
 
(terminal
 
com
 
menus,
 
tkinter,
 
pygame
 
ou
 
outra
 
biblioteca
 
gráfica
 
aprovada).
   
Página  4  de  16
 

===PAGE_BREAK===

Trabalho  Final  |  Introducao  a  Programacao  |  UFCAT  -  IA
 
4.  FORMAÇÃO  DOS  GRUPOS  
 
A  turma  de  39  alunos  será  dividida  em  grupos  de  3  a  4  integrantes,  resultando  em  
aproximadamente
 
10
 
grupos.
 
A
 
formação
 
será
 
livre,
 
devendo
 
ser
 
comunicada
 
ao
 
professor
 
ate
 
o
 
fim
 
da
 
Semana
 
1
 
por
 
meio
 
de
 
uma
 
planilha
 
disponível
 
via
 
Sigaa.
  
Criterio Detalhamento Tamanho  do  grupo  3  ou  4  integrantes  (mínimo  3,  máximo  4)  Total  estimado  de  grupos  10  grupos  (podendo  variar  entre  9  e  10)  Prazo  para  formação  Até  o  fim  da  Semana  1  (ver  cronograma)  
Lider  do  grupo  
Cada  grupo  deve  indicar  um  líder  responsável  pela  comunicação  com  o  professor  
Troca  de  grupo  
Não  é  permitida  após  o  prazo  de  formação  (salvo  alguns  situações  excepcionais.   Caso  algum  aluno  fique  sem  grupo  até  o  prazo,  o  professor  realizará  a  alocação  
automática
 
no
 
grupo
 
com
 
menor
 
número
 
de
 
integrantes.
   
Página  5  de  16
 

===PAGE_BREAK===

Trabalho  Final  |  Introducao  a  Programacao  |  UFCAT  -  IA
 
5.  REQUISITOS  TÉCNICOS  DO  PROJETO  
 
5.1  Requisitos  Obrigatórios  •  Linguagem:  Python  3.10  ou  superior.  •  O  projeto  deve  ser  executável  em  ambiente  padrão  (Windows  ou  Linux)  sem  
configurações
 
especiais
 
além
 
da
 
instalação
 
das
 
bibliotecas
 
listadas
 
no
 
requirements.txt.
 •  Deve  haver  um  arquivo  principal  de  entrada  (main.py  ou  app.py)  que  inicializa  o  
programa.
 •  O  projeto  deve  possuir  no  mínimo  3  módulos/arquivos  separados  (separação  por  
responsabilidade).
 •  O  código  deve  ser  comentado  e  conter  docstrings  nas  funções  principais.  •  Deve  ser  utilizado  controle  de  versão  com  Git,  e  o  repositório  deve  estar  publico  
no
 
GitHub
 
até
 
a
 
data
 
de
 
entrega.
 •  Interface  de  usuário  obrigatório  (terminal  interativo  com  menus,  GUI  com  
tkinter/pygame
 
ou
 
equivalente).
  
5.2  Requisitos  de  Conteúdo  Programático  O  projeto  deve  demonstrar,  de  forma  clara,  o  uso  dos  seguintes  conceitos  da  disciplina:   
Conceito Exemplos  de  Uso  no  Projeto 
Variáveis  e  tipos  de  dados  
Armazenamento  de  configurações,  dados  do  usuário,  resultados  Estruturas  de  controle  (if/elif/else)  Validação  de  entradas,  lógica  de  decisão  Laços  de  repetição  (for,  while)  Iteração  sobre  dados,  menus  em  loop,  animações  Funções  e  modularização  Separação  de  responsabilidades,  realização  de  código  Listas,  dicionários  e/ou  tuplas  Armazenamento  de  resultados,  base  de  dados  interna  
Leitura/escrita  de  arquivos  (txt,  csv  ou  json)  
Persistência  de  dados,  carregamento  de  configurações  
Tratamento  de  exceções  (try/except)  Validação  de  entradas,  erros  de  arquivo,  conexão  
Programação  Orientada  a  Objetos  (POO)  -  básica  
Pelo  menos  1  classe  com  atributos  e  métodos  
  
Página  6  de  16
 

===PAGE_BREAK===

Trabalho  Final  |  Introducao  a  Programacao  |  UFCAT  -  IA
 
6.  ENTREGAS  DO  TRABALHO  
 
O  trabalho  possui  três  momentos  de  entrega  formais,  conforme  descrito  abaixo.  Todas  
as
 
entregas
 
devem
 
ser
 
realizadas
 
pelo
 
AVA
 
(Ambiente
 
Virtual
 
de
 
Aprendizagem)
 
da
 
UFCAT.
  
6.1  Entrega  1  -  Proposta  do  Projeto  (Semana  1)  Documento  PDF  de  1  a  2  páginas  contendo:  •  Nome  do  grupo  e  lista  de  integrantes  (RA  e  nome  completo).  •  Tema  escolhido  (da  lista  ou  proposta  própria).  •  Descrição  do  projeto:  o  que  faz,  como  funciona  e  qual  o  diferencial.  •  Esboços  da  interface  (pode  ser  feito  a  mão  ou  digital).  •  Divisão  inicial  de  tarefas  entre  os  integrantes.  •  Link  do  repositório  GitHub  (pode  estar  vazio  neste  momento).   
6.2  Entrega  2  -  Checkpoint  de  Desenvolvimento  (Semana  3)  O  grupo  deve  entregar:  •  Relatório  de  progresso  (PDF,  1  página):  o  que  foi  feito,  o  que  falta,  dificuldades  
encontradas.
 •  Link  do  repositório  GitHub  atualizado  com  o  código  parcial.  •  Vídeo  demonstrativo  curto  (1  a  3  minutos)  mostrando  o  que  já  está  funcionando.   
6.3  Entrega  3  -  Entrega  Final  +  Apresentação  na  Mostra  (Semana  4)  Entrega  final  composta  por:  •  Código-fonte  completo  no  repositório  GitHub  (branch  main  atualizada).  •  Arquivo  requirements.txt  atualizado.  •  README.md  detalhado  com  instruções  de  instalação,  uso  e  descrição  do  
projeto.
 •  Documentação  técnica  (PDF,  3  a  5  páginas)  -  ver  seção  7.  •  Apresentação/poster  para  a  Mostra  UFCAT.  •  Participação  presencial  obrigatória  de  todos  os  integrantes  na  Mostra  UFCAT.    
Página  7  de  16
 

===PAGE_BREAK===

Trabalho  Final  |  Introducao  a  Programacao  |  UFCAT  -  IA
 
7.  DOCUMENTAÇÃO  TÉCNICA  
 
A  documentação  técnica  deve  ser  entregue  em  formato  PDF,  com  3  a  5  páginas,  
contendo
 
as
 
seguintes
 
seções
 
obrigatórias:
  1.  Capa:  título  do  projeto,  nomes  dos  integrantes,  RA,  curso  e  data.  2.  Introdução:  contexto,  motivação  e  objetivos  do  projeto.  3.  Descrição  do  sistema:  arquitetura  geral,  descrição  dos  módulos  e  fluxograma  de  
funcionamento.
 4.  Tecnologias  e  bibliotecas  utilizadas:  breve  justificativa  para  cada  escolha.  5.  Instruções  de  instalação  e  execução:  passo  a  passo  para  rodar  o  projeto.  6.  Divisão  de  tarefas:  descrição  do  que  cada  integrante  desenvolveu.  7.  Dificuldades  e  lições  aprendidas:  reflexão  crítica  do  grupo.  8.  Conclusão  e  trabalhos  futuros:  o  que  poderia  ser  melhorado  ou  expandido.  9.  Referências  (se  houver).   
Página  8  de  16
 

===PAGE_BREAK===

Trabalho  Final  |  Introducao  a  Programacao  |  UFCAT  -  IA
 
8.  CRONOGRAMA  
O  trabalho  deve  ser  realizado  em  4  semanas.  O  cronograma  abaixo  serve  como  
referência;
 
datas
 
exatas
 
serão
 
divulgadas
 
pelo
 
professor
 
no
 
Sigaa.
  
Semana Período Atividades  do  Grupo Entrega 
Semana  1  Dias  1-7  
Formação  dos  grupos,  escolha  do  tema,  definição  da  arquitetura  inicial,  criação  do  repositório  GitHub.  
Proposta  do  Projeto  (PDF)  
Semana  2  Dias  8-14  
Desenvolvimento  do  núcleo  do  projeto:  estruturas  de  dados,  lógica  principal,  protótipo  da  interface.  
-  (desenvolvimento  interno)  
Semana  3  Dias  15-21  
Integração  dos  módulos,  testes,  correção  de  bugs,  inicio  da  documentação.  
Checkpoint  (relatório  +  video  +  GitHub)  
Semana  4  Dias  22-30  
Finalização,  polimento  da  interface,  elaboração  do  poster/material  da  Mostra,  preparação  para  apresentação.  
Entrega  Final  +  Apresentação  na  Mostra   Atenção:  não  serão  aceitas  justificativas  de  atraso  por  problemas  técnicos  de  último  
minuto.
 
Recomenda-se
 
sempre
 
manter
 
o
 
repositório
 
atualizado
 
e
 
fazer
 
backups
 
frequentes.   
Página  9  de  16
 

===PAGE_BREAK===

Trabalho  Final  |  Introducao  a  Programacao  |  UFCAT  -  IA
 
9.  CRITÉRIOS  DE  AVALIACAO  
 
O  trabalho  vale  40  pontos,  distribuídos  conforme  a  rubrica  abaixo.  A  avaliação  será  
realizada
 
pelo
 
professor
 
e
 
poderá
 
contar
 
com
 
avaliação
 
por
 
pares
 
(peer
 
review)
 
entre
 
os
 
grupos.
  
Critério Descrição Peso Pontos 
Funcionamento  e  Qualidade  Técnica  
O  projeto  executa  corretamente  sem  erros  críticos.  Código  organizado,  modular  e  bem  comentado.  
30%  12  pts  
Uso  dos  Conceitos  da  Disciplina  
Presença  e  uso  adequado  de  todos  os  conceitos  listados  na  Seção  5.2.  
25%  10  pts  
Interface  e  Experiência  do  Usuário  
A  interface  é  intuitiva,  esteticamente  adequada  e  o  usuário  consegue  interagir  sem  instruções  externas.  
15%  6  pts  
Documentação  e  README  
Documentação  completa,  clara  e  dentro  dos  padrões  estabelecidos.  
10%  4  pts  
Apresentação  na  Mostra  
Capacidade  de  explicar  o  projeto  ao  público,  responder  perguntas  e  demonstrar  o  funcionamento.  
15%  6  pts  
Cumprimento  dos  Prazos  
Entrega  1  e  Entrega  2  dentro  do  prazo  estabelecido.  
5%  2  pts  
TOTAL   100%  40  pts   
9.1  Penalidades  
Situação Penalidade Atraso  na  Entrega  1  (Proposta)  -2  pontos  por  dia  de  atraso  Atraso  na  Entrega  2  (Checkpoint)  -1  ponto  por  dia  de  atraso  Atraso  na  Entrega  Final  -3  pontos  por  dia  de  atraso  (máximo  de  5  dias)  
Ausência  na  Mostra  UFCAT  (sem  justificativa)  
Zero  no  critério  'Apresentacao'  para  o  integrante  ausente  
Plágio  (código  ou  documentação  sem  nenhuma  alteração  do  original)  
Nota  zero  no  trabalho  para  todo  o  grupo  envolvido  
 
9.2  Bonificação  Grupos  que  implementam  funcionalidades  extras  de  forma  correta  e  relevante  poderão  
receber
 
até
 
5
 
pontos
 
bonus,
 
a
 
critério
 
do
 
professor.
 
Exemplos
 
de
 
funcionalidades
 
extras:
 1.  Integração  com  API  externa  (ex:  API  de  clima,  traducao,  dados  públicos).  2.  Deploy  em  nuvem  ou  empacotamento  como  executável  (.exe).  
Página  10  de  16
 

===PAGE_BREAK===

Trabalho  Final  |  Introducao  a  Programacao  |  UFCAT  -  IA
 
3.  Uso  de  banco  de  dados  SQLite  para  persistência.  4.  Testes  automatizados  (pytest)  com  cobertura  mínima  de  50%.    
Página  11  de  16
 

===PAGE_BREAK===

Trabalho  Final  |  Introducao  a  Programacao  |  UFCAT  -  IA
 
10.  DIRETRIZES  ÉTICAS  E  DE  CONDUTA  
 
O  uso  de  ferramentas  de  IA  generativa  (como  ChatGPT,  GitHub  Copilot,  etc.)  é  
PERMITIDO
 
como
 
apoio
 
ao
 
desenvolvimento,
 
desde
 
que:
 1.  O  grupo  compreenda  e  seja  capaz  de  explicar  todo  o  código  entregue.  2.  O  uso  seja  declarado  na  documentação,  indicando  quais  partes  foram  assistidas  
por
 
IA.
 3.  Não  haja  cópia  direta  e  integral  de  projetos  de  outros  grupos  ou  da  internet.   O  professor  poderá  realizar  arguições  individuais  durante  ou  após  a  apresentação  para  
verificar
 
o
 
entendimento
 
do
 
código
 
por
 
parte
 
de
 
cada
 
integrante.
 
Integrantes
 
que
 
não
 
consigam
 
explicar
 
o
 
código
 
do
 
próprio
 
grupo
 
poderão
 
ter
 
sua
 
nota
 
individual
 
reduzida.
  Casos  de  plágio  confirmado  (código  identico  ou  documentação  copiada  de  outros  
grupos
 
ou
 
fontes
 
externas
 
sem
 
citação)
 
resultarão
 
em
 
nota
 
zero
 
para
 
o
 
trabalho
 
inteiro
 
dos
 
grupos
 
envolvidos,
 
além
 
de
 
registro
 
no
 
histórico
 
acadêmico
 
conforme
 
normativas
 
da
 
UFCAT.
   
Página  12  de  16
 

===PAGE_BREAK===

Trabalho  Final  |  Introducao  a  Programacao  |  UFCAT  -  IA
 
11.  ESTRUTURA  RECOMENDADA  DO  REPOSITÓRIO  
 
O  repositório  GitHub  do  grupo  deve  seguir  a  estrutura  abaixo  (adaptações  são  
permitidas,
 
desde
 
que
 
justificadas
 
no
 
README):
  nome-do-projeto/  |--  main.py                   #  Arquivo  principal  de  entrada  |--  requirements.txt          #  Dependências  do  projeto  |--  README.md                 #  Documentação  principal  |--  /src                      #  Módulos  do  projeto  |--  modulo1.py  |--  modulo2.py  |--  ...  |--  /data                     #  Arquivos  de  dados  (CSV,  JSON,  
etc.)
 |--  /assets                   #  Imagens,  sons,  fontes,  etc.  |--  /docs                     #  Documentação  técnica  (PDF)  |--  /tests                    #  Testes  (opcional,  mas  
recomendado)
   
Página  13  de  16
 

===PAGE_BREAK===

Trabalho  Final  |  Introducao  a  Programacao  |  UFCAT  -  IA
 
12.  DICAS  E  BOAS  PRÁTICAS  
 
12.1  Organização  do  Grupo  1.  Definam  desde  o  início  quem  é  responsável  por  qual  parte  do  código.  2.  Utilizem  branches  no  Git  para  cada  funcionalidade  e  façam  pull  requests  para  
integrar.
 3.  Realizem  reuniões  curtas  (15  min)  pelo  menos  3  vezes  por  semana  para  
sincronizar
 
o
 
progresso.
 4.  Documentem  as  decisões  de  projeto  (o  que  foi  decidido  e  por  que)  em  um  
arquivo
 
DECISOES.md
 
no
 
repositório.
  
12.2  Código  •  Escrevam  o  código  em  portugues  ou  inglês,  mas  mantenham  a  consistência  ao  
longo
 
de
 
todo
 
o
 
projeto.
 •  Evitem  funções  com  mais  de  30  linhas;  se  necessário,  refatorem.  •  Testem  o  código  frequentemente;  não  deixem  os  testes  para  o  último  dia.  •  Usem  nomes  de  variáveis  e  funções  descritivas  (ex:  calcular_media  ao  invés  de  
cm).
  
12.3  Apresentação  na  Mostra  •  Preparem  um  script  de  apresentação  (o  que  cada  um  vai  falar).  •  Tenham  um  plano  B  caso  o  computador  principal  falhe  (cópia  do  projeto  em  
pendrive
 
ou
 
nuvem).
 •  Treinem  responder  perguntas  técnicas  e  não  técnicas  sobre  o  projeto.  •  Produzam  um  pôster  ou  banner  visual  com  o  nome,  objetivo  e  prints  do  projeto.    
Página  14  de  16
 

===PAGE_BREAK===

Trabalho  Final  |  Introducao  a  Programacao  |  UFCAT  -  IA
 
13.  RECURSOS  E  SUPORTE  
 
Recurso Descricao  /  Link Documentação  Python  3  https://docs.python.org/3/  Documentacao  tkinter  https://docs.python.org/3/library/tk.html  Pygame  https://www.pygame.org/docs/  Pandas  https://pandas.pydata.org/docs/  Matplotlib  https://matplotlib.org/stable/contents.html  NLTK  https://www.nltk.org/  scikit-learn  https://scikit-learn.org/stable/  GitHub  Docs  https://docs.github.com/pt  AVA  UFCAT  Plataforma  de  entrega  e  comunicação  oficial  da  disciplina   Atendimento  do  professor:  conforme  horário  de  atendimento  divulgado  no  Sigaa.  
Dúvidas
 
pontuais
 
podem
 
ser
 
enviadas
 
via
 
e-mail.
   
Página  15  de  16
 

===PAGE_BREAK===

Trabalho  Final  |  Introducao  a  Programacao  |  UFCAT  -  IA
 
14.  DECLARAÇÃO  DO  GRUPO  
 
Ao  submeter  a  Proposta  do  Projeto  (Entrega  1),  o  líder  do  grupo  declara,  em  nome  de  
todos
 
os
 
integrantes,
 
que:
  10.  Todos  os  integrantes  leram  e  compreenderam  esta  especificação.  11.  O  grupo  se  compromete  a  cumprir  os  prazos  estabelecidos.  12.  Todo  o  código  produzido  será  de  autoria  própria,  com  uso  declarado  de  
ferramentas
 
de
 
IA
 
quando
 
aplicável.
 13.  Todos  os  integrantes  podem  participar  presencialmente  da  apresentação  na  
Mostra
 
UFCAT.
   
Campo Informação  a  Preencher Nome  do  Grupo  /  Projeto  _______________________________________________  Líder  do  Grupo  _______________________________________________  Integrante  2  _______________________________________________  Integrante  3  _______________________________________________  Integrante  4  (se  houver)  _______________________________________________  Tema  Escolhido  _______________________________________________  Link  do  GitHub  _______________________________________________  Data  de  Submissão  _______________________________________________    
Página  16  de  16
 