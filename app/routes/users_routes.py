# TODO fazer as validacoes

from flask import Blueprint, request, jsonify
from app.db import database_instance
from sqlalchemy import select, update, delete

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

    return jsonify({'message': 'Usuário criado!'}), 200


@users_bp.route('/', methods=['GET'])
def get_users():
    users = database_instance.session.scalars(select(Users)).all()
    user_dict = [user.as_dict() for user in users]
    return jsonify({'users': user_dict}), 200


@users_bp.route('/id/<int:user_id>', methods=['GET'])
def get_user_id(user_id):
    user = database_instance.session.get(Users, user_id)
    return jsonify(user.as_dict()), 200


@users_bp.route('/id/<int:user_id>', methods=['PATCH'])
def update_user_id(user_id):
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password_hash')

    updated_values = {}

    if username is not None:
        updated_values['username'] = username

    if email is not None:
        updated_values['email'] = email

    if password is not None:
        updated_values['password_hash'] = password

    statement = update(Users).where(Users.id == user_id).values(**updated_values)
    database_instance.session.execute(statement)
    database_instance.session.commit()
    return {'message': 'usuário atualizado'}

    # if content is None:
    #     return '{ "Error" : "json data required" }', 400
    # return jsonify(user.as_dict()), 200


@users_bp.route('/id/<int:user_id>', methods=['DELETE'])
def delete_user_id(user_id):
    stmt = delete(Users).where(Users.id == user_id)
    database_instance.session.execute(stmt)
    database_instance.session.commit()
    return {'message': 'usuário deletado'}


@users_bp.route('/username/<username>', methods=['GET'])
def get_user_name(username):
    statement = select(Users).filter_by(username=username)
    user_obj = database_instance.session.scalars(statement).all()
    user_dict = [user.as_dict() for user in user_obj]
    return jsonify(user_dict), 200


@users_bp.route('/username/<username>', methods=['PATCH'])
def update_username(username):
    data = request.get_json()
    username_update = data.get('username')
    email = data.get('email')
    password = data.get('password_hash')

    updated_values = {}

    if username_update is not None:
        updated_values['username'] = username_update

    if email is not None:
        updated_values['email'] = email

    if password is not None:
        updated_values['password_hash'] = password

    statement = update(Users).where(Users.username == username).values(**updated_values)
    database_instance.session.execute(statement)
    database_instance.session.commit()
    return {'message': 'usuário atualizado'}


@users_bp.route('/username/<username>', methods=['DELETE'])
def delete_username(username):
    stmt = delete(Users).where(Users.username == username)
    database_instance.session.execute(stmt)
    database_instance.session.commit()
    return {'message': 'usuário deletado'}
