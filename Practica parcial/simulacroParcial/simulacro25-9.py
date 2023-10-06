import os
from functools import reduce
# complete con su fecha de nacimiento, nombre , legajo y dni
# Al finalizar subir el archivo al aula virtual.
mifecha = input("Ingresar fecha de nacimiento: ")
minombre = input("Ingresar nombre: ")
milegajo = int(input("Ingresar número de legajo: "))
midni = int(input("Ingresar número de dni: "))
# 1) implemente una funcion hashFecha(stringfecha) y sume el numero del día, el numero del mes y el numero del año y devuelva el resto de dividirlo por 3.
# ejemplo fecha 01-01-1989 = (01+ 01 +1989) % 3 = 1992 % 3 = 2

def es_string_valido(nombre):
    repetir = True
    try:
        return nombre
    except ValueError:
        print("Debe ingresar un número entero positivo")

def es_fecha_valida(fecha):   
    if(len(fecha) != 3):
        return False
    
    try:
        dia = int(fecha[0])
        mes = int(fecha[1])
        anio = int(fecha[2])
    except ValueError:
        return False

    if (mes < 1 or mes > 12) or (dia < 1 or dia > 31) or (anio < 1900):
        return "Se ha ingresado o un dia o un mes o un año inexistentes. Por favor, intente de nuevo"
    elif (mes == 2 and dia > 28 and not es_anio_bisiesto(anio)) or (mes == 2 and dia > 29 and es_anio_bisiesto(anio)):
        return "No es un día válido para el mes de enero"
    elif mes in [4, 6, 9, 11] and dia > 30:
        return "El mes ingresado cuenta con menos de 31 dias"
    else:
        return True
    
def es_anio_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def hashFecha(stringfecha):
    fecha = stringfecha.split('-')
    if not es_fecha_valida(fecha):
        return -1
    return reduce(lambda x, y: int(x) + int(y), fecha) % 3   

print(hashFecha(mifecha))
# 2) Explique el funcionamiento y describa el algoritmo de ordenamiento que le corresponda según su resultado anterior: 0=burbuja, 1=inserción, 2=selección.    
# Funcionamiento: Teniendo una lista...
# Algoritmo: ...compara...

print("\nResultado = 1 → ordemaniento por inserción"   
"Funcionamiento: Teniendo una lista de elementos desordenados, se considera el primer elemento como ordenado y se compara con los siguientes elementos, por lo tanto va construyendo una lista ordenada. Posteriormente evalua uno por uno los elementos de la lista desordenada insertándolos en su posición correspondiente dentro de la parte ordenada de la lista."
"Algoritmo: compara el elemento actual con cada elemento de la parte ordenada de la lista y los siguientes elementos de la parte desordenada de la lista para luego ser insertados en la parte ordenada\n"
)

# 3)  Usando el archivo CSV "datos.csv" que contiene información sobre productos. El archivo tiene el siguiente formato:
# Nombre, Precio, Cantidad
# Producto1, 10.99, 50
# Producto2, 5.99, 30
# Producto3, 8.49, 75

#Crea una lista de diccionarios donde cada diccionario represente un producto. Los diccionarios deben tener tres claves: "Nombre" del tipo string, "Precio" del tipo float 
# y "Cantidad" del tipo entero, y  los valores deben corresponder a los datos del archivo CSV
def validar_archivo(ruta):
    return os.path.exists(ruta)

def crearStock(ruta):
    lista=[]

    if validar_archivo(ruta):
        with open(ruta, 'r', encoding = 'UTF-8') as archivo:
            for linea in archivo:
                linea_producto = linea.split(';')
                producto = {
                    'nombre': linea_producto[0],
                    'precio': float(linea_producto[1]),
                    'cantidad': int(linea_producto[2])
                }
                lista.append(producto)
        return lista
    else:
        print("El archivo ingresado no existe")

archivo = input("Ingrese la ruta para el archivo de datos: ")
lista = crearStock(archivo)
print(lista)

# 4) Crear dos funcion que utilizando la estructura del punto 3, una que nos devuelva el producto mas caro y la otra que nos devuelva el producto con menor cantidad.
def productoMasCaro(lista):
    return reduce(lambda x, y: x if x['precio'] > y['precio'] else y, lista)

def productoMenorCantidad(lista):
    return reduce(lambda x, y: x if x['cantidad'] < y['cantidad'] else y, lista)

        
print("\nEl producto más caro es: ", productoMasCaro(lista))
print("El producto con menor stock disponible es:", productoMenorCantidad(lista))

# 5) Implemente una funcion que nos devuelva el total de la posible ganancia. Esto es, Cantidad * Precio para cada producto y que sume todos los resultados. (¿Se puede usar reduce? Fundamente)
def totalGanancia(lista):
    total = 0
    
    for producto in lista:
        precio = producto['precio']
        cantidad = producto['cantidad']

        total += precio * cantidad

    return total

# solución con reduce

total_ganancia = reduce(lambda x, y: x + y['precio'] * y['cantidad'], lista, 0)
print("\nGanancias totales: ", total_ganancia)