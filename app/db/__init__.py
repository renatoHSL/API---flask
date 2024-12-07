# TODO rever essa funcao

from app.db.init_db import initialize_database
from flask_sqlalchemy import SQLAlchemy

database_instance = SQLAlchemy()


def setup_database():
    initialize_database()
