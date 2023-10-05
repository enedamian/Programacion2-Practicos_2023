#split separa un string en una lista de subcadenas basandose en el separador especifico utilizado
frase = "Hola,esto,es,una,frase"
palabras = frase.split(',')

#strip elimina los caracteres que vos decidas colocar en caracteres, si no pones nada se eliminan los espacios de mas
#cadena.strip([caracteres])
texto = "   Hola, mundo   "
limpio = texto.strip()

print(limpio)
#"Hola, mundo"

#funcion para saber si un numero es primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

#listas
# lista[i] Devuelve el elemento que está en la posición i de la lista.
# lista.pop(i) Devuelve el elemento en la posición i de una lista y luego lo borra.
# lista.append(elemento) Añade elemento al final de la lista.
# lista.insert(i, elemento) Inserta elemento en la posición i.
# lista.remove(elemento) Elimina la primera vez que aparece elemento

#Diccionarios
# diccionario.get(‘key’): Devuelve el valor que corresponde con la key introducida.
# diccionario.pop(‘key’): Devuelve el valor que corresponde con la key introducida, y luego borra la key y el valor.
# diccionario.update({‘key’:’valor’}): Inserta una determinada key o actualiza su valor si ya existiera.
# «key» in diccionario: Devuelve verdadero (True) o falso (False) si la key (no los valores) existe en el diccionario.
