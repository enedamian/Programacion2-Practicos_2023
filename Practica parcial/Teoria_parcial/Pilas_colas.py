# Funciones para manejar una cola de datos
def encolar(cola, elemento):
    cola.append(elemento)
#le agrega un elemento a la cola

def desencolar(cola):
    if not esta_vacia(cola):
        return cola.pop(0)
    else:
        return None
#Devuelve el primer elemento de la cola y lo quita

def longitud(cola):
    return len(cola)
#Devuelve la longitud de una cola o pila

def esta_vacia(cola):
    return len(cola) == 0
#Devuelve verdaderi si la longitud de una cola o pila es 0 (o sea esta vacia)

# Funciones para manejar una pila de datos
def apilar(pila, elemento):
    pila.append(elemento)

def desapilar(pila):
    if not esta_vacia(pila):
        return pila.pop()
    else:
        return None
#Devuelve el ultimo elemento de la pila y lo borra de esta