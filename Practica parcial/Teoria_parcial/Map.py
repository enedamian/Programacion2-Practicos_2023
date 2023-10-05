#map(función, iterable)
#Le aplica una funcion a cada elemento del iterable, que puede ser una lista

# Definir una función que eleve un número al cuadrado
def cuadrado(x):
    return x ** 2

# Crear una lista de números
numeros = [1, 2, 3, 4, 5]

# Aplicar la función cuadrado a cada elemento de la lista usando map()
resultados = list(map(cuadrado, numeros))

print(resultados)  # Salida: [1, 4, 9, 16, 25]
