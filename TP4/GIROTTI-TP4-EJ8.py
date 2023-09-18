lista_palabras = ["arbol", "gente", "arameo", "basico", "Juan", "corcho", "dedo"]
devolver_inicial = lambda x: x[0]
lista_iniciales = list(map(devolver_inicial, lista_palabras))
print(lista_iniciales)