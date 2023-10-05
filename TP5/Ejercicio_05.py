cola_inscripciones = []
pila_inscripciones_incorrectas = []
numero_inscripcion_actual = 1

def encolar(elemento):
    cola_inscripciones.append(elemento)

def apilar():
    pila_inscripciones_incorrectas.append()

def cargar_alumnos(ruta):
    archivo = open(ruta, 'r')
    lista_alumnos = []

    for linea in archivo:
        datos = linea.split(';')
        alumnos = {
            'alumno_dni': datos[0],
            'alumno_apellido': datos[1],
            'alumno_nombre': datos[2]
        }
        lista_alumnos.append(alumnos)
    return lista_alumnos

def cargar_deportes(ruta):
    archivo = open(ruta, 'r')
    lista_deportes = []

    for linea in archivo:
        datos = linea.split(';')
        deportes = {
            'deporte_codigo': datos[0],
            'deporte_nombre': datos[1]
        }
        lista_deportes.append(deportes)
    return lista_deportes

def cargar_eventos(ruta):
    archivo = open(ruta, 'r')
    lista_eventos = []

    for linea in archivo:
        datos = linea.split(';')
        eventos = {
            'evento_codigo': datos[0],
            'evento_nombre': datos[1]
        }
        lista_eventos.append(eventos)
    return lista_eventos

def cargar_inscripciones(ruta):
    archivo = open(ruta, 'r')
    lista_inscripciones = []

    for linea in archivo:
        datos = linea.split(';')
        inscripciones = {
            'alumno_dni': datos[0],
            'evento_codigo': datos[1]
        }
        lista_inscripciones.append(inscripciones)
    return lista_inscripciones

def cargar_alumnos_deportes(ruta):
    archivo = open(ruta, 'r')
    lista_alumnos_deportes = []

    for linea in archivo:
        datos = linea.split(';')
        alumnos_deportes = {
            'alumno_dni': datos[0],
            'deporte_codigo': datos[1]
        }
        lista_alumnos_deportes.append(alumnos_deportes)
    return lista_alumnos_deportes

def es_valida(dni_alumno, codigo_evento, alumnos, eventos, alumnos_deportes):
    if dni_alumno not in [alumno['alumno_dni'] for alumno in alumnos]:
        return False
    
    if codigo_evento not in [evento['evento_codigo'] for evento in eventos]:
        return False
    
    deportes_alumno = [relacion['deporte_codigo'] for relacion in alumnos_deportes if relacion['alumno_dni'] == dni_alumno]
    evento_deporte = [evento['deporte_codigo'] for evento in eventos if evento['evento_codigo'] == codigo_evento]
    if not evento_deporte or evento_deporte[0] not in deportes_alumno:
        return False
    return True

def generar_numero_inscripcion():
    global numero_inscripcion_actual
    numero_inscripcion = numero_inscripcion_actual
    numero_inscripcion_actual += 1
    return numero_inscripcion

def generar_alumnos_eventos(alumnos, eventos, deportes, inscripciones):
    archivo = r"alumnos_eventos.csv"
    lista_alumnos_eventos = []

    for inscripcion in inscripciones:
        dni_alumno = inscripcion['alumno_dni']
        codigo_evento = inscripcion['evento_codigo']

        evento_nombre = ""
        for evento in eventos:
            if evento['evento_codigo'] == codigo_evento:
                evento_nombre = evento['evento_nombre']
                break

        if(dni_alumno in [alumno['alumno_dni'] for alumno in alumnos] 
           and codigo_evento in [evento['evento_codigo'] for evento in eventos] 
           ):
            
            numero_inscripcion = generar_numero_inscripcion()
            alumnos_eventos = {
                'alumno_dni': dni_alumno,
                'evento_codigo': codigo_evento,
                'numero_inscripcion': numero_inscripcion
            }
            lista_alumnos_eventos.append(alumnos_eventos)
            encolar(alumnos_eventos)
        else:
            pila_inscripciones_incorrectas.append(f"{dni_alumno}; {evento_nombre}")

    for inscripcion in reversed(inscripciones):
        print(f"Inscripcion incorrecta: {inscripcion}")

    archivo_alumnos_eventos = open(archivo, 'w')
    archivo_alumnos_eventos.write("alumno_dni; evento_codigo; numero_inscripcion\n")
    
    for alumno_evento in lista_alumnos_eventos:
        archivo_alumnos_eventos.write(f"{alumno_evento['alumno_dni']}; {alumno_evento['evento_codigo']}; {alumno_evento['numero_inscripcion']}\n")

    archivo_alumnos_eventos.close()

archivo_alumnos = input("ingrese la ruta del archivo de alumnos: ")
archivo_deportes = input("ingrese la ruta del archivo de deportes: ")
archivo_eventos = input("ingrese la ruta del archivo de eventos: ")
archivo_inscripciones = input("ingrese la ruta del archivo de inscripciones: ")
archivo_alumnos_deportes = input("ingrese la ruta del archivo de alumnos_deportes: ")

alumnos = cargar_alumnos(archivo_alumnos)
deportes = cargar_deportes(archivo_deportes)
eventos = cargar_eventos(archivo_eventos)
inscripciones = cargar_inscripciones(archivo_inscripciones)
alumnos_deportes = cargar_alumnos_deportes(archivo_alumnos_deportes)

generar_alumnos_eventos(alumnos, eventos, deportes, inscripciones)