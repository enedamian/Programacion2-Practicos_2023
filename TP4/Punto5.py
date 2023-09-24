""" Ordenar una lista de diccionarios por un elemento del diccionario.
ej: ordenar por edad la siguiente lista: """

personas = [{'nombre': 'Hector', 'edad': 27}, 
            {'nombre': 'Juan', 'edad': 18}, 
            {'nombre': 'Maria', 'edad': 32}, 
            {'nombre': 'Pedro', 'edad': 21}, 
            {'nombre': 'Ana', 'edad': 20}]

personas_ordenadas = sorted(personas, key=lambda x: x['edad'])
print(personas_ordenadas)