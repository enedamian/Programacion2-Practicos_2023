from flask import Blueprint, jsonify, request
from models.libros import obtener_libros, obtener_libro_por_id, crear_libro, editar_libro

#crear Blueprint
libros_blueprint = Blueprint('libros', __name__)

@libros_blueprint.route('/libros', methods=['GET'])
def get_libros():
    libros = obtener_libros()
    if len(libros) == 0:
        return jsonify({'message': 'No hay libros'}), 404
    else:
        return jsonify(libros), 200
    
@libros_blueprint.route('/libros/<int:id>', methods=['GET'])
def get_libro(id):
    libro_encontrado = obtener_libro_por_id(id)
    if not libro_encontrado:
        return jsonify({'message': 'No existe el libro con id: {}'.format(id)}), 404
    else:
        return jsonify(libro_encontrado), 200
    
@libros_blueprint.route('/libros', methods=['POST'])
def post_libro():
    is_json = request.is_json
    if not is_json:
        return jsonify({'message': 'El cuerpo de la petición debe ser un JSON'}), 400
    else:
        nuevo_libro = request.get_json()
        libro_validado = validar_campos(nuevo_libro)
        if not libro_validado:
            return jsonify({'message': 'Uno o más campos no han sido agregados'}), 404
        else:
            libro_creado = crear_libro(nuevo_libro['titulo'], nuevo_libro['autor'], nuevo_libro['anio_publicacion'])
            return jsonify(libro_creado), 201

@libros_blueprint.route('/libros/<int:id>', methods=['PUT'])
def put_libro(id):
    is_json = request.is_json
    if not is_json:
        return jsonify({'message': 'El cuerpo de la petición debe ser un JSON'}), 400
    else:
        libro_actualizado = request.get_json()
        if not validar_campos(libro_actualizado):
            return jsonify({'message': 'Uno o más campos no han sido agregados'}), 404
        else:
            libro_encontrado = obtener_libro_por_id(id)
            if not libro_encontrado:
                return jsonify({'message': 'No existe el libro con id: {}'.format(id)}), 404
            else:
                libro_editado = editar_libro(id, libro_actualizado['titulo'], libro_actualizado['autor'], libro_actualizado['anio_publicacion'])
                return jsonify(libro_editado), 200

def validar_campos(nuevo_libro):    #validacion para el POST
    campos = ['titulo', 'autor', 'anio_publicacion']
    for campo in campos:
        if campo not in nuevo_libro:
            return False
    return True