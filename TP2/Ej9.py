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

def validacion(mensaje):
    repetir = True
    try:
        while repetir:
            numero = int(input(mensaje))
            if numero >= 0:
                repetir = False
            else:
                print("El número ingresado debe ser mayor a 0\nIngrese un número entero positivo: ")
    except ValueError:
        print("Debe ingresar un número entero positivo")
    return numero


def cargar_alumnos(ruta):
    archivo = open(ruta, "r")
    lista_alumnos = []

    for linea in archivo:
        datos = linea.split(",")
        alumnos = {
            "numero_inscripcion": datos[0],
            "notas": [validacion(datos[1]), validacion(datos[2]), validacion(datos[3])],
            "promocion": calcular_promedio("notas")
        }
        notas = []

        for nota in alumnos['notas']:
            notas.append(validacion(nota))

        lista_alumnos.append(alumnos)    
    return lista_alumnos


def cargar_nombres(ruta):
    archivo = open(ruta, "r")
    lista_nombres = []
    for linea in archivo:
        datos = linea.split(',')

        nombres_alumnos = {
            "numero_inscripcion": int(datos[0]),
            "nombre": datos[1],
            "apellido": datos[2]
        }
        lista_nombres.append(nombres_alumnos)
    return lista_nombres

def calcular_promedio(notas):
    sumatoria = 0
    for nota in notas:
        sumatoria += int(nota)
    promedio = sumatoria / len(notas)    
    return promedio

def generar_promocion(lista_alumnos, lista_nombres):
    ruta_promocion = r"repo\Programacion2-Practicos\TP2\Promocion.txt"
    lista_promocion = []
    promedio = calcular_promedio()

    for alumno in lista_alumnos:
        for nombre in lista_nombres:
            if alumno["numero_inscripcion"] == nombre["numero_inscripcion"] and promedio > 7:
                lista_promocion.append(alumno)

    archivo_promocion = open(ruta_promocion, "w")
    for alumno in lista_promocion:
        archivo_promocion.write(f"{alumno['numero_inscripcion']};{alumno['nombre']};{alumno['apellido']}\n")
    lista_promocion.sort()

ruta_alumnos = "alumnos.txt"
ruta_nombres = "nombres.txt"

lista_alumnos = cargar_alumnos(ruta_alumnos)
lista_nombres = cargar_nombres(ruta_nombres)
generar_promocion(lista_alumnos, lista_nombres)