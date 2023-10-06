# 14. Utilice reduce para concatenar una lista de cadenas en una sola cadena
from functools import reduce

cadenas = ['Hola', ' ', 'Mundo', ' ', 'Python']

def concatenar_cadenas(cadena1, cadena2):
    return cadena1 + cadena2

cadena_resultante = reduce(concatenar_cadenas, cadenas)

print(f"La cadena resultante es: {cadena_resultante}")
