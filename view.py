from flask import Blueprint , request , jsonify
from src.database.model import db , User
from src.database.crud import create_user , get_user_by_username , get_user_by_email , store_otp
from src.utilities.functionality import verify_otp
from flask_jwt_extended import jwt_required
from src.auth.functionality import login_user , logout_user



register_user_db = Blueprint("register_users" , __name__)
read_user = Blueprint("read_users" , __name__ )
sent_user_otp = Blueprint("sent_otp" , __name__)
verify_user_otp = Blueprint("verify_otp" , __name__)
login = Blueprint("login_user",__name__)
logout = Blueprint("logout_user",__name__)

# register user
@register_user_db.route("/register_user" , methods = ['POST'])
def register_user():
    response = create_user(db=db , User=User)
    return response

# sent OTP
@sent_user_otp.route("/sent_otp" , methods = ['GET'])
def user_sent_otp():
    response = store_otp(db=db , User=User)
    return response


# verify otp
@verify_user_otp.route('/verify_otp' , methods=['POST'] )
def verify_the_otp() :
    user_send_otp = request.args.get("otp")
    response = verify_otp(user=User , otp=user_send_otp)
    return response


# login user
@login.route('/login',methods = ['POST'])
def login_the_user():
    user_data = request.get_json()
    print(user_data)
    response = login_user(User=User , username=user_data['username'] , password=user_data['password'])
    return response


# logout user
@logout.route('/logout' , methods = ['Post'])
def logout_the_user():
    response = logout_user()
    return response








#get user by username [Temporary]
@read_user.route("/get_user/<username>" , methods = ['GET'])
@jwt_required()
def read_user_by_username(username):
    response =  get_user_by_username(User=User , username=username)
    return response
 

# get user by email [Temporary]
@read_user.route("/get_user" , methods = ['GET'])
@jwt_required()
def read_user_by_email():
    data = request.args.get("data")
    respons =  get_user_by_email(User=User , email=data)    
    return respons