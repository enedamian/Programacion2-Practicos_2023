# complete con su fecha de nacimiento, nombre , legajo y dni
# Al finalizar subir el archivo al aula virtual.
mifecha='00-00-0000'  
minombre=''
milegajo=21000
midni=30000000
# 1) implemente una funcion hashFecha(stringfecha) y sume el numero del día, el numero del mes y el numero del año y devuelva el resto de dividirlo por 3.
# ejemplo fecha 01-01-1989 = (01+ 01 +1989) % 3 = 1992 % 3 = 2

def hashFecha(stringfecha):
    return 0

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
    lista=[]
    return lista

# 4) Crear dos funcion que utilizando la estructura del punto 3, una que nos devuelva el producto mas caro y la otra que nos devuelva el producto con menor cantidad.
def productoMasCaro(lista):
    return "nombre"
def productoMenorCantidad(lista):
    return "nombre"

# 5) Implemente una funcion que nos devuelva el total de la posible ganancia. Esto es, Cantidad * Precio para cada producto y que sume todos los resultados. (¿Se puede usar reduce? Fundamente)
def totalGanancia(lista):
    return 0