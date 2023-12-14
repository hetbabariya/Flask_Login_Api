from flask_marshmallow import Marshmallow
from marshmallow import fields

ma = Marshmallow()


class UserRequest(ma.Schema):
    username = fields.Str(required=True , error_messages={"ERROR" : "It is required"})
    email = fields.Str(required=True , error_messages={"ERROR" : "It is required"})
    password = fields.Str(required=True , error_messages={"ERROR" : "It is required"})

class UserResponse(ma.Schema):
    class Meta :
        fields = ('id' , 'username' , 'email' , 'OTP')

