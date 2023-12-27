from marshmallow import fields , Schema
from src.database.ext import ma

class CreatePost(ma.Schema):
    post = fields.String(required=True)
    caption = fields.String(required=True)


class ResponsePost(CreatePost):
    class Meta : 
        fields = ('id' ,'post','caption' ,'user_id' , 'like_count' , 'comment_count' , 'created_at') 

class UpdatePost(ma.Schema):
    post_id = fields.UUID(required=True)
    caption = fields.String(required=True)
