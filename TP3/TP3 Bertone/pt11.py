"""Dada una lista de diccionarios que contienen información de estudiantes de una materia 
(nombre_apellido, legajo, nota_parcial1, nota_parcial2, nota_prom), 
crea una lista que contenga los nombres de todos los estudiantes que han obtenido una calificación 
superior a 90 en al menos un examen utilizando list comprehensions."""

alumnos = [
    {"nombre_apellido": "Lucas Bertone", "legajo": 1606, "nota_parcial1": 95, "nota_parcial2": 92, "nota_prom": 90},
    {"nombre_apellido": "Tiago Ferracutti", "legajo": 5813, "nota_parcial1": 56, "nota_parcial2": 100, "nota_prom": 89},
    {"nombre_apellido": "Kiara Salamanca", "legajo": 7777, "nota_parcial1": 92, "nota_parcial2": 98, "nota_prom": 98},
    {"nombre_apellido": "Ignacio Sotomayor", "legajo": 2161, "nota_parcial1": 76, "nota_parcial2": 67, "nota_prom": 78}
]

estudiantesConBuenaCalificacion=[estudiante["nombre_apellido"] for estudiante in alumnos if estudiante["nota_parcial1"]>90 or estudiante["nota_parcial2"]>90]

print(estudiantesConBuenaCalificacion)