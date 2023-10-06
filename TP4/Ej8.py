# 9. Dada una lista de palabras, utiliza la función sorted con una función lambda para ordenar la lista de acuerdo a la longitud de las palabras.

nombres=["juan","julian","marto","mirta","miriam","ana","agustina","agustin"]

nombres_ordenados = sorted(nombres, key=lambda palabra: len(palabra))

print(nombres_ordenados)