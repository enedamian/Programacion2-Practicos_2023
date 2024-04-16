Personas_y_Edades={
    "Bianca": 18,
    "Lucas": 18,
    "Daniela": 38,
    "Dante": 4
}

edad_ingresada=int(input("Ingrese una edad y te dire quienes son mayores a la edad que ingresaste: "))

listademayores=[(nombre, edad) for nombre, edad in Personas_y_Edades.items() if edad_ingresada< edad ]

print(listademayores)