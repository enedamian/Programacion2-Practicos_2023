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

def calcular_promedio(lista):
    return sum(lista)/len(lista)

def cargar_distancias():
    ruta = r"c:\Programacion2\distancias.txt"
    archivo = open(ruta, 'r')
    lista_distancias=[]
    for linea in archivo:
        lista_distancias.append(int(linea))
    archivo.close() # recordar cerrar el archivo cuando terminan de utilizarlo (otra forma segura de utilizar archivos es con la sentencia with)
    return lista_distancias

def buscar_distancias_mayores(referencia, lista):
    mayores=[]
    for distancia in lista:
        if distancia>referencia:
            mayores.append(distancia)
    return mayores


lista = cargar_distancias()
promedio = calcular_promedio(lista)
mayores = buscar_distancias_mayores(promedio, lista)
print(f"La distancia promedio de los viajes es {promedio} y los viajes con distancia mayor son: {mayores}")