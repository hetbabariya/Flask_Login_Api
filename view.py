from flask import Blueprint , request , jsonify , g
from flask_jwt_extended import get_jwt_identity , create_access_token , decode_token

from src.database.model import db , User
from src.database.crud import create_user , get_user_by_username , get_user_by_email , get_user_by_id
from src.utilities.functionality import verify_otp , store_otp , forget_password , change_password , delete_user
from flask_jwt_extended import jwt_required
from src.auth.functionality import login_user , logout_user
from schemaObj import User_forgrt_pwd , user_response , user_change_pwd
# from src.auth.functionality import 


register_user_db = Blueprint("register_users" , __name__)
read_user = Blueprint("read_users" , __name__ )
sent_user_otp = Blueprint("sent_otp" , __name__)
verify_user_otp = Blueprint("verify_otp" , __name__)
login = Blueprint("login_user",__name__)
logout = Blueprint("logout_user",__name__)
forget_pwd = Blueprint("forget_password" , __name__)
change_pwd = Blueprint("change_password",__name__)
delete_act = Blueprint("delete_account",__name__)
refresh = Blueprint("Refresh_token",__name__)


# register user
@register_user_db.route("/register_user" , methods = ['POST'])
def register_user():
    response = create_user(db=db , User=User)
    return response

# sent OTP
@sent_user_otp.route("/sent_otp" , methods = ['POST'])
def user_sent_otp():
    response = store_otp(db=db , User=User)
    return response


# verify otp
@verify_user_otp.route('/verify_otp' , methods=['POST'] )
def verify_the_otp() :
    user_send_data = request.get_json()
    response = verify_otp(User=User , email = user_send_data['email'] , otp = user_send_data['otp'])
    return response


# login user
@login.route('/login',methods = ['POST'])
def login_the_user():
    user_data = request.get_json()
    response = login_user(User=User , username=user_data['username'] , password=user_data['password'])
    return response


# logout user
@logout.route('/logout' , methods = ['Post'])
def logout_the_user():
    response = logout_user()
    return response

# forget password
@forget_pwd.route('/forget_pwd' , methods = ['POST'])
def forget_user_password():
    user_data = User_forgrt_pwd.load(request.json)
    response = forget_password(new_pwd=user_data['new_password'] , email = user_data['email'] ,  User=User , otp = user_data['otp'])
    return response

# change password
@change_pwd.route("/change_pwd",methods=['GET'])
@jwt_required()
def change_user_password():
    user_data = user_change_pwd.load(request.json)
    current_user = get_jwt_identity()
    print("current_user : ",current_user)
    response = change_password(old_pwd=user_data['old_password'] , new_pwd=user_data['new_password'] , current_user=current_user , User=User)
    return response 

# delete user
@delete_act.route("/delete_user",methods = ['POST'])
@jwt_required()
def delete_user_account():
    current_user = get_jwt_identity()
    response = delete_user(current_user=current_user , User=User)
    return response

# refresh token
@refresh.route("/refresh",methods = ['POST'])
@jwt_required(refresh=True)
def get_refresh_token():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify(access_token = access_token)









# get user by username
@read_user.route("/get_user" , methods = ['GET'])
@jwt_required()
def read_user_by_username():
    # headers = request.headers
    # bearer = headers.get('Authorization')    # Bearer YourTokenHere
    # token = bearer.split()[1]
    response =  get_user_by_username(User=User , username= g.user['sub'])
    return user_response.jsonify(response)

# get by id
@read_user.route("/get_by_id" , methods = ['GET'])
@jwt_required()
def read_user_by_id():
    response =  get_user_by_id(User=User , user_id = g.user.get('sub'))
    return user_response.jsonify(response)
    

# get user by email [Temporary]
@read_user.route("/get_user" , methods = ['GET'])
@jwt_required()
def read_user_by_email():
    data = request.args.get("data")
    respons =  get_user_by_email(User=User , email=data)    
    return respons
