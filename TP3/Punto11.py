"""Dada una lista de diccionarios que contienen información de estudiantes de una materia 
(nombre_apellido, legajo, nota_parcial1, nota_parcial2, nota_final), 
crea una lista que contenga los nombres de todos los estudiantes que han 
obtenido una calificación superior a 90 en al menos un examen utilizando list comprehensions."""

# Lista de diccionarios de estudiantes
estudiantes = [
    {"nombre_apellido": "Juan Pérez", "legajo": 1001, "nota_parcial1": 85, "nota_parcial2": 92, "nota_final": 80},
    {"nombre_apellido": "María López", "legajo": 1002, "nota_parcial1": 78, "nota_parcial2": 88, "nota_final": 83},
    {"nombre_apellido": "Pedro Gómez", "legajo": 1003, "nota_parcial1": 92, "nota_parcial2": 88, "nota_final": 95}
]

# Utiliza una comprensión de lista para obtener los nombres de estudiantes con calificación superior a 90 en al menos un examen
nombres_calificacion_superior_90 = [estudiante["nombre_apellido"] for estudiante in estudiantes if estudiante["nota_parcial1"] > 90 or estudiante["nota_parcial2"] > 90 or estudiante["nota_final"] > 90]

# Imprime la lista de nombres
print(nombres_calificacion_superior_90)
