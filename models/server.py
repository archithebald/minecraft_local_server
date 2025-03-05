from marshmallow import Schema, fields, validate
from models.models_variables import BaseSchema

class ADD_MODS(BaseSchema):
    mods_ids = fields.Str(required=True, validate=validate.Length(min=1))

class CREATE(Schema):
    game_version = fields.Str(required=True, validate=validate.Length(min=1))
    description = fields.Str(required=True, validate=validate.Length(min=1))
    server_version = fields.Str(required=True, validate=validate.Length(min=1))
    ram_max = fields.Str(required=True, validate=validate.Length(min=1))
    ram_min = fields.Str(required=True, validate=validate.Length(min=1))

class GET_SERVER(BaseSchema):
    pass  

class GET_ALL_SERVERS(Schema):
    pass  

class IS_SERVER_STARTED(BaseSchema):
    pass  

class START(BaseSchema):
    pass

class STOP(BaseSchema):
    pass