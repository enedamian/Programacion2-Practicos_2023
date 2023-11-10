# complete con su fecha de nacimiento, nombre , legajo y dni
# Al finalizar subir el archivo al aula virtual.
mifecha='18-12-2001'  
minombre='Mateo Abraham'
milegajo=21698
midni=43905325
# 1) implemente una funcion hashFecha(stringfecha) y sume el numero del día, el numero del mes y el numero del año y devuelva el resto de dividirlo por 3.
# ejemplo fecha 01-01-1989 = (01 + 01 + 1989) % 3 = 1992 % 3 = 2

from functools import reduce

def hashFecha(stringfecha):
    stringfecha = stringfecha.split("-")
    suma = reduce(lambda x, y: x + y, stringfecha)
    return int(suma) % 3
print(hashFecha(mifecha))
# 2) Explique el funcionamiento y describa el algoritmo de ordenamiento que le corresponda según su resultado anterior: 0=burbuja, 1=inserción, 2=selección.    
# Funcionamiento: Teniendo una lista desordenada, compara pares de elementos (uno al lado del otro) y los intercambia si est[an en el orden incorrecto.
# Algoritmo: Toma un par de elementos, los compara, si estan desordenados los ordena, sino los deja como estan, luego procede con el siguiente par hasta llegar al final. Ya en este punto, el ultimo elemento estara ordenado, asi que en la proxima iteracion este no se verificara.

# 3)  Usando el archivo CSV "datos.csv" que contiene información sobre productos. El archivo tiene el siguiente formato:
# Nombre, Precio, Cantidad
# Producto1, 10.99, 50
# Producto2, 5.99, 30
# Producto3, 8.49, 75
#Crea una lista de diccionarios donde cada diccionario represente un producto. Los diccionarios deben tener tres claves: "Nombre" del tipo string, "Precio" del tipo float 
# y "Cantidad" del tipo entero, y  los valores deben corresponder a los datos del archivo CSV
def crearStock(rutaArchivo):
    lista=[]
    try:
        archivo = open(rutaArchivo, 'r')
        for linea in archivo:
            producto = linea.strip().split(",")
            lista.append({"Nombre":producto[0], "Precio":float(producto[1]), "Cantidad":int(producto[2])})
        archivo.close
        return lista
    except FileNotFoundError:
        print("no se encontro el archivo")

print(crearStock("Programacion2-Practicos\Practica parcial\simulacroParcial\datos.csv"))

# 4) Crear dos funcion que utilizando la estructura del punto 3, una que nos devuelva el producto mas caro y la otra que nos devuelva el producto con menor cantidad.


# 5) Implemente una funcion que nos devuelva el total de la posible ganancia. Esto es, Cantidad * Precio para cada producto y que sume todos los resultados. (¿Se puede usar reduce? Fundamente)


#No se me ocurre otra forma en la que pueda usar reduce porque no es mi fuerte el manejo de listas de diccionarios jeje
#Pero se me ocurre otra opcion que seria sin usar reduce:

