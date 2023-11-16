from flask import Flask
from models.libros import inicializar_libros
from models.socios import inicializar_socios
from models.prestamos import inicializar_prestamos

from controllers.rutas_libros import libros_blueprint
from controllers.rutas_socios import socios_blueprint
from controllers.rutas_prestamos import prestamos_blueprint

app = Flask(__name__)

inicializar_libros()
inicializar_socios()
inicializar_prestamos()

app.register_blueprint(libros_blueprint)
app.register_blueprint(socios_blueprint)
app.register_blueprint(prestamos_blueprint)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run(debug=True)