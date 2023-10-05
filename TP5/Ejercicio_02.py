import random 

pila = []

def apilar(pila, elemento):
    pila.append(elemento)

def esta_vacia():
    return len(pila) == 0

def desapilar():
    if not esta_vacia():
        pila.pop()
    else:
        return "La pila está vacía"

def longitud(pila):
    return len(pila)

for _ in range(10):
    apilar(pila, random.randint(1, 100))
print("pila inicial: ", pila)

apilar(pila, 6)
print("pila: ", pila)

desapilar()
print("pila: ", pila)

print("La pila contiene ", longitud(pila), " elementos")