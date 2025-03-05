from marshmallow import fields, Schema

class GET_SERVER_PROPERTIES(Schema):
    id = fields.Str(required=True)
    
class LIST_FILES(Schema):
    id = fields.Str(required=True)
    
class READ_FILE(Schema):
    id = fields.Str(required=True)
    path = fields.Str(required=True)
    file_name = fields.Str(required=True)
    
class MODIFY_FILE(Schema):
    id = fields.Str(required=True)
    path = fields.Str(required=True)
    file_name = fields.Str(required=True)
    updated_text = fields.Str(required=True)
    
class UPDATE_SERVER_PROPERTIES(Schema):
    id = fields.Str(required=True)
    updated_properties = fields.Str(required=True)
    
class UPDATE_SERVER_PROPERTY(Schema):
    id = fields.Str(required=True)
    updated_name = fields.Str(required=True)
    updated_value = fields.Str(required=True)
