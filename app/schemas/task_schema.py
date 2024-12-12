from marshmallow import Schema, fields


class TaskSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    status = fields.Boolean()
    created_date = fields.DateTime()
    updated_at = fields.DateTime()

    user_id = fields.Int()
