def contarElementos(lista):
    listacount = [elemento for elemento in lista if elemento.count() == 1]
    return listacount


lista = []
while True:
    elemento = input(
        "Ingrese un elemento para la lista (vacío para terminar): ")
    if elemento == "":
        break
    lista.append(elemento)
print("Lista original:" + lista)
print("Elementos únicos:" + contarElementos(lista))
