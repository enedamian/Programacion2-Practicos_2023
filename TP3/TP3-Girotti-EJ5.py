def EsPrimo(numero):
    divisor = 1
    cant_divisores = 0
    es_primo = True

    while cant_divisores <= 2 and divisor <= numero:
        if numero % divisor == 0:
            cant_divisores += 1
        divisor += 1

    if cant_divisores > 2:
        es_primo = False

    return es_primo
#===============================================================================================================================================

def NumPrimos(lista_numeros):
    lista_primos = [numero for numero in lista_numeros if numero >= 1 and EsPrimo(numero)]
    return lista_primos

l_numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

print(NumPrimos(l_numeros))