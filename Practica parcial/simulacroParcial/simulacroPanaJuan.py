from functools import reduce

# complete con su fecha de nacimiento, nombre , legajo y dni
# Al finalizar subir el archivo al aula virtual.
mifecha='22-09-2004'  
minombre='juan cruz montecino ruiz'
milegajo=21637
midni=45797939
# 1) implemente una funcion hashFecha(stringfecha) y sume el numero del día, el numero del mes y el numero del año y devuelva el resto de dividirlo por 3.
# ejemplo fecha 01-01-1989 = (01+ 01 +1989) % 3 = 1992 % 3 = 2

def hashFecha(stringfecha):
    dia,mes,anio = stringfecha.split('-')
    dia = float(dia)
    mes = float(mes)
    anio = float(anio)
    resultado = (dia + mes + anio) % 3
    return resultado

# 2) Explique el funcionamiento y describa el algoritmo de ordenamiento que le corresponda según su resultado anterior: 0=burbuja, 1=inserción, 2=selección.    
# Funcionamiento: Teniendo una lista...
# Algoritmo: ...compara...

# 3)  Usando el archivo CSV "datos.csv" que contiene información sobre productos. El archivo tiene el siguiente formato:
# Nombre, Precio, Cantidad
# Producto1, 10.99, 50
# Producto2, 5.99, 30
# Producto3, 8.49, 75

#Crea una lista de diccionarios donde cada diccionario represente un producto. Los diccionarios deben tener tres claves: "Nombre" del tipo string, "Precio" del tipo float 
# y "Cantidad" del tipo entero, y  los valores deben corresponder a los datos del archivo CSV

def crearStock(rutaArchivo):
    lista = []
    archivo = open(rutaArchivo, 'r', encoding= "utf-8")
    
    # Lee las líneas del archivo CSV y las guarda en lineas
    lineas = archivo.readlines()[:]
    
    for linea in lineas:
        nombre, precio, cantidad = linea.strip().split(',')
        producto = {
            "Nombre": nombre.strip(),
            "Precio": float(precio.strip()),
            "Cantidad": int(cantidad.strip())
        }
        lista.append(producto)
    
    # Cierra el archivo manualmente
    archivo.close()
    
    return lista


# 4) Crear dos funcion que utilizando la estructura del punto 3, una que nos devuelva el producto mas caro y la otra que nos devuelva el producto con menor cantidad.
def productoMasCaro(lista):

    productos_ordenados = sorted(lista, key=lambda producto: producto["Precio"], reverse=True)
    return productos_ordenados[0]["Nombre"], productos_ordenados[0]["Precio"]
    # precioMax = 0
    # for producto in lista:
    #    if producto["Precio"] > precioMax:
    #         precioMax = producto["Precio"]
    #         productoMasCaro = producto["Nombre"]

    # return productoMasCaro, precioMax

def productoMenorCantidad(lista):

    productos_ordenados = sorted(lista, key=lambda producto: producto["Cantidad"])
    return productos_ordenados[0]["Nombre"], productos_ordenados[0]["Cantidad"]
    # primer_producto = lista[0]
    # menor_cant =primer_producto["Cantidad"]
    # for producto in lista:
    #     if producto["Cantidad"] < menor_cant:
    #         menor_cant = producto["Cantidad"]
    #         prod_menor_cant = producto["Nombre"]
    # return prod_menor_cant, menor_cant

# 5) Implemente una funcion que nos devuelva el total de la posible ganancia. Esto es, Cantidad * Precio para cada producto y que sume todos los resultados. (¿Se puede usar reduce? Fundamente)
def totalGanancia(lista):
    return reduce(lambda acum,producto: acum+producto["Cantidad"]*producto["Precio"], lista, 0) # el 0 despues de la coma es el valor que toma x al inicio


resultado = hashFecha(mifecha)
ruta = input ("Ingrese la ruta del arhcivo CSV: ")
lista = crearStock(ruta)
producto_Mas_Caro,mayorprecio = productoMasCaro(lista)
producto_menor_cant,menorcant = productoMenorCantidad(lista)
gananciaTotal = totalGanancia(lista)

print("El producto mas caro es :",producto_Mas_Caro ,"con un precio de: ",mayorprecio)
print("El producto con menor cantidad es :",producto_menor_cant, "con una cantidad de: ",menorcant)
print("La ganancia total es: ",gananciaTotal)

