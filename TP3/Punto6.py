""" Dado un diccionario de personas y sus edades, crea una lista que 
contenga solo los nombres de las personas cuya edad es mayor a una
edad ingresada por el usuario, utilizando list comprehensions. """

personas = {
    "Juan": 30,
    "María": 25,
    "Pedro": 35,
    "Ana": 28,
    "Luis": 40
}

def leer_entero_positivo(mensaje):
    pedir = True
    while pedir:
        try:
            valor = int(input(mensaje))
            pedir = False
        except:
            print("El valor ingresado tiene que ser un entero positivo.")
    return valor

def mayores_de_edad(edad):
    try:
        lista_nombres_mayores = [nombre for nombre in personas if personas[nombre] >= edad]
        print(lista_nombres_mayores)
    except:
        print("Error!!")


mayores_de_edad(leer_entero_positivo("Ingrese la edad minima: "))