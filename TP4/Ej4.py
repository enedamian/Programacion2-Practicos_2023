# 4. A partir de una lista de números existente, crear una nueva lista incrementando en un 15% los valores originales usando map.

lista=[5,4,9,15,47,59,23,24,15,5,9,3,7,4,1,2,0,2,3,89]

def incremento(numero):
    return numero*1.15

print(list(map(incremento,lista)))