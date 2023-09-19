from functools import reduce
lista_numeros = [1,3,5,4,2,6,5,2,13,67,9,1,4,3,6,2]
mayor = reduce(lambda x,y: x if x > y else y, lista_numeros)
print(mayor)