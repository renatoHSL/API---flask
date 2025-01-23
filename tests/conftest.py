import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base import Base
from app import create_app
from app.db import database_instance


@pytest.fixture(scope="function")
def test_db():
    engine = create_engine("sqlite:///:memory:")
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(bind=engine)

    session = Session()
    try:
        yield session
    finally:
        session.close()
        engine.dispose()


@pytest.fixture
def client(test_db):
    app = create_app(test_config={
        'SQLALCHEMY_ENGINE': test_db.get_bind()
    })
    app.config['TESTING'] = True

    with app.app_context():  # Cria o contexto da aplicação
        database_instance.session.configure(bind=test_db.get_bind())  # Configura o banco de testes
        Base.metadata.create_all(bind=test_db.get_bind())  # Cria tabelas no banco de testes

    with app.test_client() as client:
        yield client
