""" Lee el contenido de un archivo de texto llamado "datos.txt" 
y crea una lista con todas las líneas del archivo, utilizando list comprehensions. """

def leer_archivo():
    ruta = "TP3\datos.txt"
    archivo = open(ruta, "r")
    #uso el .strip para que se elimine el caracter de salto de linea
    lista_lineas = [linea.strip() for linea in archivo]
    print(lista_lineas)
    archivo.close()

leer_archivo()