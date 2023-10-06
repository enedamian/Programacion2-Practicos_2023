# 7. Implemente un programa que le pida una palabra al usuario y cuenta la cantidad de vocales en ella. El programa deberá pedirle palabras al usuario hasta que éste introduzca la palabra “salir”.

def contar_vocales(palabra):
    return sum(1 for letra in palabra if letra.lower() in 'aeiou')

while True:
    palabra = input("Ingrese una palabra (o escriba 'salir' para terminar): ")
    if palabra.lower() == "salir":
        break
    num_vocales = contar_vocales(palabra)
    print(f"La palabra '{palabra}' tiene {num_vocales} vocal(es).")
