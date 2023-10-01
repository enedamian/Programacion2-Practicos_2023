import random
def longitud(cola):
    return len(cola)

long = random.randint(20,50)

listaA = []
listaB = []

for i in range(0,long):
    listaA.append(random.randint(200,5000))
    listaB.append(random.randint(200,5000))
print(f"{listaA} \n {listaB}")
print(f"Longitud de las listas: {longitud(listaA)}")