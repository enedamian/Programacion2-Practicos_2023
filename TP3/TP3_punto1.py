def cuadrado(num):
    listanum = [valor**2 for valor in num]
    return listanum


llenar_lista = [int(input("Ingrese un valor: ")) for _ in range(5)]
print(cuadrado(llenar_lista))