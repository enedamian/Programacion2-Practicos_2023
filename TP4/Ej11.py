# 13. Encuentra el número mayor de una lista utilizando reduce.
from functools import reduce

# Lista de números
numeros = [12, 45, 78, 34, 99, 23, 56]

# Función que toma dos números y devuelve el mayor de ellos
def encontrar_mayor(x, y):
    return x if x > y else y

# Encontrar el número mayor en la lista utilizando reduce
numero_mayor = reduce(encontrar_mayor, numeros)

# Imprimir el número mayor
print(f"El número mayor en la lista es: {numero_mayor}")

