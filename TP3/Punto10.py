""" Dada una lista de números, crea dos listas separadas:
una que contenga los números pares y otra que contenga los 
números impares utilizando list comprehensions. """

""" import random
tamaño = 15
lista_numeros = [random.randint(1, 100) for _ in range(tamaño)]
print(lista_numeros) """

lista_numeros = [95, 68, 17, 91, 42, 95, 13, 14, 43, 87, 3, 99, 61, 45, 62]

lista_impares = [numero for numero in lista_numeros if numero%2 != 0]
lista_pares = [numero for numero in lista_numeros if numero%2 == 0]

print(f"Lista impares: {lista_impares}")
print(f"Lista pares: {lista_pares}")