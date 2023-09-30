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
    

# Mi solucion:

def es_bisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def validacion(dia, mes, anio):
    if dia > 31 or mes > 12:
        return False
    elif mes == 2 and dia > 29 and es_bisiesto(anio):
        return False
    elif mes == 4 or mes == 6 or mes == 8 or mes == 11 and dia > 31:
        return False
    return True
    
dia = int(input("Ingrese dia: "))
mes = int(input("Ingrese mes: "))
anio = int(input("Ingrese año: "))

if validacion(dia, mes, anio):
    if es_bisiesto(anio):
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")
else:
    print("La fecha ingresada no es valida")