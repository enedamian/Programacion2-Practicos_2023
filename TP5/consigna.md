# Trabajo práctico N° 5

### IMPORTANTE: Recuerden trabajar en una rama propia

## Info para el práctico
*El módulo `random` nos permite trabajar con aleatoriedad. Nos otorga funciones para generar números pseudoaleatorios, es decir, números que parecen aleatorios pero se generan mediante un algoritmo determinista.
Podemos usar `random.randint(a, b)`, para generar un número entero aleatorio entre a y b inclusive.
Para generar números float podemos usar `random.random()` que nos devolverá un valor en el rango `[0.0, 1.0)`.*


## Ejercicios

1. crear las funciones genéricas que nos permitirán manejar una cola de datos.
    * encolar(cola,elemento) #agrega elemento al final de la cola
    * desencolar(cola,elemento) #devuelve el elemento al inicio de la cola y lo elimina de la cola
    * longitud(cola) #devuelve la longitud de la estructura
    * esta_vacia(cola) #devuelve True si la estructura está vacía
2. crear las funciones genéricas que nos permitirán manejar una pila de datos.
    * apilar(pila,elemento) #agrega elemento encima de la pila
    * desapilar(pila,elemento) #devuelve el elemento en la cima de la pila y lo elimina de la pila
    * longitud(pila) #devuelve la longitud de la estructura (pueden reutilizar el del punto anterior)
    * esta_vacia(pila) #devuelve True si la estructura está vacía (pueden reutilizar el del punto anterior)
3. Usando el módulo random, cree una función que retorne dos listas de longitud aleatoria entre 20 y 50, y cada lista con elementos de valores aleatorios entre 200 y 5000.
4. Utilizando la función anterior genere dos listas de datos. Con la lista1 se debe generar una sublista con los elementos impares de lista1 multiplicados por el valor menor de la lista2.
Con la lista2 se debe devolver el menor número primo contenido en la lista, o “-1” si no tiene números primos.
5. Un club deportivo que organiza para sus alumnos una serie de competencias para el fin de semana cerró las inscripciones a los eventos y se desea a procesarlas. Dada la siguiente estructura de datos simplificada:
    * **alumnos.csv** (con datos en el formato `alumno_dni;alumno_apellido;alumno_nombre`)
    * **eventos.csv** (con datos en el formato `evento_codigo;deporte_codigo;evento_nombre;evento_descripción`)
    * **deportes.csv** (con datos en el formato `deporte_codigo;deporte_nombre`)
    * **alumnos_deportes** (con datos en el formato `alumno_dni;deporte_codigo`)
    * **inscripciones.csv** (con datos en el formato `alumno_dni;evento_codigo`)

    se pide:
    * cargar los datos en memoria usando las estructuras adecuadas, y procesar la cola de inscripciones a los eventos deportivos registrando los datos en un nuevo archivo ***alumnos_eventos.csv*** con el formato `alumno_dni;evento_codigo;numero_inscripcion`.
    Se debe verificar que los datos cargados en la cola sean válidos (es decir que el dni exista en alumnos, que el código de deporte exista en deportes, que el código de evento exista en eventos, y que el evento en el que se inscribe el alumno sea de un deporte que el alumno realiza en el club *(un alumno puede realizar mas de un deporte)*). Si hay un registro en inscripciones que no es correcto no se debe procesar y se debe almacenar en una pila con los datos `dni_alumno; evento_nombre`.
    * luego al finalizar las inscripciones imprimir por pantalla el orden inverso al que se ejecutaron las inscripciones válidas (utilizando la pila del inciso anterior).
    * de las inscripciones válidas se pueden calcular estadísticas: mostrar cuantos inscriptos tiene cada evento, cual es el evento con mayor inscriptos, cual es el que tiene menor inscriptos, cual es el que su cantidad de inscriptos se aproxima más al promedio de `inscriptos/eventos`.


