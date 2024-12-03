from app.models.base import Base
from app.db.config import engine
import logging
from sqlalchemy import text

logging.basicConfig(level=logging.INFO)

def initialize_database():
    """Cria as tabelas no banco de dados."""
    Base.metadata.create_all(engine)
    logging.info("Banco de dados criado com sucesso!")

def test_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Conexão bem-sucedida com o banco de dados!")
    except Exception as e:
        print(f"Erro na conexão com o banco: {e}")

if __name__ == "__main__":
    test_connection()
    initialize_database()
