"""2. Implemente una función que dada una lista de nombres, devuelva una nueva lista
que contenga solo los nombres que tengan una longitud mayor o igual a una cantidad
de caracteres pasada por parámetro, utilizando list comprehensions."""
def filtrado(lista, cant_caracteres):
    nombres_filtrada = [nombre for nombre in lista if len(nombre) >= cant_caracteres]
    return nombres_filtrada

lista_nombres = ["jose", "jorge", "manolo", "maria", "godofredo", "lucia", "jimena"]
cant_caracteres = int(input("ingrese la cantidad minima de caracteres: "))
nombres_filtrados = filtrado(lista_nombres, cant_caracteres)
print(nombres_filtrados)
