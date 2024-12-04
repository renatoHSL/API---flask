from flask import Flask
from .users_routes import users_bp


def register_routes(app: Flask):
    app.register_blueprint(users_bp)
