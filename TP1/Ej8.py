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