"""Implemente un programa que a partir del ancho, alto y largo de una habitación
rectangular calcule cuántos litros de pintura se necesitan para pintarla. Suponiendo
que 1 litro de pintura sirve para 10m cuadrados y que la habitación tiene sólo una
puerta de 0,80 de ancho por 2 mts de alto.
"""
# posible solucion basica
print("Bienvenido, vamos a calcular los litros de pintura necesarios para pintar una habitación rectangular")
largo = float(input("Por favor, ingrese el largo de la habitación: "))
ancho = float(input("Por favor, ingrese el ancho de la habitación: "))
alto = float(input("Por favor, ingrese el alto de la habitación: "))
# calculamos el área a pintar (en m2)
area_pintable = (largo * alto) * 2 + (ancho * alto) * 2 - (0.8 * 2)
# 1 litro rinde 10 m2
litros = area_pintable / 10
print(f"El área a pintar es {area_pintable:.2f} metros cuadrados")
print(f"Se necesitarán {litros:.2f} litros de pintura para pintar la habitación")

#-----------------------------------------------------------
# soluciones mejoradas:

#Mi solucion:

def cant_necesaria(a, b, c):
    area_puerta = 0.8 * 2
    area_paredes = 2 * (a + b) * c
    area_total = area_paredes - area_puerta
    litros_necesarios = area_total / 10
    return litros_necesarios

ancho = float(input("Ingrese el ancho de la habitación: "))
largo = float(input("Ingrese el largo de la habitación: "))
altura = float(input("Ingrese la altura de la habitación: "))

if ancho <= 0 or largo <= 0 or altura <= 0:
    print("Las dimensiones deben tener valores positivos.")
else:
    litros = cant_necesaria(altura, largo, ancho)
    print(f"Se necesitan {litros} litros de pintura.")