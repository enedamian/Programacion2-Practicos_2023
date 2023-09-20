# 1 ----------- 
# ¿Como se podría optimizar? ¿Que pasa si el usuario ingresa cualquier cosa en lugar de un numero?
# Se podría usar funciones para separar la lógica y hacer el código más legible.
def leer_lado(mensaje):
    """Muestra el mensaje pasado por parámetro y espera el ingreso de un float"""
    seguirPidiendo = True
    while seguirPidiendo:
        try:
            lado = float(input(mensaje))
            seguirPidiendo = False
        except ValueError:
            print("Debe ingresar un número válido. Intente nuevamente.")
    return lado


def determinar_tipo(lado1, lado2, lado3):
    """determina el tipo de triangulo en función de las medidas de sus lados"""
    if lado1 == lado2 == lado3:
        return "equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "isósceles"
    else:
        return "escaleno"

# ahora el programa nos quedó mas legible:
print("Pasamos a la solución mejorada:")
print("Vamos a determinar el tipo de triángulo")
lado1 = leer_lado("Ingresá el primer lado: ")
lado2 = leer_lado("Ingresá el segundo lado: ")
lado3 = leer_lado("Ingresá el tercer lado: ")
triangulo_tipo = determinar_tipo(lado1, lado2, lado3)
print(f"El triángulo es {triangulo_tipo}")

# 2 ---------------------------------------------
# ¿Como se podría optimizar? ¿Que pasa si el usuario ingresa cualquier cosa en lugar de un numero?
# Se podría usar funciones para separar la lógica y hacer el código más legible.
def leer_lado(mensaje):
    """Muestra el mensaje pasado por parámetro y espera el ingreso de un float"""
    seguirPidiendo = True
    while seguirPidiendo:
        try:
            lado = float(input(mensaje))
            seguirPidiendo = False
        except ValueError:
            print("Debe ingresar un número válido. Intente nuevamente.")
    return lado

def calcular_area_pintable(largo, ancho, alto, aberturas):
    # calculamos el área a pintar (en m2)
    return (largo * alto) * 2 + (ancho * alto) * 2 - aberturas

def calcular_litros(area_pintable):
    # 1 litro rinde 10 m2
    return area_pintable / 10

print("Pasamos a la solución mejorada:")
print("Bienvenido, vamos a calcular los litros de pintura necesarios para pintar una habitación rectangular")
largo = leer_lado("Por favor, ingrese el largo de la habitación: ")
ancho = leer_lado("Por favor, ingrese el ancho de la habitación: ")
alto = leer_lado("Por favor, ingrese el alto de la habitación: ")
area_pintable = calcular_area_pintable(largo, ancho, alto, 0,8*2)
litros = calcular_litros(area_pintable)
print(f"El área a pintar es {area_pintable:.2f} metros cuadrados")
print(f"Se necesitarán {litros:.2f} litros de pintura para pintar la habitación")

# 3 ---------------------------------------------
# ¿Como se podría optimizar? ¿Que pasa si el usuario ingresa cualquier cosa en lugar de un numero?
# Se podría usar funciones para separar la lógica y hacer el código más legible.
def leer_lado(mensaje):
    """Muestra el mensaje pasado por parámetro y espera el ingreso de un float"""
    seguirPidiendo = True
    while seguirPidiendo:
        try:
            lado = float(input(mensaje))
            seguirPidiendo = False
        except ValueError:
            print("Debe ingresar un número válido. Intente nuevamente.")
    return lado

def leer_entero_positivo(mensaje):
    """Muestra el mensaje, espera un ingreso de teclado y valida que sea un numero entero positivo, en caso contrario sigue pidiendo el numero entero hasta que sea valido."""
    seguirPidiendo = True
    while seguirPidiendo:
        try: 
            numero = int(input(mensaje))
            if numero>0:
                seguirPidiendo=False             
            else:
                print("El numero ingresado no era positivo, no es válido.")
        except ValueError:
            print('Error, dato inválido.\nInténtelo nuevamente.')
    return numero

def calcular_area_pintable(largo, ancho, alto, aberturas):
    # calculamos el área a pintar (en m2)
    return (largo * alto) * 2 + (ancho * alto) * 2 - aberturas

def calcular_litros(area_pintable, manos_de_pintura):
    # 1 litro rinde 10 m2
    return (area_pintable / 10) * manos_de_pintura

print("Pasamos a la solución mejorada:")
print("Bienvenido, vamos a calcular los litros de pintura necesarios para pintar una habitación rectangular")
largo = leer_lado("Por favor, ingrese el largo de la habitación: ")
ancho = leer_lado("Por favor, ingrese el ancho de la habitación: ")
alto = leer_lado("Por favor, ingrese el alto de la habitación: ")
cant_manos = leer_entero_positivo("¿Cuántas manos de pintura desea aplicar?: ")
area_pintable = calcular_area_pintable(largo, ancho, alto, 0,8*2)
litros = calcular_litros(area_pintable, cant_manos)
print(f"El área a pintar es {area_pintable:.2f} metros cuadrados")
print(f"Se necesitarán {litros:.2f} litros de pintura para pintar la habitación con {cant_manos} manos de pintura.")

# 4 ------------------------
# # Se puede mejorar validando la entrada:
def leer_entero(mensaje):
    """Muestra el mensaje, espera un ingreso de teclado y valida que sea un numero entero, en caso contrario sigue pidiendo el numero entero hasta que sea valido."""
    seguirPidiendo = True
    while seguirPidiendo:
        try: 
            numero = int(input(mensaje))
            seguirPidiendo=False 
        except ValueError:
            print('Error, dato inválido.\nInténtelo nuevamente.')
    return numero

print("Pasamos a la solución mejorada:")
nro1 = leer_entero("Ingresá el primer número: ")
nro2 = leer_entero("Ingresá el segundo número: ")
nro3 = leer_entero("Ingresá el tercer número: ")
if nro1 > nro2 and nro1 > nro3:
    print(f"El número mayor es: {nro1}")
elif nro2 > nro1 and nro2 > nro3:
	print(f"El número mayor es: {nro2}")
else:
	print(f"El número mayor es: {nro3}")

# 5 ---------------------------------------------    
# Solución alternativa con funciones predefinidas de strings
print("Pasamos a la solución mejorada:")
cadena = input("Ingresá un texto: ")
cantidad_espacios = cadena.count(" ")
print(f"La cantidad de espacios es: {cantidad_espacios}")

# 6 ---------------------------------------------
# podemos optimizar el codigo validando el numero pedido
def leer_entero_positivo(mensaje):
    """Muestra el mensaje, espera un ingreso de teclado y valida que sea un numero entero positivo, en caso contrario sigue pidiendo el numero entero hasta que sea valido."""
    seguirPidiendo = True
    while seguirPidiendo:
        try: 
            numero = int(input(mensaje))
            if numero>0:
                seguirPidiendo=False             
            else:
                print("El numero ingresado no era positivo, no es válido.")
        except ValueError:
            print('Error, dato inválido.\nInténtelo nuevamente.')
    return numero

def imprimir_numeros(limite):
    for i in range(1, limite+1):
        print(i, end=" ")

print("Pasamos a la solución mejorada:")
limite = leer_entero_positivo("Hola, por favor ingresá un número entero positivo: ")
imprimir_numeros(limite)

# 7 ---------------------------------------------
# se puede optimizar validando la entrada:
def leer_entero_positivo(mensaje):
    """Muestra el mensaje, espera un ingreso de teclado y valida que sea un numero entero positivo, en caso contrario sigue pidiendo el numero entero hasta que sea valido."""
    seguirPidiendo = True
    while seguirPidiendo:
        try: 
            numero = int(input(mensaje))
            if numero>0:
                seguirPidiendo=False             
            else:
                print("El numero ingresado no era positivo, no es válido.")
        except ValueError:
            print('Error, dato inválido.\nInténtelo nuevamente.')
    return numero

def imprimir_numeros_pares(limite):
    for i in range(0,limite + 1):
        if i%2==0:
            print(i, end=" ")

print("Pasamos a la solución mejorada:")
limite = leer_entero_positivo("Hola, por favor ingresá un número entero positivo: ")
imprimir_numeros_pares(limite)
print()

# otra posible solucion:
def imprimir_numeros_impares_sin_if(limite):
    for i in range(0,limite + 1, 2):
        print(i, end=" ")

print("El resultado de la 2da posible solucion: ")
imprimir_numeros_impares_sin_if(limite)

# 8 ---------------------------------------------
#---------------------------------
#Posible mejora:
def leer_entero_positivo(mensaje):
    """Muestra el mensaje, espera un ingreso de teclado y valida que sea un numero entero positivo, en caso contrario sigue pidiendo el numero entero hasta que sea valido."""
    seguirPidiendo = True
    while seguirPidiendo:
        try: 
            numero = int(input(mensaje))
            if numero>0:
                seguirPidiendo=False             
            else:
                print("El numero ingresado no era positivo, no es válido.")
        except ValueError:
            print('Error, dato inválido.\nInténtelo nuevamente.')
    return numero

def sumar_y_promediar(limite):
    """luego permite ingresar esa cantidad de numeros, finalmente muestra su suma y su promedio"""
    suma = 0
    for i in range(limite):
        numero = leer_entero_positivo(f"Numero {i+1}: ")
        suma += numero
    print(f"La suma es: {suma} y el promedio es: {suma/limite}")

print("Pasamos a la solución mejorada:")
cantidad = leer_entero_positivo("Hola, ¿Cuántos numeros querés sumar?: ")
sumar_y_promediar(cantidad)

# 9 ---------------------------------------------
# Posible mejora

def leer_entero_positivo(mensaje):
    """Muestra el mensaje, espera un ingreso de teclado y valida que sea un numero entero positivo, en caso contrario sigue pidiendo el numero entero hasta que sea valido."""
    seguirPidiendo = True
    while seguirPidiendo:
        try: 
            numero = int(input(mensaje))
            if numero>0:
                seguirPidiendo=False             
            else:
                print("El numero ingresado no era positivo, no es válido.")
        except ValueError:
            print('Error, dato inválido.\nInténtelo nuevamente.')
    return numero

def imprimir_multiplos(nro, inicio, fin):
    for i in range(inicio, fin+1):
        if i % nro == 0:
            print(i, end=" ")
    print()


print("Pasamos a la solución mejorada:")
nroA = leer_entero_positivo("Ingrese el numero A: ")
nroB = leer_entero_positivo("Ingrese el numero B: ")
nroX = leer_entero_positivo("Ingrese el numero 'X' para buscar sus multiplos entre A y B: ")
imprimir_multiplos(nroX, nroA, nroB)

# 10 ---------------------------------------------
# posible solucion mejorada, validar datos de entrada
def pedir_lado_menor_a_40(mensaje):
    """Muestra el mensaje, espera un ingreso de teclado y valida que sea un numero entero positivo, en caso contrario sigue pidiendo el numero entero hasta que sea valido."""
    seguirPidiendo = True
    while seguirPidiendo:
        try: 
            numero = int(input(mensaje))
            if numero>0 and numero <=40:
                seguirPidiendo=False             
            else:
                print("El numero ingresado no está dentro del rango pedido.")
        except ValueError:
            print('Error, dato inválido.\nInténtelo nuevamente.')
    return numero

def dibujar_rectangulo(simbolo):
    """Dibuja un rectangulo con el simbolo indicado"""
    base=pedir_lado_menor_a_40("Ingrese la medida de la base: ")
    altura = pedir_lado_menor_a_40("Ingrese la medida de la altura: ")
    for i in range(0, altura):
        print(simbolo*base)
    

print("Pasamos a la solución mejorada:")
# tomamos el primer caracter de lo que ingrese el usuario:
car = input('Ingrese un caracter: ')[0]
dibujar_rectangulo(car)


# 11 ---------------------------------------------
# posible solucion mejorada

def leer_entero(mensaje):
    """Muestra el mensaje, espera un ingreso de teclado y valida que sea un numero entero, en caso contrario sigue pidiendo el numero entero hasta que sea valido."""
    seguirPidiendo = True
    while seguirPidiendo:
        try: 
            numero = int(input(mensaje))
            seguirPidiendo=False 
        except ValueError:
            print('Error, dato inválido.\nInténtelo nuevamente.')
    return numero

def pedir_numeros_mostrar_suma_promedio():
    suma=0
    contador=0
    nro = leer_entero("Ingresa un numero, para terminar ingresá un numero negativo: ")
    while nro >= 0:
        suma += nro
        contador += 1
        nro = leer_entero("Ingresa un numero, para terminar ingresá un numero negativo: ")
    
    if contador>0:
        print(f"Se ingresaron {contador} numeros, la suma es: {suma}, y el promedio: {(suma/contador):.2f}")
    else:
        print("No se ingresaron numeros positivos.")
    
print("Pasamos a la solución mejorada:")
pedir_numeros_mostrar_suma_promedio()