cadena = input("Ingrese una oracion: ")
contador = 0
for i in cadena:
    if i == " ":
        contador +=  1
print(f"La cantidad de espacios en la oracion ingresada es de: {contador}")
