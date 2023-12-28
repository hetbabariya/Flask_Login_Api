from src.database.ext import ma
from marshmallow import fields

class PostCommentReplySchema(ma.Schema):
    comment_id = fields.UUID()
    comment_reply = fields.String()

class PostCommentReplyResponseSchema(ma.Schema):
    class Meta :
        fields = ('id' , 'comment_reply' , 'comment_id' , 'post_id' , 'user_id' , 'reply_at' , 'modified_at' , 'reply_like_count')

class PostCommentReplyUpdateSchema(ma.Schema):
    reply_id = fields.UUID()
    comment_reply = fields.String()

class PostCommentRemoveRequest(ma.Schema):
    comment_reply_id = fields.UUID()
