'''
    É muito comum termos um conjunto de escalares, um vetor, e precisarmos executar operações aritméticas.
'''

import numpy as np

a = 2
v1 = np.array([1, 2, 3, 4, 5])
soma = v1 + a  # vai somar 2 (valor de a) a cada elemento de v1
print(soma)
print()

b = 3
c = 10
r2 = (v1 * b / c)
print(f'r2 = {r2}')
