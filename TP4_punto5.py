personas = [{'nombre': 'Hector', 'edad': 27}, {'nombre': 'Juan', 'edad': 18}, {'nombre': 'Maria', 'edad': 32}, {'nombre': 'Pedro', 'edad': 21}, {'nombre': 'Ana', 'edad': 20}]

peronasOrdenadas = sorted(personas, key=lambda x: x['edad'], reverse=False)

print(peronasOrdenadas)