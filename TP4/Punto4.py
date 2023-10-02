"""4. A partir de una lista de números existente, 
crear una nueva lista incrementando en un 15% los valores originales usando map."""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_aumentada = list(map(lambda x: x * 1.15, numeros))
print(lista_aumentada)