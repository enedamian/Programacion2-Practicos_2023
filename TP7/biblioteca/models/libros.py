import os, csv

libros = []
id_libro = 1
ruta_libros = 'models\\libros.csv'

# --------------------------- Funciones principales ---------------------------
def inicializar_libros():
    global id_libro
    if archivo_validado(ruta_libros):
        importar_libros()

def obtener_libros():
    return libros

def obtener_libro_por_id(id):
    for libro in libros:
        if isinstance(libro['id'], int):
            if libro['id'] == id:
                return libro
    return None

def crear_libro(titulo, autor, anio_publicacion):
    global id_libro
    libros.append({
        'id': id_libro,
        'titulo': titulo,
        'autor': autor,
        'anio_publicacion': anio_publicacion
    })
    id_libro += 1
    exportar_libro()
    return libros[-1]   #devuelve el ultimo elemento de la lista, o sea el título recién creado

def editar_libro(id, titulo, autor, anio_publicacion):
    for libro in libros:
        if libro['id'] == id:
            libro = {
                'titulo': titulo,
                'autor': autor,
                'anio_publicacion' : anio_publicacion
            }
            exportar_libro()
            return libro
    return None     #devuelve None si no se encuentra el libro

# ---------------------------- Funciones auxiliares ----------------------------
def archivo_validado(ruta_archivo):
    return os.path.exists(ruta_archivo)

def importar_libros():
    global libros
    global id_libro
    libros = []

    with open(ruta_libros, 'r', encoding='UTF-8') as archivo:
        reader = csv.DictReader(archivo)    # lee filas csv y las devuelve como diccionarios
        for linea in reader:      
            libro = {
                'id': int(linea['id']),     # lee los valores de la key 'id', dado que el csv ahora se lee como un diccionario
                'titulo': linea['titulo'],
                'autor': linea['autor'],
                'anio_publicacion': int(linea['anio_publicacion'])
            }
            libros.append(libro)

    if len(libros) > 0:
        id_libro = libros[-1]['id'] + 1
    else:
        id_libro = 1

def exportar_libro():
    with open(ruta_libros, 'w', encoding='UTF-8') as csvfile:
        campos = ['id', 'titulo', 'autor', 'anio_publicacion']
        writer = csv.DictWriter(csvfile, fieldnames=campos)     # lo contrario al DictReader, esta función crea archivos csv a partir de un diccionario
        writer.writeheader()    # Crea cabecera
        for libro in libros:
            writer.writerow(libro)

def existe(id):
    global libros
    for libro in libros:
        if libro['id'] == id:
            return True
    return False