def Duplicados(lista):
    lista_unica = [elemento for elemento in lista if lista.count(elemento) == 1]
    return lista_unica

lista = [2,2,2,3,4,5,6,5,7,8,9,9,10]
print(Duplicados(lista))