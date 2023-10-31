cola = [None] * 10
head = -1
tail = -1

def encolar(cola, elemento):
    global head, tail
    if(tail + 1) % len(cola) == head:
        print("Cola llena")
    else:
        if head == -1:
            head = 0
        tail = (tail + 1) % len(cola)
        cola[tail] = elemento

def desencolar(cola, elemento):
    global head, tail
    if head == -1:
        print("Cola vacia")
        return None
    elemento = cola[head]

    if head == tail:
        head = -1
        tail = -1
    else:
        head = (head + 1) % len(cola)

    return elemento

def longitud(cola):
    if head == -1:
        return 0
    elif head <= tail:
        return tail - head + 1
    else:
        return len(cola) - head + tail + 1
    
def vacia(cola):
    return len(cola) == 0