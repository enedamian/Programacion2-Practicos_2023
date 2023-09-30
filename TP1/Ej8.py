"""
Desarrollar un programa que permita al usuario indicar cuantos valores quiere ingresar, 
luego que permita la carga de los valores por teclado y nos muestre posteriormente la suma 
de los valores ingresados y su promedio.
"""
# posible solución basica
limite = int(input("Hola, ¿Cuántos numeros querés sumar?: "))
suma=0
for i in range(0,limite):
    numero = int(input(f"Numero {i+1}: "))
    suma += numero
            
print(f"La suma es: {suma} y el promedio es: {suma/limite}")

#-----------------------------------------------------------
# soluciones mejoradas:

# Mi solución:

valores = int(input("Indique cuantos valores quiere ingresar: "))

if valores <= 0:
    print("Debe ingresar una cantidad positiva de valores. ")
else:
    valo = []
    for i in range(valores):
        valor = float(input("Ingrese el valor {}: ".format(i + 1)))
        valo.append(valor)

suma = sum(valo)
promedio = suma / valores

print("La suma de los valores es: {}".format(suma))
print(f"El promedio es: {promedio}")