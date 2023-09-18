"""Dado un diccionario de personas y sus edades, crea una lista que contenga solo los nombres de 
las personas cuya edad es mayor a una edad ingresada por el usuario, utilizando list comprehensions."""

personas = {
    "Juan": 30,
    "María": 25,
    "Pedro": 35,
    "Ana": 28,
    "Luis": 40
}

edad_minima = int(input("ingrese la edad minima requerida: "))
#items es para trabajar diccionarios con su parametro y valor, te los devuelve en una tupla
lista_nombres = [nombre for nombre, edad in personas.items() if edad > edad_minima]

print(f"las personas mayores a {edad_minima} son:")
print(lista_nombres)