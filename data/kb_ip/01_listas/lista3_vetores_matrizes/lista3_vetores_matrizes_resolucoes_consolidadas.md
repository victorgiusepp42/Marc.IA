---
tipo: resolucao_aluno
etapa: 1
lista: lista3_vetores_matrizes
autor_original: Victor Giusepp Almeida
fonte_dir: 01_listas/lista3_vetores_matrizes/resolucoes_aluno
data_processamento: 2026-07-05
status: consolidado
observacao: Resolucoes de Victor consolidadas para melhor retrieval (cada uma era 1 chunk de ~500 tokens).
---

# Resolucoes — lista3_vetores_matrizes

> Consolidado de 15 resolucoes do aluno. Cada resolucao e separada por `=== EX NN ===`.

## === EX 01: 10_Matrizes2x2_SomaAB (Portugol Studio) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista3_vetores_matrizes
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista3_vetores_matrizes/10_Matrizes2x2_SomaAB.por
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

programa {
  funcao inicio() {
    inteiro A[2][2], B[2][2], C[2][2], i, j

    escreva("Preencha a primeira matriz 2x2: \n")
    para (i = 0; i < 2; i++) {
      para (j = 0; j < 2; j++) {
        escreva("A[", i+1, "][", j+1, "]: ")
        leia(A[i][j])
      }
    }

    escreva("\nPreencha a segunda matriz 2x2: \n")
    para (i = 0; i < 2; i++) {
      para (j = 0; j < 2; j++) {
        escreva("B[", i+1, "][", j+1, "]: ")
        leia(B[i][j])
      }
    }

    //gera matriz C somando os elementos na mesma posição de A e B
    para (i = 0; i < 2; i++) {
      para (j = 0; j < 2; j++) {
        C[i][j] = A[i][j] + B[i][j]
      }
    }

    escreva("\nMatriz C (A + B):\n")
    para (i = 0; i < 2; i++) {
      para (j = 0; j < 2; j++) {
        escreva(C[i][j], "\t")
      }
      escreva("\n")
    }
  }
}
```

## === EX 02: 11_Matriz3x3_AcimaDiagonal (Portugol Studio) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista3_vetores_matrizes
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista3_vetores_matrizes/11_Matriz3x3_AcimaDiagonal.por
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

programa {
  funcao inicio() {
    inteiro matriz[3][3], i, j

    para (i = 0; i < 3; i++) {
      para (j = 0; j < 3; j++) {
        escreva("Elemento [", i+1, "][", j+1, "]: ")
        leia(matriz[i][j])
      }
    }

    escreva("\nElementos acima da diagonal principal: \n")
    //Nos elementos acima da diagonal principal j > i
    para (i = 0; i < 3; i++) {
      para (j = 0; j < 3; j++) {
        se (j > i) {
          escreva("[", i+1, "][", j+1, "] = ", matriz[i][j], "\n")
        }
      }
    }
  }
}
```

## === EX 03: 12_Matriz3x3_abaixoDiagonal (Portugol Studio) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista3_vetores_matrizes
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista3_vetores_matrizes/12_Matriz3x3_abaixoDiagonal.por
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

programa {
  funcao inicio() {
    inteiro matriz[3][3], i, j

    para (i = 0; i < 3; i++) {
      para (j = 0; j < 3; j++) {
        escreva("Elemento [", i+1, "][", j+1, "]: ")
        leia(matriz[i][j])
      }
    }

    escreva("\nElementos abaixo da diagonal principal: \n")
    //Nos elementos abaixo da diagonal principal j < i
    para (i = 0; i < 3; i++) {
      para (j = 0; j < 3; j++) {
        se (j < i) {
          escreva("[", i+1, "][", j+1, "] = ", matriz[i][j], "\n")
        }
      }
    }
  }
}
```

## === EX 04: 13_Matriz5x5_MaiorElemento (Portugol Studio) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista3_vetores_matrizes
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista3_vetores_matrizes/13_Matriz5x5_MaiorElemento.por
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

programa {
  funcao inicio() {
    inteiro matriz[5][5], i, j, maior, linMaior, colMaior

    para (i = 0; i < 5; i++) {
      para (j = 0; j < 5; j++) {
        escreva("Elemento [", i+1, "][", j+1, "]: ")
        leia(matriz[i][j])
      }
    }

    //inicializa o maior com o primeiro elemento e guarda sua posição
    maior = matriz[0][0]
    linMaior = 0
    colMaior = 0

    para (i = 0; i < 5; i++) {
      para (j = 0; j < 5; j++) {
        se (matriz[i][j] > maior) {
          maior = matriz[i][j]
          linMaior = i
          colMaior = j
        }
      }
    }

    escreva("\nMaior elemento: ", maior)
    escreva("\nPosição: [", linMaior+1, "][", colMaior+1, "]")
  }
}
```

## === EX 05: 14_Vetor_OrdenacaoCrescente (Portugol Studio) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista3_vetores_matrizes
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista3_vetores_matrizes/14_Vetor_OrdenacaoCrescente.por
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

programa {
  funcao inicio() {
    inteiro vetor[10], i, j, temp

    para (i = 0; i < 10; i++) {
      escreva("Digite o ", i + 1, "º número: ")
      leia(vetor[i])
    }

    //Compara elementos em pares e troca se necessário, repetindo até o vetor estar ordenado
    para (i = 0; i < 9; i++) {
      para (j = 0; j < 9 - i; j++) {
        se (vetor[j] > vetor[j + 1]) {
          //troca os elementos usando variável auxiliar temp
          temp = vetor[j]
          vetor[j] = vetor[j + 1]
          vetor[j + 1] = temp
        }
      }
    }

    escreva("\nVetor ordenado (crescente): [")
    para (i = 0; i < 9; i++) {
      escreva(vetor[i], ", ")
    }
    escreva(vetor[9], "] ")
  }
}
```

## === EX 06: 15_Matriz3x3_SomaLinhaColuna (Portugol Studio) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista3_vetores_matrizes
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista3_vetores_matrizes/15_Matriz3x3_SomaLinhaColuna.por
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

programa {
  funcao inicio() {
    inteiro matriz[3][3], i, j, somaLinha, somaColuna

    para (i = 0; i < 3; i++) {
      para (j = 0; j < 3; j++) {
        escreva("Elemento [", i+1, "][", j+1, "]: ")
        leia(matriz[i][j])
      }
    }

    escreva("\nSoma por linha: \n")
    //para cada linha, percorre todas as colunas acumulando a soma
    para (i = 0; i < 3; i++) {
      somaLinha = 0
      para (j = 0; j < 3; j++) {
        somaLinha = somaLinha + matriz[i][j]
      }
      escreva("Soma da linha ", i+1, ": ", somaLinha, "\n")
    }

    escreva("\nSoma por coluna: \n")
    //para cada coluna, percorre todas as linhas acumulando a soma
    para (j = 0; j < 3; j++) {
      somaColuna = 0
      para (i = 0; i < 3; i++) {
        somaColuna = somaColuna + matriz[i][j]
      }
      escreva("Soma da coluna ", j+1, ": ", somaColuna, "\n")
    }
  }
}
```

## === EX 07: 1_Inteiros_Vetor_Soma (Portugol Studio) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista3_vetores_matrizes
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista3_vetores_matrizes/1_Inteiros_Vetor_Soma.por
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

programa {
  	funcao inicio() {
    		inteiro vetor[10], soma, i
        		soma = 0

        para (i = 0; i < 10; i++) {
          escreva("Digite o ", i + 1, "° número: ")
          leia(vetor[i])
        }

        para (i = 0; i < 10; i++) {
          soma = soma + vetor[i]
        }

        escreva("Soma dos elementos: ", soma)
    }
}
```

## === EX 08: 2_Vetor_Menor_Maior (Portugol Studio) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista3_vetores_matrizes
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista3_vetores_matrizes/2_Vetor_Menor_Maior.por
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

programa {
	funcao inicio() {
		inteiro vetor[8],maior,menor, i

		para (i = 0; i < 8; i++) {
			escreva("Digite o ",i + 1, "° número: ")
			leia(vetor[i])
		}

		maior = vetor[0]
		menor = vetor[0]

		para (i = 1; i < 8; i++) {
			se (vetor[i] > maior) {
				maior = vetor[i]
			} senao se (vetor[i] < menor) {
				menor = vetor[i]
			}
		}
		escreva("\n O maior valor do vetor é ", maior)
		escreva("\n O menor valor do vetor é ", menor)
	}
}
```

## === EX 09: 3_Vetor_Conta_Pares (Portugol Studio) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista3_vetores_matrizes
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista3_vetores_matrizes/3_Vetor_Conta_Pares.por
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

programa {
  funcao inicio() {
    inteiro vetor[10], contaPares, i
    contaPares = 0

    para (i = 0; i < 10; i++) {
      escreva("Digite o ", i + 1, "º número: ")
      leia(vetor[i])
    }

    //verifica cada elemento do vetor se é par 
    para (i = 0; i < 10; i++) {
      se (vetor[i] % 2 == 0) {
        contaPares = contaPares + 1
      }
    }

    escreva("\nQuantidade de números pares: ", contaPares)
  }
}
```

## === EX 10: 4_Vetores_Soma_AB (Portugol Studio) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista3_vetores_matrizes
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista3_vetores_matrizes/4_Vetores_Soma_AB.por
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

programa {
  funcao inicio() {
    inteiro A[5], B[5], C[5], i

    escreva("Digite os elementos do Vetor A :\n")
    para (i = 0; i < 5; i++) {
      escreva("A[", i+1, "]: ")
      leia(A[i])
    }

    escreva("\nDigite os elementos do Vetor B :\n")
    para (i = 0; i < 5; i++) {
      escreva("B[", i+1, "]: ")
      leia(B[i])
    }

    //registra no Vetor C a soma das posições correspondentes de A e B
    para (i = 0; i < 5; i++) {
      C[i] = A[i] + B[i]
    }

    escreva("\n --> Vetor C (soma de A e B): \n")
    para (i = 0; i < 5; i++) {
      escreva("C[", i+1, "] = ", C[i], "\n")
    }
  }
}
```

## === EX 11: 5_Vetor_OrdemInversa (Portugol Studio) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista3_vetores_matrizes
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista3_vetores_matrizes/5_Vetor_OrdemInversa.por
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

programa {
  funcao inicio() {
    inteiro vetor[10], i

    para (i = 0; i < 10; i++) {
      escreva("Digite o ", i + 1, "º número: ")
      leia(vetor[i])
    }

    escreva("\n--> Vetor na ordem inversa: [")
    //Exibe do último ao primeiro elemento do vetor
    para (i = 9; i > 0; i--) {
      escreva(vetor[i], ", ")
    }
    escreva(vetor[0],"]")
  }
}
```

## === EX 12: 6_Matriz3x3_Exibir (Portugol Studio) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista3_vetores_matrizes
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista3_vetores_matrizes/6_Matriz3x3_Exibir.por
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

programa {
  funcao inicio() {
    inteiro matriz[3][3], i, j

    escreva("Preencha a matriz 3x3: \n")
    para (i = 0; i < 3; i++) {
      para (j = 0; j < 3; j++) {
        escreva("Elemento [", i+1, "][", j+1, "]: ")
        leia(matriz[i][j])
      }
    }

    escreva("\n-Matriz 3x3-\n")
    //Laço externo: i percorre linhas
    //Laço interno: j percorre colunas
    para (i = 0; i < 3; i++) {
      para (j = 0; j < 3; j++) {
        escreva(matriz[i][j], "\t")
      }
      escreva("\n")
    }
  }
}
```

## === EX 13: 7_Matriz3x3_Soma (Portugol Studio) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista3_vetores_matrizes
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista3_vetores_matrizes/7_Matriz3x3_Soma.por
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

programa {
  funcao inicio() {
    inteiro matriz[3][3], i, j, soma
    soma = 0

    para (i = 0; i < 3; i++) {
      para (j = 0; j < 3; j++) {
        escreva("Elemento [", i+1, "][", j+1, "]: ")
        leia(matriz[i][j])
      }
    }

    //acumula a soma na variável percorrendo todos os elementos da matriz
    para (i = 0; i < 3; i++) {
      para (j = 0; j < 3; j++) {
        soma = soma + matriz[i][j]
      }
    }

    escreva("\nSoma de todos os elementos: ", soma)
  }
}
```

## === EX 14: 8_Matriz4x4_DiagonalPrincipal (Portugol Studio) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista3_vetores_matrizes
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista3_vetores_matrizes/8_Matriz4x4_DiagonalPrincipal.por
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

programa {
  funcao inicio() {
    inteiro matriz[4][4], i, j, somaDiagonal
    somaDiagonal = 0

    para (i = 0; i < 4; i++) {
      para (j = 0; j < 4; j++) {
        escreva("Elemento [", i+1, "][", j+1, "]: ")
        leia(matriz[i][j])
      }
    }

    //Soma os elementos onde o índice de linha é igual ao índice de coluna (i=j)
    para (i = 0; i < 4; i++) {
      somaDiagonal = somaDiagonal + matriz[i][i]
    }

    escreva("\nSoma da diagonal principal: ", somaDiagonal)
  }
}
```

## === EX 15: 9_Matriz3x3_MatrizIdentidade (Portugol Studio) ===

```
---
tipo: resolucao_aluno
etapa: 1
lista: lista3_vetores_matrizes
linguagem: portugol
fonte: docs/materiais_kb/Listas_Exercicios/Victor_Giusepp_Almeida_Lista3_vetores_matrizes/9_Matriz3x3_MatrizIdentidade.por
autor: Victor Giusepp Almeida
data_processamento: 2026-07-04
observacao: código de produção do aluno, NÃO canônico
---

programa {
   funcao inicio() {
      inteiro matriz[3][3], i, j
      logico identidade

      para (i = 0; i < 3; i++) {
         para (j = 0; j < 3; j++) {
            escreva("Elemento [", i+1, "][", j+1, "]: ")
            leia(matriz[i][j])
         }
      }

      identidade = verdadeiro

      //Matriz identidade: diagonal principal deve ser 1, restante deve ser 0
      para (i = 0; i < 3; i++) {
         para (j = 0; j < 3; j++) {
            se (i == j) {
               se (matriz[i][j] != 1) {
                  identidade = falso
               }
            } senao {
               se (matriz[i][j] != 0) {
                  identidade = falso
               }
            }
         }
      }

      se (identidade==verdadeiro) {
         escreva("\nA matriz É uma matriz identidade.")
      } senao {
         escreva("\nA matriz NÃO e uma matriz identidade.")
      }
   }
}
```
