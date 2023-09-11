"""Implemente un programa que le pida una palabra al usuario y cuenta la cantidad de vocales en ella. 
El programa deberá pedirle palabras al usuario hasta que éste introduzca la palabra “salir”."""

palabra = ""
while palabra != "salir":
    palabra = input("ingrese una palabra distinta a salir para que se cuenten las vocales: ")
    palabra = palabra.lower()
    vocales = [letra for letra in palabra if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'] 
    print(f"palabra tiene {len(vocales)} vocales")
