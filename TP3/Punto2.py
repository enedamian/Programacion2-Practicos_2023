""" Implemente una función que dada una lista de nombres, 
devuelva una nueva lista que contenga solo los nombres que tengan 
una longitud mayor o igual a una cantidad de caracteres pasada por 
parámetro, utilizando list comprehensions. """

lista_nombres = ["Juan", "Baucha", "Gabriel", "Mohhammed", "Mateo", "Damian", "Maximiliano"]

def leer_entero_positivo(mensaje):
    seguir_pidiendo = True
    while seguir_pidiendo:
        try:
            numero = int(input(mensaje))
            if numero >= 0:
                seguir_pidiendo=False             
            else:
                print("El numero ingresado no es válido. Debe ingresar un numero positivo.")
        except ValueError:
            print('Error, debe ingresar un numero entero positivo.\nInténtelo nuevamente:')
    return numero

def crear_lista(largo):
    lista_nueva = [nombre for nombre in lista_nombres if len(nombre) >= largo]
    return lista_nueva

longitud = leer_entero_positivo("Ingrese longitud de caracteres: ")

print(crear_lista(longitud))