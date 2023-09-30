"""Dada una cadena de texto ingresada por consola, decir cuántos “espacios” contiene."""

# solucion con FOR (la idea del ejercicio era practicar un ciclo)
cadena = input("Ingresá un texto: ")
contador = 0
for car in cadena:
    if car == " ":
        contador += 1
print(f"La cantidad de espacios es: {contador}")

#-----------------------------------------------------------
# soluciones mejoradas:

# Mi solucion:

def contar_espacio(cadena):
    i = 0

    for caracter in cadena:
        if caracter == " ":
            i += 1
    
    return i

cadena = input("Ingrese un string:\n") 
cant_espacios = contar_espacio(cadena)
print(f"\nEl string tiene {cant_espacios} espacios.")