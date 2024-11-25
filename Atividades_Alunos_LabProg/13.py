import numpy as np
'''
Crie dois arrays 1D de tamanho 5. Eleve cada elemento do primeiro array ao
quadrado e subtraia o correspondente elemento do segundo array
'''
 
a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([6, 7, 8, 9, 10])

b1 = np.power(a1,2)
print(b1)

b2 = np.subtract(b1, a2)
print(b2)