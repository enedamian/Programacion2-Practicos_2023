# Dado un rango de números, crea una lista que contenga todos los números primos dentro de ese rango utilizando list comprehensions.

def es_primo(numero):
    """Indentifica si un numero natural es primo

    Args:
        numero (number): numero a identificar

    Returns:
        boolean: True si es primo, False si no
    """
    if numero == 1:
        return False
    for num in range(2, numero // 2 + 1):
        if numero % num == 0:
            return False
    return True


def numeros_primos(limite):
    """lista numeros primos menores al límite

    Args:
        limite (number): limite de busqueda

    Returns:
        list: numeros primos
    """
    return [numero for numero in range(2, limite) if es_primo(numero)]