from src.database.ext import ma
from marshmallow import fields

class PostLikeSchema(ma.Schema):
    post_id = fields.UUID()

class PostLikeResponse(PostLikeSchema):
    class Meta : 
        fields = ('id' , 'post_id','user_id','like_at')


class DeletePostLikeRequest(ma.Schema):
    post_id = fields.UUID()