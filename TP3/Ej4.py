# 4. Dado un diccionario de palabras y sus definiciones, crea una lista que contenga sólo las palabras que comienzan con una letra específica (por ejemplo, "a") indicada por el usuario, utilizando list comprehensions.
diccionario_definiciones = {
    "Python": "Un lenguaje de programación de alto nivel conocido por su simplicidad y legibilidad de código.",
    "Diccionario": "Una estructura de datos que almacena pares clave-valor.",
    "Programación": "El proceso de escribir y diseñar programas de computadora.",
    "Algoritmo": "Un conjunto de pasos bien definidos y ordenados para resolver un problema o realizar una tarea.",
    "Variable": "Un espacio de almacenamiento nombrado utilizado para guardar datos en un programa."
}

letra="A"

def filtrarPorLetra (diccionario_definiciones, letra):
    filtrado= [nombre for nombre in diccionario_definiciones.keys() if nombre[0]==letra]
    return print(filtrado)

filtrarPorLetra (diccionario_definiciones, letra)