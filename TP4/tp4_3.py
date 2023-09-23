#3. Crea una función lambda que devuelva el mayor de dos números.
num1,num2= int(input("Ingrese el primer numero: ")),int(input("Ingrese un segundo numero: "))
mayor = lambda x,y: "el primer numero" if x>=y else "el segundo numero"
#mayor = lambda x,y: x if x>=y else y
print(f"El mayor entre {num1} y {num2} es: {mayor(num1,num2)}") 