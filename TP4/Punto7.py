""" Dada una lista con números, filtrar los números pares 
y devolverlos en una nueva lista. """

mi_lista = [1, 11, 20, 30, 41, 50, 69, 70, 80, 90]

lista_pares = list(filter(lambda x: x%2==0, mi_lista))
print(lista_pares)