""" Dada una lista de palabras, utiliza la función sorted con una función
lambda para ordenar la lista de acuerdo a la longitud de las palabras. """

palabras = ["manzana", "perro", "gato", "computadora", "sol", "ratón", "flor", "casa", "hoja", "lápiz"]

palabras_ordenadas = (sorted(palabras, key=lambda x: len(x)))

print(palabras)
print(palabras_ordenadas)