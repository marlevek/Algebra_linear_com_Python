'''
    Para que as operações matemáticas entre as matrizes aconteçam é preciso observar as dimensões das matrizes.
    As matrizes têm que ter a mesma dimensão.
'''

import numpy as np

A = np.array([[1, 1], [2, 2]])
B = np.array([[20, 20], [40, 40]])
C = np.array([[1, 2, 3], [4, 5, 6]])
S = A + B
print(f'S = {S}')
print()

D = A / B
print(f'D = {D}')
print()

M = A * B  # aqui não é o produto entre matrizes mas sim entre os elementos
print(f'M = {M}')
m = np.multiply(A, B)  # mesmo resultado do que o anterior
print(m)

