from flask import Blueprint, request, jsonify
from app.db import database_instance
from sqlalchemy import select

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


@users_bp.route('/id/<int:user_id>', methods=['PUT'])
def update_user_id(user_id):
    user = database_instance.session.get(Users, user_id)
    return jsonify(user.as_dict()), 200


@users_bp.route('/username/<username>', methods=['GET'])
def get_user_name(username):
    statement = select(Users).filter_by(username=username)
    user_obj = database_instance.session.scalars(statement).all()
    user_dict = [user.as_dict() for user in user_obj]
    return jsonify(user_dict), 200


@users_bp.route('/username/<username>', methods=['PUT'])
def update_username(username):
    pass
