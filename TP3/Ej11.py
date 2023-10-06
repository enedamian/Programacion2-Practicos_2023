# 11. Dada una lista de diccionarios que contienen información de estudiantes de una materia (nombre_apellido, legajo, nota_parcial1, nota_parcial2, nota_final), crea una lista que contenga los nombres de todos los estudiantes que han obtenido una calificación superior a 90 en al menos un examen utilizando list comprehensions.

diccionario_estudiantes = {
    "Estudiante1": {
        "nombre_apellido": "Juan Pérez",
        "legajo": "001",
        "nota_parcial1": 85,
        "nota_parcial2": 92,
        "nota_final": 89
    },
    "Estudiante2": {
        "nombre_apellido": "María López",
        "legajo": "002",
        "nota_parcial1": 78,
        "nota_parcial2": 85,
        "nota_final": 80
    },
    "Estudiante3": {
        "nombre_apellido": "Pedro Gómez",
        "legajo": "003",
        "nota_parcial1": 92,
        "nota_parcial2": 88,
        "nota_final": 90
    },
    "Estudiante4": {
        "nombre_apellido": "Luisa Martínez",
        "legajo": "004",
        "nota_parcial1": 76,
        "nota_parcial2": 84,
        "nota_final": 79
    },
    "Estudiante5": {
        "nombre_apellido": "Ana Rodríguez",
        "legajo": "005",
        "nota_parcial1": 88,
        "nota_parcial2": 90,
        "nota_final": 89
    }
}

def estudiantes_con_calificacion_superior(diccionario_estudiantes):
    lista = [estudiante['nombre_apellido'] for estudiante in diccionario_estudiantes if any(nota > 90 for nota in (estudiante['nota_parcial1'], estudiante['nota_parcial2'], estudiante['nota_final']))]
    return print(lista)

estudiantes_con_calificacion_superior(diccionario_estudiantes)