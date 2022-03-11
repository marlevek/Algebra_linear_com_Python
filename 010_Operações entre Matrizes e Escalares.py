'''
    É muito comum precisarmos fazer operações entre matrizes e escalares. Por exemplo, multiplicar, somar, dividir
todos os elementos de uma matriz por um dado número.
'''

import numpy as np

c = 2
d = 10
a = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
b = c * a
print(f'b = {b}')
print()

e = a - c * d
print(f'e = {e}')