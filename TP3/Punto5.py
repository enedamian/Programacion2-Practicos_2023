"""5. Dado un rango de números, crea una lista que contenga todos los números 
primos dentro de ese rango utilizando list comprehensions."""
#funcion eficiente para saber si el numero es primo
def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

minimo_numeros = int(input("ingrese el minimo del rango: "))
maximo_numeros = int(input("ingrese el maximo del rango: "))

lista_numeros = [numero for numero in range(minimo_numeros, maximo_numeros) if es_primo(numero)]
print(lista_numeros)