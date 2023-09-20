"""Pedir 3 números enteros e implementar un algoritmo para determinar cuál es el
mayor de los 3 y mostrar un mensaje por pantalla."""
# posible solucion basica
nro1 = int(input("Ingresá el primer número: "))
nro2 = int(input("Ingresá el segundo número: "))
nro3 = int(input("Ingresá el tercer número: "))
if nro1 > nro2 and nro1 > nro3:
    print(f"El número mayor es: {nro1}")
elif nro2 > nro1 and nro2 > nro3:
    print(f"El número mayor es: {nro2}")
else:
    print(f"El número mayor es: {nro3}")
    
#-----------------------------------------------------------
# soluciones mejoradas: