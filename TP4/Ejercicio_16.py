import datetime

lista_alumnos = [{"nombre":"Joaquin", "fecha_nacimiento":datetime.date(1990, 7, 2), "telefono":"123456789"}, { "nombre":"Maria", "fecha_nacimiento":datetime.date(1995, 5, 16), "telefono":"123456789"}, { "nombre":"Pedro", "fecha_nacimiento":datetime.date(1992, 9, 12), "telefono":"123456789"}, { "nombre":"Ana", "fecha_nacimiento":datetime.date(1991, 9, 22), "telefono":"123456789"}, { "nombre":"Florencia", "fecha_nacimiento":datetime.date(1994, 12, 8), "telefono":"123456789"}, { "nombre":"Hector", "fecha_nacimiento":datetime.date(1993, 4, 4), "telefono":"123456789"}]
fecha_actual = datetime.date.today()

# no_cumplen_anios = [alumno["nombre"] for alumno in lista_alumnos if (fecha_actual - alumno["fecha_nacimiento"]).days < 18*365]
no_cumplen_anios = sorted(
    filter(lambda x: (fecha_actual.month, fecha_actual.day) < (x['fecha_nacimiento'].month, x['fecha_nacimiento'].day), lista_alumnos)
)

for alumno in no_cumplen_anios:
    print(f"Nombre: {alumno['nombre']}, Fecha de Nacimiento: {alumno['fecha_nacimiento']}, Teléfono: {alumno['telefono']}")