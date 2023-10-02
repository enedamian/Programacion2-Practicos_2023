lista = [1, 2, 3, 2, 10, 2]

def eliminar_repetidos(lista):
    nueva_lista = []
    [nueva_lista.append(num) for num in lista if num not in nueva_lista]
    return nueva_lista

lista_sin_repetir = eliminar_repetidos(lista)
print(lista_sin_repetir)