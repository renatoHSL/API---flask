# TODO fazer as validacoes
# Dá pra mudar pra service várias partes da rota

from flask import Blueprint, request, jsonify
from app.db import database_instance
from sqlalchemy import select, update, delete
from app.schemas.user_schema import UserSchema
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from app.models import Users

users_bp = Blueprint('users', __name__, url_prefix='/api/v1/users')

user_schema = UserSchema()


@users_bp.route('/', methods=['POST'])
def create_user():
    """
    Cria um novo usuário
    ---
    tags:
      - Users
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              username:
                type: string
                example: "joao"
              email:
                type: string
                example: "joao@email.com"
              password_hash:
                type: string
                example: "senha123"
    responses:
      200:
        description: Usuário criado com sucesso
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "Usuário criado!"
      422:
        description: Dados inválidos
    """
    json_input = request.get_json()
    try:
        data = user_schema.load(json_input)
        print("EM ROUTES Dados validados:", data)
    except ValidationError as err:
        print("Erro de validação:", err.messages)
        return {"EM ROUTES errors": err.messages}, 422
    username = data.get('username')
    email = data.get('email')
    password = data.get('password_hash')
    if not username or not email or not password:
        return {"error": "username or email or password is required"}

    user = Users(username=username, email=email, password_hash=password)
    print("DATABASE INSTANCE:", database_instance)
    try:
        database_instance.session.add(user)
        database_instance.session.commit()
    except IntegrityError:
        database_instance.session.rollback()  # Reverte a transação
        return {"error": "User already exists."}, 409

    return jsonify({'message': 'Usuário criado!'}), 200


@users_bp.route('/', methods=['GET'])
def get_users():
    """
    Lista todos os usuários
    ---
    tags:
      - Users
    responses:
      200:
        description: Lista de usuários retornada com sucesso
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    example: 1
                  username:
                    type: string
                    example: "joao"
                  email:
                    type: string
                    example: "joao@email.com"
      404:
        description: Nenhum usuário encontrado
    """
    users = database_instance.session.scalars(select(Users)).all()
    if not users:
        return {"error": "No user on the database"}, 404
    user_dict = [user.as_dict() for user in users]
    return jsonify({'users': user_dict}), 200


@users_bp.route('/id/<int:user_id>', methods=['GET'])
def get_user_id(user_id):
    """
    Retorna informações de um usuário pelo ID
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        required: true
        schema:
          type: integer
        description: ID do usuário
    responses:
      200:
        description: Usuário encontrado com sucesso
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                username:
                  type: string
                  example: "joao"
                email:
                  type: string
                  example: "joao@email.com"
      404:
        description: Usuário não encontrado
    """
    user = database_instance.session.get(Users, user_id)
    print("teste", user)
    if not user:
        return {"error": "User not found"}, 404
    return jsonify(user.as_dict()), 200


@users_bp.route('/id/<int:user_id>', methods=['PATCH'])
def update_user_id(user_id):
    """
    Atualiza informações de um usuário pelo ID
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        required: true
        schema:
          type: integer
        description: ID do usuário
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              username:
                type: string
                example: "joao atualizado"
              email:
                type: string
                example: "joao_atualizado@email.com"
              password_hash:
                type: string
                example: "nova_senha123"
    responses:
      200:
        description: Usuário atualizado com sucesso
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "usuário atualizado"
      422:
        description: Dados inválidos
    """
    json_input = request.get_json()
    try:
        data = user_schema.load(json_input)
    except ValidationError as err:
        return {"errors": err.messages}, 422
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


@users_bp.route('/id/<int:user_id>', methods=['DELETE'])
def delete_user_id(user_id):
    """
    Deleta um usuário pelo ID
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        required: true
        schema:
          type: integer
        description: ID do usuário
    responses:
      200:
        description: Usuário deletado com sucesso
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "usuário deletado"
      404:
        description: Usuário não encontrado
    """
    user = database_instance.session.get(Users, user_id)
    if not user:
        return {"error": "User not found"}, 404
    stmt = delete(Users).where(Users.id == user_id)
    database_instance.session.execute(stmt)
    database_instance.session.commit()
    return {'message': 'usuário deletado'}
