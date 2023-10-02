from functools import reduce
"""14. Utilice reduce para concatenar una lista de cadenas en una sola cadena
"""
lista_cadenas = ["Hola ", "mundo", "!"]
cadena = reduce(lambda x, y: x + y, lista_cadenas)
print(cadena)