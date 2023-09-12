def PedirPalabras():
    palabra = "hola"
    while(palabra != "salir"):
        palabra = input("Ingrese una palabra").lower()
        lista_vocales = [letra for letra in palabra if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"]
        print(len(lista_vocales))

PedirPalabras()        
    
