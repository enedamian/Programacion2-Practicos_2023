lista_dic = [{'nombre': 'Hector', 'nota': 70}, {'nombre': 'Juan', 'nota': 45}, {'nombre': 'Maria', 'nota': 75}, {'nombre': 'Pedro', 'nota': 80}, {'nombre': 'Ana', 'nota': 60},  {'nombre': 'Florencia', 'nota': 95}]

aprobados = filter(lambda x: x['nota'] >= 70, lista_dic)

for alumno in aprobados:
    print(f"Nombre: {alumno['nombre']} - Nota: {alumno['nota']}")