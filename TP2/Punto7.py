""" Un almacén guarda los códigos, los nombres de los productos y sus precios,
respectivamente, separados por punto y coma ( ; ) en el archivo productos.txt. Hacer
un algoritmo y luego los procedimientos necesarios que permitan tomar los datos del
archivo y buscar el precio de un artículo ingresado por teclado. Para probar el
algoritmo crear un archivo “productos.txt” y cargarle datos al estilo:
100;arroz;10
102;fideos;5
135;lentejas;8
138;porotos;6
140;sal gruesa;5
201;aceite;20 ( etc… ) """

def ingreso_alumnos():
    salir = True
    while(salir):
        try:
            archivo = open("C:\Archivos de código\programacion2\Trabajo Practico 2\productos.txt", "r")
            contenido = archivo.readlines()
            lista_diccionarios_productos = list()
            for linea in contenido:
                lista = linea.split(";")
                print(lista)
                lista_diccionarios_productos.append({"Codigos" : lista[0], "Producto": lista[1], "Precio": lista[2]})
            print(lista_diccionarios_productos)
            archivo.close() 
            salir = False
        except:
            print("No se pudo abrir el archivo") 
            salir=False 
   
    return lista
ingreso_alumnos()