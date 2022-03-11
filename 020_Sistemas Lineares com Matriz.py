# CALCULANDO O CRUZAMENTO ENTRE RETAS

# Ex.: temos duas retas y1 e y2, e queremos achar o ponto de cruzamento entre elas.
# Ou seja, queremos achar os valores de x e y que pertencem às duas retas ao mesmo
# tempo.

# 1. importar numpy
import numpy as np
from numpy.linalg import inv, det

A = np.array([[1, -2], [1, 3]])
B = np.array([[5], [2]])
det_A = det(A)
print(f'det_a = {det_A}')

inv_A = inv(A)
X = inv_A.dot(B)
print(f'y = {X[0]}, x = {X[1]}')

