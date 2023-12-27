from flask import Blueprint , request , jsonify , g
from flask_jwt_extended import get_jwt_identity , create_access_token , decode_token

from src.database.model.user import db , User
from src.database.model.post_model import Post
from src.database.model.post_like import PostLike
from src.database.model.post_comment import PostComment

from src.database.crud import create_user , get_user_by_username , get_user_by_email , get_user_by_id ,get_all_user
from src.utilities.functionality import verify_otp , store_otp , forget_password , change_password , delete_user
from flask_jwt_extended import jwt_required
from src.auth.functionality import login_user , logout_user
from src.utilities.helper.post_create import create_post_In_db
from src.utilities.helper.post_caption_update import  update_post_caption
from src.utilities.helper.post_like import  post_like_by_user
from src.utilities.helper.post_comment import add_post_comment
from src.utilities.helper.post_comment_update import update_post_comment
from src.utilities.helper.get_all_post_of_user import get_all_posts_of_user
from src.utilities.helper.post_id_all_like import all_like_by_post_id
from src.utilities.helper.post_id_all_comment import all_comment_by_post_id
from schemaObj import (
                        User_forgrt_pwd ,
                        user_response ,
                        user_change_pwd ,
                        create_post ,
                        update_post ,
                        post_like ,
                        post_comment_schema ,
                        post_comment_update_schema,
                        user_response_single,
                        post_id_rquest_schema
                       )


register_user_db = Blueprint("register_users" , __name__)
read_user = Blueprint("read_users" , __name__ )
getAllUser = Blueprint("get_all_user" , __name__ )
sent_user_otp = Blueprint("sent_otp" , __name__)
verify_user_otp = Blueprint("verify_otp" , __name__)
login = Blueprint("login_user",__name__)
logout = Blueprint("logout_user",__name__)
forget_pwd = Blueprint("forget_password" , __name__)
change_pwd = Blueprint("change_password",__name__)
delete_act = Blueprint("delete_account",__name__)
refresh = Blueprint("Refresh_token",__name__)
createpost = Blueprint("create_post",__name__)
updatePost  = Blueprint("update_post" , __name__)
Postlike  = Blueprint("Post_like" , __name__)
create_post_Comment  = Blueprint("comment" , __name__)
update_comment  = Blueprint("update_comment" , __name__)
getAllPostOfUser  = Blueprint("get_all_post_of_user" , __name__)
getAllUserOfLikeOfPostId  = Blueprint("get_all_user_of_like_of_post_id" , __name__)
getAllUserOfCommentOfPostId  = Blueprint("get_all_user_of_comment_of_post_id" , __name__)


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
@change_pwd.route("/change_pwd",methods=['POST'])
@jwt_required()
def change_user_password():
    user_data = user_change_pwd.load(request.json)
    current_user_id = get_jwt_identity()
    response = change_password(old_pwd=user_data['old_password'] , new_pwd=user_data['new_password'] , current_user_id=current_user_id , User=User)
    return response 

# delete user
@delete_act.route("/delete_user",methods = ['POST'])
@jwt_required()
def delete_user_account():
    current_user_id = get_jwt_identity()
    response = delete_user(current_user_id=current_user_id , User=User)
    return response

# refresh token
@refresh.route("/refresh",methods = ['POST'])
@jwt_required(refresh=True)
def get_refresh_token():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify(access_token = access_token)


# create post
@createpost.route("/create_post",methods =['POST'])
@jwt_required()
def create_user_post():
    identity = get_jwt_identity()
    data = create_post.load(request.json)
    response = create_post_In_db(identity= identity , user_post=data['post'] , caption=data['caption'] , db=db , Post=Post)
    return response


# update post - caption
@updatePost.route("/update_caption" , methods = ['PATCH'])
@jwt_required()
def update_caption():
    data = update_post.load(request.json)
    response = update_post_caption(post_id=data['post_id'] , caption = data['caption'] , db=db)
    return response


# post like
@Postlike.route("/post_like" , methods = ['POST'])
@jwt_required()
def like_the_post():
    data = post_like.load(request.json)
    identity = get_jwt_identity()
    response = post_like_by_user(db=db , PostLike=PostLike , current_user_id=identity , post_id=data['post_id'])
    return response


# post comment
@create_post_Comment.route("/post_comment" , methods = ['POST'])
@jwt_required()
def post_comment_by_user():
    data = post_comment_schema.load(request.json)
    user_id = get_jwt_identity()
    response = add_post_comment(db=db , PostComment=PostComment , comment=data['comment'] , post_id=data['post_id'],user_id=user_id)
    return response


# update comment
@update_comment.route("/update_comment",methods=['PATCH'])
@jwt_required()
def post_update_comment():
    data = post_comment_update_schema.load(request.json)
    user_id = get_jwt_identity()
    response = update_post_comment(db=db , comment_id=data['comment_id'] , comment=data['comment'])
    return response


# get all post of user
@getAllPostOfUser.route("/get_all_posts" , methods = ['GET'])
@jwt_required()
def get_all_post_by_user_id():
    user_id = get_jwt_identity()
    posts = get_all_posts_of_user(current_user_id=user_id)
    return posts


# get all like_user of  specific post
@getAllUserOfLikeOfPostId.route('/get_user_of_like' , methods=["GET"])
@jwt_required()
def get_all_user_of_like():
    data = post_like.load(request.json)
    response = all_like_by_post_id(post_id = data['post_id'])
    return response

# get all comment_user of specific post
@getAllUserOfCommentOfPostId.route('/get_user_of_comment' , methods=["GET"])
@jwt_required()
def get_all_user_of_comemnt():
    data = post_id_rquest_schema.load(request.json)
    response = all_comment_by_post_id(post_id = data['post_id'])
    return response










# get all user
@getAllUser.route("/get_all_user" , methods = ['GET'])
@jwt_required()
def get_all_user_form_db():
    response = get_all_user(User=User)
    return response
    

# get user by username
@read_user.route("/get_user/<string:username>" , methods = ['GET'])
@jwt_required()
def read_user_by_username(username):
    response =  get_user_by_username(User=User , username=username)
    print(response)
    return user_response_single.dump(response)


# get by id
@read_user.route("/get_by_id" , methods = ['GET'])
@jwt_required()
def read_user_by_id():
    id = get_jwt_identity()
    response =  get_user_by_id(User=User , user_id = id)
    return user_response_single.dump(response)


# get user by email [Temporary]
@read_user.route("/get_user" , methods = ['GET'])
@jwt_required()
def read_user_by_email():
    data = request.args.get("data")
    respons =  get_user_by_email(User=User , email=data)    
    return user_response_single.dump(respons)
