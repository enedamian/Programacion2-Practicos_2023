diccionario = {
    "manzana": "una fruta roja",
    "banana": "una fruta amarilla",
    "pera": "una fruta verde",
    "uva": "una fruta morada",
    "naranja": "una fruta naranja"
}
letra_inicial = input("Introduce la letra inicial: ").lower()  # Pide al usuario la letra inicial y la convierte a minúsculas

palabras_con_letra_inicial = [palabra for palabra in diccionario.keys() if palabra.startswith(letra_inicial)]

print("Palabras que comienzan con la letra '{}':".format(letra_inicial))
for palabra in palabras_con_letra_inicial:
    print(palabra)
