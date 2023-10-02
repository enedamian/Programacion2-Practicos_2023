"""11. Dada una lista de diccionarios con los alumnos y notas de un curso, calcular el promedio del curso.
 Puede usar una lista como la siguiente: 
```python
lista_dic = [{'nombre': 'Hector', 'nota': 70}, {'nombre': 'Juan', 'nota': 45}, {'nombre': 'Maria', 'nota': 75}, {'nombre': 'Pedro', 'nota': 80}, {'nombre': 'Ana', 'nota': 60},  {'nombre': 'Florencia', 'nota': 95}]
```"""

lista_dic = [{'nombre': 'Hector', 'nota': 70}, {'nombre': 'Juan', 'nota': 45}, {'nombre': 'Maria', 'nota': 75}, {'nombre': 'Pedro', 'nota': 80}, {'nombre': 'Ana', 'nota': 60},  {'nombre': 'Florencia', 'nota': 95}]
promedio_alumnos = sum(alumno ["nota"] for alumno in lista_dic)/len(lista_dic)
print(promedio_alumnos)