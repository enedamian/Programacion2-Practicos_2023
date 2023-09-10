# Implemente una función que dada una lista de números, devuelva una nueva lista que contenga el cuadrado de cada número utilizando list comprehensions.

def cuadrados(lista):
    """Calcula cuadrados de elementos de una lista

    Args:
        lista (list): lista cuyos elementos se elevan al cuadrado

    Returns:
        list: lista con los elementos del argumento al cuadrado
    """
    return [numero**2 for numero in lista]