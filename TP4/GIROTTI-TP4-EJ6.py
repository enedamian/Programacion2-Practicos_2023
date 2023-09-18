lista_celsius = [39,25,15,32,12]
lista_farenheit = list(map(lambda x: (x*1.8)+32, lista_celsius))
print(lista_farenheit)