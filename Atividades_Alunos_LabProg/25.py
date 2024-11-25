import numpy as np

'''
Crie um array bidimensional 4x3 com números inteiros aleatórios entre 1 e 10. Calcule:
a. A soma de todos os elementos.
b. O produto dos elementos em cada linha
''' 

a1 = np.random.randint(1, 11, size=(4, 3))
print(a1)

a = np.sum(a1)
print(f'A soma de todos os elementos e igual : {a}')

l1 = np.prod(a1, axis=1)
print(l1)

