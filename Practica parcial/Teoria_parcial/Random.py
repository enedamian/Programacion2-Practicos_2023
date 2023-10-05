import random

numero_random = random.randint(20, 50)
# Genera un numero al azar entre 20 y 50 inclusives

lista1 = [random.randint(200, 5000) for _ in range(numero_random)]
# Genera un numero al azar entre los valores 200 y 5000 en cada espacio de la lista en el rango del numero random
