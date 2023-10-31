import random
listaAleat = []

def ListaAleatoria():
        for x in range(random.randint(20,50)):
            listaAleat.append(random.randint(200,5000))
        
        longitud = len(listaAleat) 
        print(f"La longitud de la lista es: {longitud}, y sus valores son: {listaAleat}")

ListaAleatoria()