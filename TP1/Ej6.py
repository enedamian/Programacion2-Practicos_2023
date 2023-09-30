"""
Realizar un programa que solicite al usuario un número entero positivo, 
y luego en pantalla muestre la secuencia de números desde el 1 hasta el número ingresado.
Ej: usuario ingresa 10, en pantalla se mostrará 1 2 3 4 5 6 7 8 9 10
"""
# posible solucion basica
limite = int(input("Hola, por favor ingresá un número entero positivo: "))        
for i in range(1, limite+1):
    print(i, end=" ")

print()
# Observar que la condición del for no llega a limite, frena en el numero anterior
# Es decir, itera mientras i < limite+1

#-----------------------------------------------------------
# soluciones mejoradas:

# Mi solucion:

def secuencia(num):
    secuencia_numeros = []

    for i in range(1, num + 1):
        secuencia_numeros.append(i)
    return secuencia_numeros

num = int(input("Ingrese un número entero positivo: "))

if num <= 0:
    print("Ingrese un número entero positivo.")
else:
    sec = secuencia(num)
    print(sec)
