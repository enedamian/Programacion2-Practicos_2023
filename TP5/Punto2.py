#crear las funciones genéricas que nos permitirán manejar una pila de datos.
def apilar(pila,elemento): #agrega elemento encima de la pila
    pila.append(elemento)

def desapilar(pila,elemento): #devuelve el elemento en la cima de la pila y lo elimina de la pila
    if not esta_vacia(pila):
        return pila.pop()
    else:
        return "La pila esta vacia."   
         
def longitud(pila): #devuelve la longitud de la estructura (pueden reutilizar el del punto anterior)
    return len(pila)

def esta_vacia(pila): #devuelve True si la estructura está vacía (pueden reutilizar el del punto anterior)
    return len(pila) == 0