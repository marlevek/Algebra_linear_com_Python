import numpy as np


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print()

# selecionando o primeiro elemento da primeira linha (a11)
print(a[0, 0])
print()

# Extraindo uma linha inteira da matriz
a1n = a[0, :]  # primeira linha inteira da matriz
print(f'a1n = {a1n}')
print()

# Segunda linha da matriz
print(a[1, :])


