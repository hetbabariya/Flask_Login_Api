from src.database.ext import ma
from marshmallow import fields

class PostCommentSchema(ma.Schema):
    post_id = fields.UUID()
    comment = fields.String()

class PostCommentResponseSchema(PostCommentSchema):
    class Meta :
        fields = ('id' , 'user_id' , 'post_id' , 'comment','comment_at' , 'comment_like_count' , 'comment_reply_count')

class PostCommentUpdateSchema(ma.Schema):
    comment_id = fields.UUID()
    comment = fields.String()

class PostRequestForCommentUser(ma.Schema):
    post_id = fields.UUID()


class PostCommentDelRequest(ma.Schema):
    comment_id = fields.UUID()