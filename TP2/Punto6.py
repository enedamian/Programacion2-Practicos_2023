""" Escriba un programa que permita leer de un archivo distancias.txt (cada renglón
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
son: … , … , …. , …. “ """

def leer_archivo():
   lista = list()
   try:
       archivo = open("C:\Archivos de código\programacion2\Programacion2-Practicos\TP2\distancias punto 6.txt", "r")
       lineas = archivo.readlines()
       for linea in lineas:
            lista.append(linea.strip())  # Agregamos strip() para eliminar caracteres de nueva línea
       archivo.close() 
   except:
        print("No se pudo abrir el archivo")    
   print(lista)
   return lista


def promedio_de_lista(lista):
    suma = 0
    for linea in lista:
        suma += float(linea)
    
    # Comprobación para evitar división por cero
    if len(lista) == 0:
        return 0
    
    return suma / len(lista)

def numeros_superan_promedio(lista, promedio):
    lista_superan = list()
    for linea in lista:
        if float(linea) > promedio:
            lista_superan.append(linea)
    return lista_superan

lista = leer_archivo()
promedio = promedio_de_lista(lista)
print(f"La distancia promedio de los viajes es {promedio} y los viajes con distancia mayor son: {numeros_superan_promedio(lista, promedio)}")
