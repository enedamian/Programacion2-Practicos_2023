estudiantes = [
    {"nombre" : "Gonzalo", "legajo" : 21547, "nota1" : 93, "nota2" : 68, "nota3" : 32},
    {"nombre" : "Juan", "legajo" : 35647, "nota1" : 16, "nota2" : 95, "nota3" : 90},
    {"nombre" : "Pepe", "legajo" : 22457, "nota1" : 84, "nota2" : 16, "nota3" : 16} 
    ]

lista_masnoventa = [estud for estud in estudiantes if estud["nota1"] > 90]

print (lista_masnoventa)

