"""Escriba un programa que permita ingresar un número, se debe validar que
realmente se haya ingresado un número, y crear una lista para almacenar por
separado los dígitos del número. Luego recorrer la lista y mostrar el índice que
contiene el dígito mayor"""

def leer_entero(mensaje:str)-> int:
    """Espera un ingreso de teclado y valida que sea un numero entero, en caso contrario sigue pidiendo el numero entero hasta que sea valido."""
    seguir_pidiendo = True
    while seguir_pidiendo:
        try:             
            numero = int(input(mensaje))
            seguir_pidiendo=False             
        except ValueError:
            print('Error, debe ingresar un numero entero.\nInténtelo nuevamente:')
    return numero

def separar_digitos(numero):
    lista = []
    str_nro = str(abs(numero))
    for digito in str_nro:
        lista.append(int(digito))
    return lista

def buscar_indice_mayor(lista):
    mayor = 0
    pos = 0   
    for i in range(0,len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
            pos = i
    return pos

def buscar_indice_mayor_con_MAX(lista):
    mayor = max(lista)
    return lista.index(mayor)

numero = leer_entero("Ingrese un numero: ")
lista_digitos = separar_digitos(numero)
pos = buscar_indice_mayor_con_MAX(lista_digitos)
print(f"El digito mayor es: {lista_digitos[pos]}, en la posición {pos} de la lista.")