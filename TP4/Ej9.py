# 10. Dada una lista de palabras, generar una lista con las iniciales de cada palabra.

nombres=["juan","julian","marto","mirta","miriam","ana","agustina","agustin"]

def primerLetra(nombre):
    return nombre[0]

listaLetras=list(map(primerLetra,nombres))

print(listaLetras)