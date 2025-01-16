# {
#     "username": "user",
#     "password_hash": "123456"
# }
# TODO rever validacao

from flask import Blueprint, request, jsonify
from app.db import database_instance
from sqlalchemy import select, update, delete

from app.models import Users

login_bp = Blueprint('login', __name__, url_prefix='/api/v1/login')


@login_bp.route('/', methods=['POST'])
def auth():
    json_input = request.get_json()

    username = json_input.get('username')
    password = json_input.get('password_hash')

    if not username or not password:
        return {"error": "username or password is required"}

    statement = select(Users).filter_by(username=username)
    user_obj = database_instance.session.scalars(statement).first()
    if not user_obj:
        return {"error": "User not found"}, 404

# gerar token jwt
