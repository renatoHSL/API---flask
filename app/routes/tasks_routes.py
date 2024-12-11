from flask import Blueprint, request, jsonify
from app.db import database_instance
from sqlalchemy import select, update, delete

from app.models import Users, Tasks

tasks_bp = Blueprint('tasks', __name__, url_prefix='/api/v1/tasks')


@tasks_bp.route('/', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    user_id = data.get('user_id')

    task = Tasks(title=title, description=description, user_id=user_id)
    database_instance.session.add(task)
    database_instance.session.commit()
    return {'message': 'Task criada!'}


@tasks_bp.route('/', methods=['GET'])
def get_task():
    tasks = database_instance.session.scalars(select(Tasks)).all()
    task_dict = [task.as_dict() for task in tasks]
    return jsonify({'tasks': task_dict}), 200


@tasks_bp.route('/<int:user_id>', methods=['GET'])
def get_tasks(tasks_id):
    return {'message': 'Task encontrada'}


@tasks_bp.route('/', methods=['DELETE'])
def delete_task():
    return {'message': 'Task deletada!'}


@tasks_bp.route('/', methods=['PUT'])
def update_task():
    return {'message': 'Task atualizada!'}
