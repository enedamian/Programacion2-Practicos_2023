# Trabajo práctico N° 4

### IMPORTANTE: Recuerden trabajar en una rama propia

## Ejercicios

1. Crea una función lambda que tome un número como argumento y devuelva su cuadrado.
2. Crea una función lambda que tome dos números como argumentos y devuelva su suma.
3. Crea una función lambda que devuelva el mayor de dos números.
4. A partir de una lista de números existente, crear una nueva lista incrementando en un 15% los valores originales usando map.
5. Ordenar una lista de diccionarios por un elemento del diccionario. ej: ordenar por edad la siguiente lista: 
```python
personas = [{'nombre': 'Hector', 'edad': 27}, {'nombre': 'Juan', 'edad': 18}, {'nombre': 'Maria', 'edad': 32}, {'nombre': 'Pedro', 'edad': 21}, {'nombre': 'Ana', 'edad': 20}]
```
7. Dada una lista con números, filtrar los números pares y devolverlos en una nueva lista.
8. Dada una lista de temperaturas en grados celsius generar una nueva lista con las temperaturas expresadas en grados fahrenheit, la fórmula para convertir la temperatura es `°F=(°C*(9/5))+32`.
9. Dada una lista de palabras, utiliza la función sorted con una función lambda para ordenar la lista de acuerdo a la longitud de las palabras.
10. Dada una lista de palabras, generar una lista con las iniciales de cada palabra.
11. Dada una lista de diccionarios con los alumnos y notas de un curso, calcular el promedio del curso. Puede usar una lista como la siguiente: 
```python
lista_dic = [{'nombre': 'Hector', 'nota': 70}, {'nombre': 'Juan', 'nota': 45}, {'nombre': 'Maria', 'nota': 75}, {'nombre': 'Pedro', 'nota': 80}, {'nombre': 'Ana', 'nota': 60},  {'nombre': 'Florencia', 'nota': 95}]
```
13. Encuentra el número mayor de una lista utilizando reduce.
14. Utilice reduce para concatenar una lista de cadenas en una sola cadena
15. Filtrar una lista de diccionarios por una condición. Ej: filtrar la lista del punto 10 para obtener notas de los alumnos aprobados.
16. Dada una lista de diccionarios con nombre, fecha de nacimiento, y teléfono, crear una nueva lista con los diccionarios de las personas que aún no cumplieron años respecto a la fecha actual del sistema, y esa lista ordenarla por la fecha de nacimiento de menor a mayor. Puede usar una lista como la siguiente:
```python
import datetime
lista_alumnos = [{"nombre":"Joaquin", "fecha_nacimiento":datetime.date(1990, 7, 2), "telefono":"123456789"}, { "nombre":"Maria", "fecha_nacimiento":datetime.date(1995, 5, 16), "telefono":"123456789"}, { "nombre":"Pedro", "fecha_nacimiento":datetime.date(1992, 9, 12), "telefono":"123456789"}, { "nombre":"Ana", "fecha_nacimiento":datetime.date(1991, 9, 22), "telefono":"123456789"}, { "nombre":"Florencia", "fecha_nacimiento":datetime.date(1994, 12, 8), "telefono":"123456789"}, { "nombre":"Hector", "fecha_nacimiento":datetime.date(1993, 4, 4), "telefono":"123456789"}]
```


