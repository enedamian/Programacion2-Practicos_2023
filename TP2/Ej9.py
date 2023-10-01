"""Un profesor almacenó los datos de los alumnos de su materia en un archivo
alumnos.txt. En cada línea guardó el número de inscripción del alumno y sus tres
notas finales (oral, escrito y trabajos prácticos). El archivo está ordenado por número
de inscripción.
En otro archivo, ordenado alfabéticamente por apellido, guarda por línea, número de
inscripción, apellido y nombre de cada uno.
Desea escribir un programa para generar un archivo Promoción.txt con los apellidos
y nombres de los alumnos que promocionan la materia, esto es, alumnos que el
promedio de las tres notas supere los 7 puntos.
El archivo debe quedar ordenado alfabéticamente
"""

# mi solucion:

def cargar_alumnos(ruta):
    archivo = open(ruta, "r")
    lista_alumnos = []

    for linea in archivo:
        datos = linea.split(",")



def calcular_promedio(notas):
    sumatoria = 0
    for nota in notas:
        sumatoria += int(nota)
    promedio = sumatoria / len(notas)
    
    return promedio