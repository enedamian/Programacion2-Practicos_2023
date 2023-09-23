# Inicializar una cola vacía con una lista y dos índices
cola = [None] * 10  # Puedes ajustar el tamaño de la cola según tus necesidades
head = -1
tail = -1
# Función para agregar un elemento a la cola (encolar)
def encolar(elemento):
    global head, tail
    if (tail + 1) % len(cola) == head:
        print("La cola está llena")
    else:
        if head == -1:
            head = 0
        tail = (tail + 1) % len(cola)
        cola[tail] = elemento

# Función para eliminar y retornar el elemento más antiguo de la cola (desencolar)
def desencolar():
    global head, tail
    if head == -1:
        print("La cola está vacía")
        return None
    elemento = cola[head]
    if head == tail:
        head = -1
        tail = -1
    else:
        head = (head + 1) % len(cola)
    return elemento

# Función para verificar si la cola está vacía
def is_empty():
    return head == -1

# Función para obtener el tamaño de la cola
def size():
    if head == -1:
        return 0
    elif head <= tail:
        return tail - head + 1
    else:
        return len(cola) - head + tail + 1

#usando las funciones:
encolar(1)
encolar(2)
encolar(3)
encolar(4)
print("cola:",cola)
print("desencolar:",desencolar())
print("tamaño:",size())
print("cola:",cola)
print("indice head:",head,"- indice tail:", tail)
print("desencolar:",desencolar())
print("tamaño:",size())
print("cola:",cola)
print("indice head:",head,"- indice tail:", tail)
print("desencolar:",desencolar())
print("desencolar:",desencolar())
print("desencolar:",desencolar())
print("indice head:",head,"- indice tail:", tail)

#para que observen como se va moviendo el indice HEAD de la cola
for i in range(-1,20):
    print("i: ", i, "len:", len(cola), " - próximo indice HEAD '(i+1) mod len:'",((i + 1) % len(cola)))