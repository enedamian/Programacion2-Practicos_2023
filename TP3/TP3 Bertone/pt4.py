palabras_y_definiciones={
    "Python": "lenguaje de programacion mas usado actualmente",
    "C++" : "Lenguaje usado para crear videojuegos u otras cosas",
    "Java": "Lenguaje muy utilizado para comenzar a programar",
    "Boca": "Equipo mas grande del futbol",
    "Javascrip": "Lenguaje utilizado para desarrollo web"
}

ingresodeletra=input("Ingrese un caracter: ")
caracter= ingresodeletra[0]

palabras_con_letra_de_user=[ (palabra, definicion) for palabra, definicion in palabras_y_definiciones.items() if palabra[0]==caracter]

print(palabras_con_letra_de_user)