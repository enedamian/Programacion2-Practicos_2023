lista_dicc = [{'nombre_apellido':"Matias Cappa",'legajo':11111,'nota_parcial1':60 ,'nota_parcial2':90,'nota_final':75},
              {'nombre_apellido':"J A",'legajo':10101,'nota_parcial1':90,'nota_parcial2':10,'nota_final':50},
              {'nombre_apellido':"M B",'legajo':98764,'nota_parcial1':50,'nota_parcial2':80,'nota_final':65}]
lista_nueva = [elem['nombre_apellido'] for elem in lista_dicc for a,b in elem.items() if (a=="nota_parcial1" and b>=90) or(a=="nota_parcial2" and b>=90)]
print(lista_nueva)
"""
alumnos =[{"nombre":"pepe","nota1":90, "nota2":84}, {"nombre":"pepe2","nota1":50, "nota2":94},{"nombre":"pepe3","nota1":80, "nota2":84}]
nombres = [elem["nombre"] for elem in alumnos if (elem["nota1"]>=90) or (elem["nota2"]>=90)]
print(nombres)
"""