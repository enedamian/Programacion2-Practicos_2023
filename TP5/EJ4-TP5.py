import random
from functools import reduce
listaAleat = []

def ListaAleatoria():
        for x in range(random.randint(20,50)):
            listaAleat.append(random.randint(200,5000))
        return listaAleat

listaAleat1 = ListaAleatoria()
listaAleat2 = ListaAleatoria()

impares = lambda x: x % 3 == 0
menor = lambda x,y: x if x < y else y

listaImparesL1 = list(filter(impares, listaAleat1))
menorL2 = reduce(menor, listaAleat2)

listaAleat3 = []

for x in range(len(listaImparesL1)):
      listaAleat3.append(listaImparesL1[x] * menorL2)

print(listaAleat3)

