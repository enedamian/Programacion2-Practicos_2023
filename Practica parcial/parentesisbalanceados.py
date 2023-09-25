def estan_parentesis_y_llaves_balanceados(cadena):
    pila = []
    for caracter in cadena:
        if caracter in '({[':
            pila.append(caracter)
        elif caracter in '])}':
            if pila == []:
                return False  # No hay un paréntesis o llave abierta correspondiente
            tope = pila.pop()
            if (caracter == ')' and tope != '(') or (caracter == '}' and tope != '{') or (caracter == ']' and tope != '['):
                return False  # No hay un paréntesis o llave abierta correspondiente
    return len(pila) == 0  # La pila debe estar vacía al final


# Ejemplo de uso
cadena1 = "({[]})"
cadena2 = "({[}])"
cadena3 = "({)}"

print("Cadena 1 está balanceada:", estan_parentesis_y_llaves_balanceados(cadena1))
print("Cadena 2 está balanceada:", estan_parentesis_y_llaves_balanceados(cadena2))
print("Cadena 3 está balanceada:", estan_parentesis_y_llaves_balanceados(cadena3))

