"""7. Dada una lista con números, filtrar los números pares y devolverlos en una nueva lista.
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2==0 ,numeros))
print(pares)