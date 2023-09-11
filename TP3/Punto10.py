"""Dada una lista de números, crea dos listas separadas: una que contenga los números pares 
y otra que contenga los números impares utilizando list comprehensions."""

# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Utiliza list comprehensions para crear listas separadas de pares e impares
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

# Imprime las listas de pares e impares
print("Números pares:", pares)
print("Números impares:", impares)
