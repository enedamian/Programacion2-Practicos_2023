"""Dadas dos listas de números del mismo tamaño, crea una nueva lista que contenga la 
multiplicación de los elementos correspondientes de ambas listas utilizando list comprehensions."""

lista1 = [1,2,3,4,5,6,7,8,9]
lista2 = [9,8,7,6,5,4,3,2,1]

#zip combina los elementos de la lista 1 y la lista 2 en tuplas
lista_nueva = [a * b for a,b in zip(lista1, lista2)]

print(lista_nueva)