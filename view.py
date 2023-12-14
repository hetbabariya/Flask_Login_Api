from flask import Blueprint , request , jsonify
from src.database.model import db , User
from src.database.crud import create_user , get_user_by_username , get_user_by_email , store_otp


register_user_db = Blueprint("register_users" , __name__)
read_user = Blueprint("read_users" , __name__ )
sent_otp = Blueprint("sent_otp" , __name__)

# register user
@register_user_db.route("/register_user" , methods = ['POST'])
def register_user():
    response = create_user(db=db , User=User)
    return response

# sent OTP
@sent_otp.route("/sent_otp" , methods = ['GET'])
def user_sent_otp():
    response = store_otp(db=db , User=User)
    return response

#get user by username [Temporary]
@read_user.route("/get_user/<username>" , methods = ['GET'])
def read_user_by_username(username):
    response =  get_user_by_username(User=User , username=username)
    return response
 

# get user by email [Temporary]
@read_user.route("/get_user" , methods = ['GET'])
def read_user_by_email():
    data = request.args.get("data")
    respons =  get_user_by_email(User=User , email=data)    
    return respons