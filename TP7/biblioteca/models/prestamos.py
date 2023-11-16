import os, csv, datetime

prestamos = []
id_prestamo = 1
ruta_prestamos = 'models\\prestamos.csv'

# --------------------------------- Funciones CRUD ---------------------------------
def inicializar_prestamos():
    global id_prestamo
    if validacion(ruta_prestamos):
        importar_prestamos()

def obtener_prestamos():
    return prestamos

def obtener_prestamo_por_id(id):
    for prestamo in prestamos:
        if prestamo['id'] == id:
            return prestamo
    return None

def crear_prestamo(socio_dni, libro_id, fecha_retiro, fecha_devolucion):
    global id_prestamo
    prestamos.append({
        'id': id_prestamo,
        'socio_dni': socio_dni,
        'libro_id': libro_id,
        'fecha_retiro': fecha_retiro,
        'fecha_devolucion': fecha_devolucion
    })
    id_prestamo += 1
    exportar_prestamo()
    return prestamos[-1]

def editar_prestamo(id, socio_dni, libro_id, fecha_retiro, fecha_devolucion):
    for prestamo in prestamos:
        if prestamo['id'] == id:
            prestamo = {
               'socio_dni': socio_dni,
                'libro_id': libro_id,
                'fecha_retiro': fecha_retiro,
                'fecha_devolucion': fecha_devolucion
            }
            exportar_prestamo()
            return prestamo
    return None

def eliminar_prestamo(id):
    global prestamos
    for prestamo in prestamos:
        if prestamo['id'] == id:
            prestamos.remove(prestamo)
            exportar_prestamo()
            return True

# ---------------------------- Funciones adicionales prestamo ----------------------------  
def obtener_prestamos_sin_devolver():
    prestamos_sin_devolver = []
    for prestamo in prestamos:
        if prestamo['fecha_devolucion'] == '' or datetime.datetime.strptime(prestamo['fecha_devolucion'], '%d-%m-%Y') > datetime.datetime.now():
            prestamos_sin_devolver.append(prestamo)
    return prestamos_sin_devolver

def libro_prestado(id_libro):
    prestamos_vigentes = obtener_prestamos_sin_devolver()
    for prestamo in prestamos_vigentes:
        if prestamo['libro_id'] == id_libro:
            return True
    return False

# --------------------------------- Funciones auxiliares ---------------------------------
def existe_prestamo(id):
    for prestamo in prestamos:
        if prestamo['id'] == id:
            return True
    return False

def validacion(ruta):
    return os.path.exists(ruta)

def importar_prestamos():
    global prestamos
    global id_prestamo
    prestamos = []

    with open(ruta_prestamos, 'r', encoding='UTF-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for linea in reader:
            prestamo = {
                'id': int(linea['id']),
                'socio_dni': int(linea['socio_dni']),
                'libro_id': int(linea['libro_id']),
                'fecha_retiro': linea['fecha_retiro'],
                'fecha_devolucion': linea['fecha_devolucion']
            }
            prestamos.append(prestamo)

        if len(prestamos) > 0:
            id_prestamo = prestamos[-1]['id'] + 1
        else:
            id_prestamo = 1

def exportar_prestamo():
    with open(ruta_prestamos, 'w', encoding='UTF-8') as csv_file:
        campos = ['id','socio_dni', 'libro_id', 'fecha_retiro', 'fecha_devolucion']
        writer = csv.DictWriter(csv_file, fieldnames=campos)
        writer.writeheader()
        for prestamo in prestamos:
            writer.writerow(prestamo)