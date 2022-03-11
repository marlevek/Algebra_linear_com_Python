'''
    Uma matriz inversa deve satisfazer a condição:
    A * B = B * A = I, onde I é matriz identidade

'''

import numpy as np
from numpy.linalg import inv  # importando a função inversa

A = np.array([[1, 2], [3, 4]])
B = inv(A)
print(B)
print()

