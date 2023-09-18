estudiantesLista = [
    {"nombre_apellido": "Estudiante1", "legajo": 1111, "nota_parcial1": 85, "nota_parcial2": 88, "nota_final": 88},
    {"nombre_apellido": "Estudiante2", "legajo": 2222, "nota_parcial1": 88, "nota_parcial2": 91, "nota_final": 95},
    {"nombre_apellido": "Estudiante3", "legajo": 3333, "nota_parcial1": 78, "nota_parcial2": 80, "nota_final": 92},
    {"nombre_apellido": "Estudiante4", "legajo": 4444, "nota_parcial1": 69, "nota_parcial2": 42, "nota_final": 98},
]

nombres_con_calificacion_alta = [estudiante["nombre_apellido"] for estudiante in estudiantesLista if estudiante["nota_parcial1"] > 90 or estudiante["nota_parcial2"] > 90 or estudiante["nota_final"] > 90]

print(nombres_con_calificacion_alta)
