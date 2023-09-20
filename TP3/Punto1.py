#Implemente una función que dada una lista de números,
#devuelva una nueva lista que contenga el cuadrado de cada número utilizando list comprehensions.

lista_original = [1, 5, 10, 20, 2, 8]

def modificar_lista(lista):
    lista_nueva = [elemento**2 for elemento in lista]
    return lista_nueva

print(f"La lista original es: {lista_original}")
print(f"Si elevamos los elementos al cuadrado, la lista queda: {modificar_lista(lista_original)}")