# Inicializar una pila vacía como una lista
pila = []

# Función para agregar un elemento a la pila (apilar)
def apilar(elemento):
    pila.append(elemento)

# Función para eliminar y retornar el elemento en la cima de la pila (desapilar)
def desapilar():
    if not is_empty():
        return pila.pop()
    else:
        return "La pila está vacía"

# Función para verificar si la pila está vacía
def is_empty():
    return len(pila) == 0

# Función para obtener el tamaño de la pila
def size():
    return len(pila)

# Ejemplo de uso
apilar(1)
apilar(2)
apilar(3)

print("Tamaño de la pila:", size())

print("Elementos de la pila (desde la cima hacia abajo):")
while not is_empty():
    print(desapilar())

print("Tamaño de la pila después de hacer desapilar:", size())