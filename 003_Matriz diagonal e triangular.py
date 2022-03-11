'''
    Matriz quadrada - tamanho das linhas = tamanho das colunas
    Matriz diagonal - todos os elementos fora da diagonal principal forem nulos
    Matriz triangular superior - quando os elementos abaixo da diagonal principal são todos iguais a zero.
    matiz triangular inferior - quando os elementos acima da diagonal principal são todos iguais a zero.
'''

import numpy as np

# Ex. matriz diagonal
matriz_diagonal = np.diag([1, 5, 7, 8, 9])
print(matriz_diagonal)
print(matriz_diagonal.shape)  # mostrará 5 linhas e 5 colunas (5, 5)

