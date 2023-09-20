""" Dado un rango de números, crea una lista que contenga todos 
los números primos dentro de ese rango utilizando list comprehensions. """

def leer_entero_positivo(mensaje):
    pedir = True
    while pedir:
        try:
            valor = int(input(mensaje))
            pedir = False
        except:
            print("El valor ingresado tiene que ser un entero positivo.")
    return valor

def es_primo(numero):
    if numero == 1:
        return False
    else:
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
    return True

menor = leer_entero_positivo("Ingrese el numero mas bajo: ")
mayor = leer_entero_positivo("Ingrese el numero mas alto: ")

lista_primos = [numero for numero in range(menor, mayor) if es_primo(numero)]
print(lista_primos)