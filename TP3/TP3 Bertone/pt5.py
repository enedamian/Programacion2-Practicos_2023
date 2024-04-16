def es_primo(numero):
    if numero <= 1:
        return False  
    elif numero <= 3:
        return True   
    elif numero % 2 == 0 or numero % 3 == 0:
        return False  
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False  
        i += 6  
    return True
  


rangomin=int(input("Ingrese el rango minimo: "))
rangomax=int(input("Ingrese el rango maximo: "))
ListaDePrimos=[numero for numero in range(rangomin, rangomax) if es_primo(numero)]

print(ListaDePrimos)

