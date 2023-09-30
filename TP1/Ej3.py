"""Extienda el programa anterior para permitir múltiple cantidad de “manos” de pintura"""
# posible solucion basica
print("Bienvenido, vamos a calcular los litros de pintura necesarios para pintar una habitación rectangular")
largo = float(input("Por favor, ingrese el largo de la habitación: "))
ancho = float(input("Por favor, ingrese el ancho de la habitación: "))
alto = float(input("Por favor, ingrese el alto de la habitación: "))
cant_manos = int(input("¿Cuántas manos de pintura desea darle a las paredes?: "))
# calculamos el área a pintar (en m2)
area_pintable = (largo * alto) * 2 + (ancho * alto) * 2 - (0.8 * 2)
# 1 litro rinde 10 m2
litros_mano = area_pintable / 10
litros_total = litros_mano * cant_manos
print(f"El área a pintar es {area_pintable:.2f} metros cuadrados")
print(f"Se necesitarán {litros_mano:.2f} litros para cada mano de pintura en la habitación")
print(f"Se necesitarán {litros_total:.2f} litros en total para realizar las {cant_manos} manos de pintura.")

#-----------------------------------------------------------
# soluciones mejoradas:

#Mi solucion:

def cant_necesaria(a, b, c, f):
    area_puerta = 0.8 * 2
    area_paredes = 2 * (a + b) * c
    area_total = area_paredes - area_puerta
    litros_necesarios = (area_total / 10) * f
    return litros_necesarios

ancho = float(input("Ingrese el ancho de la habitación: "))
largo = float(input("Ingrese el largo de la habitación: "))
altura = float(input("Ingrese la altura de la habitación: "))
manos = int(input("Ingrese cantidad de manos que desea pasar de pintura: "))

if ancho <= 0 or largo <= 0 or altura <= 0 or manos <= 0:
    print("Las dimensiones deben tener valores positivos.")
else:
    litros = cant_necesaria(altura, largo, ancho, manos)
    print(f"Se necesitan {litros} litros de pintura.")