""" Usando el módulo random, cree una función que retorne dos listas
de longitud aleatoria entre 20 y 50, y cada lista con elementos 
de valores aleatorios entre 200 y 5000. """

import random
#FORMA 1
""" longitud1 = random.randint(20, 50)
print(f"La lista 1 posee {longitud1} numeros.")

lista1 = []
lista2 = []
numero = 0

while numero < longitud1:
    lista1.append(random.randint(200, 5000))
    numero += 1
print(lista1)
numero = 0

longitud2 = random.randint(20, 50)
print(f"La lista 2 posee {longitud2} numeros.")

while numero < longitud2:
    lista2.append(random.randint(200, 5000))
    numero += 1
print(lista2) """

#FORMA 2
""" def crear_listas():
    numero = 0

    lista1 = []
    longitud1 = random.randint(20, 50)
    
    while numero < longitud1:
        lista1.append(random.randint(200, 5000))
        numero += 1
    numero = 0
    
    lista2 = []
    longitud2 = random.randint(20, 50)
    while numero < longitud2:
        lista2.append(random.randint(200, 5000))
        numero += 1
    
    return lista1, lista2 """

