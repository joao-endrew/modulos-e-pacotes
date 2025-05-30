
#módulo completo

'''import statistics

elementos = [1.5, 1.9, 2.1, 2.9, 3, 3.6, 4.2, 5, 5.5, 6.1, 10.3, 11, 12.9, 13]

m = statistics.mean(elementos)

med = statistics.median(elementos)

print(m)
print(med)'''


#uso de apelido

'''import statistics as est

elementos = [1.5, 1.9, 2.1, 2.9, 3, 3.6, 4.2, 5, 5.5, 6.1, 10.3, 11, 12.9, 13]

m = est.mean(elementos)

med = est.median(elementos)

print(m)
print(med)'''


#apenas as funções mean e median

'''from statistics import mean, median

elementos = [1.5, 1.9, 2.1, 2.9, 3, 3.6, 4.2, 5, 5.5, 6.1, 10.3, 11, 12.9, 13]

m = mean(elementos)

med = median(elementos)

print(m)
print(med)'''


#todas as funções

from statistics import *

elementos = [1.5, 1.9, 2.1, 2.9, 3, 3.6, 4.2, 5, 5.5, 6.1, 10.3, 11, 12.9, 13]

m = mean(elementos)

med = median(elementos)

print(m)
print(med)
