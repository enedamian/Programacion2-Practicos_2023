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
for palabra in lista:
    print(lista)    


# otro ej
alumnos =[{"nombre":"pepe","nota1":90, "nota2":84}, {"nombre":"pepe2","nota1":50, "nota2":94},{"nombre":"pepe3","nota1":80, "nota2":84}]
nombres = [elem["nombre"] for elem in alumnos if (elem["nota1"]>=90) or (elem["nota2"]>=90)]
print(nombres)