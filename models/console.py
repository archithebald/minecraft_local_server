from marshmallow import fields, Schema

class SEND_COMMAND(Schema):
    id = fields.Str(required=True)
    command = fields.Str(required=True)