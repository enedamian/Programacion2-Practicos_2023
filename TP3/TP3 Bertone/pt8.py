lista=[12, 22, 45, 22, 78, 78 ,78, 15, 12, 14]
listasinduplicados=[]

[listasinduplicados.append(i) for i in lista if i not in listasinduplicados]
#el not in comprueba si esta duplicado en lista


print(listasinduplicados)