palabras = {
    "Altruismo": "Tendencia a procurar el bien de las personas de manera desinteresada",
    "Vernáculo": "Que es propio del país o la región de la persona de quien se trata",
    "Avaricia": "Afán de poseer muchas riquezas por el solo placer de atesorarlas",
    "Sublime": "Que es extraordinariamente bello y produce una gran emoción"
}

def comienza_con(palabras, letra):
    return [palabra for palabra in palabras if palabra[0].lower() == letra]

print(comienza_con(palabras, 'a'))