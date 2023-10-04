import datetime

lista_alumnos = [{"nombre":"Joaquin", "fecha_nacimiento":datetime.date(1990, 7, 2), "telefono":"123456789"}, { "nombre":"Maria", "fecha_nacimiento":datetime.date(1995, 5, 16), "telefono":"123456789"}, { "nombre":"Pedro", "fecha_nacimiento":datetime.date(1992, 9, 12), "telefono":"123456789"}, { "nombre":"Ana", "fecha_nacimiento":datetime.date(1991, 9, 22), "telefono":"123456789"}, { "nombre":"Florencia", "fecha_nacimiento":datetime.date(1994, 12, 8), "telefono":"123456789"}, { "nombre":"Hector", "fecha_nacimiento":datetime.date(1993, 4, 4), "telefono":"123456789"}]

listacumpleaños = list(filter(lambda x: x['fecha_nacimiento'] < datetime.date.today(), lista_alumnos))

listafinal=list(sorted(listacumpleaños, key=lambda x: x['fecha_nacimiento']))

print(listafinal)