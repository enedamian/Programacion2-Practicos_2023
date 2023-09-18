def contar_vocales(palabra):

    vocales = ['a', 'e', 'i', 'o', 'u']
    contador = 0
    vocaleslist =[letra for letra in palabra if letra.lower() in vocales contador+=1]
    return contador

while True:
    palabra = input("Ingrese una palabra o escriba 'salir' para terminar: ")
    
    if palabra.lower() == "salir":
        break
    
    cantidad_de_vocales = contar_vocales(palabra)
    
    print(f"La palabra '{palabra}' contiene {cantidad_de_vocales} vocales.".format(palabra, cantidad_de_vocales))
