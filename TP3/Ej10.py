# 10. Dada una lista de números, crea dos listas separadas: una que contenga los números pares y otra que contenga los números impares utilizando list comprehensions.

lista = [1,2,3,4,5,6,7,8,9]

def separaParesImpares(lista):
    pares = [par for par in lista if par%2==0]
    impares = [impar for impar in lista if impar%2!=0]
    return print(pares,impares)

separaParesImpares(lista)