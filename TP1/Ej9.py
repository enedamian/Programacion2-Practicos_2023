"""Se desea realizar una aplicación que solicite al usuario tres números enteros
positivos (A, B, y X), y que muestre por pantalla todos los múltiplos de X que estén
entre A y B inclusive. """

#posible solucion básica
nroA = int(input("Ingrese el numero A: "))
nroB = int(input("Ingrese el numero B: "))
nroX = int(input("Ingrese el numero 'X' para buscar sus multiplos entre A y B: "))
for i in range(nroA, nroB+1):
    if i % nroX == 0:
        print(i, end=" ")
print()

#-----------------------------------------------------------
# soluciones mejoradas:
