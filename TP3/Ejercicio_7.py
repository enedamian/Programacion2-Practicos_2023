def validar(palabra):
    if " " in palabra:
        return False
    return True

def contar_vocales(palabra):
    vocales = 'aeiou'
    cantidad_vocales = len([char for char in palabra.lower() if char in vocales])
    return cantidad_vocales

def iterar(mensaje):
    palabra = input(mensaje).lower()
    while palabra != 'salir':
        cantidad_vocales = contar_vocales(palabra)
        print(f"la palabra {palabra} tiene {cantidad_vocales} vocales.")
        palabra = input("Ingrese otra palabra ('salir' para terminar el loop):\n").lower()

palabra = input("ingrese una palabra (o 'salir' para terminar):\n")
iterar(palabra)

