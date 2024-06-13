from flask import Blueprint
from services.to_do import mostrar_to_dos, find_to_do, create_usuario, update_to_do, delete_to_do

to_do = Blueprint('to_do', __name__)

#Mostrar todos los usuarios
@to_do.route('/', methods=['GET'])
def get_to_dos():
    return mostrar_to_dos()

#Buscar usuario
@to_do.route('/<id>', methods=['GET'])
def get_to(id):
    return find_to_do(id)

#Crear Usuario
@to_do.route('/', methods=['POST'])
def create_to_do():
    return create_usuario()

#Inicio de session
@to_do.route('/<id>', methods=['POST'])
def login_to_do(id):
    return find_to_do(id)

#Editar usuario
@to_do.route('/<id>', methods=['PUT'])
def update_todo(id):
    return update_to_do(id)

#Eliminar Usuario
@to_do.route('/<id>', methods=['DELETE'])
def delete_todo(id):
    return delete_to_do(id)
