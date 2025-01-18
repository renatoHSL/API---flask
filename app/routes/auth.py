# {
#     "username": "user",
#     "password_hash": "123456"
# }
# TODO rever validacao
#  Testando uso do JWT

from flask import Blueprint, request, jsonify
from app.db import database_instance
from sqlalchemy import select

from app.models import Users

import jwt

from datetime import datetime, timedelta

login_bp = Blueprint('login', __name__, url_prefix='/api/v1/login')

SECRET_KEY = "chave_secreta"


@login_bp.route('/', methods=['POST'])
def auth():
    json_input = request.get_json()
    print("funcionando")
    username = json_input.get('username')
    password = json_input.get('password_hash')

    if not username or not password:
        return {"error": "username or password is required"}

    statement = select(Users).filter_by(username=username)
    user_obj = database_instance.session.scalars(statement).first()
    if not user_obj:
        return {"error": "User not found"}, 404

    if password != user_obj.password_hash:
        return {"error": "Password incorrect"}

    print(user_obj)

    key = "secret"
    encoded = jwt.encode({"some": "payload"}, key, algorithm="HS256")
    # jwt.decode(encoded, key, algorithms="HS256")

    payload = {
        "user_id": user_obj.id,
        "username": user_obj.username,
        "role": "admin" if user_obj.is_admin else "user",
        "exp": datetime.utcnow() + timedelta(hours=1)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    # Retorno estruturado com o token
    return jsonify({
        "message": "Login feito",
        "access_token": token,
        "token_type": "Bearer",
        "expires_in": 3600
    }), 200
