from flask import request, Response
from config.mongodb import mongo
from bson import json_util, ObjectId

#Funcion para agregar usuario
def create_usuario():
    data = request.get_json()
    numero_cuenta = data.get('numero_cuenta', None)
    nombre = data.get('nombre', None)
    apellido_pat = data.get('apellido_pat', None)
    apellido_mat = data.get('apellido_mat', None)
    email = data.get('email', None)
    telefono = data.get('telefono', None)
    rol = data.get('rol', None)
    contrasena = data.get('contrasena', None)
     
    if numero_cuenta:
        response = mongo.db.to_do.insert_one({
            'numero_cuenta': numero_cuenta,
            'nombre': nombre,
            'apellido_pat': apellido_pat,
            'apellido_mat': apellido_mat,
            'email': email,
            'telefono': telefono,
            'rol': rol,
            'contrasena': contrasena
        })
        result = {
            'id': str(response.inserted_id),
            'numero_cuenta': numero_cuenta,
            'nombre': nombre,
            'apellido_pat': apellido_pat,
            'apellido_mat': apellido_mat,
            'email': email,
            'telefono': telefono,
            'rol': rol,
            'contrasena': contrasena
        }
        return result
    else:
        return 'invalid payload', 400

#Función para mostrar Usuarios
def mostrar_to_dos():
    data = mongo.db.to_do.find()
    result = json_util.dumps(data)
    return Response(result, mimetype='application/json')

#Buscar registro por id
def find_to_do(id):
    data = mongo.db.to_do.find_one({'numero_cuenta': id})
    result = json_util.dumps(data)
    return Response(result, mimetype='application/json')

#Editar usuario
def update_to_do(id):
    data = request.get_json()
    if len(data) == 0:
        return 'Invalid payload', 400
    
    response = mongo.db.to_do.update_one({'_id': ObjectId(id)}, {'$set': data})
    
    if response.modified_count >= 1:
        return 'Updated successfully', 200
    else:
        return 'Not found', 404

#Eliminar usuario
def delete_to_do(id):
    response = mongo.db.to_do.delete_one({'_id': ObjectId(id)})
    if response.deleted_count >= 1:
        return 'Deleted successfully', 200
    else:
        return 'Not found', 400
    