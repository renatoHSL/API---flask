from flask import Blueprint, request
from app.db import database_instance
from flask import jsonify

from app.models import Users

users_bp = Blueprint('users', __name__, url_prefix='/api/v1/users')


@users_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password_hash')
    print(type(password))
    if not username or not email or not password:
        return {"error": "username or email or password is required"}

    user = Users(username=username, email=email, password_hash=password)
    database_instance.session.add(user)
    database_instance.session.commit()

    return {'message': 'Usuário criado!'}


@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = database_instance.session.get(Users, user_id)
    user_db_id = user.id
    if user_id == user_db_id:
        return user.as_dict()


# @users_bp.route('/<username>', methods=['GET'])
# def get_user(username):
#     return {'message': 'Usuário encontrado'}


@users_bp.route('/', methods=['GET'])
def get_users():
    return {'message': 'Lista de usuários'}
