lista_palabras = ['bueno', 'mundo', 'adios', 'hola']

iniciales = [palabra[0] for palabra in lista_palabras]
print(iniciales)

# solucion usando map:
iniciales = list(map(lambda palabra: palabra[0], lista_palabras))

# solucion evitando datos hardcordeados:

def validar(mensaje):
    repetir = True
    while repetir:
        try:
            palabra = input(mensaje)
            repetir = False
        except ValueError:
            print("Debe ingresar un valor del tipo string")
    return palabra

def obtener_iniciales(lista):
    return [palabra[0] for palabra in lista]

