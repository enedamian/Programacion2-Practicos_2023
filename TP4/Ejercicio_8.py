lista = [9.2, 16.5, 35.2, 40.0]

convertir_a_fahreheit = list(map(lambda x: (x*9/5)+32, lista))
print(convertir_a_fahreheit)