def Palabras(letra_inicial):
    dicc_palabras = {"arbol": "tronco y copa", "barba": "conjunto de pelos", "ambiguo": "de definicion vaga", "copa": "vaso de vidrio modelado"}
    lista_palabras = [palabra for palabra in dicc_palabras.keys() if palabra.startswith(letra_inicial)]
    return lista_palabras

print(Palabras("a"))