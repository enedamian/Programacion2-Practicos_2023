estudiante_1 = {
    "nombre": "Federico",
    "legajo": 10283,
    "nota_parcial1": 90,
    "nota_parcial2": 100,
    "nota_final": 95
}
estudiante_2 = {
    "nombre": "Jose",
    "legajo": 20586,
    "nota_parcial1": 89,
    "nota_parcial2": 76,
    "nota_final": 85
    }

estudiantes = [estudiante_1, estudiante_2]

def notas_mas_altas(estudiantes):
    return [estudiante["nombre"] for estudiante in estudiantes if estudiante["nota_parcial1"] > 90 or estudiante["nota_parcial2"] > 90 or estudiante["nota_final"] > 90]

print(notas_mas_altas(estudiantes))