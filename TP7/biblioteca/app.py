from flask import Flask
from models.libros import inicializar_libros

from controllers.rutas_libros import libros_blueprint

app = Flask(__name__)

inicializar_libros()

app.register_blueprint(libros_blueprint)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run(debug=True)