from marshmallow import validate, fields, Schema

class BaseSchema(Schema):
    id = fields.Str(required=True, validate=validate.Length(min=1))