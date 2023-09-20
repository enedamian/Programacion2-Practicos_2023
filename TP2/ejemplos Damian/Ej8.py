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

def cargar_datos_de_productos():
    ruta = r"c:\Programacion2\productos.txt"
    lista_productos=[]
    with open(ruta, 'r') as archivo:
        for linea in archivo:
            producto = linea.split(";")
            dic_prod = {"codigo":producto[0], "nombre":producto[1], "precio":int(producto[2])}
            lista_productos.append(dic_prod)
            print(lista_productos[len(lista_productos)-1])
    return lista_productos

def cargar_datos_stock():
    ruta = r"c:\Programacion2\stock.txt"
    lista_stock=[]
    with open(ruta, 'r') as archivo:
        for linea in archivo:
            stock = linea.split(";")
            # formato “codigo de producto; stock mínimo; stock real”
            dic_prod = {"codigo":stock[0], "stock_minimo":int(stock[1]), "stock_real":int(stock[2])}
            lista_stock.append(dic_prod)
            print(lista_stock[len(lista_stock)-1])
    return lista_stock

def generar_archivo_compras():
    ruta = r"c:\Programacion2\compras.txt"
    lista_productos = cargar_datos_de_productos()
    lista_stock = cargar_datos_stock()
    lista_compras = []
    for producto in lista_productos:
        for stock in lista_stock:
            if producto["codigo"] == stock["codigo"] and stock["stock_minimo"] >= stock["stock_real"]:
                lista_compras.append(producto)
    
    with open(ruta, 'w') as archivo:
        for producto in lista_compras:
            archivo.write(producto["codigo"]+";"+producto["nombre"]+"\n")


generar_archivo_compras()



