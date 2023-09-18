Personas = [{'nombre': 'Hector', 'edad': 27}, {'nombre': 'Juan', 'edad': 18}, 
 {'nombre': 'Maria', 'edad': 32}, {'nombre': 'Pedro', 'edad': 21}, 
 {'nombre': 'Ana', 'edad': 20}]

ordenar_lista_dicc = lambda x: x['edad']

print(sorted(Personas, key=ordenar_lista_dicc))