numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def es_primo(num):
    if num == 1:
        return False
    else:
        for n in range(2, num):
            return num % n != 0
                
def numeros_primos(numeros):
    return [numero for numero in range(2, numeros[9]) if es_primo(numero)]

print(numeros_primos(numeros))