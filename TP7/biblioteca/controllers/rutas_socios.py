from flask import Blueprint, jsonify, request
from models.socios import obtener_socios, obtener_socio_por_id, crear_socio, editar_socio, eliminar_socio, existe_socio

socios_blueprint = Blueprint('socios', __name__)

@socios_blueprint.route('/socios', methods=['GET'])
def get_socios():
    socios = obtener_socios()
    if len(socios) == 0:
        return jsonify({'message': 'no hay socios'}), 404
    else:
        return jsonify(socios), 200
    
@socios_blueprint.route('/socios/<int:id>', methods=['GET'])
def get_socio_by_id(id):
    socio_encontrado = obtener_socio_por_id(id)
    if not socio_encontrado:
        return jsonify({'message': f'no se ha encontrado el socio {id}'})
    else:
        return jsonify(socio_encontrado)
    
@socios_blueprint.route('/socios', methods=['POST'])
def agregar_socio():
    is_json = request.is_json
    if not is_json:
        return jsonify({'message': 'El objeto agregado no está en formato JSON'})
    else:
        nuevo_socio = request.get_json()
        socio_validado = validar_socio(nuevo_socio)
        if not socio_validado:
             return jsonify({'message': 'Faltan uno o más campos'}), 404
        else:
            socio_creado = crear_socio(nuevo_socio['dni'], nuevo_socio['nombre'], nuevo_socio['apellido'], nuevo_socio['telefono'], nuevo_socio['email'])
            return jsonify(socio_creado), 201
        
@socios_blueprint.route('socios/<int:id>', methods=['PUT'])
def update_socio(id):
    socio_existe = existe_socio(id)
    if not socio_existe:
        return jsonify({'message': f'no se ha encontrado al socio {id}'})
    else:
        is_json = request.is_json
        if not is_json:
            return jsonify({'message': 'los datos ingresados no se encuentran en formato JSON'})
        else:
            nuevo_socio = request.get_json()
            socio_validado = validar_socio(nuevo_socio)
            if not socio_validado:
                return jsonify({'message': 'Faltan uno o más campos'}), 404
            else:
                socio_actualizado = editar_socio(id, nuevo_socio['dni'], nuevo_socio['nombre'], nuevo_socio['apellido'], nuevo_socio['telefono'], nuevo_socio['email'])
                return jsonify(socio_actualizado), 200
        
@socios_blueprint.route('/socios/<int:id>', methods=['DELETE'])
def remover_socio(id):
    socio_existe = existe_socio(id)
    if not socio_existe:
        return jsonify({'message': f'no se ha encontrado al socio {id}'})
    else:
        eliminar_socio(id)
        return jsonify({'message': f'se ha eliminado el socio {id} de forma exitosa'})
        
def validar_socio(nuevo_socio):
    campos = ['dni', 'nombre', 'apellido', 'telefono', 'email']
    for campo in campos:
        if not campo in nuevo_socio:
            return False
    return True

