# 2. Implemente una función que dada una lista de nombres, devuelva una nueva lista que contenga solo los nombres que tengan una longitud mayor o igual a una cantidad de caracteres pasada por parámetro, utilizando list comprehensions.

listaNombres=["genaro","damian","fernando","ricardo","ana","agustina","julian","franco","saul","armando"]
longitud=6

def nombresMayorALongitud (listaNombres,longitud):
    listaLongitud=[nombre for nombre in listaNombres if len(nombre)>longitud]
    return print(listaLongitud)

nombresMayorALongitud(listaNombres,longitud)

print(listaNombres)