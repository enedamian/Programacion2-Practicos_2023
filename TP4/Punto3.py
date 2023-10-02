"""3. Crea una función lambda que devuelva el mayor de dos números."""

mayor = lambda num1, num2: num1 if num1 > num2 else num2
#ahora mayor es como una funcion, y cuando se lo llama con valores con parametro hace lo que le asignes
print(mayor(4,2))