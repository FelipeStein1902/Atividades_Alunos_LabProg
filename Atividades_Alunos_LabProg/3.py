import numpy as np
'''
Crie um array de números de 0 a 50. Extraia os elementos pares e os
múltiplos de 5 desse array.
'''

a1 = np.array(range(0,51))
print(a1)

pares = a1[a1 % 2 == 0]
m5 = a1[a1 % 5 == 0]
print(pares)
print(m5)