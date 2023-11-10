# Trabajo práctico API

## Desarrollo de una API REST para la gestión de viajes ofrecidos por una empresa

### Puntos a desarrollar:

1. Crear una nueva carpeta API_viajes para alojar el proyecto.
2. Crear el entorno virtual .venv para el proyecto.
3. Activar el entorno virtual e instalar Flask.
4. Crear el archivo app.py.
5. Cargar los datos desde el archivo destinos.py
6. Creación de rutas (endpoints):
    * Obtener todos los viajes (```GET```).
    * Obtener detalles de un viaje por su ID (```GET```).
    * Agregar un nuevo viaje (POST). Debe recibir los datos en formato JSON.
    * Actualizar la información de un viaje por su ID (PUT). Debe recibir los datos en formato JSON. La actualización de los datos puede ser completa o parcial (por ejemplo, puede enviarse solo el campo tipo_viaje o precio -o cualquier otro campo-, o varios campos en el JSON).
    * Eliminar un viaje por su ID (```DELETE```). Verificar si se vendieron viajes, en ese caso no eliminar y devolver una advertencia (si ```"cupo_actual < cupo_max"``` significa que se vendieron viajes).

IMPORTANTE: Agrega validaciones para asegurarte de que los datos proporcionados a la API sean correctos y válidos en todo momento, de lo contrario retornar un mensaje de datos incorrectos con un código de respuesta de error.