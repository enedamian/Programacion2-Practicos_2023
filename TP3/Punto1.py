"""1. Implemente una función que dada una lista de números, 
devuelva una nueva lista que contenga el cuadrado de cada número utilizando list comprehensions."""
def cuadrados(lista):
    lista = [numero**2 for numero in listanumeros]
    return lista

listanumeros = [1, 2, 3, 4, 5, 6]
listacuadrados = cuadrados(listanumeros)
print(listacuadrados)