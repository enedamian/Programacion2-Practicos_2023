from functools import reduce
lista=[7,8,94,3,65,43,77]

def numeromayor(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2


resultado=reduce(numeromayor, lista)
print(resultado)