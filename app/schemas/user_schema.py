from marshmallow import Schema, fields, validate, pre_load


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(validate=[validate.Length(min=3, max=20)], required=True)
    email = fields.Str(required=True, validate=validate.Email(error="Not a valid email address"))
    password = fields.Str(
        attribute="password_hash", required=True, validate=[validate.Length(min=6, max=36)], load_only=True
    )

    @pre_load
    def process_input(self, data, **kwargs):
        data["email"] = data["email"].lower().strip()
        return data
