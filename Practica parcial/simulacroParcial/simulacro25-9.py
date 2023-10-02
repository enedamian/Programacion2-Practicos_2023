DireccionArchivo = "Practica parcial\simulacroParcial\datos.csv"
# complete con su fecha de nacimiento, nombre , legajo y dni
# Al finalizar subir el archivo al aula virtual.
mifecha='17-07-2000'  
minombre='Gianluca Fagherazzi'
milegajo=21813
midni=42708929
# 1) implemente una funcion hashFecha(stringfecha) y sume el numero del día, el numero del mes y el numero del año y devuelva el resto de dividirlo por 3.
# ejemplo fecha 01-01-1989 = (01+ 01 +1989) % 3 = 1992 % 3 = 2

def hashFecha(stringfecha):
    lista_fecha = [int(fecha) for fecha in stringfecha.split("-")]
    suma_fecha = sum(lista_fecha) % 3
    return suma_fecha

print(hashFecha(mifecha))
# 2) Explique el funcionamiento y describa el algoritmo de ordenamiento que le corresponda según su resultado anterior: 0=burbuja, 1=inserción, 2=selección.    
# Funcionamiento: Teniendo una lista...
# Algoritmo: ...compara...

# Algoritmo de seleccion:
# teniendo una lista, busca el elemento mas pequeño de esta, y lo posiciona primero. luego busca el siguiente
# elemento mas pequeño, y lo pone en el siguiente lugar, y asi hasta que ordena toda la lista

# 3)  Usando el archivo CSV "datos.csv" que contiene información sobre productos. El archivo tiene el siguiente formato:
# Nombre, Precio, Cantidad
# Producto1, 10.99, 50
# Producto2, 5.99, 30
# Producto3, 8.49, 75

#Crea una lista de diccionarios donde cada diccionario represente un producto. Los diccionarios deben tener tres claves: "Nombre" del tipo string, "Precio" del tipo float 
# y "Cantidad" del tipo entero, y  los valores deben corresponder a los datos del archivo CSV

def crearStock(archivo):
    with open(archivo,"r") as archivo_productos:   
        lista_productos = []
        for linea in archivo_productos:
            Nombre_producto, Precio, Cantidad = linea.split(",")
            Precio = float(Precio)
            Cantidad = float(Cantidad)
            Producto = {"Producto":Nombre_producto, "Precio":Precio, "Cantidad":Cantidad}
            lista_productos.append(Producto)
    return lista_productos

from functools import reduce

# 4) Crear dos funcion que utilizando la estructura del punto 3, una que nos devuelva el producto mas caro y la otra que nos devuelva el producto con menor cantidad.
def productoMasCaro(lista):
    Nombre_Mas_caro = reduce(lambda x, y: x if x["Precio"] > y["Precio"] else y, lista)
    return Nombre_Mas_caro

def productoMenorCantidad(lista):
    MenorCantidad = reduce(lambda x, y: x if x["Cantidad"] < y["Cantidad"] else y, lista)
    return MenorCantidad

# print(productoMasCaro(crearStock(DireccionArchivo)))
# print(productoMenorCantidad(crearStock(DireccionArchivo)))

# 5) Implemente una funcion que nos devuelva el total de la posible ganancia. Esto es, Cantidad * Precio para cada producto y que sume todos los resultados. (¿Se puede usar reduce? Fundamente)
def totalGanancia(lista):
    #GananciaPosible = sum(x["Precio"] * x["Cantidad"] for x in lista)
    GananciaPosible = reduce(lambda x, y: x + (y["Precio"] * y["Cantidad"]) ,lista, 0)
    return GananciaPosible
    
#print(totalGanancia(crearStock(DireccionArchivo)))

#si se puede utilizar reduce para realizar esa funcion, como esta en el ejemplo

