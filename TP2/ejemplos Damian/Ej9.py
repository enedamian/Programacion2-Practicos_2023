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
def calcular_promedio(notas):
    return sum(notas) / len(notas)

def cargar_alumnos():
    ruta_alumnos = r"c:\Programacion2\alumnos.txt"
    # Leer datos de alumnos y notas desde el archivo alumnos.txt
    alumnos = []
    with open(ruta_alumnos, 'r') as archivo:
        for linea in archivo:
            datos = linea.strip().split(';')
            numero_inscripcion = int(datos[0])
            notas=[]
            for nota in datos[1:]: 
                notas.append(int(nota))
            promedio = calcular_promedio(notas)
            alumnos.append({"numero_inscripcion":numero_inscripcion, "promedio":promedio})
    return alumnos

def cargar_nombres():
    # Leer datos de nombres y apellidos desde el archivo ordenado alfabéticamente
    ruta_nombres = r"c:\Programacion2\nombres_apellidos.txt"
    nombres_apellidos = []
    with open(ruta_nombres, 'r') as archivo:
        for linea in archivo:
            datos = linea.split(';')
            numero_inscripcion = int(datos[0])
            apellido = datos[1]
            nombre = datos[2]
            nombres_apellidos.append({"numero_inscripcion":numero_inscripcion,"apellido":apellido, "nombre":nombre} )
    return nombres_apellidos

# Calcular y escribir en Promoción.txt los alumnos que promocionan
ruta_promocion = r"c:\Programacion2\promocion.txt"
promocionados = []
alumnos = cargar_alumnos()
nombres_apellidos = cargar_nombres()
for alumno in alumnos:
    if alumno["promedio"] > 7:
        for nombre in nombres_apellidos:
            if alumno["numero_inscripcion"] == nombre["numero_inscripcion"]:
                promocionados.append(str(nombre["numero_inscripcion"]) + ";" + nombre["apellido"] + ", " + nombre["nombre"])

promocionados.sort()  # Ordenar alfabéticamente por apellido y nombre

with open(ruta_promocion, 'w') as archivo_promocion:
    for elemento in promocionados:
        archivo_promocion.write(f"{elemento}\n")