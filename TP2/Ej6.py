"""Escriba un programa que permita leer de un archivo distancias.txt (cada renglón
tiene una distancia válida) las distancias recorridas por el vehículo de una empresa,
luego calcular cual es la distancia promedio, y mostrar por pantalla el promedio y
todas las distancias mayores al promedio.
Ej del contenido del archivo:
150
120
50
34
250
Salida: “La distancia promedio de los viajes es … y los viajes con distancia mayor
son: … , … , …. , …. “
"""

def cargar_distancias(ruta):

    archivo = open(ruta, "r")
    distancias = []

    for linea in archivo:
        distancias.append(int(linea))
    
    archivo.close()

    return distancias

def calcular_promedio(distancias):
    total = sum(distancias)
    cantidad = len(distancias)
    promedio = total / cantidad
    
    return promedio

def distancias_mayores(distancias, promedio):
    distancias_mayores = []

    for distancia in distancias:
        if distancia > promedio:
            distancias_mayores.append(distancia)

    return distancias_mayores

ruta = "repo\Programacion2-Practicos\TP2\distancias.txt"
distancias = cargar_distancias(ruta)
promedio = calcular_promedio(distancias)
mayores = distancias_mayores(distancias, promedio)

print(f"La distancia promedio de los viajes es {promedio} y los viajes con distancia mayor son: {mayores}", end="")