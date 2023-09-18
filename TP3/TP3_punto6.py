
personas = {
    "Juan": 25,
    "Maria": 30,
    "Luis": 22,
    "Ana": 35,
    "Pedro": 18
}

edad_minima = int(input("Ingrese la edad mínima: "))

nombres_mayores = [nombre for nombre, edad in personas.items() if edad >= edad_minima]

print(f"Nombres de personas mayores de {edad_minima} años:".format(edad_minima))
for nombre in nombres_mayores:
    print(nombre)
