while True:
    palabra=input("Ingrese una palabra: ").lower()

    if palabra=='salir':
        break
    
    vocales=[letra for letra in palabra if letra in 'aeiou']

    cantidadvocales=len(vocales) #len devuelve la cantidad de vocales

    print(f"La palabra {palabra} contiene una cantidad de {cantidadvocales} vocales")



