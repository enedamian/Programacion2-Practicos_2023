lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

pares=[numero for numero in lista if numero%2==0]
impares=[numero for numero in lista if numero%2 !=0]

print(f"Lista de pares={pares} Lista impares={impares}")