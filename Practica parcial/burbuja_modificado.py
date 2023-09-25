lista_ejemplo=[1,4,7,9,-1,-6,10]

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


print (burbuja(lista_ejemplo))
