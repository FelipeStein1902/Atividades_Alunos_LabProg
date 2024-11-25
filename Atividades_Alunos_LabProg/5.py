import numpy as np
'''
Crie uma matriz 4x4 preenchida com números de 1 a 16. Obtenha a
transposta dessa matriz e multiplique a matriz original pela transposta.
'''

a1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(a1)

a2 = np.transpose(a1)
print(a2)

a3 = np.multiply(a1,a2)
print(a3)