# 9. Dadas dos listas de números del mismo tamaño, crea una nueva lista que contenga la multiplicación de los elementos 

def multiplicar_listas(lista1, lista2):
    return [x * y for x, y in zip(lista1, lista2)]

# zip función en Python que combina dos listas en una sola lista de tuplas, donde cada tupla contiene un elemento de la lista1 y un elemento correspondiente de la lista2.