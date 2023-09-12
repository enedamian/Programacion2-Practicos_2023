def Edades(edad):
    dict_edades = {"Alberto": 61, "Juan": 31, "Ana": 17, "Pedro": 22}
    l_nombres_mayorEdad = [nombre for nombre,age in dict_edades.items() if age > edad]
    return l_nombres_mayorEdad

print(Edades(18))