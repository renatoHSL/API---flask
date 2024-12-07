from app.models.base import Base
from app.db.config import engine
import logging

logging.basicConfig(level=logging.INFO)


def initialize_database():
    """Cria as tabelas no banco de dados."""
    Base.metadata.create_all(engine)
    logging.info("Banco de dados criado com sucesso!")


if __name__ == "__main__":
    initialize_database()
