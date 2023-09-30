texto = input("ingrese un texto: ")

contador = 0;

for caracter in texto: 
    if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
        contador += 1

print("La cantidad de vocales es: ", contador)