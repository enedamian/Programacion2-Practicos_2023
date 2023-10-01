#Encuentra el número mayor de una lista utilizando reduce.
from functools import reduce
import random

lista_aleatorios = [random.randint(1, 100) for _ in range(12)]

#primera forma usando reduce sin lambda
def encontrar_maximo(x, y):
    if x > y:
        return x
    else:
        return y
    
numero_mayor = reduce(encontrar_maximo, lista_aleatorios)
print(lista_aleatorios)
print(numero_mayor)

#segunda forma usando lambda
numero_mayor = reduce(lambda x, y: x if x > y else y, lista_aleatorios)