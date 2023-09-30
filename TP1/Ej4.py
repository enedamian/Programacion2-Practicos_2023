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

# Mi solucion:

def num_mayor(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
num_1 = int(input("Ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))
num_3 = int(input("Ingrese el tercer número: "))

mayor = num_mayor(num_1, num_2, num_3)
print(f"El número mayor es: {mayor}")