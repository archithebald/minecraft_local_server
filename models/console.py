from marshmallow import fields, validate
from models.models_variables import BaseSchema

class SEND_COMMAND(BaseSchema):
    command = fields.Str(required=True, validate=validate.Length(min=1))