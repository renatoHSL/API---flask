from flask import Blueprint

tasks_bp = Blueprint('tasks', __name__, url_prefix='/api/v1/tasks')


@tasks_bp.route('/<int:tasks_id>', methods=['GET'])
def get_tasks(tasks_id):
    return {'message': 'Task encontrada'}


@tasks_bp.route('/', methods=['GET'])
def get_tasks():
    return {'message': 'Lista de tasks'}


@tasks_bp.route('/', methods=['POST'])
def create_task():
    return {'message': 'Task criada!'}


@tasks_bp.route('/', methods=['DELETE'])
def delete_task():
    return {'message': 'Task deletada!'}


@tasks_bp.route('/', methods=['PUT'])
def update_task():
    return {'message': 'Task atualizada!'}
