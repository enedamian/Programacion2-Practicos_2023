"""
Escriba un programa que permita al usuario ingresar las medidas de 2 lados de un rectángulo, 
y que luego mediante la impresión repetida de un caracter (ej: *) lo dibuje en la pantalla. 
Para este ejercicio tomaremos un máximo de 40 para el lado más largo, 
con el fin de evitar problemas de visualización en la consola. Verificar en los datos de entrada 
que se cumpla este requisito
"""
# posible solucion basica
car = input('Ingrese un caracter: ')
base = int(input('Ingrese la base: '))
altura = int(input('Ingrese la altura: '))
for i in range(0,altura):
    print()
    for j in range(0,base):
        print(car, end="")
print()

#-----------------------------------------------------------
# posible solucion basica alternativa:
car = input('Ingrese un caracter: ')
base = int(input('Ingrese la base: '))
altura = int(input('Ingrese la altura: '))
for i in range(0,altura):
    print(car * base)
print()

#-----------------------------------------------------------
# soluciones mejoradas:

# Mi solucion:

def dibujar_rectangulo(lado1, lado2):
    char = '*'
    for i in range(lado1):
        for j in range(lado2):
            print(char, end = "")
        print()


ancho = int(input("Ingrese el ancho del rectángulo: "))
altura = int(input("Ingrese la altura del rectángulo: "))

if ancho < 0 or altura < 0:
    print("Ingrese un valor positivo")
else:
    if ancho > 10 or altura > 10:
        print("Ingrese un valor no mayor a 10 para los lados")
    else:
        rectangulo = dibujar_rectangulo(altura, ancho)
        print(rectangulo)