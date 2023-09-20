def buscar_palabra(texto):
    palabras = texto.split()
    mas_larga = palabras[0]
    for palabra in palabras:
        if len(palabra) > len(mas_larga):
            mas_larga = palabra
    return mas_larga

texto = input("Ingrese una oracion: ")
palabra_mas_larga = buscar_palabra(texto)
cantidad_letras = len(palabra_mas_larga)
print(f"La palabra más larga del texto es '{palabra_mas_larga}' y contiene {cantidad_letras} letras")
