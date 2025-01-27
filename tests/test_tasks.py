from flask import Flask
from app.routes.tasks_routes import create_task, get_tasks, get_tasks_id, update_task_by_id, delete_task_by_id, \
    get_user_tasks_by_id, update_tasks_by_user_id, delete_tasks_by_user_id
from app.db import database_instance
from app.models import Base, Tasks
import unittest


class TestTaskIntegration(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        database_instance.init_app(self.app)

        with self.app.app_context():
            Base.metadata.create_all(bind=database_instance.engine)

    def test_create_task(self):
        with self.app.app_context():
            with self.app.test_request_context(
                    json={"title": "Limpar chão", "description": "Limpeza rotineira", "user_id": 1}
            ):
                response = create_task()
                print("response", response)

            task = database_instance.session.query(Tasks).filter_by(user_id=1).first()
            print("task retorno", task)
            self.assertIsNotNone(task)
            self.assertEqual(task.title, "Limpar chão")

    def test_get_task(self):
        with self.app.app_context():
            task = Tasks(title="Lavar roupa", description="lavar", user_id=1)
            print(task)
            database_instance.session.add(task)
            database_instance.session.commit()

            with self.app.test_request_context():
                response = get_tasks()

            self.assertEqual(response[0].json["tasks"][0]["title"], "Lavar roupa")

    def test_get_tasks_id(self):
        with self.app.app_context():
            task = Tasks(title="Lavar roupa", description="lavar", user_id=1)
            database_instance.session.add(task)
            database_instance.session.commit()

            with self.app.test_request_context():
                response = get_tasks_id(1)

            self.assertEqual(response[0].json["tasks"][0]["title"], "Lavar roupa")

    def test_update_task_by_id(self):
        with self.app.app_context():
            task = Tasks(title="Lavar roupa", description="lavar", user_id=1)
            database_instance.session.add(task)
            database_instance.session.commit()

            with self.app.test_request_context(
                    json={"title": "Lavar chão", "description": "lavando", "user_id": "1"}):
                response = update_task_by_id(1)

            updated_task = database_instance.session.query(Tasks).get(1)

            self.assertEqual(updated_task.title, "Lavar chão")
            self.assertEqual(updated_task.description, "lavando")
            self.assertEqual(response, {'message': 'task atualizada'})

    def test_delete_task_by_id(self):
        with self.app.app_context():
            task = Tasks(title="Lavar roupa", description="lavar", user_id=1)
            database_instance.session.add(task)
            database_instance.session.commit()

            with self.app.test_request_context():
                response = delete_task_by_id(1)

            deleted_task = database_instance.session.query(Tasks).get(1)

            self.assertIsNone(deleted_task)
            self.assertEqual(response, {'message': 'task deletada'})

    def test_get_user_tasks_by_id(self):
        with self.app.app_context():
            task = Tasks(title="Lavar roupa", description="lavar", user_id=1)
            database_instance.session.add(task)
            database_instance.session.commit()

            with self.app.test_request_context():
                response = get_user_tasks_by_id(1)
                print("Response JSON:", response[0].json)

            self.assertEqual(response[0].json["tasks"][0]["title"], "Lavar roupa")

    def test_update_tasks_by_user_id(self):
        with self.app.app_context():
            task = Tasks(title="Lavar roupa", description="lavar", user_id=1)
            database_instance.session.add(task)
            database_instance.session.commit()

            with self.app.test_request_context(
                    json={"title": "Lavar chão", "description": "lavando", "user_id": "1"}):
                response = update_tasks_by_user_id(1)

            updated_task = database_instance.session.query(Tasks).get(1)

            self.assertEqual(updated_task.title, "Lavar chão")
            self.assertEqual(updated_task.description, "lavando")
            self.assertEqual(response, {'message': 'Task atualizada'})

    def test_delete_tasks_by_user_id(self):
        with self.app.app_context():
            task = Tasks(title="Lavar roupa", description="lavar", user_id=1)
            database_instance.session.add(task)
            database_instance.session.commit()

            with self.app.test_request_context():
                response = delete_tasks_by_user_id(1)

            deleted_task = database_instance.session.query(Tasks).get(1)

            self.assertIsNone(deleted_task)
            self.assertEqual(response, {'message': 'task deletada'})
