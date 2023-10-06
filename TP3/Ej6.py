# 6. Dado un diccionario de personas y sus edades, crea una lista que contenga solo los nombres de las personas cuya edad es mayor a una edad ingresada por el usuario, utilizando list comprehensions.

personasEdades = {
    "Juan": 30,
    "María": 25,
    "Pedro": 35,
    "Luisa": 28,
    "Ana": 22
}

edad = 25
def mayoresQue(personasEdades,edad):
    listaMayores=[nombres for nombres, anios in personasEdades.items() if anios>edad]
    return print(listaMayores)

mayoresQue(personasEdades,edad)