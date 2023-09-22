""" Dada una lista de diccionarios que contienen información de
estudiantes de una materia:
(nombre_apellido, legajo, nota_parcial1, nota_parcial2, nota_final),
crea una lista que contenga los nombres de todos los estudiantes que
han obtenido una calificación superior a 90 en al menos un examen 
utilizando list comprehensions. """

estudiantes = [
    {
        "nombre_apellido": "Juan Pérez",
        "legajo": "12345",
        "nota_parcial1": 85,
        "nota_parcial2": 78,
        "nota_final": 82
    },
    {
        "nombre_apellido": "María González",
        "legajo": "23456",
        "nota_parcial1": 90,
        "nota_parcial2": 88,
        "nota_final": 89
    },
    {
        "nombre_apellido": "Carlos Rodríguez",
        "legajo": "34567",
        "nota_parcial1": 75,
        "nota_parcial2": 100,
        "nota_final": 95
    },
]

lista_nombres = [estudiante["nombre_apellido"] for estudiante in estudiantes if estudiante["nota_parcial1"] > 90 or estudiante["nota_parcial2"] > 90]

print(lista_nombres)