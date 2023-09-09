def reverso(texto:str)->str:
    ultPos = len(texto) - 1
    reverso = ""
    for i in range(ultPos,-1,-1):
        reverso += texto[i]
    return reverso

def leer_entero(mensaje:str)-> int:
    """Espera un ingreso de teclado y valida que sea un numero entero, en caso contrario sigue pidiendo el numero entero hasta que sea valido."""
    seguir_pidiendo = True
    while seguir_pidiendo:
        try:             
            numero = int(input(mensaje))
            seguir_pidiendo=False             
        except ValueError:
            print('Error, debe ingresar un numero entero.\nInténtelo nuevamente:')
    return numero

def leer_entero_positivo(mensaje:str)-> int:
    """Espera un ingreso de teclado y valida que sea un numero entero positivo, en caso contrario sigue pidiendo el numero hasta que sea valido."""
    seguir_pidiendo = True
    while seguir_pidiendo:
        try:             
            numero = int(input(mensaje))
            if numero >= 0:
                seguir_pidiendo=False             
            else:
                print("El numero ingresado no es válido. Debe ingresar un numero positivo.")
        except ValueError:
            print('Error, debe ingresar un numero entero positivo.\nInténtelo nuevamente:')
    return numero

def leer_float(mensaje:str)->float:
    """muestra el 'mensaje' y espera un valor ingresado por teclado para convertirlo a float"""
    seguir_pidiendo = True
    while seguir_pidiendo:
        try:
            nro = float(input(mensaje))
            seguir_pidiendo = False
        except ValueError:
            print("Debe ingresar un número válido. Intente nuevamente.")
    return nro

def pedir_edad()->int:
    """Pide la edad del usuario y valida que el numero esté entre 1 y 119"""
    seguir_pidiendo=True
    while seguir_pidiendo:
        print('Ingresá tu edad: ')
        edad = leer_entero()
        if edad > 0 and edad < 120:
            seguir_pidiendo=False
    return edad

def es_año_bisiesto(year:int)->bool:
    """Toma el año de ingreso y devuelve True si el año es bisiesto, False en caso contrario"""
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True  
    else:
        return False