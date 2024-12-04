from flask import Blueprint

users_bp = Blueprint('users', __name__, url_prefix='/api/v1/users')


@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return {'message': 'Usuário encontrado'}


@users_bp.route('/', methods=['GET'])
def get_users():
    return {'message': 'Lista de usuários'}


@users_bp.route('/', methods=['POST'])
def create_user():
    return {'message': 'Usuário criado!'}
