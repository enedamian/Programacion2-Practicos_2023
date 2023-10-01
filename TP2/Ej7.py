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

def cargar_productos(ruta):
    archivo = open(ruta, "r")
    lista_productos = []

    for linea in archivo:
        datos = linea.split(";")

        productos = {
            "codigo": datos[0],
            "nombre": datos[1],
            "precio": int(datos[2])
        }

        lista_productos.append(productos)

    archivo.close()

    return lista_productos


def buscar_precio(lista_productos, producto_buscado):
    for producto in lista_productos:
        if producto["nombre"] == producto_buscado:
            return producto["precio"]
        
    return "Producto no encontrado"


archivo = cargar_productos("repo\Programacion2-Practicos\TP2\productos.csv")

producto_buscado = input("Ingrese el nombre del producto a buscar: ").lower()

if producto_buscado == 'arroz' or producto_buscado == 'fideos' or producto_buscado == 'lentejas' or producto_buscado == 'porotos' or producto_buscado == 'sal gruesa':
    precio = buscar_precio(archivo, producto_buscado)
    print(f"El precio de {producto_buscado} es: {precio}")
else:
    print("Producto no encontrado")