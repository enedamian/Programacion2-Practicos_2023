# 3. Lee el contenido de un archivo de texto llamado "datos.txt" y crea una lista con todas las líneas del archivo, utilizando list comprehensions.
ruta = r"C:\Users\genar\OneDrive\Documentos\GitHub\Programacion2-Practicos\TP3\datos.txt"

def leerArchivo (ruta):
    archivo=open(ruta,'r') 
    listaNumeros = [linea.strip() for linea in archivo.readlines()]
    archivo.close()
    return print(listaNumeros)

leerArchivo(ruta)
