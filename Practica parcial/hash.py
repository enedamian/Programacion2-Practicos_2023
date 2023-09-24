
def hash_simple(numero):
    """ funcion que retorna el resto de dividirlo por 10 """
    return numero % 10 #hash uniforme


def hash_simple2(cadena):
    """ funcion que retorna el valor de la suma de los valores ASCII de los caracteres de una cadena """
    suma = 0
    for caracter in cadena:
        suma += ord(caracter)
    return suma #hash no uniforme


def hash_un_poquito_complicado(cadena):
    """ funcion que retorna un valor para la cadena según los valores asignados a las vocales """
    diccionario = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}
    #opcion 0
    suma=0
    for letra in cadena:
        if letra.lower() == "a":
            suma += 1
        elif letra.lower() == "e":
            suma += 2
        elif letra.lower() == "i":
            suma += 3
        elif letra.lower() == "o":
            suma += 4
        elif letra.lower() == "u":
            suma += 5
    
    #opcion 1
    suma = 0
    for letra in cadena:
        if letra.lower() in "aeiou":
            suma += diccionario[letra]
    
    #opcion 2
    suma=0
    for letra in cadena:
        if letra.lower() in diccionario.keys():
            suma += diccionario[letra]
    # nos da la libertad de modificar el diccionario y no tener que modificar la funcion

    return suma % 5 # hash uniforme

# print(hash_simple(123))
# print(hash_simple(15639))
# print(hash_simple(12))
# print(hash_simple(165495521839))
# print(hash_simple(12198816514984652))

# print(hash_simple2("hola"))
# print(hash_simple2("chau"))
# print(hash_simple2("probando con una cadena muy muy muy muy larga"))

print(hash_un_poquito_complicado("hola"))
print(hash_un_poquito_complicado("chau"))
print(hash_un_poquito_complicado("probando con una cadena muy muy muy muy larga"))