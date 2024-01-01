from marshmallow import fields , Schema
from src.database.ext import ma

class CreatePost(ma.Schema):
    post = fields.String(required=True)
    caption = fields.String(required=True)


class ResponsePost(CreatePost):
    id = fields.UUID()
    user_id = fields.UUID()
    created_at = fields.DateTime()
    like_count = fields.Integer()
    comment_count = fields.Integer()

class postCreateResponse(ma.Schema):
    message = fields.String()
    data = fields.List(fields.Nested(ResponsePost))

class UpdatePost(ma.Schema):
    post_id = fields.UUID(required=True)
    caption = fields.String(required=True)

class DeletePostRequest(ma.Schema):
    post_id = fields.UUID()
    
