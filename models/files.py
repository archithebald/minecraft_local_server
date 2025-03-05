from marshmallow import fields, Schema
from models.models_variables import BaseSchema

class GET_SERVER_PROPERTIES(BaseSchema):
    pass
    
class LIST_FILES(BaseSchema):
    pass
    
class READ_FILE(BaseSchema):
    path = fields.Str(required=True)
    file_name = fields.Str(required=True)
    
class MODIFY_FILE(BaseSchema):
    path = fields.Str(required=True)
    file_name = fields.Str(required=True)
    updated_text = fields.Str(required=True)
    
class UPDATE_SERVER_PROPERTIES(BaseSchema):
    updated_properties = fields.Str(required=True)
    
class UPDATE_SERVER_PROPERTY(BaseSchema):
    updated_name = fields.Str(required=True)
    updated_value = fields.Str(required=True)
