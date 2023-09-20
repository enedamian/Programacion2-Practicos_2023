ladoA = float(input("Ingrese un lado del triangulo: "))
ladoB = float(input("Ingrese un ladod el triangulo: "))
ladoC = float(input("Ingrese el lado restante: "))

if (ladoA == ladoB and ladoA == ladoC):
    print("Es un triangulo equilatero.")
elif (ladoA != ladoB and ladoA != ladoC):
    print("Es un triangulo escaleno.")
else:
    print("Es un triangulo isosceles.")
