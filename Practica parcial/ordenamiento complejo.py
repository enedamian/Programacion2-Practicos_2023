lista = [1,8,3,-5,-8,-6,-3,4,9]

# ordenar la lista poniendo primero los impares y despues los pares, y de menor a mayor 
# ej: [-5,-3,1,3,9,-8,-6,4,8]
def ordenar_complejo(lista):
    lista_impares = sorted(list(filter(lambda x: x%2 != 0, lista)))
    lista_pares = sorted(list(filter(lambda x: x%2 == 0, lista)))
    return lista_impares + lista_pares

def burbuja(lista):
    longitud= len(lista)
    for i in range(0,longitud):
        for j in range(0,longitud-1):
            if lista[j]%2==0 and lista[j+1]%2==1: # par  impar
                lista[j],lista[j+1]=lista[j+1],lista[j]
            elif lista[j]%2==1 and lista[j+1]%2==0: # impar  par
                pass
            elif lista[j]>lista[j+1]:# par  par   ||  impar impar
                lista[j],lista[j+1]=lista[j+1],lista[j]
    return lista

# ordenar generando las dos sublistas
print(ordenar_complejo(lista))
# ordenar con burbuja modificado
print(burbuja(lista))
print("La lista ahora nos quedó con el orden modificado por el algoritmo burbuja:",lista)
# volvemos a desordenar la lista
lista = [1,8,3,10,7,-5,-8,-6,-3,4,9]
#mismo ordenamiento con sorted usando funcion lambda:
print(sorted(lista, key=lambda x: (x%2 == 0, x)))

            