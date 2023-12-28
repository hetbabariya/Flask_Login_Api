from src.database.ext import ma
from marshmallow import fields

class commentLikeRequestSchema(ma.Schema):
    comment_id = fields.UUID()

class commmentReplyLikeRequestSchema(ma.Schema):
    reply_id = fields.UUID()

class ResponseSchema(ma.Schema):
    id = fields.UUID()
    post_id = fields.UUID()
    comment_id = fields.UUID()
    user_id = fields.UUID()
    comment_like_at = fields.DateTime()
    reply_id = fields.UUID()

class commentLikeResponseSchema(ma.Schema):
    message = fields.String()
    data = fields.List(fields.Nested(ResponseSchema))

class commentLikeDelete(ma.Schema):
    comment_like_id = fields.UUID()
