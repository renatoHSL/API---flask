import os
from flask import Flask
from flasgger import Swagger
from app.db.config import DATABASE_URL
from app.routes import register_routes
from app.db import initialize_database, database_instance


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if test_config is not None:
        app.config.from_mapping(test_config)

    swagger = Swagger(app, template={
        "swagger": "2.0",
        "info": {
            "title": "API Flask com Swagger",
            "description": "Documentação interativa da API usando Flasgger",
            "version": "1.0.0"
        },
        "host": "localhost:5000",
        "basePath": "/",
        "schemes": ["http"],
    })

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    database_instance.init_app(app)

    register_routes(app)

    return app


if __name__ == "__main__":
    flask_app = create_app()

    with flask_app.app_context():
        initialize_database()

    flask_app.run()
