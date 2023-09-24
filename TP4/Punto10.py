""" Dada una lista de palabras, generar una lista con las 
iniciales de cada palabra. """

palabras = ["manzana", "perro", "gato", "computadora", "sol", "ratón", "flor", "casa", "hoja", "lápiz"]

#usando list comprehensions
def buscar_iniciales(palabra):
    return palabra[0]

iniciales = [buscar_iniciales(palabra) for palabra in palabras]
print(iniciales)


#usando map
iniciales = list(map(lambda palabra: palabra[0], palabras))
print(iniciales)