import csv

def cargar_socios():
    socios = []
    with open('socios.csv', newline='') as csvfile:
        socios_csv = csv.reader(csvfile, delimiter=';')
        for socio in socios_csv:
            socios.append(socio)
    return socios

def obtener_socio_por_id(socios, id):
    for socio in socios:
        if socio[0] == id:
            return socio
    return None

def obtener_socios_por_nombre(socio, nombre):
    socios_nombre = []
    for socio in socios:
        if socio[1] == nombre:
            socios_nombre.append(socio)
    return socios_nombre

def obtener_socios_por_dni(socio, dni):
    socios_dni = []
    for socio in socios:
        if socio[2] == dni:
            socios_dni.append(socio)
    return socios_dni

def obtener_socios_por_email(socio, email):
    socios_email = []
    for socio in socios:
        if socio[3] == email:
            socios_email.append(socio)
    return socios_email

def obtener_socios_por_telefono(socio, telefono):
    socios_telefono = []
    for socio in socios:
        if socio[4] == telefono:
            socios_telefono.append(socio)
    return socios_telefono

def obtener_socio_por_apellido(socio, apellido):
    socios_apellido = []
    for socio in socios:
        if socio[1] == apellido:
            socios_apellido.append(socio)
    return socios_apellido
