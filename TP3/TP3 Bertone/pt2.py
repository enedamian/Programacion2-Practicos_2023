def ListaNombresLargos(lista, cant_caracteres):
    listafiltrada=[nombre for nombre in lista if len(nombre)>=cant_caracteres]

    return listafiltrada;

lista_nombres=["Gamo", "Guti", "Nickanme", "Lucas", "Santi", "Ignacio"]
cantidad_caracteres=int(input("Ingrese una cantidad de caracteres a filtrar: "))
nombres_filtrados=ListaNombresLargos(lista_nombres, cantidad_caracteres)

print(nombres_filtrados)

