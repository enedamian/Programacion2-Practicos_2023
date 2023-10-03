max = lambda x, y: x if x > y else y

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
print(f"El mayor entre {num1} y {num2} es {max(num1, num2)}")