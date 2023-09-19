lista_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_numeros_masQuince = [list(map(lambda x: x + x/100 * 15, lista_numeros))]
print(lista_numeros_masQuince)