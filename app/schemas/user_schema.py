from marshmallow import Schema, fields, validate, pre_load
from marshmallow import ValidationError


def validate_username(value):
    if not value.isalnum():
        raise ValidationError("Username must contain only letters and numbers.")


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(
        validate=[
            validate.Length(min=3, max=20),
            validate_username
        ],
        required=True
    )
    email = fields.Str(
        required=True,
        validate=validate.Email(error="Invalid email format. Please enter a valid email.")
    )
    password = fields.Str(
        attribute="password_hash",
        required=True,
        validate=[validate.Length(min=6, max=36)],
        load_only=True
    )

    @pre_load
    def process_input(self, data, **kwargs):
        data["email"] = data["email"].lower().strip()
        return data
