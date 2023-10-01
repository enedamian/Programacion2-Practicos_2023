#Utilice reduce para concatenar una lista de cadenas en una sola cadena
from functools import reduce

lista = ["Hola", ", Mundo!"]
concatenacion = reduce(lambda x, y: x + y, lista)

print(concatenacion)