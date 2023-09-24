""" A partir de una lista de números existente, crear una nueva lista
incrementando en un 15% los valores originales usando map. """

items = [4, 7, 9, 2, 5]
quince_porciento_con_map = list(map(lambda x: x*0.15+x, items))

print(quince_porciento_con_map)