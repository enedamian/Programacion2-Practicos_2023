import random
from functools import reduce

direccion_alumnos_deportes = 'TP5/alumnos_deportes.csv'
direccion_alumnos = 'TP5/alumnos.csv'
direccion_deportes = 'TP5/deportes.csv'
direccion_eventos = 'TP5/eventos.csv'
direccion_inscripciones = 'TP5/inscripciones.csv'
# Funciones para manejar una cola de datos
def encolar(cola, elemento):
    cola.append(elemento)

def desencolar(cola):
    if not esta_vacia(cola):
        return cola.pop(0)
    else:
        return None

def longitud(cola):
    return len(cola)

def esta_vacia(cola):
    return len(cola) == 0

# Funciones para manejar una pila de datos
def apilar(pila, elemento):
    pila.append(elemento)

def desapilar(pila):
    if not esta_vacia(pila):
        return pila.pop()
    else:
        return None

# Función para generar listas aleatorias
def generar_listas_aleatorias():
    longitud1 = random.randint(20, 50)
    longitud2 = random.randint(20, 50)
    # La utilizacion de _ en el for es una convencion de progamadores en python para variables descartables
    lista1 = [random.randint(200, 5000) for _ in range(longitud1)]
    lista2 = [random.randint(200, 5000) for _ in range(longitud2)]
    return lista1, lista2

# Función para multiplicar elementos impares y encontrar el menor número primo
def procesar_listas(lista1, lista2):
    minimo_lista2 = reduce(lambda x, y: x if x < y else y, lista2)
    # minimo_lista2 = min(lista2) esta es otra manera de hacerlo
    sublista_impares = [x * minimo_lista2 for x in lista1 if x % 2 != 0]
    
    #funcion para saber si un numero es primo
    def es_primo(numero):
        if numero <= 1:
            return False
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True

    lista2_primos = [x for x in lista2 if es_primo(x)]
    menor_primo = reduce(lambda x, y: x if x < y else y, lista2_primos, -1)
    menor_primo = min(lista2_primos) if lista2_primos else -1

    return sublista_impares, menor_primo

# Estructuras de datos para el club deportivo
alumnos = {}
eventos = {}
deportes = {}
alumnos_deportes = []
inscripciones = []

# Función para cargar los datos desde archivos CSV
def cargar_datos_desde_archivos():
    with open(direccion_alumnos, 'r') as file:
        for line in file:
            dni, apellido, nombre = line.strip().split(';')
            alumnos[dni] = {'apellido': apellido, 'nombre': nombre}
    
    with open(direccion_eventos, 'r') as file:
        for line in file:
            codigo, deporte, nombre, descripcion = line.strip().split(';')
            eventos[codigo] = {'deporte': deporte, 'nombre': nombre, 'descripcion': descripcion}
    
    with open(direccion_deportes, 'r') as file:
        for line in file:
            codigo, nombre = line.strip().split(';')
            deportes[codigo] = nombre
    
    with open(direccion_alumnos_deportes, 'r') as file:
        for line in file:
            dni, deporte_codigo = line.strip().split(';')
            alumnos_deportes.append({'dni': dni, 'deporte_codigo': deporte_codigo})
    
    with open(direccion_inscripciones, 'r') as file:
        for line in file:
            dni, evento_codigo = line.strip().split(';')
            inscripciones.append({'dni': dni, 'evento_codigo': evento_codigo})

# Función para procesar las inscripciones y generar el archivo alumnos_eventos.csv
def procesar_inscripciones():
    pila_inscripciones_invalidas = []
    cola_inscripciones_validas = []

    for inscripcion in inscripciones:
        dni = inscripcion['dni']
        evento_codigo = inscripcion['evento_codigo']

        # Verificar si la inscripción es válida
        if dni in alumnos and evento_codigo in eventos:
            deporte_del_alumno = [ad['deporte_codigo'] for ad in alumnos_deportes if ad['dni'] == dni]
            if deporte_del_alumno and eventos[evento_codigo]['deporte'] in deporte_del_alumno:
                numero_inscripcion = len(cola_inscripciones_validas) + 1
                cola_inscripciones_validas.append({'dni': dni, 'evento_codigo': evento_codigo, 'numero_inscripcion': numero_inscripcion})
            else:
                pila_inscripciones_invalidas.append(f"{dni}; {eventos[evento_codigo]['nombre']}")

    # Escribir las inscripciones válidas en el archivo alumnos_eventos.csv
    with open('TP5/alumnos_eventos.csv', 'w') as file:
        for inscripcion in cola_inscripciones_validas:
            file.write(f"{inscripcion['dni']};{inscripcion['evento_codigo']};{inscripcion['numero_inscripcion']}\n")

    return pila_inscripciones_invalidas

# Función para imprimir el orden inverso de las inscripciones válidas
def imprimir_inscripciones_inversas(pila):
    while not esta_vacia(pila):
        inscripcion = desapilar(pila)
        print(f"Inscripción inversa: DNI: {inscripcion.split(';')[0]}, Evento: {inscripcion.split(';')[1]}")

# Función para calcular estadísticas de inscripciones válidas
def calcular_estadisticas(inscripciones_validas):
    inscripciones_por_evento = {}
    for inscripcion in inscripciones_validas:
        evento_codigo = inscripcion['evento_codigo']
        if evento_codigo in inscripciones_por_evento:
            inscripciones_por_evento[evento_codigo] += 1
        else:
            inscripciones_por_evento[evento_codigo] = 1

    evento_mas_inscriptos = max(inscripciones_por_evento, key=inscripciones_por_evento.get)
    evento_menos_inscriptos = min(inscripciones_por_evento, key=inscripciones_por_evento.get)

    total_inscripciones = len(inscripciones_validas)
    promedio_inscripciones = total_inscripciones / len(eventos)

    return inscripciones_por_evento, evento_mas_inscriptos, evento_menos_inscriptos, promedio_inscripciones

# Cargar datos desde archivos
cargar_datos_desde_archivos()

# Procesar inscripciones
inscripciones_invalidas = procesar_inscripciones()

# Imprimir inscripciones inversas
print("Inscripciones inversas:")
imprimir_inscripciones_inversas(inscripciones_invalidas)

# Calcular estadísticas
inscripciones_validas = [inscripcion for inscripcion in inscripciones if inscripcion not in inscripciones_invalidas]
inscripciones_por_evento, evento_mas_inscriptos, evento_menos_inscriptos, promedio_inscripciones = calcular_estadisticas(inscripciones_validas)

print("\nEstadísticas de inscripciones:")
for evento_codigo, cantidad_inscripciones in inscripciones_por_evento.items():
    print(f"Evento {eventos[evento_codigo]['nombre']} ({eventos[evento_codigo]['descripcion']}): {cantidad_inscripciones} inscritos")

print(f"\nEvento con más inscriptos: {eventos[evento_mas_inscriptos]['nombre']} ({eventos[evento_mas_inscriptos]['descripcion']})")
print(f"Evento con menos inscriptos: {eventos[evento_menos_inscriptos]['nombre']} ({eventos[evento_menos_inscriptos]['descripcion']})")
print(f"Promedio de inscriptos por evento: {promedio_inscripciones:.2f}")
