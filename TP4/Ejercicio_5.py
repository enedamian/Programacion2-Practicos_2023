personas = [{'nombre': 'Hector', 'edad': 27}, {'nombre': 'Juan', 'edad': 18}, {'nombre': 'Maria', 'edad': 32}, {'nombre': 'Pedro', 'edad': 21}, {'nombre': 'Ana', 'edad': 20}]

ordenar_por_edad = sorted(personas, key = lambda x: x['nombre'])

for persona in ordenar_por_edad:
    print(persona)