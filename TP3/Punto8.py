"""Dada una lista con elementos duplicados, crea una nueva lista que 
contenga solo los elementos únicos utilizando list comprehensions."""

mi_lista = [1, 2, 2, 3, 4, 4, 5, 6, 6, 1]

#utilizo set para crear un set de elementos unicos desordenados, y luego los meto en una lista con list
#set te crea un conjunto de elementos
nueva_lista = list(set(mi_lista))

print(nueva_lista)

