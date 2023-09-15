def ListasParImpar(lista):
    pares = [num for num in lista if num % 2 == 0]
    impares = [num for num in lista if num % 2 != 0]
    return pares, impares

lista_1 = [1,2,3,4,5,6,7,8,9,10]

print(ListasParImpar(lista_1))