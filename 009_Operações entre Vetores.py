import numpy as np

a = 2
v1 = np.arange(1, 6)  # arange = forma um vetor unidimensional com 5 elementos, começando do 1
v2 = np.array([2, 3, 5, 1, 4])
v3 = v1 * v2
print(f'A multiplicação entre v1 e v2 é {v3}')
print()

v4 = v1 + v2 - a * v1
print(f' v4 = {v4}')

