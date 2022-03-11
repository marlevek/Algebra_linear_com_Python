# para calcular determinante de uma matriz no Python, antes é preciso importar o numpy
# também importar a função det do módulo linalg
# O det só pode ser calculado para matriz quadradda

import numpy as np
from numpy.linalg import det

# PARA MATRIZES ATÉ 3 X 3
# criando matriz 3 x 3
A = np.array([[1, 2,4], [5, 3, -1], [7, 2, 0]])
det_A = det(A)
print(f'det_A =  {det_A}')

# PARA MATRIZES MAIOReS DO QUE 3 X 3
B = np.array([[1, 2, 4, 5, 6, 7], [5, 3, -1, 5, 1, 2], [7, 2, 0, 1, 4, 9], [1, 2, 1, 5, 6, 5], [-7, 2, 4, -1, 6, 6], [0, 2, 5, 5, 9, 7]])  # matriz 6 x 6
print(det(B))


