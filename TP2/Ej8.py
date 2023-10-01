"""El mismo almacén del punto anterior almacena los datos del stock de productos en
el archivo stock.txt separados por punto y coma ( ; ) con el formato “codigo de
producto; stock mínimo; stock real”. Escriba un programa, que a partir de
información contenida en los archivos, genere otro archivo de texto, Compras.txt,
conteniendo todos los productos cuyo stock se encuentra por debajo del mínimo.
Utilizar el archivo productos.txt del punto anterior, y crear un archivo stock.txt y
cargarle datos utilizando los códigos de los productos del archivo anterior. Ej:
100;50;60
102;50;20
135;20;15
138;20;20
140;10;8
201;20;30 ( etc… )"""


# mi solucion:

def cargar_productos(ruta):
    archivo = open(ruta, "r")
    lista_productos = []

    for linea in archivo:
        linea_producto = linea.split(";")

        productos = {
            "codigo": int(linea_producto[0]),
            "nombre": linea_producto[1],
            "precio": int(linea_producto[2])
        }

        lista_productos.append(productos)

    archivo.close()

    return lista_productos


def cargar_stock(ruta):
    archivo = open(ruta, "r")
    lista_stock = []

    for linea in archivo:
        linea_stock = linea.split(";")

        productos_stock = {
            "codigo": int(linea_stock[0]),
            "stock_minimo": int(linea_stock[1]),
            "stock_real": int(linea_stock[2])
        }

        lista_stock.append(productos_stock)
    
    archivo.close()
    
    return lista_stock


def generar_compras(lista_productos, lista_stock):
    ruta = r"repo\Programacion2-Practicos\TP2\Compras.txt"
    lista_compras = []

    for producto in lista_productos:
        for stock in lista_stock:
            if producto["codigo"] == stock["codigo"] and stock["stock_real"] < stock["stock_minimo"]:
                lista_compras.append(producto)
                
    archivo_compras = open(ruta, "w")
    archivo_compras.write("Codigo - Nombre\n")
    
    for compra in lista_compras:
        archivo_compras.write(f"{compra['codigo']};{compra['nombre']}\n")


ruta_productos = "repo\Programacion2-Practicos\TP2\productos.csv"
ruta_stock = "repo\Programacion2-Practicos\TP2\stock.csv"

lista_productos = cargar_productos(ruta_productos)
lista_stock = cargar_stock(ruta_stock)
generar_compras(lista_productos, lista_stock)
