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

# Mi solución:

def buscar_multiplo(a, b, c):
    multiplos = []

    for i in range(a, b):
        if i % c == 0:
            multiplos.append(i)

    return multiplos

A = int(input("Introduce un numero entero: "))
B = int(input("Introduce otro numero entero: "))
X = int(input("Introduce otro numero entero: "))

if A <= 0 or B <= 0 or X <= 0:
    print("Solo se aceptan valores positivos")
else:
    lista_multiplos = buscar_multiplo(A, B, X)
    print(f"Los numeros multiplos de {X} entre {A} y {B} son: {lista_multiplos}")
