def encolar(cola,elemento):
    return cola.append(elemento)

def desencolar(cola,elemento):
    pos=0
    for i in cola:
        if i==elemento:
            cola.pop(pos)
        pos = pos +1
    return cola
    
def longitud(cola):
    return len(cola)

listaA = []
hola = True
print("Ingrese 'LISTO' para dejar de agregar elementos a la lista.")
while hola:
    elemento = input("Ingrese un elemento: ")
    if elemento=='LISTO' or elemento=='listo':
        hola = False
    else:
        encolar(listaA,elemento)
print(listaA)
print(f"La longitudad de la lista es de: {longitud(listaA)}")
elemnto2= input("Escriba un elemento de la lista para eliminarlo: ")
desencolar(listaA,elemnto2)
print(listaA)