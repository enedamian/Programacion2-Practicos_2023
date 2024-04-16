with open("TP3/datos.txt", "r") as archivo:
    datos=[linea.strip() for linea in archivo ]

print(datos)