# 5. Ordenar una lista de diccionarios por un elemento del diccionario. ej: ordenar por edad la siguiente lista: 
# ```python
# personas = [{'nombre': 'Hector', 'edad': 27}, {'nombre': 'Juan', 'edad': 18}, {'nombre': 'Maria', 'edad': 32}, {'nombre': 'Pedro', 'edad': 21}, {'nombre': 'Ana', 'edad': 20}]
# ```

# Lista de diccionarios
personas = [{'nombre': 'Hector', 'edad': 27}, {'nombre': 'Juan', 'edad': 18}, {'nombre': 'Maria', 'edad': 32}, {'nombre': 'Pedro', 'edad': 21}, {'nombre': 'Ana', 'edad': 20}]

# Ordenar la lista de personas por la clave 'edad'
personas_ordenadas = sorted(personas, key=lambda x: x['edad'])

# Imprimir la lista ordenada
for persona in personas_ordenadas:
    print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}")
