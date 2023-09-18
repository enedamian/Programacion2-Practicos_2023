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

rango_inferior = int(input("Ingrese el rango inferior: "))
rango_superior = int(input("Ingrese el rango superior: "))

numeros_primos = [numero for numero in range(rango_inferior, rango_superior + 1) if es_primo(numero)]

print("Números primos en el rango [{}, {}]: {}".format(rango_inferior, rango_superior, numeros_primos))