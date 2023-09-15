def Multiplicacion(lista1, lista2):
    listaResultado = [valor1 * valor2 for valor1, valor2 in zip(lista1,lista2)]
    return listaResultado

lista_1 = [1,2,3,4,5]
lista_2 = [1,2,3,4,5]

print(Multiplicacion(lista_1, lista_2))