# conceitos bastante utilizados na área de mineração e análise de dados.

import numpy as np
import numpy.linalg as al
A = np.array([[4, 2, 0], [-1, 1, 0], [0, 1, 2]])
autovalores, autovetores = al.eig(A)
print(autovalores)
print(autovetores)