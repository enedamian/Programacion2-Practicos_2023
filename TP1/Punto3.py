def leer_float(mensaje):
    pedir = True
    while pedir:
        try:
            valor = float(input(mensaje))
            pedir = False
        except:
            print("El valor ingresado no es un numero valido.")
    return valor

def leer_float2(mensaje):
    pedir = True
    while pedir:
        try:
            valor = int(input(mensaje))
            pedir = False
        except:
            print("El valor ingresado no es valido.")
    return valor

ancho = leer_float("ingrese el ancho de la habitacion: ")
largo = leer_float("ingrese el largo de la habitacion: ")
alto = leer_float("ingrese el alto de la pared: ")
manos_de_pintura = leer_float2("ingrese la cantidad de manos de pintura que necesita aplicar: ")
pared_A = ancho * alto
pared_B = alto * largo
puerta = 0.8 * 2
superficie_total_a_pintar = pared_A * 2 + pared_B * 2 - puerta
litros = (superficie_total_a_pintar / 10) * manos_de_pintura
print(f"Para pintar {superficie_total_a_pintar} m2 y aplicar {manos_de_pintura} manos de pintura, se necesitan {litros : .2f} litros de pintura.")