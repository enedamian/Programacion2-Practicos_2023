# 5. Dado un rango de números, crea una lista que contenga todos los números primos dentro de ese rango utilizando list comprehensions.

start = 0
end = 600

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numerosPrimos (start, end):
    listaPrimos=[numero for numero in range(start, end + 1) if es_primo(numero)]
    return print(listaPrimos)

numerosPrimos (start, end)