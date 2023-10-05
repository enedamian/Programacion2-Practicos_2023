import random
from functools import reduce

def generar_listas():
    longitud_lista_1, longitud_lista_2 = random.randint(20, 50), random.randint(20, 50)
    lista_1 = [random.randint(200, 5000) for _ in range(longitud_lista_1)]
    lista_2 = [random.randint(200, 5000) for _ in range(longitud_lista_2)]

    return lista_1, lista_2

def impares(lista):
    impares = list(filter(lambda x: x % 2 == 0, lista))
    return impares

def valor_minimo(lista):
    return reduce(lambda x, y: x if x < y else y, lista)

def generar_sublista(lista_1, lista_2):
    valor_min = valor_minimo(lista_2)
    producto = [valor_min * impar for impar in lista_1]
    return producto

def es_primo(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generar_lista_primos(lista):  
    return [num for num in lista if es_primo(num)]

def devolver(lista):
    if valor_minimo(lista):
        return lista
    else:
        return -1

lista_1, lista_2 = generar_listas()
print("lista 1: ", lista_1)
print("")
print("lista_2: ", lista_2)
lista_impares = impares(lista_1)
print("lista impares: ", lista_impares)
print("")
valor_min = valor_minimo(lista_2)
print("valor mínimo: ", valor_min)
print("")
sublista = generar_sublista(lista_1, lista_2)
print("sublista: ", sublista)
print("")
lista_primos = generar_lista_primos(lista_2)
print("lista de números primos: ", lista_primos)
print("")
print("Menor número primo: ", valor_minimo(lista_primos))