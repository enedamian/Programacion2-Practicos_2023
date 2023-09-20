""" Escriba un programa que permita cargar las notas de exámenes, primero debe
permitir ingresar por teclado la cantidad de notas que desea cargar, y luego
cargarlas en una lista, y posteriormente debe buscar la nota más alta, mostrarla, e
indicar en qué índice del arreglo se encuentra. """

cantidad = int(input("Ingrese la cantidad de notas que desea cargar: "))
notas = [cantidad]
mas_alta = 0
indice = 0

for i in range(cantidad):
    notas.append(float(input("Ingrese la nota: ")))
    if(notas[i] > mas_alta):
        mas_alta = notas[i]
        indice = i
print(f"La nota mas altas es {mas_alta} y se encuentra en la posicion {indice} del arreglo.")