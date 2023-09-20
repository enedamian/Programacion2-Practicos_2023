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
caracter = input("Ingrese un caracter: ")[0]
repeticiones = leer_entero("Ingrese la cantidad de repeticiones: ")

print(caracter * repeticiones)