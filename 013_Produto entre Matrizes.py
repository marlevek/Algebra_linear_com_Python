'''
    Só podemos fazer o produto entre matrizes quando o número de colunas da primeira matriz for igual ao número de linhas da segunda matriz.
    Ou seja, a ordem dos produtos entre as matrizes importa.
    Usamos a função do numpy: np.dot(m1, m2).
'''
import numpy as np

A = np.array([[2,1], [5, 3], [4, 2]])  # matriz 2 x 3
B = np.array([[3, 1, 0], [4, 2, 1]])   # matriz 3 x 2
R = np.dot(A, B)  # multiplicação entre matrizes
print(f'R = {R}')
print()

R1 = np.dot(B, A)
print(f'R1 = {R1}')
