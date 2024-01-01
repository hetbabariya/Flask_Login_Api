from src.database.ext import ma
from marshmallow import fields


class UserRequest(ma.Schema):
    username = fields.Str(error_messages={"ERROR" : "It is required"})
    email = fields.Str(error_messages={"ERROR" : "It is required"})
    password = fields.Str(error_messages={"ERROR" : "It is required"})
    is_public = fields.Boolean(error_messages={"ERROR" : "It is required"})

class UserResponse(UserRequest):
    is_valid = fields.Boolean()
    is_active = fields.Boolean()
    is_delete = fields.Boolean()
    follower_count = fields.Integer()
    following_count = fields.Integer()
    post_count = fields.Integer()

class AllUserResponse(ma.Schema):
    data = fields.List(fields.Nested(lambda : UserResponse(exclude=['password'])))


class UserRegisterResponse(ma.Schema):
    message = fields.String()
    data = fields.List(fields.Nested(lambda: UserRequest(exclude=['password'])))


class UserForgrtPwd(ma.Schema):
    email = fields.Str(required=True , error_messages={"ERROR" : "It is required"})
    new_password = fields.Str(required=True , error_messages={"ERROR" : "It is required"})
    otp = fields.Str(required=True , error_messages={"ERROR" : "It is required"})

class UserChangePwd(ma.Schema):
    old_password = fields.Str(required=True , error_messages={"ERROR" : "It is required"})
    new_password = fields.Str(required=True , error_messages={"ERROR" : "It is required"})
    