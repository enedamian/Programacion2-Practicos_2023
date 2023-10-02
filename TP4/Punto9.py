"""9. Dada una lista de palabras, utiliza la función sorted con una función lambda para ordenar 
la lista de acuerdo a la longitud de las palabras.
"""

palabras = ["casa", "perro", "gato", "computadora"]
palabras_ordenadas = list(sorted(palabras, key=lambda palabra: len(palabra)))
print(palabras_ordenadas)