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

A = leer_entero_positivo("Ingrese el parametro mas chico: ")
B = leer_entero_positivo("Ingrese el parametro mas grande: ")
X = leer_entero_positivo("Ingrese el numero del que desea saber los multiplos: ")

while A <= B:
    if A % X == 0:
        print(A, end=" ")
    A += 1