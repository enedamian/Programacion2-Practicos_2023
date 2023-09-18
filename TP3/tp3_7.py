# Implemente un programa que le pida una palabra al usuario y cuenta la cantidad de vocales en ella.
#El programa deberá pedirle palabras al usuario hasta que éste introduzca la palabra “salir”.
def pedir():
    a=""
    lista =[]
    while a!="salir":
        a = input("Introduzca una palabra: ")
        lista.append(a)
    return lista

lista = pedir()
print(lista)    