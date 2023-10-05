import random 

cola = []

def encolar(cola, elemento):
    cola.append(elemento)

def desencolar(cola):
    if len(cola) == 0:
        print("La cola está vacía")
        return None
    else:
        return cola.pop(0)
    
def longitud(cola):
    return len(cola)

def esta_vacia(cola):
    return len(cola) == 0

# Llenar la cola con numeros aleatorios
for _ in range(10):
    encolar(cola, random.randint(1, 100))
print("Cola inicial: ", cola)

encolar(cola, 2)
print(cola)

elemento = desencolar(cola)

print("elemento desencolado: ", elemento)
print(cola)
print("longitud: ", longitud(cola))
if esta_vacia(cola):
    print("La lista está vacía")
else:
    print("La lista contiene elementos")