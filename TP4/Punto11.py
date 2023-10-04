lista_dic = [{'nombre': 'Hector', 'nota': 70}, {'nombre': 'Juan', 'nota': 45}, {'nombre': 'Maria', 'nota': 75}, {'nombre': 'Pedro', 'nota': 80}, {'nombre': 'Ana', 'nota': 60},  {'nombre': 'Florencia', 'nota': 95}]

notas = list(map(lambda x: x['nota'], lista_dic))

promedio= sum(notas)/len(notas)

print(f"El promedio de las notas es {promedio}")