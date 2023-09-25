# el siguiente código fue hecho entre todos en la clase del 4/9 y se puede mejorar
# reescribir el código para que sea más eficiente y más legible
"""
- Crear una lista que contenga todas las palabras del texto.
- Contar la frecuencia de aparición de cada palabra en el texto.
- Encontrar la palabra más frecuente y la palabra menos frecuente en el texto.
- Encuentra la longitud promedio de las palabras en el texto.
- Imprimir las estadísticas generadas.
"""
import os

def existe_archivo(ruta):
    """Devulve True si el archivo existe, y False en caso contrario"""
    if os.path.isfile(ruta):
        return True 
    else:
        return False

def generar_lista_sin_signos(lista):
    lista_limpia =[]
    for palabra in lista:
        lista_limpia.append(palabra.strip(" ,.¡!¿?\n").lower())
    return lista_limpia

def generar_lista_palabras(ruta_archivo):
    """Devueelve la li de palabras contenidas en el archivo de texto que se ingresa por parametro"""
    if existe_archivo(ruta_archivo):
        archivo = open(ruta_archivo, 'r', encoding="utf-8")
        lista_palabras = []
        for linea in archivo:
            lista_aux = linea.split(" ")
            lista_palabras += generar_lista_sin_signos(lista_aux)
        archivo.close()
        return lista_palabras
    else:
        return []

def contar_frecuencia_palabras(lista):
    """Devuelve un diccionario con la cantidad de aparicion de cada palabra en la lista"""
    dic_palabras = {} #es lo mismo que = dict()
    for palabra in lista:
        if palabra in dic_palabras:
            dic_palabras[palabra] += 1
        else:
            dic_palabras[palabra] = 1 
    return dic_palabras

def buscar_palabra_mas_frecuente(diccionario):
    """devuelve la llave de la palabra mas frecuente"""
    frec_mayor=0
    llave_mayor=""
    for llave in diccionario:
        if diccionario[llave] > frec_mayor and len(llave)>2:
            frec_mayor = diccionario[llave]
            llave_mayor = llave
    return llave_mayor

def calcular_longitud_promedio_palabras(lista):
    suma=0
    for palabra in lista:
        suma += len(palabra)
    return int(suma/len(lista))

def buscar_palabra_menos_frecuente(diccionario):
    """devuelve la llave de la palabra menos frecuente"""
    frec_menor=150
    llave_menor=""
    for llave in diccionario:
        if diccionario[llave] < frec_menor and len(llave)>2:
            frec_menor = diccionario[llave]
            llave_menor = llave
    return llave_menor

def generar_lista_palabras_menos_frecuentes(diccionario):
    frec_menor=0
    for llave in diccionario:
        if frec_menor == 0 and len(llave)>2:
            frec_menor = diccionario[llave]        
        if diccionario[llave] < frec_menor and len(llave)>2:
            frec_menor = diccionario[llave]
    
    print(frec_menor)
    lista_palabras_poco_frec = []
    for llave in diccionario:
        if diccionario[llave] == frec_menor:
            lista_palabras_poco_frec.append(llave)
    return lista_palabras_poco_frec

nombre_de_archivo = input("Ingrese la ruta al archivo que desea analizar: ")
lista_palabras = generar_lista_palabras(nombre_de_archivo)
dic_frecuencia_palabras = contar_frecuencia_palabras(lista_palabras)
palabra_mas_frec = buscar_palabra_mas_frecuente(dic_frecuencia_palabras)
palabra_menos_frec = buscar_palabra_menos_frecuente(dic_frecuencia_palabras)
longitud_promedio_palabras=calcular_longitud_promedio_palabras(lista_palabras)
print("La palabra mas frecuente es: '", palabra_mas_frec,"' con", dic_frecuencia_palabras[palabra_mas_frec], "apariciones.")
print("La palabra menos frecuente es: '",palabra_menos_frec, "'")
lista_poco_frec = generar_lista_palabras_menos_frecuentes(dic_frecuencia_palabras)
print("las palabras menos frecuentes son:", lista_poco_frec)
print("La longitud promedio de las palabras es:", longitud_promedio_palabras)

# fin codigo clase 4-9 a mejorar
