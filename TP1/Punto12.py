def leer_entero_positivo(mensaje):
    pedir = True
    while pedir:
        try:
            valor = int(input(mensaje))
            if valor >= 0:
                pedir = False
            else:
                print("El valor ingresado tiene que ser un entero positivo.")
        except ValueError:
            print("El valor ingresado tiene que ser un entero positivo.")
    return valor

seguir = True
numeros = []
print("Para finalizar, ingrese 0.")
while seguir:
    numero = leer_entero_positivo("Ingrese un entero positivo: ")
    if numero == 0:
        seguir = False
    else:
        numeros.append(numero)
ordenada = True
for j in range(len(numeros) - 1):
    if numeros[j] > numeros[j+1]:
        ordenada = False
if ordenada:
    print("La secuencia esta ordenada.")
else:
    print("La secuencia no esta ordenada.")