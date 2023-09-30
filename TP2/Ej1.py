"""Escribir un procedimiento “reverso” que permita ingresar como parámetro una
cadena, y devuelva la cadena invertida (“hola” se convierte en “aloh”). Escribir luego
un programa que determine si una cadena de caracteres es un palíndromo (un
palíndromo es un texto que se lee igual en sentido directo y en inverso, ej.: “radar”).
Sugerencia: para evitar diferencias entre mayúsculas y minúsculas en las cadenas,
utilice la función del tipo string .upper() ó .lower() en las cadenas, ya que Radar es
distinto a radaR"""

# from funciones_tp2 import reverso

def reverso(texto):
    ultPos = len(texto) - 1
    reverso = ""
    for i in range(ultPos,-1,-1):
        reverso += texto[i]
    return reverso

cadena = input("Ingrese un texto: ")
cadena = cadena.lower()
cadena_invertida = reverso(cadena)
if cadena == cadena_invertida:
    print(f"{cadena} es palíndromo.")
else:
    print(f"{cadena} NO es palíndromo.")

# Mi solucion:

def reverso(cadena):
    
    nueva_cadena = ""

    for letra in cadena:
        nueva_cadena = letra + nueva_cadena
    
    return nueva_cadena

def es_palindromo(cadena):
    palindromo = True;

    segunda_cadena = reverso(cadena)

    if cadena == segunda_cadena:
        return palindromo

cadena = input("Ingrese un string:\n")
nueva_cadena = cadena.lower()

cadena_reverso = reverso(nueva_cadena)
print(cadena_reverso)

if es_palindromo(nueva_cadena):
    print(f"{nueva_cadena} es un palindromo")
else:
    print(f" {nueva_cadena} no es un palindromo")


