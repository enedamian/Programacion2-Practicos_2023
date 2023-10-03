from functools import reduce
lista_dic = [{'nombre': 'Hector', 'nota': 70}, {'nombre': 'Juan', 'nota': 45}, {'nombre': 'Maria', 'nota': 75}, {'nombre': 'Pedro', 'nota': 80}, {'nombre': 'Ana', 'nota': 60},  {'nombre': 'Florencia', 'nota': 95}]

notas = list(map(lambda x : x['nota'], lista_dic))

# solucion con map:
suma = 0
for nota in notas:
    suma += nota

promedio_curso = suma / len(lista_dic)
print(promedio_curso)

# solucion con reduce:
suma_notas = reduce(lambda x, y: x + y['nota'], lista_dic, 0)
promedio = suma_notas / len(lista_dic)
print(promedio)