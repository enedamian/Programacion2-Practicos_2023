# Dado un diccionario de palabras y sus definiciones, crea una lista que contenga sólo las palabras que comienzan con una letra específica (por ejemplo, "a") indicada por el usuario, utilizando list comprehensions.

def palabras_con_inicial(definiciones, letra):
    """filtra palabras por su inicial

    Args:
        definiciones (dict): diccionario con palabras y sus definiciones
        letra (string): caracter con el cual debe empezar la palabra

    Returns:
        lista: palabras que comienzan con la letra especificada
    """
    return [palabra for palabra in definiciones if palabra[0] == letra]