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

@app.route('/viajes', methods = ['POST'])
def agregar_viaje():
    nuevo_destino = {
        'name': request.form['name'],
        'price': request.form['price'],
        'country': request.form['country']
    }
    nuevo_id = max(destinos.keys()) + 1
    destinos[nuevo_id] = nuevo_destino
    return jsonify(nuevo_destino)

    

@app.route('/viajes/<int:id>', methods = ['PUT'])
def actualizar_viaje(id):
    viaje = [destino for destino in destinos if destino["id"] == id]
    if len(viaje)==0:
        return jsonify({'error': 'No existe un viaje con ese ID'})
    else:
        # modificar el destino
        return jsonify(f'viaje {id} con destino a {viaje["name"]} actualizado correctamente')


@app.route('/')
def index():
    return jsonify(destinos)

if __name__ == '__main__':
    app.run(debug=True)