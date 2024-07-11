from marshmallow import Schema, fields

class ClotheSchema(Schema):
    id = fields.Str(dump_only=True)
    type_id = fields.Int(required = True)
    name = fields.Str(required=True)
    color = fields.Str(required=True)
    

class ClotheUpdateSchema(Schema):
    type_id = fields.Int()
    name = fields.Str()
    color = fields.Str()

class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    password = fields.Str(required=True)
        