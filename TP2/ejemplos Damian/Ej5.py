"""
Escriba un programa que permita cargar una lista de alumnos junto con su nota del
parcial. Seleccione la estructura de datos que mejor se adapte al problema. Luego
de ingresados los datos debe generar una lista donde figure si aprobaron o no (se
aprueba con 40 o más). El listado a mostrar por pantalla debe ser como el siguiente
(el resultado no se almacena, se calcula):
ALUMNOS         PARCIAL     RESULTADO
Smith, Juan     70          Aprobado
Suárez, María   35          Desaprobado"""

# podemos usar una lista de diccionarios

def leer_entero_positivo(mensaje):
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

def cargar_notas_alumnos(cantidad):
    lista = []    
    for i in range (0, cantidad):
        alumno = dict()
        alumno["nombre"] = input(f"Nombre del alumno {i+1}:")
        alumno["nota"] = leer_entero_positivo(f"Nota del alumno {alumno['nombre']}: ")
        lista.append(alumno)
    return lista

def imprimir_listado_estado_alumnos(lista_alumnos):
    print(f"{'ALUMNOS':20s} {'NOTAS':10s} RESULTADOS")
    for alumno in lista_alumnos:
        # la cadena está formateada con un ancho fijo para cada variable, 
        # el formato de la nota indica alineacion a la izquierda desde donde se debe comenzar a escribir
        # '<' para alinear a la izq; '>' para alinear a la derecha, '^' para centrar alineacion
        print(f"{alumno['nombre']:20s} {alumno['nota']:<10d} {'Aprobado' if alumno['nota'] >= 40 else 'Desaprobado' }")

cantidad = leer_entero_positivo("¿Cuantas notas desea cargar?: ")
alumnos = cargar_notas_alumnos(cantidad)
imprimir_listado_estado_alumnos(alumnos)


