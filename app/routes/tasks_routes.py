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
    """
    Cria uma nova tarefa
    ---
    tags:
      - Tasks
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              title:
                type: string
                example: "Nova tarefa"
              description:
                type: string
                example: "Descrição da tarefa"
              user_id:
                type: integer
                example: 1
    responses:
      200:
        description: Tarefa criada com sucesso
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "Task criada!"
      422:
        description: Dados inválidos
    """
    json_input = request.get_json()
    print("json", json_input)
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
    """
    Lista todas as tarefas
    ---
    tags:
      - Tasks
    responses:
      200:
        description: Lista de tarefas retornada com sucesso
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    example: 1
                  title:
                    type: string
                    example: "Nova tarefa"
                  description:
                    type: string
                    example: "Descrição"
                  user_id:
                    type: integer
                    example: 1
      404:
        description: Nenhuma tarefa encontrada
    """
    tasks = database_instance.session.scalars(select(Tasks)).all()
    if not tasks:
        return {"error": "No tasks on the database"}, 404
    task_dict = [task.as_dict() for task in tasks]
    return jsonify({'tasks': task_dict}), 200


@tasks_bp.route('/id/<int:task_id>', methods=['GET'])
def get_tasks_id(task_id):
    """
    Retorna uma tarefa específica pelo ID
    ---
    tags:
      - Tasks
    parameters:
      - name: task_id
        in: path
        required: true
        schema:
          type: integer
        description: ID da tarefa
    responses:
      200:
        description: Tarefa encontrada
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                title:
                  type: string
                  example: "Nova tarefa"
                description:
                  type: string
                  example: "Descrição"
                user_id:
                  type: integer
                  example: 1
      404:
        description: Tarefa não encontrada
    """
    task = database_instance.session.get(Tasks, task_id)
    if not task:
        return {"error": "Task not found"}, 404
    return jsonify(task.as_dict()), 200


@tasks_bp.route('/id/<int:task_id>', methods=['PATCH'])
def update_task_by_id(task_id):
    """
    Atualiza uma tarefa pelo ID
    ---
    tags:
      - Tasks
    parameters:
      - name: task_id
        in: path
        required: true
        schema:
          type: integer
        description: ID da tarefa a ser atualizada
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              title:
                type: string
                example: "Título atualizado"
              description:
                type: string
                example: "Descrição atualizada"
              user_id:
                type: integer
                example: 1
    responses:
      200:
        description: Tarefa atualizada com sucesso
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "tasks atualizada"
      404:
        description: Tarefa não encontrada
    """
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
    return {'message': 'task atualizada'}


@tasks_bp.route('/id/<int:task_id>', methods=['DELETE'])
def delete_task_by_id(task_id):
    """
    Deleta uma tarefa pelo ID
    ---
    tags:
      - Tasks
    parameters:
      - name: task_id
        in: path
        required: true
        schema:
          type: integer
        description: ID da tarefa a ser deletada
    responses:
      200:
        description: Tarefa deletada com sucesso
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "task deletada"
      404:
        description: Tarefa não encontrada
    """
    task = database_instance.session.get(Tasks, task_id)
    if not task:
        return {"error": "Task not found"}, 404
    stmt = delete(Tasks).where(Tasks.id == task_id)
    database_instance.session.execute(stmt)
    database_instance.session.commit()
    return {'message': 'task deletada'}


@tasks_bp.route('/user_id/<int:user_id>', methods=['GET'])
def get_user_tasks_by_id(user_id):
    """
        Lista todas as tarefas de um usuário
        ---
        tags:
          - Tasks
        parameters:
          - name: user_id
            in: path
            required: true
            schema:
              type: integer
            description: ID do usuário cujas tarefas serão listadas
        responses:
          200:
            description: Lista de tarefas retornada com sucesso
            content:
              application/json:
                schema:
                  type: array
                  items:
                    type: object
                    properties:
                      id:
                        type: integer
                        example: 1
                      title:
                        type: string
                        example: "Título da tarefa"
                      description:
                        type: string
                        example: "Descrição da tarefa"
                      user_id:
                        type: integer
                        example: 1
          404:
            description: Nenhuma tarefa encontrada para o usuário
        """
    tasks = database_instance.session.scalars(
        select(Tasks).where(Tasks.user_id == user_id)
    ).all()
    if not tasks:
        return {"error": "Task not found"}, 404
    task_dict = [task.as_dict() for task in tasks]
    return jsonify({'tasks': task_dict}), 200


@tasks_bp.route('/user_id/<int:user_id>', methods=['PATCH'])
def update_tasks_by_user_id(user_id):
    """
        Atualiza todas as tarefas de um usuário
        ---
        tags:
          - Tasks
        parameters:
          - name: user_id
            in: path
            required: true
            schema:
              type: integer
            description: ID do usuário cujas tarefas serão atualizadas
        requestBody:
          required: true
          content:
            application/json:
              schema:
                type: object
                properties:
                  title:
                    type: string
                    example: "Título atualizado"
                  description:
                    type: string
                    example: "Descrição atualizada"
                  user_id:
                    type: integer
                    example: 2
        responses:
          200:
            description: Tarefas atualizadas com sucesso
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    message:
                      type: string
                      example: "Task atualizada"
          404:
            description: Nenhuma tarefa encontrada para o usuário
        """
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
    """
        Deleta todas as tarefas de um usuário
        ---
        tags:
          - Tasks
        parameters:
          - name: user_id
            in: path
            required: true
            schema:
              type: integer
            description: ID do usuário cujas tarefas serão deletadas
        responses:
          200:
            description: Tarefas deletadas com sucesso
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    message:
                      type: string
                      example: "task deletada"
          404:
            description: Nenhuma tarefa encontrada para o usuário
        """
    stmt = delete(Tasks).where(Tasks.user_id == user_id)
    result = database_instance.session.execute(stmt)
    database_instance.session.commit()
    if result.rowcount == 0:
        return {"error": "Task not found"}, 404
    return {'message': 'task deletada'}
