def leer_entero(mensaje):
    pedir = True
    while pedir:
        try:
            valor = int(input(mensaje))
            if valor>0:
                pedir = False
        except:
            print("El valor ingresado tiene que ser positivo.")
    return valor

alto = leer_entero("Ingrese la altura del rectangulo: ")
ancho = leer_entero("Ingrese el ancho del rectangulo: ")
if ancho<=40 and alto<=40:
    caracter = input("Ingrese el caracter que desea utilizar: ")[0]
    for i in range(alto):
        print(caracter*ancho)