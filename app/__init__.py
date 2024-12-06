import os

from flask import Flask
from app.routes import register_routes
from app.models import Base
from flask_sqlalchemy import SQLAlchemy

database_instance = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(os.path.dirname(__file__), 'db', 'data', 'database.db')
    # )
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'data', 'database.db')}"

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Inicialize o db com o app
    database_instance.init_app(app)

    @app.route('/')
    def index():
        return "Hello, Flask!"

    register_routes(app)

    return app


if __name__ == "__main__":
    flask_app = create_app()
    flask_app.run()
