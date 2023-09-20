def leer_entero(mensaje):
    pedir = True
    while pedir:
        try:
            valor = int(input(mensaje))
            pedir = False
        except:
            print("Por favor, ingrese un valor valido.")
    return valor

suma = 0
parar = True
contador = 0
while parar:
    numero = leer_entero("Ingrese un numero entero positivo, para finalizar ingresar un negativo: ")
    if numero >= 0:
        suma += numero
        contador += 1
    else:
        parar = False
promedio = suma / contador
print(f"El promedio es {promedio}, con un total de {contador, .2} ingresos.")