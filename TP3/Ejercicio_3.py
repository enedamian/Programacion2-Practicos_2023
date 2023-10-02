def crear_lista(ruta):
    archivo = open(ruta, "r")
    contenido = archivo.read()
    return [linea for linea in contenido.split("\n")]

ruta = "datos.txt"
print(crear_lista(ruta))