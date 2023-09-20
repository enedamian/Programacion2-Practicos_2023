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