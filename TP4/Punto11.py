""" Dada una lista de diccionarios con los alumnos y notas de un curso,
calcular el promedio del curso. Puede usar una lista como la siguiente: 
 """
lista_dic = [{'nombre': 'Hector', 'nota': 70},
             {'nombre': 'Juan', 'nota': 45},
             {'nombre': 'Maria', 'nota': 75},
             {'nombre': 'Pedro', 'nota': 80}, 
             {'nombre': 'Ana', 'nota': 60},  
             {'nombre': 'Florencia', 'nota': 95}]

#usando reduce
""" from functools import reduce

# Función para calcular el promedio
def calcular_promedio(acumulador, elemento):
    acumulador['suma'] += elemento['nota']
    acumulador['contador'] += 1
    return acumulador

# Inicializar el acumulador
acumulador_inicial = {'suma': 0, 'contador': 0}

# Usar reduce para calcular el promedio
resultado_acumulado = reduce(calcular_promedio, lista_dic, acumulador_inicial)

# Calcular el promedio final
promedio = resultado_acumulado['suma'] / resultado_acumulado['contador']

print(promedio) """

#otra forma

# Calcular la suma de todas las notas
suma_notas = sum(alumno['nota'] for alumno in lista_dic)

# Calcular el promedio
promedio = suma_notas / len(lista_dic)

print("El promedio del curso es:", "{:.2f}".format(promedio))