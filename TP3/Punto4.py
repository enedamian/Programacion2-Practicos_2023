""" Dado un diccionario de palabras y sus definiciones, 
crea una lista que contenga sólo las palabras que comienzan con una
letra específica (por ejemplo, "a") indicada por el usuario, 
utilizando list comprehensions. """

#diccionario creado por chatGPT
diccionario = {
    "Python": "Un lenguaje de programación de alto nivel conocido por su simplicidad y legibilidad.",
    "Programación": "El proceso de escribir, probar y mantener el código de un programa de computadora.",
    "Inteligencia Artificial": "La capacidad de las máquinas para realizar tareas que normalmente requieren inteligencia humana.",
    "Base de datos": "Un conjunto organizado de datos que se pueden acceder y gestionar fácilmente.",
    "Algoritmo": "Un conjunto de instrucciones paso a paso para realizar una tarea específica o resolver un problema.",
    "Cifrado": "El proceso de convertir información legible en un formato ilegible para protegerla de accesos no autorizados.",
    "Redes sociales": "Plataformas en línea que permiten a las personas conectarse y comunicarse entre sí.",
    "HTML": "Lenguaje de marcado utilizado para crear páginas web.",
    "Integración continua": "Un enfoque de desarrollo de software en el que las actualizaciones se prueban y se integran automáticamente en el proyecto principal.",
    "Sistema operativo": "El software que administra el hardware de una computadora y proporciona una interfaz para que los usuarios interactúen con ella."
}

#trabajamos con todo en minuscula para evitar errores

def seleccionar_palabras(letra):
    try:
        lista_palabras = [palabra for palabra in diccionario if palabra[0].lower() == letra]
        print(lista_palabras)
    except:
        print("Error, por favor ingrese una letra!!")

letra = input("Ingrese una letra: ").lower()
seleccionar_palabras(letra)