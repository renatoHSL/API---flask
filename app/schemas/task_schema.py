# import datetime as dt

from marshmallow import Schema, fields, validate, post_dump


# from app.models import Tasks


class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(
        validate=[
            validate.Length(min=3, max=20, error="O título deve ter entre 3 e 20 caracteres.")
        ],
        required=True)
    description = fields.Str(
        validate=[
            validate.Length(min=5, max=45, error="A descrição deve ter entre 5 e 45 caracteres.")
        ],
        required=True)
    done = fields.Boolean(
        attribute="is_done",
        missing=False
    )

    user_id = fields.Int()

    @post_dump(pass_many=True)
    def wrap(self, data, many, **kwargs):
        key = "tasks" if many else "task"
        return {key: data}

    # @post_load
    # def make_object(self, data, **kwargs):
    #     if not data:
    #         return None
    #     return Tasks(
    #         title=data["title"],
    #         description=data["description"],
    #         is_done=data["is_done"],
    #         created_date=dt.datetime.now(dt.timezone.utc),
    #         updated_at=dt.datetime.now(dt.timezone.utc),
    #     )
