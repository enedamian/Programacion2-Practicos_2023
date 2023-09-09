"""
Escriba un programa que permita cargar las notas de exámenes, primero debe
permitir ingresar por teclado la cantidad de notas que desea cargar, y luego
cargarlas en una lista, y posteriormente debe buscar la nota más alta, mostrarla, e
indicar en qué índice del arreglo se encuentra.
"""
def leer_entero_positivo(mensaje):
    """Espera un ingreso de teclado y valida que sea un numero entero positivo, en caso contrario sigue pidiendo el numero hasta que sea valido."""
    seguir_pidiendo = True
    while seguir_pidiendo:
        try:             
            numero = int(input(mensaje))
            if numero >= 0:
                seguir_pidiendo=False             
            else:
                print("El numero ingresado no es válido. Debe ingresar un numero positivo.")
        except ValueError:
            print('Error, debe ingresar un numero entero positivo.\nInténtelo nuevamente:')
    return numero

def leer_notas(cantidad):
    lista_notas = []
    for i in range(0, cantidad):
        lista_notas.append(leer_entero_positivo(f"Ingrese la nota N° {i+1}: "))
    return lista_notas

def buscar_indice_nota_mayor(lista):
    mayor = 0
    pos = 0 
    for i in range(0,len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
            pos = i
    return pos

# definicion alternativa de la búsqueda:
def buscar_indice_mayor_con_MAX(lista):
    mayor = max(lista)
    return lista.index(mayor)

cantidad = leer_entero_positivo("Ingrese la cantidad de notas que desea cargar: ")
lista_notas = leer_notas(cantidad)
indice_nota_mayor = buscar_indice_nota_mayor(lista_notas)
print(f"La nota mayor es {lista_notas[indice_nota_mayor]} en el índice {indice_nota_mayor} de la lista, y fua la nota N° {indice_nota_mayor+1}.")

