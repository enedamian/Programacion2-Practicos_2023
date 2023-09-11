#EJ2:
def ListaNombres(cant_car):
    listaNom = ["Carla", "Juan", "Pepe", "Gonzalo", "Humberto", "Lola"]
    listaModif = [nombre for nombre in listaNom if len(nombre) >= cant_car]
    return listaModif

print(ListaNombres(4))

