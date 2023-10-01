""" Utilizando la función anterior genere dos listas de datos.
Con la lista1 se debe generar una sublista con los elementos
impares de lista1 multiplicados por el valor menor de la lista2.
Con la lista2 se debe devolver el menor número primo contenido
en la lista, o “-1” si no tiene números primos. """
import random

#funcion para crear las listas
def crear_listas():
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
    
    return lista1, lista2

#funcion para ordenar el arreglo
def selection_sort(arreglo):
    for i in range(len(arreglo) - 1):
        menor = i

        for j in range(i + 1, len(arreglo)):
            if arreglo[j] < arreglo[menor]:
                menor = j
        if menor != i:
            arreglo[menor], arreglo[i] = arreglo[i], arreglo[menor]
    return arreglo

#creamos las listas
listas_tupla = crear_listas()

#las ordenamos
selection_sort(listas_tupla[1])

lista2 = listas_tupla[1]

#multiplicamos todos los elementos por el menor numero de la lista2 y seleccionamos los impares para la nueva lista
#lista_nueva = [numero*lista2[0] for numero in listas_tupla[0] if numero % 2 != 0]

#otra forma es primero crear la lista de impares y despues multiplicarlos por el menor de lista2
lista_nueva = [numero for numero in listas_tupla[0] if numero % 2 != 0]
lista_nueva = list(map(lambda x: x*lista2[0], lista_nueva))
print(lista_nueva)

def es_primo(numero):
    if numero == 1:
        return False
    else:
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
    return True

lista_primos = [numero for numero in lista2 if es_primo(numero)]
if lista_primos == 0:
    print("-1")
else:
    selection_sort(lista_primos)
    print(lista_primos[0])