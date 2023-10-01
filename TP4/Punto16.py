""" Dada una lista de diccionarios con nombre, fecha de nacimiento,
y teléfono, crear una nueva lista con los diccionarios de las
personas que aún no cumplieron años respecto a la fecha actual
del sistema, y esa lista ordenarla por la fecha de nacimiento de
menor a mayor. Puede usar una lista como la siguiente: """
import datetime

lista_alumnos = [
    {"nombre":"Joaquin", "fecha_nacimiento":datetime.date(1990, 7, 2), "telefono":"123456789"},
    { "nombre":"Maria", "fecha_nacimiento":datetime.date(1995, 5, 16), "telefono":"123456789"}, 
    { "nombre":"Pedro", "fecha_nacimiento":datetime.date(1992, 9, 12), "telefono":"123456789"}, 
    { "nombre":"Ana", "fecha_nacimiento":datetime.date(1991, 9, 22), "telefono":"123456789"}, 
    { "nombre":"Florencia", "fecha_nacimiento":datetime.date(1994, 12, 8), "telefono":"123456789"}, 
    { "nombre":"Hector", "fecha_nacimiento":datetime.date(1993, 4, 4), "telefono":"123456789"}]

fecha_actual = datetime.date.today()

personas_no_cumplieron = [persona for persona in lista_alumnos if persona["fecha_nacimiento"] < fecha_actual]
#ordenamos la lista
personas_no_cumplieron.sort(key=lambda x: x["fecha_nacimiento"])

for persona in personas_no_cumplieron:
    print(f'Nombre: {persona["nombre"]}, Fecha de nacimiento: {persona["fecha_nacimiento"]}')