#8. Dada una lista con elementos duplicados,
# crea una nueva lista que contenga solo los elementos únicos utilizando list comprehensions.

lista_duplicada = [1,1,1,2,2,2,2,3,3,3,3]
lista_nueva = []
[lista_nueva.append(elem) for elem in lista_duplicada if elem not in lista_nueva]
print(lista_nueva)
