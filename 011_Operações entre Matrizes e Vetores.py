"""
    Nesse caso, precisamos ter cuidado, pois não podemos fazer operação entre matriz e vetor sem que as dimensões estejam adequadas.
    No caso da multiplicação de um vetor por uma matriz precisamos que a dimensão do vetor seja compatível com a dimensão da matriz.
"""

import numpy as np

L = np.array([1, 2])
A = np.array([1, 2, 3])  # A é um vetor, temos apenas um colchetes
B = np.array([[1, 1, 1], [2, 2, 2]])  # B é uma matriz, tem 2 colchetes
C = A * B
print(f'C = {C}')
print()

b = np.array(([1, 1, 1], [2, 2, 2]))
a = np.array([1, 2, 3])
G = b - a
G1 = a - b
print(f'G = {G}')
print()
print(f'G = {G1}')
print()

D = a / b
print(f'D = {D}')

