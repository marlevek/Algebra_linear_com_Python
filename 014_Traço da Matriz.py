'''
    Para compreender alguns teoremas, iremos precisar entender o que é o traço de uma matriz.
    Em álgebra linear, o traço de uma matriz quadrada é definido como a soma dos elementos da sua diagonal principal.
    Nos casos onde a matriz não é quadrada, teremos a soma dos elementos que fazem parte de uma diagonal principal referente a uma matriz quadrada.
'''

import numpy as np

a = np.array([[1, 1], [2, 2]])
b = np.array([[1, 1, 1], [3, 3, 3]])
tr_a = np.trace(a)
print(a)
print(f'tr_a = {tr_a}')
print()

print(b)
tr_b = np.trace(b)
print(f'tr_b = {tr_b}')
print()

#----------------------------------PROPRIEDADES DO TRAÇO DE UMA MATRIZ----------------------------------
'''
1. tr(A + B) = tr(A) + tr(B)

2. tr(x * A) = x * tr(A)

3. O traço de uma matriz quadrada é igual ao traço de sua transposta. 

4. tr(AB) = tr(BA) - o traço de um produto de matrizes quadradas não depende da ordem do produto

5. O traço de uma matriz simétrica é igual à soma dos seus valores próprios (autovalores) - essa é bem importante.

'''

# exemplos das propriedades
a = np.array([[1, 1], [2, 2]])
b = np.array([[3, 3], [4, 4]])
tr_ab = np.trace(a * b)
tr_ab1 = np.trace(b * a)
print(f'Propriedade do Produto: tr_ab = {tr_ab}')
print(f'tr_ab = {tr_ab1} ')
print()
tr_a_mais_b = np.trace(b + a)
print(f'Propriedade da soma: {tr_a_mais_b}')
