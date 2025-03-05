from marshmallow import fields
from models.models_variables import BaseSchema

class SEND_COMMAND(BaseSchema):
    command = fields.Str(required=True)