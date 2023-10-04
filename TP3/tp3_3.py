# 3. Lee el contenido de un archivo de texto llamado "datos.txt" 
#y crea una lista con todas las líneas del archivo, utilizando list comprehensions.
import os
def existe_archivo(ruta):
    if os.path.isfile(ruta):
        return True 
    else:
        return False
    
def crear_lista(ruta):
    if existe_archivo(ruta):
        archivo = open(ruta,"r",encoding="UTF-8")
        lista_nueva = [linea.strip(" \n").lower() for linea in archivo]
        archivo.close()
    return lista_nueva
nombre_de_archivo = input("Ingrese la ruta al archivo que desea analizar: ")
lista_palabras = crear_lista(nombre_de_archivo)
print(lista_palabras)
"""
for i in range(len(lista_palabras)):
    print(lista_palabras[i])
"""