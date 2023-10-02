personas = {}

def edad_es_mayor(personas, edad_minima):
    return [nombre for nombre, edad in personas.items() if edad > edad_minima]

