def cargar_archivo(ruta, cantidad_espacios):
   try:
        archivo = open(ruta, 'r')
        contenido = archivo.readlines()
        lista_diccionarios = []

        # Obtiene los nombres de las columnas de la primera línea
        nombres_columnas = contenido[0].strip().split(';')

        # Itera sobre las líneas restantes
        for linea in contenido[1:]:
            valores = linea.strip().split(';')

            # Crea un diccionario usando los nombres de las columnas como claves
            diccionario = {nombres_columnas[i]: valores[i] for i in range(len(nombres_columnas))}
            lista_diccionarios.append(diccionario)

        return lista_diccionarios
   
   except FileNotFoundError:
        print("Error: El archivo no se encontró.")
        return []

ruta = r"Programacion2-Practicos\TP5\alumnos.csv"
alumnos = cargar_archivo(ruta, 3)

ruta = "Programacion2-Practicos\TP5\eventos.csv"
eventos = cargar_archivo(ruta, 4)

ruta = "Programacion2-Practicos\TP5\deportes.csv"
deportes = cargar_archivo(ruta, 2)

ruta = r"Programacion2-Practicos\TP5\alumnos_deportes.csv"
alumnos_deportes = cargar_archivo(ruta, 2)

ruta = "Programacion2-Practicos\TP5\inscripciones.csv"
inscripciones = cargar_archivo(ruta, 2)

def encolar(cola,elemento): #agrega elemento al final de la cola
    cola.append(elemento)

#funciones pana juan 

def comparar_valores_clave(list1, list2, clave):
    # Obtener una lista de los valores de la clave en la primera lista
    valores_list1 = [diccionario[clave] for diccionario in list1]
    #Iterar a través de la segunda lista y verificar si algún valor coincide
    for diccionario in list2:
        if diccionario[clave] in valores_list1:
            return True
    #Si no se encuentra ninguna coincidencia, devolver False
    return False

def chequeo_dni_deporte_evento (alumnos, eventos, deportes, inscripciones):
    if comparar_valores_clave(inscripciones, alumnos, "alumno_dni"): #dni exista en alumnos
        if comparar_valores_clave(inscripciones, eventos, "evento_codigo"): #código de evento exista en eventos
            if comparar_valores_clave(eventos, deportes, "deporte_codigo"): #código de deporte exista en deportes
                if alumno_hace_deporte(inscripciones, alumnos_deportes, eventos):
                    return True
                else:
                    return False
            
def alumno_hace_deporte(inscrip, alum_deportes, event):
    for inscriptos in inscrip:
        if inscriptos["alumno_dni"] == alumnos_deportes["alumno_dni"]:
            if event["evento_codigo"] == alum_deportes["deporte_codigo"]:
                return True
            else:
                return False


if chequeo_dni_deporte_evento(alumnos, eventos, deportes, inscripciones):
    print("todo ok")
    if alumno_hace_deporte(inscripciones, alumnos_deportes, eventos):
        print("alumno hace deporte")