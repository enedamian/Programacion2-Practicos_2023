"""
Escriba un programa que permita cargar una lista de alumnos junto con su nota del
parcial. Seleccione la estructura de datos que mejor se adapte al problema. Luego
de ingresados los datos debe generar una lista donde figure si aprobaron o no (se
aprueba con 40 o más). El listado a mostrar por pantalla debe ser como el siguiente
(el resultado no se almacena, se calcula):
ALUMNOS         PARCIAL     RESULTADO
Smith, Juan     70          Aprobado
Suárez, María   35          Desaprobado"""


# Mi solución:

def validacion(mensaje):
    positivo = True

    while positivo:
        try:
            nota = int(input(mensaje))
            if nota >= 0:
                positivo = False
            else:
                print("La nota debe ser positiva, ingrese nuevamente")
        
        except ValueError:
            print("Debe ingresar un numero entero positivo. Intente nuevamente")

    return nota

def cargar_notas(cantidad):
    lista_alumnos = []
    i = 0

    while i < cantidad:
        alumnos = dict()

        alumnos["nombre"] = input(f"Nombre del alumno {i + 1}: ")
        alumnos["nota"] = validacion(f"Nota del alumno {alumnos['nombre']}: ")

        lista_alumnos.append(alumnos)

        i += 1

    return lista_alumnos

def imprimir(lista):
   print(f"ALUMNOS         PARCIAL     RESULTADO")
   for alumno in lista:
       nota = alumno["nota"]
       resultado = "Aprobado" if int(nota) >= 40 else "Desaprobado"
       print(f"{alumno['nombre']}     {nota}          {resultado}")

cantidad = validacion("Ingrese la cantidad de alumnos: ")
lista_alumnos = cargar_notas(cantidad)
imprimir(lista_alumnos)