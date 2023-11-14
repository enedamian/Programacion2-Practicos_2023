import os, csv

socios = []
id_socio = 1
ruta_socios = 'models\\socios.csv'

# --------------------------------- Funciones principales ---------------------------------
def inicializar_socios():
    global id_socio
    if validacion(ruta_socios):
        importar_socios()

def obtener_socios():
    return socios

def obtener_socio_por_id(id):
    for socio in socios:
        if socio['id'] == id:
            return socio
    return None

def crear_socio(dni, nombre, apellido, telefono, email):
    global id_socio
    socios.append({
        'id': id_socio,
        'dni': dni,
        'nombre': nombre,
        'apellido': apellido,
        'telefono': telefono,
        'email': email
    })
    id_socio += 1
    exportar_socio()
    return socios[-1]

def editar_socio(id, dni, nombre, apellido, telefono, email):
    for socio in socios:
        if socio['id'] == id:
            socio = {
                'dni': dni,
                'nombre': nombre,
                'apellido': apellido,
                'telefono': telefono,
                'email': email
            }
            exportar_socio()
            return socio
    return None

def eliminar_socio(id):
    global socios
    for socio in socios:
        if socio['id'] == id:
            socios.remove(socio)
            break
        exportar_socio()    

# --------------------------------- Funciones auxiliares ---------------------------------
def validacion(ruta):
    return os.path.exists(ruta)

def existe(id):
    global socios
    for socio in socios:
        if socio['id'] == id:
            return True
    return False

def importar_socios():
    global socios
    global id_socio
    socios = []

    with open(ruta_socios, 'r', encoding='UTF-8') as archivo:
        reader = csv.DictReader(archivo)
        for linea in reader:
            socio = {
                'id': int(linea['id']),
                'dni': int(linea['dni']),
                'nombre': linea['apellido'],
                'apellido': linea['apellido'],
                'telefono': linea['telefono'],
                'email': linea['email']
            }
            socios.append(socio)
    if len(socios)>0:
        id_socio= socios[-1]["id"]+1
    else:
        id_socio = 1

def exportar_socio():
    with open(ruta_socios, 'w', encoding='UTF-8') as csv_file:
        campos = ['id', 'dni', 'nombre', 'apellido', 'telefono', 'email']
        writer = csv.DictWriter(csv_file, fieldnames=campos)
        writer.writeheader()
        for socio in socios:
            writer.writerow(socio)