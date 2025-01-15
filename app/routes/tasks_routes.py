# TODO fazer as validacoes

from flask import Blueprint, request, jsonify
from app.db import database_instance
from sqlalchemy import select, update, delete
from app.schemas.task_schema import TaskSchema
from marshmallow import ValidationError

from app.models import Tasks

tasks_bp = Blueprint('tasks', __name__, url_prefix='/api/v1/tasks')

task_schema = TaskSchema()


@tasks_bp.route('/', methods=['POST'])
def create_task():
    json_input = request.get_json()
    try:
        data = task_schema.load(json_input)
    except ValidationError as err:
        return {"errors": err.messages}, 422
    title = data.get('title')
    description = data.get('description')
    user_id = data.get('user_id')

    task = Tasks(title=title, description=description, user_id=user_id)
    database_instance.session.add(task)
    database_instance.session.commit()
    return {'message': 'Task criada!'}


@tasks_bp.route('/', methods=['GET'])
def get_tasks():
    tasks = database_instance.session.scalars(select(Tasks)).all()
    if not tasks:
        return {"error": "No tasks on the database"}, 404
    task_dict = [task.as_dict() for task in tasks]
    return jsonify({'tasks': task_dict}), 200


@tasks_bp.route('/id/<int:task_id>', methods=['GET'])
def get_tasks_id(task_id):
    task = database_instance.session.get(Tasks, task_id)
    if not task:
        return {"error": "Task not found"}, 404
    return jsonify(task.as_dict()), 200


@tasks_bp.route('/id/<int:task_id>', methods=['PATCH'])
def update_task_by_id(task_id):
    json_input = request.get_json()
    try:
        data = task_schema.load(json_input)
    except ValidationError as err:
        return {"errors": err.messages}, 422
    title = data.get('title')
    description = data.get('description')
    user_id = data.get('user_id')

    updated_values = {}

    if title is not None:
        updated_values['title'] = title

    if description is not None:
        updated_values['description'] = description

    if user_id is not None:
        updated_values['user_id'] = user_id

    statement = update(Tasks).where(Tasks.id == task_id).values(**updated_values)
    database_instance.session.execute(statement)
    database_instance.session.commit()
    return {'message': 'tasks atualizada'}


@tasks_bp.route('/id/<int:task_id>', methods=['DELETE'])
def delete_task_by_id(task_id):
    task = database_instance.session.get(Tasks, task_id)
    if not task:
        return {"error": "Task not found"}, 404
    stmt = delete(Tasks).where(Tasks.id == task_id)
    database_instance.session.execute(stmt)
    database_instance.session.commit()
    return {'message': 'task deletada'}


@tasks_bp.route('/user_id/<int:user_id>', methods=['GET'])
def get_user_tasks(user_id):
    tasks = database_instance.session.scalars(
        select(Tasks).where(Tasks.user_id == user_id)
    ).all()
    if not tasks:
        return {"error": "Task not found"}, 404
    task_dict = [task.as_dict() for task in tasks]
    return jsonify({'tasks': task_dict}), 200


@tasks_bp.route('/user_id/<int:user_id>', methods=['PATCH'])
def update_tasks_by_user_id(user_id):
    json_input = request.get_json()
    try:
        data = task_schema.load(json_input)
    except ValidationError as err:
        return {"errors": err.messages}, 422
    title = data.get('title')
    description = data.get('description')
    user_id_updated = data.get('user_id')

    updated_values = {}

    if title is not None:
        updated_values['title'] = title

    if description is not None:
        updated_values['description'] = description

    if user_id_updated is not None:
        updated_values['user_id'] = user_id_updated

    statement = update(Tasks).where(Tasks.user_id == user_id).values(**updated_values)
    database_instance.session.execute(statement)
    database_instance.session.commit()
    return {'message': 'Task atualizada'}


@tasks_bp.route('/user_id/<int:user_id>', methods=['DELETE'])
def delete_tasks_by_user_id(user_id):
    stmt = delete(Tasks).where(Tasks.user_id == user_id)
    result = database_instance.session.execute(stmt)
    database_instance.session.commit()
    if result.rowcount == 0:
        return {"error": "Task not found"}, 404
    return {'message': 'task deletada'}
