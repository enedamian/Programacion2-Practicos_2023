from functools import reduce

# complete con su fecha de nacimiento, nombre , legajo y dni
# Al finalizar subir el archivo al aula virtual.
mifecha='07-11-1989'
minombre='Sebastian Fell'
milegajo=21603
midni=34573130
# 1) implemente una funcion hashFecha(stringfecha) y sume el numero del día, el numero del mes y el numero del año y devuelva el resto de dividirlo por 3.
# ejemplo fecha 01-01-1989 = (01+ 01 +1989) % 3 = 1992 % 3 = 2

def esAnioBisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def esFechaValida(lista_fecha):
    if len(lista_fecha) != 3:
        return False
    try:
        dia = int(lista_fecha[0])
        mes = int(lista_fecha[1])
        anio = int(lista_fecha[2])
    except ValueError:
        return False
    if (mes < 1 or mes > 12) or (dia < 1 or dia > 31):
        return False
    if mes == 2 and (dia > 29 or (dia == 29 and not esAnioBisiesto(anio))):
        return False
    if mes in [4, 6, 9, 11] and dia > 30:
        return False
    return True

def hashFecha(stringfecha: str):
    lista_fecha = stringfecha.split("-")
    if not esFechaValida(lista_fecha):
        return -1
    return reduce(lambda x, y: int(x) + int(y), lista_fecha) % 3

print(hashFecha(mifecha)) #resultado: 0

# 2) Explique el funcionamiento y describa el algoritmo de ordenamiento que le corresponda según su resultado anterior: 0=burbuja, 1=inserción, 2=selección.

# Funcionamiento: El ordenamiento burbuja compara cada elemento con el siguiente y los intercambia si están en el orden incorrecto, repitiendo el proceso la cantidad de elementos que haya menos 1
# Algoritmo: El algoritmo primero recorre la lista n - 1 veces (siendo n la longitud de la lista). Dentro de dicho ciclo, recorre la lista nuevamente, pero esta vez una cantidad n-1-i veces (siendo i el índice del primer ciclo). Esto se hace porque con cada ciclo el último elemento ya queda ordenado y por lo tanto no es necesario compararlo (lo cual optimiza el código). Luego en cada paso se compara el elemento j (el indice del segundo bucle) con el elemento siguiente y si estos están desornados se intercambian.


# 3)  Usando el archivo CSV "datos.csv" que contiene información sobre productos. El archivo tiene el siguiente formato:
# Nombre, Precio, Cantidad
# Producto1, 10.99, 50
# Producto2, 5.99, 30
# Producto3, 8.49, 75

#Crea una lista de diccionarios donde cada diccionario represente un producto. Los diccionarios deben tener tres claves: "Nombre" del tipo string, "Precio" del tipo float
# y "Cantidad" del tipo entero, y  los valores deben corresponder a los datos del archivo CSV

def crearStock(ruta):
    try:
        archivo = open(ruta, "r")
        lista=[]
        for linea in archivo:
                datos = linea.split(",")
                lista.append({"Nombre": datos[0].strip(), "Precio": float(datos[1]), "Cantidad": int(datos[2])})
        archivo.close()
        return lista
    except FileNotFoundError:
        return []

# 4) Crear dos funcion que utilizando la estructura del punto 3, una que nos devuelva el producto mas caro y la otra que nos devuelva el producto con menor cantidad.
def productoMasCaro(lista):
    def mayorPrecio(x, y):
        if x["Precio"] > y["Precio"]:
            return x
        else:
            return y

    mas_caro = reduce(mayorPrecio, lista)
    return mas_caro["Nombre"]

def productoMenorCantidad(lista):
    def menorCantidad(x, y):
        if x["Cantidad"] < y["Cantidad"]:
            return x
        else:
            return y

    menor_cantidad = reduce(menorCantidad, lista)
    return menor_cantidad["Nombre"]

# 5) Implemente una funcion que nos devuelva el total de la posible ganancia. Esto es, Cantidad * Precio para cada producto y que sume todos los resultados. (¿Se puede usar reduce? Fundamente)
def totalGanancia2(lista):
    return reduce(lambda x,y: x + y["Precio"] * y["Cantidad"], lista, 0)