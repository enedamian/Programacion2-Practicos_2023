personas={
    "Jose":30,
    "Matias":21,
    "Samuel": 31,
    "Elias":45,
    "Samantha": 14,
}

edad_min= int(input("Ingrese la edad minima: "))
lista = [nombre for nombre, edad in personas.items() if edad >= edad_min]
print(lista)