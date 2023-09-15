lista1=[2,4,6,8,10,12]
lista2=[1,3,5,7,9,11]

listamultiplicada=[a*b for a,b in zip(lista1, lista2)]
#el zip junta las listas y bueno multiplicariamos los elementos

print(listamultiplicada)