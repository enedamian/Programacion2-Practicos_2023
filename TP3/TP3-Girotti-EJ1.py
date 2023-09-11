#EJ1:
def CuadradoElementos(lista):
    listaCuadrados = [valor**2 for valor in lista]
    return listaCuadrados

listaNumeros = [1,2,3,4,5,6,7,8,9,10]
print(CuadradoElementos(listaNumeros))