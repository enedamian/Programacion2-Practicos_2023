def separarListas(lista):
    Par_Impar_Separados= [numeros for numeros in lista if numeros % 2 == 0] + [numeros for numeros in lista if numeros % 2 != 0]
    return Par_Impar_Separados

listaOriginal = [1,2,3,4,5,6,7,8,9,10]
print(separarListas(listaOriginal))