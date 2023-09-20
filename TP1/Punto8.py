def leer_entero_positivo(mensaje):
    pedir = True
    while pedir:
        try:
            valor = int(input(mensaje))
            if valor>0:
                pedir = False
        except:
            print("El valor ingresado tiene que ser un entero positivo.")
    return valor

cantidad = leer_entero_positivo("Cuantos valores desea ingresar?")
lista = []
suma = 0
for i in range(cantidad):
    lista.append(leer_entero_positivo(f"Ingrese el valor '{i+1}': "))
    suma += lista[i]
print(f"La suma es: {suma} y el promedio es {suma/cantidad}")