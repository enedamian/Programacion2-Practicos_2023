"""
Escriba un programa que permita el ingreso de números enteros positivos para calcular su promedio, 
el ingreso finaliza cuando el usuario ingresa un número negativo. Luego mostrar el promedio 
y la cantidad de valores que se ingresaron. Ej: “El promedio es ….. con un total de …. ingresos.”
"""
# posible solucion basica

suma = 0
contador = 0
nro=0
while nro >= 0:
    nro = int(input("Ingrese un numero, para terminar ingresá un numero negativo: "))
    if nro >= 0:
        suma += nro
        contador += 1
print(f"Se ingresaron {contador} numeros, la suma es: {suma}, y el promedio: {suma/contador}")

#-----------------------------------------------------------
# soluciones mejoradas:

# Mi solución:

num = int(input("Ingrese un número entero: "))
suma = 0
contador = 0

while(num >= 0):
    suma += num
    contador +=1
    num = int(input("Ingrese otro número entero (negativo para terminar): "))

if contador > 0:
    promedio = suma / contador
    print(f"El promedio es: {promedio} con un total de {contador} ingresos")
else:
    print("No ingresó ningún número positivo")