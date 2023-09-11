"""Dado un diccionario de palabras y sus definiciones, crea una lista que contenga sólo las 
palabras que comienzan con una letra específica (por ejemplo, "a") indicada por el usuario, 
utilizando list comprehensions."""

# Diccionario de palabras y definiciones
diccionario = {
    'manzana': 'Una fruta roja o verde que crece en los árboles.',
    'banana': 'Una fruta amarilla y alargada que crece en plátanos.',
    'perro': 'Un animal doméstico que suele ser leal y compañero del hombre.',
    'gato': 'Un animal doméstico que suele ser independiente y cariñoso.',
    'abeja': 'Un insecto volador que produce miel y poliniza las flores.'
}

# Letra específica proporcionada por el usuario
letra_inicial = input("Ingrese una letra para filtrar palabras: ")

# Usar list comprehension para crear la lista de palabras que comienzan con la letra proporcionada
#keys te da las parametros que estan dentro de los diccionarios
#startswith te la la letra con la que inicia el parametro
palabras_con_letra = [palabra for palabra in diccionario.keys() if palabra.startswith(letra_inicial.lower())]

# Imprimir la lista de palabras resultante
print(f"Palabras que comienzan con '{letra_inicial}': {palabras_con_letra}")
