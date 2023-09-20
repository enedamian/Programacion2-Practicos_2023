def leer_float(mensaje):
    pedir = True
    while pedir:
        try:
            valor = float(input(mensaje))
            pedir = False
        except:
            print("El valor ingresado no es un numero valido.")
    return valor

ancho = leer_float("ingrese el ancho de la habitacion: ")
largo = leer_float("ingrese el largo de la habitacion: ")
alto = leer_float("ingrese el alto de la pared: ")
pared_A = ancho * alto
pared_B = alto * largo
puerta = 0.8 * 2
superficie_total_a_pintar = pared_A * 2 + pared_B * 2 - puerta
litros = superficie_total_a_pintar / 10
print(f"Para pintar {superficie_total_a_pintar} m2 se necesitan {litros : .2f} litros de pintura.")