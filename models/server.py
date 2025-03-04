from marshmallow import Schema, fields

class ADD_MODS(Schema):
    id = fields.Str(required=True)
    mods_ids = fields.Str(required=True)
    
class CREATE(Schema):
    game_version = fields.Str(required=True)
    description = fields.Str(required=True)
    server_version = fields.Str(required=True)
    ram_max = fields.Str(required=True)
    ram_min = fields.Str(required=True)
    
class GET_SERVER(Schema):
    id = fields.Str(required=True)
    
class IS_SERVER_STARTED(Schema):
    id = fields.Str(required=True)
    
class START(Schema):
    id = fields.Str(required=True)

class STOP(Schema):
    id = fields.Str(required=True)