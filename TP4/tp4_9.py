#9. Dada una lista de palabras, utiliza la función sorted con 
# una función lambda para ordenar la lista de acuerdo a la longitud de las palabras.

lista= ["messi","mascherano","lavezzi","barovero","orion"]
lista_nueva = list(sorted(lista, key=lambda x: len(x)))

print(lista_nueva)