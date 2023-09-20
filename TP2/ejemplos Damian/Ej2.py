"""Escriba una función llamada EsBisiesto que permita ingresar un número de año y
devuelva verdadero en caso que el año sea bisiesto, o falso cuando no lo es. Un año
es bisiesto si: es divisible entre cuatro y (no es divisible entre 100 o es divisible entre
400). Utilizarlo en un programa que permita ingresar dia, mes y año y muestre por
pantalla si la fecha es válida o no."""

def es_bisiesto(year):
    """Toma el año de ingreso y devuelve True si el año es bisiesto, False en caso contrario"""
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True  
    else:
        return False