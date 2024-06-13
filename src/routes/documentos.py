from flask import Blueprint
from services.documentos import create_documento, mostrar_documentos, find_documento, update_documento, delete_documento

documentos = Blueprint('documentos', __name__)

@documentos.route('/', methods=['POST'])
def get_to_dos():
    return create_documento()

@documentos.route('/', methods=['get'])
def get_documentos():
    return mostrar_documentos()

@documentos.route('/<id>', methods=['GET'])
def get_documento_by_id(id):
    return find_documento(id)

@documentos.route('/<id>', methods=['PUT'])
def update_todo(id):
    return update_documento(id)

#Eliminar Usuario
@documentos.route('/<id>', methods=['DELETE'])
def delete_todo(id):
    return delete_documento(id)