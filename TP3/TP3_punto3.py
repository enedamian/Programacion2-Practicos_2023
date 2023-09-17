
with open("datos.txt", "r") as archivo:
    # se abre el archivo archivito.txt en modo lectura, y se le asigna un nombre a la variable que representa al archivo
    lineas = [linea.strip() for linea in archivo]
    # crea una lista con cada renglon del archivo quitandole los espacios inecesarios  con strip

