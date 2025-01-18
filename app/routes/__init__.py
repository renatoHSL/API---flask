from flask import Flask
from .users_routes import users_bp
from .tasks_routes import tasks_bp
from .auth import login_bp


def register_routes(app: Flask):
    app.register_blueprint(users_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(login_bp)
