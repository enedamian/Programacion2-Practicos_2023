import csv

# Esta función carga los datos del archivo 'libros.csv' y los almacena en una lista de diccionarios.
def cargar_libros():
    libros = []  # Se inicializa una lista vacía para almacenar los libros.
    with open('libros.csv', newline='') as csvfile:  # Abre el archivo 'libros.csv'.
        libros_csv = csv.DictReader(csvfile, delimiter=',')  # Lee el archivo CSV como un diccionario.
        for libro in libros_csv:  # Itera sobre cada fila del archivo CSV.
            libros.append(libro)  # Agrega cada fila (cada libro) a la lista de libros.
    return libros  # Devuelve la lista de libros como una lista de diccionarios.

# Esta función busca libros según un criterio específico (ID, título, fecha o año).
def buscar_libros(libros, tipo, valor):
    libros_encontrados = []  # Inicializa una lista vacía para almacenar los libros encontrados.
    for libro in libros:  # Itera sobre cada libro en la lista de libros proporcionada.
        if libro[tipo] == valor:  # Comprueba si el campo 'tipo' del libro coincide con el 'valor' proporcionado.
            libros_encontrados.append(libro)  # Si coincide, agrega el libro a la lista de libros encontrados.
    return libros_encontrados  # Devuelve la lista de libros que cumplen con el criterio de búsqueda.
