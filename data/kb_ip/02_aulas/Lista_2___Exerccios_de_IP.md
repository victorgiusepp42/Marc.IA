---
tipo: lista_exercicios
etapa: 0
topico: vetores_matrizes_listas
fonte: docs/materiais_kb/AULAS/Lista_2_-_Exerccios_de_IP.txt
data_processamento: 2026-07-04
autor_original: Prof. Dr. Márcio de Souza Dias (UFCAT/IMTec)
status: extraido_pdf_bruto
ordem_aula: '0'
observacao: Texto extraído automaticamente do PDF; revisar figuras/diagramas que não vieram.
---

# Lista_2_-_Exerccios_de_IP

Estruturas de Decisão e Repetição em Algoritmos | Introdução à Programação
LISTA 2 DE EXERCÍCIOS
Estruturas de Decisão e Repetição em Algoritmos
Introdução à Programação | Pseudocódigo
Referência Rápida — Estruturas Abordadas

SE/ENTÃO Seleção simples Executar só se verdadeiro
SE/ENTÃO/SENÃO Seleção composta Dois caminhos alternativos
SE encadeado Múltiplas condições Mais de 2 situações
CASO SELECIONE Seleção múltipla Valores distintos de 1 variável
ENQUANTO/FAÇA Repetição pré-testada Qtd. desconhecida, pode ser O
PARA/ATÉ/FAÇA Repetição contada Qtd. de iterações conhecida
REPITA/ATÉ Repetição pós-testada Executa pelo menos 1 vez


===PAGE_BREAK===

Estruturas de Decisão e Repetição em Algoritmos | Introdução à Programação

Exercícios — Enunciados
| Exercicio 1: Triângulo ou Não Triângulo SE/ENTÃO/SENÃO
Leia três valores reais A, Be C que representam os comprimentos dos lados de um triângulo.
Verifique se eles formam um triângulo válido. Para ser válido, o comprimento de cada lado deve ser
menor que a soma dos outros dois.
Se for válido, classifique o triângulo como:

- Equilátero: os três lados são iguais

- Isósceles: exatamente dois lados são iguais

- Escaleno: os três lados são diferentes

Dica Use SE encadeado: primeiro valide o triângulo, depois classifique.
| Exercicio 2: Dia da Semana por Extenso CASO SELECIONE
Leia um número de 1 a 7 e escreva o dia da semana correspondente por extenso:

1 = Segunda-feira, 2 = Terça-feira, 3 = Quarta-feira,

4 = Quinta-feira, 5 = Sexta-feira, 6 = Sábado, 7 = Domingo.
Se o valor informado estiver fora do intervalo de 1 a 7, exiba: "Dia inválido!”.

Dica Utilize CASO SELECIONE para mapear cada número ao dia correspondente.
| Exercicio 3: Reajuste Salarial SE/ENTÃO/SENÃO |
Uma empresa concederá reajuste salarial de acordo com o salário atual do funcionário:

- Salário até R$ 1.000,00 — reajuste de 15%

- Salário entre R$ 1.000,01 e R$ 2.500,00 — reajuste de 10%

- Salário acima de R$ 2.500,00 — reajuste de 5%
Leia o salário atual e exiba o novo salário após o reajuste.

Dica Calcule o novo salário multiplicando pelo fator (ex: salario * 1.15).
| Exercicio 4: Potenciação sem Operador * PARA/ATÉ/FAÇA |
Leia dois inteiros não-negativos: a base X e o expoente Y.


===PAGE_BREAK===

Estruturas de Decisão e Repetição em Algoritmos | Introdução à Programação
Calcule X elevado a Y (X*Y) sem utilizar o operador de potenciação (* ou **).
Use um laço de repetição que multiplica a base Y vezes.
Exiba o resultado ao final.
Tratamento especial: qualquer número elevado a O deve resultar em 1.
Dica  Inicialize resultado <- 1 e multiplique por X a cada iteração do laço.
| Exercicio 5: Maior Divisor Comum (MDC) por Subtrações ENQUANTO/FAÇA |
Leia dois números inteiros positivos A e B.
Calcule o MDC (Máximo Divisor Comum) utilizando o método das subtrações sucessivas:
- Enquanto A e B forem diferentes, subtraia o menor do maior.
- Quando se igualarem, esse valor é o MDC.
Exiba o MDC ao final.
Dica Use ENQUANTO a <> b FAÇA e dentro compare qual é maior para subtrair.
| Exercicio 6: Relatório de Vendas Mensais PARA/ATÉ/FAÇA + SE |
Uma empresa possui 6 vendedores. Leia o nome e o valor total vendido por cada um.
Ao final, exiba:
a) O total de vendas da empresa no mês
b) A média de vendas por vendedor
c) Quantos vendedores ficaram abaixo da média
d) O nome do vendedor que mais vendeu
Dica Use um laço PARA para ler os dados. Guarde o maior valor e o nome correspondente.
| Exercicio 7: Adivinhe o Número Secreto REPITA/ATÉ + SE
O programa define internamente um número secreto (ex: 42).
O usuário tem até 5 tentativas para adivinhar o número.
A cada tentativa incorreta, informe se o chute foi 'Muito alto' ou 'Muito baixo”.
Se o usuário acertar, exiba 'Parabens! Você acertou em X tentativa(s)!".
Se esgotar as tentativas sem acertar, exiba 'Fim de jogo! O número era 42'.


===PAGE_BREAK===

Estruturas de Decisão e Repetição em Algoritmos | Introdução à Programação
Dica Use REPITA...ATÉ (acertou OU tentativas = 5). Incremente o contador dentro do laço.
| Exercicio 8: Contagem de Notas de um Caixa CASO SELECIONE + ENQUANTO |
Um caixa eletrônico possui notas de R$ 2, R$ 5, R$ 10, R$ 20, R$ 50 e R$ 100.
O operador digita o valor de cada nota inserida e O para encerrar.
Ao final, exiba quantas notas de cada valor foram inseridas e o total em caixa.
Dica Use ENQUANTO nota <> O FAÇA e CASO SELECIONE para incrementar o contador de
cada nota.
| Exercicio 9: Verificador de Número Perfeito PARA/ATÉ/FAÇA + SE |
Um número perfeito é aquele cuja soma dos seus divisores próprios (excluindo ele mesmo) é igual
a ele.
Exemplo: 6 é perfeito porque seus divisores próprios são 1,2 e 3,€ 1+2+3 = 6.
Leia um número inteiro N maior que 1.
Verifique todos os números de 1 a N e exiba quais são números perfeitos nesse intervalo.
Exiba também a quantidade total de números perfeitos encontrados.
Dica Use dois laços: o externo de 2 até N, o interno de 1 até num-1 para somar divisores.
| Exercicio 10: Conversão de Base Decimal para Binária | ENQUANTO/FAÇA + MOD
Leia um número inteiro positivo N em base decimal.
Converta-o para base binária usando o método das divisões sucessivas por 2.
O número binário é formado pelos restos das divisões lidos de baixo para cima.
Exemplo: 13 em binário é 1101.
Exiba o número binário resultante.
Dica Acumule os restos (MOD 2) e ao final exiba-os na ordem inversa. Use uma string para
concatenar.


===PAGE_BREAK===

Estruturas de Decisão e Repetição em Algoritmos | Introdução à Programação
| Exercicio 11: Análise Estatística de Sequência ENQUANTO/FAÇA + SE |
Leia uma sequência de números reais positivos. O usuário encerra digitando O (zero).

Ao final, calcule e exiba:
a) Quantidade de números lidos
b) Soma total
c) Média aritmética
d) Maior e menor valor da sequência
e) Quantidade de valores acima da média
Obs: se o usuário digitar O de imediato, exiba 'Nenhum numero foi informado".
Dica Guarde maior e menor a partir do primeiro número lido. A contagem acima da média só é
possível após calcular a média.
