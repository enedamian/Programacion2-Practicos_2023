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
       archivo = open("distancias punto 6.txt","r")
       lineas = archivo.readlines()
       for linea in archivo:
            lista.append(linea)
       archivo.close() 
   except:
        print("No se pudo abrir el archivo")    
   
   return lista
   
def promedio_de_lista(lista):
    suma = 0
    cantidad = 0
    for linea in lista:
        suma += float(linea)
        cantidad += 1
    return suma / cantidad
    

def numeros_superan_promedio(lista,promedio):
    lista_superan = list()
    for linea in lista:
        if float(linea) > promedio:
            lista_superan.append(linea)
    return lista_superan

lista = leer_archivo()
promedio = promedio_de_lista(lista)
print(f"La distancia promedio de los viaes es {promedio} y los vias con distancia mayor son: {numeros_superan_promedio(lista,promedio)}")
#print(promedio_de_lista())