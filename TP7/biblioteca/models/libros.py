import os

libros = []
id_libro = 1
ruta_libros = 'models\\libros.csv'

def inicializar_libros():
    global id_libro
    if archivo_validado(ruta_libros):
        importar_libros()

def obtener_libros():
    return libros

def obtener_libro_por_id(id):
    print(f"Buscando libro con ID: {id}")
    for libro in libros:
        print(f"Comparando con libro existente: {libro['id']}")
        if isinstance(libro['id'], int) and libro['id'] == id:
            print('id encontrado')
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

    return libros[-1]   #devuelve el primer elemento de la lista, o sea el título recién creado

def editar_libro(id, titulo, autor, anio_publicacion):
    for libro in libros:
        if libro['id'] == id:
            libro = {
                'titulo': titulo,
                'autor': autor,
                'anio_publicacion' : anio_publicacion
            }
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
        for i, linea in enumerate(archivo):             # uso el enumarate archivo para enumerar cada fila
            if i > 0:   # Omitir primera linea
                linea_separada = linea.strip().split(',')
                libro = {
                    'id': linea_separada[0],
                    'titulo': linea_separada[1],
                    'autor': linea_separada[2],
                    'anio_publicacion': linea_separada[3]
                }
                libros.append(libro)
            else:
                print(f"Error en el formato de línea: {linea}")
    if len(libros) > 0:
        id_libro = int(libros[-1]['id']) + 1
    else:
        id_libro = 1

def exportar_libro(ruta):
    with open(ruta, 'w', encoding='UTF-8') as archivo:
        campos = ['id', 'titulo', 'autor', 'anio_publicacion']
        