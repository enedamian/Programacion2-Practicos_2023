# Inicializar una cola vacía como una lista
cola = []
# Función para agregar un elemento a la cola (encolar)
def encolar(cola, elemento):
    cola.append(elemento)

# Función para eliminar y retornar el elemento más antiguo de la cola 
def desencolar(cola):
    if not is_empty(cola):
        return cola.pop(0)
    else:
        return "La cola está vacía"
# Función para verificar si la cola está vacía
def is_empty(cola):
    return len(cola) == 0
# Función para obtener el tamaño de la cola
def size(cola):
    return len(cola)

encolar(cola,"Tarea 1")
encolar(cola, "Tarea 2")
encolar(cola, "Tarea 3")

print("Tamaño de la cola:", size(cola))

print("Elementos de la cola (desde el inicio hasta el final):")
while not is_empty(cola):
    print(desencolar(cola))

print("Tamaño de la cola después de hacer pop:", size(cola))