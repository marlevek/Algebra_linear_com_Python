# Através da álgebra linear consiguimos trabalhar com: vetores, espaços vetoriais, trnasformações lineares, matrizes e tensores.

#--------------------- ESCALARES-------------------
'''
    São variáveis que admitem apenas um valor específico.
    São úteis para modelar problemas principalmente em uma dimensão.
    Portanto, um escalar é um número qualquer (inteiro, real, natural e até mesmo complexo)
'''

# Exemplos de escalares com Python:
t = 37  # t pode ser por exemplo a temperatura em graus Celcius
vel = 80  # escalar que pode representar a velocidade


#---------------------VETORES----------------------
'''
    São variáveis que tentam representar (modelar ou armazenar) dimensões mais elevadas do que os escalares.
    Com vetores, podemos representar conjuntos de dados.
    Podem armazenar coleções de escalares
'''

# Exemplos de vetores:
# antes temos que importar o NumPY
import numpy as np

vt = np.array([27, 37])  # vetor com 2 dimensões
vv = np.array([20, 15, 100])  # vetor com 3 dimensões
vm = np.array([100, 205, 777, 111])  # vetor com 4 dimensões

#---------------------MATRIZES----------------------
'''
    São uma forma inteligente e simplificada para representar coleções de vetores.
    Seus elementos podem ser números reais, números complexos, expressões algébricas e até funções.
    Para trabalhar com matrizes em Python é necessário antes importar a biblioteca numpy
'''

# Exemplos:
a = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))  # representação de uma matriz 3 x 3
print(a)
print()
b = np.matrix(([1, 2, 3], [4, 5, 6])) # matriz 2 x 3
print(b)
print()
c = np.array(([1, 2, 4], [0, 5, -1], [7, 0, 0]))
print(c)
print()
