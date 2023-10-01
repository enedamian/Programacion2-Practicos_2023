"""Escriba un programa que permita ingresar un número, se debe validar que
realmente se haya ingresado un número, y crear una lista para almacenar por
separado los dígitos del número. Luego recorrer la lista y mostrar el índice que
contiene el dígito mayor"""

#Mi solucion:

def validacion():

    repetir = True

    while repetir:
        try:
            numero = int(input("Ingrese un número entero positivo: "))

            if numero > 0:
                repetir = False
            else:
                print("Ingrese un número mayor a 0")
                numero = int(input("Ingrese un número: "))

        except ValueError:
            print("Debe ingresar un número entero positivo.\nIntentar nuevamente: ")

    return numero;
   
def almacenar_lista():
    lista = []

    numero = validacion()

    while numero != 0:
        digito = numero % 10
        lista.insert(0, digito)
        numero = numero // 10

    return lista

def indice_mayor(lista):
    max = lista[0]

    for numero in lista:
        if numero > max:
            max = numero
    return max

lista = almacenar_lista()
print(lista)

print(f"El digito mayor se encuentra en el indice {lista.index(indice_mayor(lista))}")
