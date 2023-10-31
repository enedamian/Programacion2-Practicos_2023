pila = [None] * 10
top = -1

def apilar(pila,elemento):
    global top
    if top + 1 == len(pila):
        print("Pila llena")
    else:
        top += 1
        pila[top] = elemento

def desapilar(pila,elemento):
    global top
    
    if top == -1:
        print("Pila vacia")
        return None
    elemento = pila[top]
    top -= 1

    return elemento

def pilaVacia(pila):
    return len(pila) == 0

def longitudPila(pila):
    return len(pila)