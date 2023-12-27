from src.database.ext import ma
from marshmallow import fields




class UserRequest(ma.Schema):
    username = fields.Str(error_messages={"ERROR" : "It is required"})
    email = fields.Str(error_messages={"ERROR" : "It is required"})
    password = fields.Str(error_messages={"ERROR" : "It is required"})
    is_public = fields.Boolean(error_messages={"ERROR" : "It is required"})

class UserResponse(ma.Schema):
    class Meta :
        fields = ('id' , 'username' , 'email' , 'is_public' , 'follower_count' , 'following_count' , 'post_count')


class UserForgrtPwd(ma.Schema):
    email = fields.Str(required=True , error_messages={"ERROR" : "It is required"})
    new_password = fields.Str(required=True , error_messages={"ERROR" : "It is required"})
    otp = fields.Str(required=True , error_messages={"ERROR" : "It is required"})

class UserChangePwd(ma.Schema):
    old_password = fields.Str(required=True , error_messages={"ERROR" : "It is required"})
    new_password = fields.Str(required=True , error_messages={"ERROR" : "It is required"})
    