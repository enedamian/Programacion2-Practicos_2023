from functools import reduce

lista_strings = ['hola', 'mundo']

concatenar = reduce(lambda x, y: x + y, lista_strings)
print(concatenar)