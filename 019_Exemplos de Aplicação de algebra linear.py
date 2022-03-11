'''
Suponha que vc precisa avaliar as notas em várias disciplinas para 4 turmas da faculdade
A tabela abaixo representa as médias das notas obtidas por disciplina

            LÓGICA      CÁLCULO     PYTHON      INGLÊS
TURMA A       6            5          9           6
TURMA B       8            9          8           7
TURMA C       9            9          8           6
TURMA D       7            8          6           9

'''

import numpy as np

# representando a tabela (T) em Python
T = np.array([[6, 5, 9, 6], [8, 9, 8, 7], [9, 9, 8, 6], [7, 8, 6, 9]])
print(T)

# Tirando a média das notas obtidas nas 4 turmas por disciplina - Precisamos manter as colunas fixas e coletar as linhas
media_logica = T[:, 0].mean()
print(f'A média das turmas em lógica é {media_logica}')
media_calculo = T[1, :].mean()
print(f'A média das turmas em cálculo é {media_calculo}')
media_python = T[2, :].mean()
print(f'A média das turmas em Python é {media_python}')
media_ingles = T[3, :].mean()
print(f'A média das turmas em Inglês é {media_ingles}')
print()

# Calculando a média de todas as notas por turmas. Agora precisamos manter as linhas fixas e coletar todas as colunas
media_A = T[0, :].mean()
print(f'A média da turma A para todas as 4 disciplinas é {media_A}')
media_B = T[1, :].mean()
print(f'A média da turma B para todas as 4 disciplinas é {media_B}')
media_C = T[2, :].mean()
print(f'A média da turma C para todas as 4 disciplinas é {media_C}')
media_D = T[3, :].mean()
print(f'A média da turma D para todas as 4 disciplinas é {media_D}')

# Média geral
med_faculdade = T.mean()
print(f'A méida geral foi: {med_faculdade}')

# obtendo o desvio padrão das médias das notas
std_faculdade = T.std()
print(f'O desvio padrão de todas as turmas e todas as disciplinas é {std_faculdade:.2f}')
