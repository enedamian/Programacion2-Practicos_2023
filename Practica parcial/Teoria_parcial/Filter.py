lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = filter(lambda x: x % 2 == 0, lista)
resultado_lista = list(resultado)  # Convierte el resultado en una lista

print(resultado_lista)  # Esto imprimirá [2, 4, 6, 8, 10], que son los números pares de la lista original.

mi_diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
claves_filtradas = filter(lambda clave: mi_diccionario[clave] >= 3, mi_diccionario.keys())
claves_filtradas_lista = list(claves_filtradas)

print(claves_filtradas_lista)  # Esto imprimirá ['c', 'd', 'e']

mi_diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
valores_filtrados = filter(lambda valor: valor >= 3, mi_diccionario.values())
valores_filtrados_lista = list(valores_filtrados)

print(valores_filtrados_lista)  # Esto imprimirá [3, 4, 5]

