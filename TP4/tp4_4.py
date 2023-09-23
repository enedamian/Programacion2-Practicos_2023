#4. A partir de una lista de números existente, 
#crear una nueva lista incrementando en un 15% los valores originales usando map.
lista_num = [1,2,3,4,5,6]
quince_porciento_extra = list(map(lambda x: x*1.15,lista_num))
print(quince_porciento_extra)