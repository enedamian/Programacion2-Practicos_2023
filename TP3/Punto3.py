"""3. Lee el contenido de un archivo de texto llamado "datos.txt" y 
crea una lista con todas las líneas del archivo, utilizando list comprehensions."""
with open("TP3/datos.txt", "r") as archivo:
    #strip le quita los espacios a la linea
    lineas = [linea.strip() for linea in archivo]

print(lineas)
