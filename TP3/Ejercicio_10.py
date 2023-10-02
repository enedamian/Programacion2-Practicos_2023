lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def separar_listas(lista):
    lista_pares = [num for num in lista if num % 2 == 0]
    lista_impares = [num for num in lista if num % 2 != 0]
    print(f"Numeros pares: {lista_pares}")
    print(f"Numeros impares: {lista_impares}")

separar_listas(lista_numeros)