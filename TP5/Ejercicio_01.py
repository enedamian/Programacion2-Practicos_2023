import random 

cola = [random.randint(1, 100) for _ in range(10)]
print(cola)

head = -1
tail = -1

def encolar(cola, elemento):
    global head, tail
    if (tail + 1) % len(cola) == head:
        print("La cola está llena")
    else:
        if head == -1:
            head = 0
        tail = (tail + 1) % len(cola)
        cola[tail] = elemento

print(encolar(cola, 2))