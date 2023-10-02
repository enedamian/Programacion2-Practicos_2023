lista_1 = [1, 2, 3, 4, 5]
lista_2 = [6, 7, 8, 9, 10]

def multiplicar(lista, otra_lista):
    return [lista[i] * otra_lista[i] for i in range(len(lista))]

nueva_lista = multiplicar(lista_1, lista_2)
print(nueva_lista)