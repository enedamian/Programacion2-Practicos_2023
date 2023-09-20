def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vocales:
            contador += 1
    return contador

texto_ingresado = input("Ingrese un texto: ")
cantidad_vocales = contar_vocales(texto_ingresado)
print("La cantidad total de vocales en el texto es:", cantidad_vocales)