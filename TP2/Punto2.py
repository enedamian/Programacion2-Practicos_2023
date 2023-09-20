""" Escriba una función llamada EsBisiesto que permita ingresar un número de año y
devuelva verdadero en caso que el año sea bisiesto, o falso cuando no lo es. Un año
es bisiesto si: es divisible entre cuatro y (no es divisible entre 100 o es divisible entre
400). Utilizarlo en un programa que permita ingresar dia, mes y año y muestre por
pantalla si la fecha es válida o no. """

def EsBisiesto(año):
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

def FechaValida(dia, mes, año):
    meses_30_dias = [4, 6, 9, 11]
    meses_31_dias = [1, 3, 5, 7, 8, 10, 12]

    if mes < 1 or mes > 12:
        return False

    if mes in meses_30_dias and (dia < 1 or dia > 30):
        return False

    if mes in meses_31_dias and (dia < 1 or dia > 31):
        return False

    if mes == 2:
        if EsBisiesto(año):
            if dia < 1 or dia > 29:
                return False
        else:
            if dia < 1 or dia > 28:
                return False

    return True

def main():
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))

    if FechaValida(dia, mes, año):
        print("La fecha es válida.")
    else:
        print("La fecha no es válida.")

if __name__ == "__main__":
    main()
