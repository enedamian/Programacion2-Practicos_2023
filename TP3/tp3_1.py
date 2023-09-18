#Implemente una función que dada una lista de números, devuelva una nueva lista que contenga el cuadrado de cada número utilizando list comprehensions.
def lista_cuadrada(lista):
    lista_nueva =[elem**2 for elem in lista]
    return lista_nueva

def ingreso_num(mensaje):
    pedir=0
    lista=[]
    print(mensaje)
    while(pedir<5):
        try:
            valor = int(input())
            lista.append(valor)
            pedir +=1
        except:
            print("El valor ingresado no es valido")
    return lista

lista = ingreso_num("Ingrese 5 numeros para agregar a la lista: ")
print(lista_cuadrada(lista))

