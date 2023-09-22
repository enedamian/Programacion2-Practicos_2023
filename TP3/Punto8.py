""" Dada una lista con elementos duplicados, crea una nueva lista que
contenga solo los elementos únicos utilizando list comprehensions. """

mi_lista = [1, 2, 2, 3, 4, 5, 4]

nueva_lista = []
#agregamos el numero a la nueva lista si este no existe ya.
[nueva_lista.append(numero) for numero in mi_lista if numero not in nueva_lista]
print(nueva_lista)