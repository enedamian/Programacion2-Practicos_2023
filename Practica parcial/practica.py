# 1 - calcular un hash en funcion del apellido que suma valores segun el ASCII de cada consonante y devuelve el resto de la division por 5 en el rango [2,3,4]
# los módulos 0 y 1 se reemplazan por 2
# asumimos que el apellido no contiene comas ni puntos
def hash_apellido(apellido):
    suma=0
    apellido = apellido.strip(" ,.¡!¿?\n").lower()
    for caracter in apellido.lower():
        if caracter not in "aeiou":
            suma += ord(caracter)
    # para evitar division por 0, asumo que los valores 0 y 1 se reemplazan por 2
    valor= suma % 5
    if valor == 0 or valor == 1:
        valor = 2
    return valor


# 2 - dada una lista numerica, generar una nueva lista eliminando elementos duplicados que sean multiplos del hash anterior (a excepcion del 0 y 1)

def es_multiplo(numero, multiplo):
    return numero % multiplo == 0

hash = hash_apellido("Perez")
print("hash del apellido:",hash)
lista_con_repetidos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 2, 5, 10,12, 9, 6 ] # num for num in lista_con_repetidos if es_multiplo(numero,hash)
nueva_lista = [numero for numero in lista_con_repetidos if not(lista_con_repetidos.count(numero)>1 and es_multiplo(numero,hash))]
print(nueva_lista)

for numero in lista_con_repetidos:
    if lista_con_repetidos.count(numero)>1 and es_multiplo(numero,hash):
        lista_con_repetidos.remove(numero)

# 3 - dada una lista generar un nueva lista con todos los elementos pero sin que se repita ninguno (eliminar duplicados pero dejar uno solo)

lista_sin_repetir= list(set(lista_con_repetidos))
print("set: ", lista_sin_repetir)

# 4 - Tomar el código de la clase del 