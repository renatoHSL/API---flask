from flask import Flask
from app.routes.users_routes import create_user, get_users, get_user_id, update_user_id, delete_user_id
from app.db import database_instance
from app.models import Base, Users
import unittest


class TestUserIntegration(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        database_instance.init_app(self.app)

        with self.app.app_context():
            Base.metadata.create_all(bind=database_instance.engine)

    def test_create_user(self):
        with self.app.app_context():
            with self.app.test_request_context(
                    json={"username": "joaquim", "email": "joaquim@email.com", "password": "senha123"}
            ):
                response = create_user()

            user = database_instance.session.query(Users).filter_by(username="joaquim").first()
            self.assertIsNotNone(user)  # O usuário deve existir
            self.assertEqual(user.email, "joaquim@email.com")

    def test_get_users(self):
        with self.app.app_context():
            user1 = Users(username="joao", email="joao@email.com", password_hash="senha123")
            user2 = Users(username="maria", email="maria@email.com", password_hash="senha123")
            database_instance.session.add_all([user1, user2])
            database_instance.session.commit()

            with self.app.test_request_context():
                response = get_users()

            self.assertEqual(response[0].json["users"][0]["username"], "joao")
            self.assertEqual(response[0].json["users"][1]["username"], "maria")

    def test_get_user_id(self):
        with self.app.app_context():
            user = Users(id=1, username="joao", email="joao@email.com", password_hash="senha123")
            print(user)
            database_instance.session.add(user)
            database_instance.session.commit()

            with self.app.test_request_context():
                response = get_user_id(1)

            self.assertEqual(response[0].json["username"], "joao")

    def test_update_user_id(self):
        with self.app.app_context():
            user = Users(id=1, username="joao", email="joao@email.com", password_hash="senha123")
            print(user)
            database_instance.session.add(user)
            database_instance.session.commit()

            with self.app.test_request_context(
                    json={"username": "joaquim", "email": "joaquim@email.com", "password": "senha123"}):
                response = update_user_id(1)
                print(response)

            updated_user = database_instance.session.query(Users).get(1)

            self.assertEqual(updated_user.username, "joaquim")
            self.assertEqual(updated_user.email, "joaquim@email.com")
            self.assertEqual(response, {'message': 'usuário atualizado'})

    def test_delete_user_id(self):
        with self.app.app_context():
            user = Users(id=1, username="joao", email="joao@email.com", password_hash="senha123")
            print(user)
            database_instance.session.add(user)
            database_instance.session.commit()

            with self.app.test_request_context():
                response = delete_user_id(1)
                print(response)

            deleted_user = database_instance.session.query(Users).get(1)
            print("deleted", deleted_user)

            self.assertIsNone(deleted_user)
            self.assertEqual(response, {'message': 'usuário deletado'})


if __name__ == "__main__":
    unittest.main()

# TODO exemplo com uso de mocks

# from unittest.mock import MagicMock, patch
# import unittest
# from flask import Flask
# from app.routes.users_routes import create_user
# from app.db import database_instance
# from app.models import Base  # Certifique-se de importar corretamente os modelos
#
#
# class TestCreateUser(unittest.TestCase):
#     @patch("app.db.database_instance.session")  # Substitui apenas a sessão pelo mock
#     @patch("app.schemas.user_schema")  # Substitui o user_schema pelo mock
#     def test_create_user_success(self, mock_user_schema, mock_session):
#         # Configurar o mock da sessão
#         mock_add = MagicMock()
#         mock_commit = MagicMock()
#         mock_session.add = mock_add
#         mock_session.commit = mock_commit
#
#         # Simular dados validados do user_schema
#         mock_user_schema.load.return_value = {
#             "username": "joao",
#             "email": "joao@email.com",
#             "password_hash": "senha123"
#         }
#
#         # Criar um app Flask e vincular o banco de dados
#         app = Flask(__name__)
#         app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # Banco em memória
#         app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#         database_instance.init_app(app)  # Inicializa o banco normalmente
#
#         # Usar o contexto do Flask durante o teste
#         with app.app_context():
#             # Criar tabelas antes de rodar os testes
#             with database_instance.engine.connect() as connection:
#                 Base.metadata.create_all(bind=connection)
#
#             with app.test_request_context(
#                     json={"username": "joao", "email": "joao@email.com", "password": "senha123"}
#             ):
#                 # Executar a função que estamos testando
#                 response = create_user()
#
#         # Verificar se os métodos do banco foram chamados corretamente
#         mock_add.assert_called_once()  # Verifica se o método add foi chamado
#         mock_commit.assert_called_once()  # Verifica se o método commit foi chamado
#
#         # Verificar o retorno da função
#         self.assertEqual(response[1], 200)  # Código HTTP
#         self.assertEqual(response[0].json["message"], "Usuário criado!")  # Resposta JSON
#
#
# if __name__ == "__main__":
#     unittest.main()
