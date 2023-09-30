"""
Realizar un programa que solicite al usuario un número entero positivo, 
y luego en pantalla muestre solamente los números pares desde el 1 hasta el número ingresado.
Ej: usuario ingresa 10, en pantalla se mostrará 2 4 6 8 10
"""
# posible solucion basica
limite = int(input("Hola, por favor ingresá un número entero positivo: "))
for i in range(0,limite + 1):
    if i%2==0:
        print(i, end=" ")


#-----------------------------------------------------------
# soluciones mejoradas:

# Mi solucion:

def secuencia(num):
    secuencia_numeros = []

    for i in range(2, num + 1, 2):
        secuencia_numeros.append(i)
    return secuencia_numeros

num = int(input("Ingrese un número entero positivo: "))

if num <= 0:
    print("Ingrese un número entero positivo.")
else:
    sec = secuencia(num)
    print(sec)