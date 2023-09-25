

# complete con su fecha de nacimiento, nombre , legajo y dni
# Al finalizar subir el archivo al aula virtual.
mifecha='27-07-2003'  
minombre='Jeremias'
milegajo=21974
midni=45064291
# 1) implemente una funcion hashFecha(stringfecha) y sume el numero del día, el numero del mes y el numero del año y devuelva el resto de dividirlo por 3.
# ejemplo fecha 01-01-1989 = (01+ 01 +1989) % 3 = 1992 % 3 = 2

def hashFecha(stringfecha):
    dia,mes,anio=map(int,stringfecha.split("-"))
    
    return  (dia + mes + anio) % 3

# 2) Explique el funcionamiento y describa el algoritmo de ordenamiento que le corresponda según su resultado anterior: 0=burbuja, 1=inserción, 2=selección.    
# Funcionamiento: Teniendo una lista...  
# Algoritmo: ...compara...
def burbuja():
    Burbuja="El Ordenamiento burbuja consiste en comparar cada elemento de la estructura con el siguiente e intercambiándolos si corresponde. esto se repite hasta q la estructura este ordenada "
    lista= [1,4,7,9,-1,-6,10]
    longitud= len(lista)
    for i in range(0,longitud):
        for j in range(0,longitud-1):
            if lista[j]%2==0 and lista[j+1]%2==1: # par  impar
                lista[j],lista[j+1]=lista[j+1],lista[j]
            elif lista[j]%2==1 and lista[j+1]%2==0: # impar  par
                pass
            elif lista[j]>lista[j+1]:# par  par   ||  impar impar
                lista[j],lista[j+1]=lista[j+1],lista[j]
    return Burbuja

# 3)  Usando el archivo CSV "datos.csv" que contiene información sobre productos. El archivo tiene el siguiente formato:
# Nombre, Precio, Cantidad
# Producto1, 10.99, 50
# Producto2, 5.99, 30
# Producto3, 8.49, 75

#Crea una lista de diccionarios donde cada diccionario represente un producto. Los diccionarios deben tener tres claves: "Nombre" del tipo string, "Precio" del tipo float 
# y "Cantidad" del tipo entero, y  los valores deben corresponder a los datos del archivo CSV

def crearStock(ruta):
    lista = [] 
    
    archivo = open(ruta, 'r', newline='') #abre archivo
    lector =archivo.readlines() # lee linea por linea
    #
    for linea in lector: # recorrer el archivo
        nombre, precio, cantidad = linea.strip().split(", ") 
        #.strip(): Este método se utiliza para eliminar cualquier espacio en blanco
        #.split(", "): Este método se utiliza para dividir la cadena en partes más pequeñas basadas en un delimitador.
        #En este caso, el delimitador es ", "
        producto = {"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)}
        lista.append(producto)# append agrega un diccionario producto a una lista llamada lista.
        #En este contexto, lista parece ser una lista que se utiliza para almacenar información sobre los productos.

    archivo.close()  # Cierra el archivo después de leer los datos

    return lista


# 4) Crear dos funcion que utilizando la estructura del punto 3, una que nos devuelva el producto mas caro y la otra que nos devuelva el producto con menor cantidad.
def productoMasCaro(lista):
    nombre= max(lista, key=lambda x: x['precio'])
    #max es una función en Python que se utiliza para encontrar el elemento máximo en una secuencia (como una lista)
    #key es un argumento opcional que permite especificar una función que se utilizará para calcular un valor de comparación para cada elemento en la lista antes de encontrar el máximo
    #lambda x: x['precio'] es una función lambda. Esta función toma un argumento x (que representa un elemento de la lista lista) y devuelve el valor de la clave 'precio' de ese elemento. En otras palabras, esta función lambda extrae el valor de 'precio' de cada elemento de la lista.
    return nombre['nombre']
def productoMenorCantidad(lista):
    nombre= min(lista, key=lambda x: x['cantidad'])
    return nombre

# 5) Implemente una funcion que nos devuelva el total de la posible ganancia. Esto es, Cantidad * Precio para cada producto y que sume todos los resultados. (¿Se puede usar reduce? Fundamente)
def totalGanancia(lista):
    return sum(producto["cantidad"] * producto["precio"] for producto in lista)

#1
print(hashFecha(mifecha))
#2
resultado = burbuja()
print(resultado)
#3
rutas = r"C:\Users\Jeremias\Desktop\materia-PROG2-git\Programacion2-Practicos\Practica parcial\simulacroParcial\datos.csv"
stock=crearStock(rutas)
            # Imprime el stock
for producto in stock:
    print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
#4
print("El producto mas caro es el " + productoMasCaro(stock))
print(f"El producto de menor cantidad es el {productoMenorCantidad(stock)}")
#5
print(f"El total de la posible ganancia es: {totalGanancia(stock)}")
