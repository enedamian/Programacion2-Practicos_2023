from functools import reduce

lista = [1, 2, 3, 4, 5]
resultado = reduce(lambda x, y: x + y, lista)
print(resultado)  # Esto imprimirá 15, que es la suma de los números en la lista.

menor = reduce(lambda x, y: x if x < y else y, lista, -1)
# Esto te devuelve el menor valor de la lista, o -1 si la lista esta vacia