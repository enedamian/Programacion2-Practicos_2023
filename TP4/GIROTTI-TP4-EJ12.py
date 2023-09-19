from functools import reduce

lista_cadenas = ["Hola","Adios","Buenos dias", "Buenas tardes", "Buenas noches"]
lista_cadenas_unidas = reduce(lambda x, y: x + " " + y, lista_cadenas)

print(lista_cadenas_unidas)