from functools import reduce
lista = [2, 8, 10]

max = reduce(lambda x, y: x if x > y else y, lista)
print(max)