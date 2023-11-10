from flask import Flask, request, jsonify
from destinos import destinos
app = Flask(__name__)

# obtener todos los viajes
@app.route('/viajes', methods = ['GET']) 
def obtener_todos_los_viajes():
    return jsonify(destinos)

# obtener un viaje
@app.route('/viajes/<int:id>', methods = ['GET'])
def obtener_viaje(id):
    if id in destinos:
        return jsonify({id: destinos[id]})
    return jsonify({'error': 'viaje no encontrado'}), 404

@app.route('/login/', methods = ['GET'])
def show_login_form_get():
    return 'No estás logeado. Esto es un GET'

@app.route('/viajes/nuevo', methods = ['POST'])
def agregar_viaje():
    if request.method == 'POST':
        nuevo_destino = {
            'name': request.form['name'],
            'price': request.form['price'],
            'country': request.form['country']
        }
        nuevo_id = max(destinos.keys()) + 1
        destinos[nuevo_id] = nuevo_destino
        return jsonify(nuevo_destino)
    else:
        return jsonify({'error': 'No se pudo agregar el viaje'})
    

@app.route('/viajes/<int:id>/<string:destino>', methods = ['PUT'])
def actualizar_viaje(id, destino):
    if id not in destinos:
        return jsonify({'error': 'No existe un viaje con ese ID'})
    elif destino in destinos:
        return jsonify({'error': 'Ya existe un destino con ese nombre'})
    else:
        destinos[id] = destino
        return jsonify(f'viaje {id} con destino a {destino} actualizado correctamente')

@app.route('/login/', methods = ['POST'])
def show_login_form():
    if 'name' in request.form:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        return 'Hola ' + name + ' ' + email + ' ' + password
    return 'No estás logeado. Esto es un POST'

@app.route('/')
def index():
    return jsonify(destinos)

if __name__ == '__main__':
    app.run(debug=True)