import random

def generar_listas():
    longitud_lista_1, longitud_lista_2 = random.randint(20, 50), random.randint(20, 50)
    lista_1 = [random.randint(200, 5000) for _ in range(longitud_lista_1)]
    lista_2 = [random.randint(200, 5000) for _ in range(longitud_lista_2)]

    return lista_1, lista_2

lista_1, lista_2 = generar_listas()

print("Lista 1: ", lista_1)
print("")
print("Lista_2: ", lista_2)