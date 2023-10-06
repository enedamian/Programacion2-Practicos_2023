# 1. Implemente una función que dada una lista de números, devuelva una nueva lista que contenga el cuadrado de cada número utilizando list comprehensions.

lista = [8,4,4,6,9,7,9]

def listaAlCuadrado(lista):
    listaCuadrada = [x*x for x in lista]
    return print(listaCuadrada)

print(listaAlCuadrado(lista))