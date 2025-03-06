from marshmallow import fields, Schema, validate
from models.models_variables import BaseSchema

class GET_SERVER_PROPERTIES(BaseSchema):
    pass
    
class LIST_FILES(BaseSchema):
    pass
    
class READ_FILE(BaseSchema):
    path = fields.Str(required=True, validate=validate.Length(min=1))
    file_name = fields.Str(required=True, validate=validate.Length(min=1))
    
class MODIFY_FILE(BaseSchema):
    path = fields.Str(required=True, validate=validate.Length(min=1))
    file_name = fields.Str(required=True, validate=validate.Length(min=1))
    updated_text = fields.Str(required=True, validate=validate.Length(min=1))
    
class UPDATE_SERVER_PROPERTIES(BaseSchema):
    updated_properties = fields.Str(required=True, validate=validate.Length(min=1))
    
class UPDATE_SERVER_PROPERTY(BaseSchema):
    updated_name = fields.Str(required=True, validate=validate.Length(min=1))
    updated_value = fields.Str(required=True, validate=validate.Length(min=1))

class ADD_MODS(BaseSchema):
    mods_ids = fields.Str(required=True, validate=validate.Length(min=1))

class REMOVE_MODS(BaseSchema):
    slugs = fields.Str(required=True, validate=validate.Length(min=1))
    
class LIST_MODS(BaseSchema):
    pass

class ADD_TO_WHITELIST(BaseSchema):
    usernames = fields.Str(required=True, validate=validate.Length(min=1))