#sorted(iterable, key=None, reverse=False)
#iterable es la lista
#key es de que forma queres que los ordene
#reverse es si los ordena de mayor a menor o viceversa

def orden_numeros():
    numeros = [4, 2, 8, 1, 6, 3]
    # Ordenar la lista de números en orden ascendente
    numeros_ordenados = sorted(numeros)
    print(numeros_ordenados)  # Salida: [1, 2, 3, 4, 6, 8]

def orden_alfabetico():
    palabras = ["manzana", "banana", "kiwi", "uva", "pera"]
    # Ordenar la lista de palabras en orden alfabético
    palabras_ordenadas = sorted(palabras)
    print(palabras_ordenadas)  # Salida: ['banana', 'kiwi', 'manzana', 'pera', 'uva']

def orden_descendiente():
    numeros = [4, 2, 8, 1, 6, 3]
    numeros_descendentes = sorted(numeros, reverse=True)
    print(numeros_descendentes)  # Salida: [8, 6, 4, 3, 2, 1]

def orden_por_longitud():
    palabras = ["manzana", "banana", "kiwi", "uva", "pera"]
    # Ordenar la lista de palabras por longitud
    palabras_ordenadas_por_longitud = sorted(palabras, key=len)
    print(palabras_ordenadas_por_longitud)  # Salida: ['kiwi', 'uva', 'pera', 'banana', 'manzana']

def orden_ultima_letra():
    palabras = ["manzana", "banana", "kiwi", "uva", "pera"]
    # Ordenar la lista de palabras por la última letra de cada palabra
    palabras_ordenadas_por_ultima_letra = sorted(palabras, key=lambda x: x[-1])
    print(palabras_ordenadas_por_ultima_letra)  
    # Salida: ['banana', 'kiwi', 'manzana', 'uva', 'pera']

def orden_segundo_elemento_tupla():
    tuplas = [(1, 5), (3, 2), (7, 8), (2, 4)]
    # Ordenar la lista de tuplas por el segundo elemento de cada tupla
    tuplas_ordenadas_por_segundo_elemento = sorted(tuplas, key=lambda x: x[1])
    print(tuplas_ordenadas_por_segundo_elemento)
    # Salida: [(3, 2), (2, 4), (1, 5), (7, 8)]


