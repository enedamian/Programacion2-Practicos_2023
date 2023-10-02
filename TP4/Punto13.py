from functools import reduce
"""13. Encuentra el número mayor de una lista utilizando reduce.
"""
lista_numeros = [1, 5, 3, 6, 2, 10]
mayor = reduce(lambda x, y: x if x > y else y, lista_numeros)
print(mayor)