square = lambda x: x ** 2

"""
def validar(mensaje):
    repetir = True
    while repetir:
        try:
            numero = int(input(mensaje))
            if numero >= 0:
                repetir = False
            else:
                print("El numero debe ser positivo.")
        except ValueError:
            print("Debe ingresar un numero entero positivo. Reingrese:\n")
    return numero
"""
validar = lambda mensaje: int(input(mensaje)) if (lambda x: x >= 0)(int(input(mensaje))) else validar("El numero debe ser positivo. Reingrese:\n")

num = validar("ingrese un numero: ")
print(f"El cuadrado de {num} es {square(num)}") 