# MATRIZ LINHA E COLUNA: devemos colocar um conjunto a mais de colchetes, senão a representação será de um vetor e não de uma matriz.

import numpy as np

b = np.array([[2, 4, 6]])
print(b)
print()

# MATRIZ COLUNA
c = np.array([[2], [-4], [6], [-10]])
print(c)
print()

# TAMBÉM PODEMOS USAR A FUNÇÃO TRANSPOSE PARA OBTER UMA MATRIZ COLUNA
dt = np.transpose([[2, -4, 6, -10]])
print(dt)

