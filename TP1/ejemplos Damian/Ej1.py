"""
Realizar un programa que pida los tres lados de un triángulo e indique el tipo de
triángulo que es según sus lados: Equilátero (tres lados iguales), Isósceles (dos
lados iguales) o Escaleno (tres lados distintos).
"""
# posible solucion basica
print("Vamos a determinar el tipo de triángulo")
lado1 = float(input("Ingresá el primer lado: "))
lado2 = float(input("Ingresá el segundo lado: "))
lado3 = float(input("Ingresá el tercer lado: "))
if lado1 == lado2 == lado3:
    print("El triángulo es equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")

#-----------------------------------------------------------
# soluciones mejoradas: