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