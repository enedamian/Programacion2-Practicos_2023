"""5. Ordenar una lista de diccionarios por un elemento del diccionario. 
ej: ordenar por edad la siguiente lista: 
personas = [{'nombre': 'Hector', 'edad': 27}, {'nombre': 'Juan', 'edad': 18}, {'nombre': 'Maria', 'edad': 32}, {'nombre': 'Pedro', 'edad': 21}, {'nombre': 'Ana', 'edad': 20}]"""
personas = [{'nombre': 'Hector', 'edad': 27}, {'nombre': 'Juan', 'edad': 18}, {'nombre': 'Maria', 'edad': 32}, {'nombre': 'Pedro', 'edad': 21}, {'nombre': 'Ana', 'edad': 20}]

sorted_personas = sorted(personas, key=lambda diccionario: diccionario['edad'])
#la diferencian entre sorted y sort que es sorted crea una nueva lista
print(personas)