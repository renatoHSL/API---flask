from marshmallow import Schema, fields, validate


class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(validate=[validate.Length(min=3, max=20)], required=True)
    description = fields.Str(validate=[validate.Length(min=5, max=45)], required=True)
    status = fields.Boolean()
    created_date = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    user_id = fields.Int()
