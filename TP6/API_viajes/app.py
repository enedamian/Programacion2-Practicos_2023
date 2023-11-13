from flask import Flask, request, jsonify
from destinos import destinos
app = Flask(__name__)

# obtener un viaje por id
def obtener_viaje_por_id(id):
    for viaje in destinos:
        if viaje['id'] == id:
            return viaje
    return None

# obtener todos los viajes
@app.route('/viajes', methods = ['GET']) 
def obtener_todos_los_viajes():
    return jsonify(destinos)

# obtener un viaje
@app.route('/viajes/<int:id>', methods = ['GET'])
def obtener_viaje(id):
    viaje = obtener_viaje_por_id(id)
    if viaje:
        return jsonify({id: destinos[id]})
    return jsonify({'error': 'viaje no encontrado'}), 404

def obtener_prox_id():
    return max(destino['id'] for destino in destinos) + 1 if destinos else 1

@app.route('/viajes', methods = ['POST'])
def agregar_viaje():
    nuevo_viaje = request.get_json()
    nuevo_viaje['id'] = obtener_prox_id()
    destinos.append(nuevo_viaje)
    return jsonify({'message': f'se ha creado un nuevo usuario con la id {obtener_prox_id()}'}), 201

@app.route('/viajes/<int:id>', methods = ['PUT'])
def actualizar_viaje(id):
    viaje = obtener_viaje_por_id(id)
    if viaje:
        datos_actualizados = request.get_json()
        viaje.update(datos_actualizados)
        return jsonify({'message': f'se ha actualizado el viaje {id} con éxito'})
    return jsonify({'error': 'viaje no encontrado'}), 404

@app.route('/viajes/<int:id>', methods = ['DELETE'])
def eliminar_viaje(id):
    viaje = obtener_viaje_por_id(id)
    if viaje:
        if viaje['cupo_actual'] < viaje['cupo_max']:
            return jsonify({'advertencia': f'se han vendido cupos del viaje {id}'})
        else:
            destinos.remove(viaje)
            return jsonify({'message': f'se ha eliminado el viaje {id}'})
    return jsonify({'error': 'viaje no encontrado'}), 404

@app.route('/')
def index():
    return jsonify(destinos)

if __name__ == '__main__':
    app.run(debug=True)