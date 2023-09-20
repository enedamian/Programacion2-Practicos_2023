def contar_letras(texto):
    contador = 0
    for caracter in texto:
        if caracter.isalpha():
            contador += 1
    return contador
def contar_palabras(texto):
    cant_palabras = texto.split()
    return len(cant_palabras)
def total_caracteres(texto):
    total = len(texto)
    return total

texto = input("Ingrese una oracion: ")
cantidad_letras = contar_letras(texto)
cantidad_palabras = contar_palabras(texto)
cantidad_caracteres = total_caracteres(texto)

print(f"El numero total de caracteres en la oracion es de: {cantidad_caracteres}.")
print(f"La cantidad total de letras es de: {cantidad_letras}")
print(f"La cantidad de palabras separadas por uno o mas espacios es de: {cantidad_palabras}")