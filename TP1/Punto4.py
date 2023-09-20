def leer_entero_positivo(mensaje):
    pedir = True
    while pedir:
        try:
            valor = int(input(mensaje))
            pedir = False
        except:
            print("El valor ingresado tiene que ser un entero positivo.")
    return valor

#creamos una lista para almacenar los numeros
lista_numeros = []

#agregamos los tres numeros
for i in range(3):
    numero = leer_entero_positivo(f"Introduce el numero #{i+1}: ")
    lista_numeros.append(numero)

#asumimos que el mayor es el primero de la lista
mayor = lista_numeros[0]
#recorremos y comparamos
for numero in lista_numeros:
    if numero > mayor:
        mayor = numero
#imprimimos el resultado
print(f"El numero mas grande de los tres ingresados es: {mayor}")