from functools import reduce
lista=['Hola','como','estas','vos']

resultado = reduce(lambda x, y: x + y, lista)

print(resultado)