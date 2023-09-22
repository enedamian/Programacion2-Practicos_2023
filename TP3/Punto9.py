""" Dadas dos listas de números del mismo tamaño, crea una nueva lista
que contenga la multiplicación de los elementos correspondientes de
ambas listas utilizando list comprehensions. """

""" import random
tamaño = 5
lista1 = [random.randint(1, 100) for _ in range(tamaño)]
lista2 = [random.randint(1, 100) for _ in range(tamaño)]
print("Lista 1:", lista1)
print("Lista 2:", lista2) """

Lista_1 = [88, 40, 26, 87, 96]
Lista_2 = [54, 73, 42, 55, 16]

lista_multiplicaciones = [a * b for a, b in zip(Lista_1, Lista_2)]

print(lista_multiplicaciones)