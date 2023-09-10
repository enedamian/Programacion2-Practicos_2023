# Lee el contenido de un archivo de texto llamado "datos.txt" y crea una lista con todas las líneas del archivo, utilizando list comprehensions.

import os


def crear_lista_con_lineas():
    """Crea una lista con las líneas del archivo datos.txt

    Returns:
        list: lista con las líneas del archivo
    """
    path = "datos.txt"
    if not(os.path.isfile(path)):
        print("El archivo no existe")
        return []

    with open(path, 'r') as archivo:
        lineas = [linea for linea in archivo]
    return lineas