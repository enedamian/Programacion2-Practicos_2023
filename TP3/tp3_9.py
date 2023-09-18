lista_a = [1,2,3,4,5]
lista_b = [6,7,8,9,10]

nueva_lista = [num1*num2 for num1, num2 in zip(lista_a,lista_b)]
print(nueva_lista)
