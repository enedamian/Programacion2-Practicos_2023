#5. Ordenar una lista de diccionarios por un elemento del diccionario. 
#ej: ordenar por edad la siguiente lista: 
"""
personas = [{'nombre': 'Hector', 'edad': 27}, {'nombre': 'Juan', 'edad': 18}, 
{'nombre': 'Maria', 'edad': 32}, {'nombre': 'Pedro', 'edad': 21}, {'nombre': 'Ana', 'edad': 20}]
"""
personas = [
    {'nombre': 'Hector', 'edad': 27},
    {'nombre': 'Juan', 'edad': 18},
    {'nombre': 'Maria', 'edad': 32},
    {'nombre': 'Pedro', 'edad': 21},
    {'nombre': 'Ana', 'edad': 20}
]
personas_ordenadas = lambda persona: persona["edad"]
lista_personas_ordenadas = sorted(personas,key=personas_ordenadas)
print(lista_personas_ordenadas)