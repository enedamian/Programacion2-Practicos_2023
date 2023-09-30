def total_caracteres(u):
    contador = 0

    for i in range(len(u)):
        contador += 1

    return contador

def total_letras(u):
    contador = 0

    for j in u:
        if j.isalpha():
            contador += 1
    
    return contador

def cantidad_palabras(u):
    palabras = u.split(u)
    return len(palabras)
        

texto = input("Ingrese una oración:\n")
menu_activo = True

while menu_activo:
    print("---------menu---------")
    print("1. Total caracteres")
    print("2. Total letras")
    print("3. Cantidad de palabras")
    print("4. salir")
    print("-----------------------")

    op = int(input("Seleccione una opción: "))

    if op == 1:
        caracteres = total_caracteres(texto)
        print(f"Total de caracteres en la oración: {caracteres}")
    elif op == 2:
        letras = total_letras(texto)
        print(f"Total de letras en la oración: {letras}")
    elif op == 3:
        palabras = cantidad_palabras(texto)
        print(f"Cantidad de palabras: {palabras + 1}")
    elif op == 4:
        print("Cerrando programa...")
        menu_activo = False
    else:
        print("Opción no válida.")

