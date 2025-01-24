from flask import Flask
from app.routes.tasks_routes import create_task, get_tasks, get_tasks_id, update_task_by_id, delete_task_by_id, \
    get_user_tasks, update_tasks_by_user_id, delete_tasks_by_user_id
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
