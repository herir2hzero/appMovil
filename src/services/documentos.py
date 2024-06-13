from flask import request, Response
from config.mongodb import mongo
from bson import json_util, ObjectId

#crear documento
def create_documento():
    data = request.get_json()
    numero_cuenta = data.get('numero_cuenta_alumno', None)
    nombre_documento = data.get('nombre_documento', None)
    comentario = data.get('comentario', None)
     
    if numero_cuenta:
        response = mongo.db.documentos.insert_one({
            'numero_cuenta_alumno': numero_cuenta,
            'nombre_documento': nombre_documento,
            'comentario': comentario
        })
        result = {
            'id': str(response.inserted_id),
            'numero_cuenta_alumno': numero_cuenta,
            'nombre_documento': nombre_documento,
            'comentario': comentario,
        }
        return result
    else:
        return 'invalid payload', 400
    
#Mostrar documentos
def mostrar_documentos():
    data = mongo.db.documentos.find()
    result = json_util.dumps(data)
    return Response(result, mimetype='application/json')

#Buscar documento por numero de cuenta
def find_documento(id):
    data = mongo.db.documentos.find_one({'_id': ObjectId(id)})
    result = json_util.dumps(data)
    return Response(result, mimetype='application/json')

#Editar documento
def update_documento(id):
    data = request.get_json()
    if len(data) == 0:
        return 'Invalid payload', 400
    response = mongo.db.documentos.update_one({'_id': ObjectId(id)}, {'$set': data})
    
    if response.modified_count >= 1:
        return 'Updated successfully', 200
    else:
        return 'Not found', 404

#Eliminar documento
#Eliminar usuario
def delete_documento(id):
    response = mongo.db.documentos.delete_one({'_id': ObjectId(id)})
    if response.deleted_count >= 1:
        return 'Deleted successfully', 200
    else:
        return 'Not found', 400