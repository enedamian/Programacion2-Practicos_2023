# Trabajo práctico integrador APIs

## Desarrollo de una API REST para la gestión de libros en una biblioteca

### Puntos a desarrollar:

1. Crear una nueva carpeta `biblioteca` para alojar el proyecto.
2. Dentro de la carpeta "biblioteca" crear el entorno virtual `.venv` para el proyecto, y una vez activado el entorno virtual instalarle Flask.
3. Crear el archivo `app.py` y las carpetas `modelos\` (para la gestión de datos) y `controladores\` (para las rutas).
4. En la carpeta `modelos\` crear los archivos que carguen en memoria y gestionen los datos almacenados en los archivos `libros.csv`, `socios.csv` y `prestamos.csv`:
    * Libros: `id, titulo, autor, año_publicacion`
    * Socios: `id, dni, nombre, apellido, teléfono, email`
    * Prestamos: `id, socio_dni, libro_id, fecha_retiro, fecha_devolucion`
    Observación: Los datos de los libros, socios y préstamos deben cargarse en memoria en listas de diccionarios. 
    En el caso de los préstamos inicialmente no hay datos cargados en el archivo, deberán cargarse los préstamos con el uso de la API.
5. En la carpeta `controladores\` crear los archivos que gestionarán las rutas, definir los blueprints en cada archivo y luego en `app.py` importarlos y registrarlos.
6. Creación de rutas (endpoints):
    * Libros:
        * Obtener la lista de todos los libros (`GET`).
        * Obtener detalles de un libro por su ID (`GET`).
        * Agregar un nuevo libro (`POST`). Debe recibir los datos en formato JSON.
        * Actualizar la información de un libro por su ID (`PUT`). Debe recibir los datos en formato JSON.
    * Socios:
        * Obtener la lista de todos los socios (`GET`).
        * Obtener detalles de un socio por su ID (`GET`).
        * Agregar un nuevo socio (`POST`). Debe recibir los datos en formato JSON.
        * Actualizar la información de un socio por su ID (`PUT`). Debe recibir los datos en formato JSON.
        * Eliminar un socio por su ID (`DELETE`). Realizar validaciones antes de eliminar el socio: no debe tener pendiente una devolución.
    * Préstamos:
        *ACLARACIÓN: de cada libro la biblioteca tiene solamente un ejemplar*.
        * Obtener la lista de todos los libros prestados que aún no se han devuelto (`GET`).
        * Obtener detalles de un prestamo de libro por su ID (`GET`).
        * Generar un nuevo prestamo (`POST`). Debe recibir los datos en formato JSON.
        * Registrar la devolución de un prestamo por su ID (`PUT`). Debe recibir los datos en formato JSON.
7. Persistencia de datos:
    Los datos que irá manejando la API deben actualizarse en los archivos del modelo a medida que se van generando/modificando.

IMPORTANTE: Agrega validaciones para asegurarte de que los datos proporcionados a la API sean correctos y válidos en todo momento, de lo contrario retornar un mensaje de datos incorrectos con un código de respuesta de error.