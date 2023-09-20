def leer_entero_positivo(mensaje):
    pedir = True
    while pedir:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                pedir = False
            else:
                print("El valor ingresado tiene que ser un entero positivo.")
        except ValueError:
            print("El valor ingresado tiene que ser un entero positivo.")
    return valor

numero = leer_entero_positivo("Ingrese un entero positivo: ")
for i in range(numero):
    print(f"{i+1}", end=" ")
