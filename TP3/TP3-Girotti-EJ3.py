#EJ3:
archivo = "TP3/texto-ej3.txt"

def LecturaArchivo(archivo):
    lector = open(archivo, "r")
    listaLineas = [linea.strip() for linea in lector]
    return listaLineas

print(LecturaArchivo(archivo))