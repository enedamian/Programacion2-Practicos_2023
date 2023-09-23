#2. Crea una función lambda que tome dos números como argumentos y devuelva su suma.
num1,num2= int(input("Ingrese el primer numero: ")),int(input("Ingrese un segundo numero: "))
suma =lambda x,y: x + y
print(suma(num1,num2)) 