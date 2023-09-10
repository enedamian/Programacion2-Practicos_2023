# Implemente una función que dada una lista de nombres, devuelva una nueva lista que contenga solo los nombres que tengan una longitud mayor o igual a una cantidad de caracteres pasada por parámetro, utilizando list comprehensions.

def nombres_mayores(nombres, caracteres):
    return [nombre for nombre in nombres if len(nombre) >= caracteres]
