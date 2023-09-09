"""Un almacén guarda los códigos, los nombres de los productos y sus precios,
respectivamente, separados por punto y coma ( ; ) en el archivo productos.txt. Hacer
un algoritmo y luego los procedimientos necesarios que permitan tomar los datos del
archivo y buscar el precio de un artículo ingresado por teclado. Para probar el
algoritmo crear un archivo “productos.txt” y cargarle datos al estilo:
100;arroz;10
102;fideos;5
135;lentejas;8
138;porotos;6
140;sal gruesa;5
201;aceite;20 ( etc… )"""

def cargar_datos_de_archivo():
    ruta = r"c:\Programacion2\productos.txt"
    lista_productos=[]
    with open(ruta, 'r') as archivo:
        for linea in archivo:
            producto = linea.split(";")
            dic_prod = {"codigo":producto[0], "nombre":producto[1], "precio":int(producto[2])}
            lista_productos.append(dic_prod)
            print(lista_productos[len(lista_productos)-1])
    return lista_productos

def buscar_precio(nombre_producto):
    precio = -1
    for producto in lista_productos:
        if producto["nombre"] == nombre_producto:
            precio = producto['precio']
    return precio


lista_productos = cargar_datos_de_archivo()
prod_buscado = input("Ingrese el nombre del producto que desea buscar: ")
precio = buscar_precio(prod_buscado)
if precio != -1:
    print(f"El precio de {prod_buscado} es {precio}.")
else:
    print("No se encontró el producto ingresado.")