""" Implemente un programa que le pida una palabra al usuario 
y cuenta la cantidad de vocales en ella. El programa deberá 
pedirle palabras al usuario hasta que éste introduzca 
la palabra “salir”. """

dict_nombres = dict()

def ingreso_palabras(mensaje):
    salir = True
    while(salir == True):
        try:
            nombre = input(mensaje)
            nombre = nombre.lower()
            if nombre == "salir":
                salir = False
            else:
                contador = 0
                vocales = ['a', 'e', 'i', 'o', 'u']
                for caracter in nombre:
                    if caracter in vocales:
                        contador += 1
                dict_nombres[nombre] = contador
        except:
            print("Error!")
            salir = False
    
ingreso_palabras("Ingrese una palabra: ")
print(dict_nombres)