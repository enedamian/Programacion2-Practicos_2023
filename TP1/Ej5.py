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