from src.database.ext import ma
from marshmallow import fields

class UserfollowRequestSchema(ma.Schema):
    user_id = fields.UUID()

