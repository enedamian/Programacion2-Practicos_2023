def pedircantidad():
    while True:
        try:
            numerovalido = int(input("Ingrese el valor mínimo de caracteres por nombre: "))
            return numerovalido
        except ValueError:
            print("Debe ingresar un número válido. Intente nuevamente.")

cantidad = pedircantidad()
nombres = [input("ingrese nombres ") for _ in range(5)]   
# se llena la lista con el input 
listaFiltrada = [nombre for nombre in nombres if len(nombre)>=cantidad]
print(listaFiltrada)
