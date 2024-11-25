import numpy as np
'''
Gere um conjunto de dados simulando as alturas (em cm) de 100 pessoas,
usando uma distribuição normal com média 170 e desvio padrão 10. Depois
calcule:
a. O percentil 25, 50 (mediana) e 75.
b. A quantidade de pessoas com altura acima de 180 cm.
c. Plote um histograma dos dados usando Matplotlib (não precisa
detalhar o código da plotagem).
'''

import numpy as np
import matplotlib.pyplot as plt

# Gerar o conjunto de dados simulando as alturas
np.random.seed(0)  # Para garantir reprodutibilidade
alturas = np.random.normal(loc=170, scale=10, size=100)

# a
percentis = np.percentile(alturas, [25, 50, 75])
print(f"Percentis: 25% = {percentis[0]}, 50% (mediana) = {percentis[1]}, 75% = {percentis[2]}")

# b
acima_180 = np.sum(alturas > 180)
print(f"Número de pessoas com altura acima de 180 cm: {acima_180}")

# c
plt.hist(alturas, bins=15, edgecolor='black')
plt.title('Histograma das Alturas')
plt.xlabel('Altura (cm)')
plt.ylabel('Frequência')
plt.show()
