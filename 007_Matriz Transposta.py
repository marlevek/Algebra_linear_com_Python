'''
    Nesse caso, troca-se as linhas pelas colunas ou vice-versa.
    Para uma matriz quadrada a transposição não altera a diagonal principal da matriz.
'''

import numpy as np

a = np.array([[1, 0, 3], [2, 1, 4]])
print('a = ', a)
print()
at = np.transpose(a)
print('at = ', at)
print()

# PARA OBTERMOS A MATRIZ TRANSPOSTA NO PYTHON PODEMOS TAMBÉM USAR O MÉTODO '.T'
b = np.array([[1, 5, 3], [2, 3, 4]])
mt = a.T  # esse .T calcula a transposta imediata da matriz
print(mt)


# PROPRIEDADES DA MATRIZ TRANSPOSTA:

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a == b)
print()

# (a + b).T
print(a.T + b.T)
print()

# (a.T).T == a

# (x * a).T == x * a.T
x = 5
print(5 * a.T)


