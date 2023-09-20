""" Escriba un programa que permita ingresar un número, se debe validar que
realmente se haya ingresado un número, y crear una lista para almacenar por
separado los dígitos del número. Luego recorrer la lista y mostrar el índice que
contiene el dígito mayor. """

# Función para verificar si una cadena es un número
def es_numero(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False

# Solicitar al usuario ingresar un número hasta que se ingrese uno válido
numero = input("Ingresa un número: ")
while not es_numero(numero):
    numero = input("Ingresa un número válido: ")

# Convierte el número en una lista de dígitos
digitos = [int(digito) for digito in str(numero)]

# Encuentra el índice del dígito mayor
mayor = 0
aux = 0
for i in digitos:
    if (digitos[aux] > mayor):
        mayor = digitos[aux]
        aux += 1

# Imprime la lista de dígitos y el índice del dígito mayor
print("Lista de dígitos:", digitos)
print("El índice del dígito mayor es:", mayor)
