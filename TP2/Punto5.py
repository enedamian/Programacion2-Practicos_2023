""" Escriba un programa que permita cargar una lista de alumnos junto con su nota del
parcial. Seleccione la estructura de datos que mejor se adapte al problema. Luego
de ingresados los datos debe generar una lista donde figure si aprobaron o no (se
aprueba con 40 o más). El listado a mostrar por pantalla debe ser como el siguiente
(el resultado no se almacena, se calcula): 
ALUMNOS PARCIAL RESULTADO
Smith, Juan 70 Aprobado
Suárez, María 35 Desaprobado """


def ingreso_alumnos():
    salir = True
    while(salir):
        try:
            cantidad = int(input("Cantidad de alumnos a ingresar: "))
            lista_alumnos = dict()
            for i in range(cantidad):
                 nombre = input("Ingrese nombre: ")
                 nota = float(input("Ingrese nota: "))
                 lista_alumnos[nombre] = nota
            salir = False
        except:
            print("Ingrese adecuadamente el valor.")
        return lista_alumnos

NOTA_DE_EXIMICION = 40
def imprimir_lista(alumnos:dict):
    print("{:<30} {:<30} {:<30} ".format("ALUMNOS","PARCIAL","RESULTADO"))
    items = alumnos.items()
    for item in items:
         print("{:<30} {:<30} {:<30} ".format(item[0],item[1],"Aprobado" if item[1]>=NOTA_DE_EXIMICION else "Desaprobado"))


imprimir_lista(ingreso_alumnos())