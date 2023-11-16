from flask import Blueprint, jsonify, request
from models.prestamos import obtener_prestamos, obtener_prestamo_por_id, obtener_prestamos_sin_devolver, crear_prestamo, editar_prestamo, eliminar_prestamo, libro_prestado
from models.libros import existe_libro
from models.socios import existe_socio

prestamos_blueprint = Blueprint('prestamos_blueprint', __name__)

@prestamos_blueprint.route('/prestamos', methods=['GET'])
def get_prestamos():
    prestamos = obtener_prestamos
    if len(prestamos) == 0:
        return jsonify({'message': 'no hay prestamos'}), 404
    else:
        return jsonify(prestamos), 200
    
@prestamos_blueprint.route('/prestamos/<int:id>', methods=['GET'])
def get_prestamo(id):
    prestamo_encontrado = obtener_prestamo_por_id(id)
    if not prestamo_encontrado:
        return jsonify({'message': 'prestamo no encontrado'}), 404
    else:
        return jsonify(prestamo_encontrado), 200
    
@prestamos_blueprint.route('/prestamos/pendientes', methods=['GET'])
def get_prestamos_pendientes():
    prestamo = obtener_prestamos_sin_devolver()
    if len(prestamo) == 0:
        return jsonify({'message': 'no hay prestamos pendientes'}), 404
    else:
        return jsonify(prestamo), 200

@prestamos_blueprint.route('/prestamos', methods=['POST'])
def post_prestamo():
    prestamo_nuevo = request.get_json()
    is_json = request.is_json
    if is_json:
        if 'socio_id' in prestamo_nuevo and 'libro_id' in prestamo_nuevo and 'fecha_retiro' in prestamo_nuevo and 'fecha_devolucion' in prestamo_nuevo:
            if existe_socio(prestamo_nuevo['socio_dni']):
                if existe_libro(prestamo_nuevo['libro_id']):
                    prestamo_creado = crear_prestamo(prestamo_nuevo['socio_id'], prestamo_nuevo['libro_id'], prestamo_nuevo['fecha_retiro'], prestamo_nuevo['fecha_devolucion'])
                    return jsonify(prestamo_creado), 201
                else:
                    return jsonify({'message': 'el libro no existe'}), 404
            else:
                return jsonify({'message': 'el socio no existe'}), 404
        else:
            return jsonify({'message': 'faltan campos'}), 400
    else:
        return jsonify({'message': 'el prestamo agregado no está en formato JSON'}), 400

@prestamos_blueprint.route('/prestamos/<int:id>', methods=['PUT'])
def update_prestamo(id):
    prestamo_existe = obtener_prestamo_por_id(id)
    prestamo_existente = request.get_json()
    prestamo_validado = validar_prestamo()
    if prestamo_existe:
        if request.is_json:
            if prestamo_validado:
                if existe_libro(prestamo_existente['libro_id']):
                    if existe_socio(prestamo_existente['socio_id']):
                        if not libro_prestado(prestamo_existente['libro_id']):
                            prestamo_actualizado = editar_prestamo(id, prestamo_existente['socio_id'], prestamo_existente['libro_id'], prestamo_existente['fecha_retiro'], prestamo_existente['fecha_devolucion'])
                            if prestamo_actualizado:
                                return jsonify(prestamo_actualizado), 200   
                            else:
                                return jsonify({'error': 'prestamo no encontraod'}) 
                        else:
                            return jsonify({'error': 'el libro ya está prestado'})
                    else:
                        return jsonify({'error': 'socio no existe'})
                else:
                    return jsonify({'error': 'libro no existe'})
            else:
                return jsonify({'message': 'los datos ingresados no son validos'}), 400
        else:
            return jsonify({'message': 'los datos ingresados no se encuentra en formato JSON'}), 400
    else:
        return jsonify({'message': f'No se ha encontrado al prestamo {id}'}), 400
            
@prestamos_blueprint.route('/prestamos/<int:id>', methods=['DELETE'])
def remover_prestamo(id):
    prestamo_existe = obtener_prestamo_por_id(id)
    if not prestamo_existe:
         return jsonify({'message': f'No se ha encontrado al prestamo {id}'}), 400
    else: 
        eliminar_prestamo(id)
        return jsonify({'message': f'prestamo {id} eliminado correctamente'}), 200
            
def validar_prestamo(prestamo):
    campos = ['socio_dni', 'libro_id', 'fecha_retiro', 'fecha_devolucion']
    for campo in prestamo:
        if not campo in campos:
            return False
    return True
