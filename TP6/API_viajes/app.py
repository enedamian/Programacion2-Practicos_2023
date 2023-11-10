from flask import Flask, jsonify, request
from destinos import destinos_argentina as viajes
app = Flask(__name__) #creamos una instancia de la clase Flask

@app.route("/destinos/", methods=["GET"])
def obtener_todos_viajes():
    return jsonify(viajes), 200

@app.route("/destinos/<int:id>", methods=["GET"])
def detalles_viaje_id(id):
    viaje_encontrado = [viaje for viaje in viajes if viaje["id"] == id]
    if len(viaje_encontrado) > 0:
        return jsonify(viaje_encontrado), 200
    else:
        return jsonify("ID no encontrado"), 404

@app.route("/destinos/", methods=["POST"])
def nuevo_viaje():
    if request.is_json:
        if "ciudad" and "fecha_ida" and "fecha_vuelta" and "descripcion" and "tipo_viaje" and "precio" and "estrellas" and "transporte" and "cupo_max" and "cupo_actual" in request.json:
            viaje_nuevo = request.get_json()
            viaje_nuevo["id"] = viajes[-1]["id"]+1
            viajes.append(viaje_nuevo)
            return jsonify(viaje_nuevo), 201 #viaje creado   
        else:
            return jsonify({"message": "No se pudo crear el viaje, faltan datos"}), 400 #viaje no creado
    else:
        return jsonify({"message": "No se pudo crear el viaje, no se recibió un json"}), 400
    
@app.route("/destinos/<int:id>", methods=["PUT"])
def actualizar_viaje(id):
    viaje_encontrado = [viaje for viaje in viajes if viaje["id"] == id]
    if len(viaje_encontrado[0]) > 0:
        viaje_actualizado = request.get_json()
        for key, value in viaje_actualizado.items():
            viaje_encontrado[0][key] = value
        return jsonify(viaje_encontrado[0]), 200
    else:
        return jsonify({"message": "No se pudo encontrar el id"}), 404
    
@app.route("/destinos/<int:id>", methods=["DELETE"])
def borrar_viaje(id):
    viaje_para_borrar = [viaje for viaje in viajes if viaje["id"] == id]
    if len(viaje_para_borrar) > 0:
        viaje_para_borrar=viaje_para_borrar[0]
        if viaje_para_borrar["cupo_actual"] < viaje_para_borrar["cupo_max"]:
            return jsonify({"message": "ADVERTENCIA! Se han vendido viajes de este id"})
        else:
            viajes.remove(viaje_para_borrar)
            return jsonify({"message": "Se ha eliminado correctamente el viaje. ",'viaje borrado' :viaje_para_borrar}), 200
    else:
        return jsonify({"message": "No se pudo encontrar el id"}), 404