import numpy as np
'''
Crie um array com os números inteiros de 0 a 20. Converta esse array para o
tipo de dado float e exiba o resultado.
'''

a1 = np.arange(1,21)
print(a1)

f1 = a1.astype(float)
print(f1)