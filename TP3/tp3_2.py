def nombres_longitud(lista,caracteres):
    nombres_long= [nombre for nombre in lista if len(nombre) >= caracteres]
    return nombres_long
caracteres = int(input("Ingrese cantidad minima de caracteres: "))
lista_nombres =["matias","jorgelina","elias","martina","jose","samuel","susana"]
lista_nueva = nombres_longitud(lista_nombres,caracteres)
print(lista_nueva)