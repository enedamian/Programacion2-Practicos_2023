def verif_orden(secuencia):
    for i in range(1, len(secuencia)):
        if secuencia[i-1] > secuencia[i]:
            return False
    return True

secuencia = []

num = int(input("Ingrese un número entero (0 para terminar): "))

while num != 0:
    if num < 0:
        print("Ingrese un número positivo: ")
    else:
        secuencia.append(num)

    num = int(input("Ingrese un número entero (0 para terminar): "))

if len(secuencia) <= 1:
    print(f"La secuencia tiene menos de dos elementos: {secuencia}")
elif verif_orden(secuencia):
    print("La secuencia está ordenada de menor a mayor.")
else:
    print("La secuencia no está ordenada de menor a mayor.")
    