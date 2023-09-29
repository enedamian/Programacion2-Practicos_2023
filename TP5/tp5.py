import random 
#Creamos las funciones genericas para manejar una cola de datos..

def encolar(cola,elemento):       # Encolar incluye cada elemento dentro de la cola
    cola.append(elemento)           

def desencolar(cola,elemento): # Desencolar elimina al elemento en la primer posicion del arreglo es decir el primero que se incluyo cuando se armaba la cola
    if not is_empty():
        return cola.pop(0)
    else:
        return "La cola esta vacia..."
    
def is_empty(cola):
    return len(cola) == 0

def size(cola):
    return len(cola)


#Ahora creamos las funciones para la pila de datos..

def apilar(pila,elemento):
    pila.append(elemento)

def desapilar(pila,elemento):
    if not is_empty_pila():
        return pila.pop()
    else:
        return "La pila esta vacia..."
    
def is_empty_pila(pila):
    return len(pila) == 0

def size_pila(pila):
    return len(pila)


#Usando el módulo random, cree una función que retorne dos listas de longitud aleatoria entre 20 y 50, y cada lista con elementos de valores aleatorios entre 200 y 5000.

def lista_random():

    len_list_1, len_list_2 = random.randint(20, 50), random.randint(20,50)

    list_num_1 = list()
    list_num_2 = list()

    for nums in range(len_list_1):
        nums = random.randint(200,5000)
        list_num_1.append(nums)

    for nums in range(len_list_2):
        nums = random.randint(200,5000)
        list_num_2.append(nums)

    return list_num_1,list_num_2

def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True


def usar_listas():
    
    lista_1,lista_2 = lista_random()

    sublista_primos = [numero for numero in lista_2 if es_primo(numero)] #Con la funcion sorted ordenamos los elementos en este caso numeros de la lista 2, sabemos que en la primera posicion de la lista estara el menor numero

    if not sublista_primos:
        sublista_primos = -1
    else:
        sublista_primos_ordenada = sorted(sublista_primos)
        

    sublista_impares = [numero for numero in lista_1 if numero % 2 != 0]
    
    sublista_impares_multiplicados = list()
    
    for numero in sublista_impares:
        multiplicados = numero * sublista_primos_ordenada[0]
        sublista_impares_multiplicados.append(multiplicados)

    # multipilicacion_menor_primo_por_impares = [numero for numero in sublista_impares]
    print(sublista_impares_multiplicados)
    print(sublista_impares)
    print(f"Numero menor primos: {sublista_primos_ordenada[0]}")



    
