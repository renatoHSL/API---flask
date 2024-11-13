from ..models.base import Base
from ..models.config import engine


def initialize_database():
    Base.metadata.create_all(engine)
    print("Banco de dados criado")


if __name__ == "__main__":
    initialize_database()
