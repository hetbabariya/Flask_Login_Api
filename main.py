from flask import Flask

# from src.database.model import  db
from src.database.ext import  db
from config import Config
from src.auth.config import jwt , initialize_jwt
from view import (
    register_user_db,
    read_user,
    getAllUser,
    sent_user_otp,
    verify_user_otp,
    login,
    logout,
    forget_pwd,
    change_pwd,
    delete_act,
    refresh,
    createpost,
    updatePost,
    Postlike,
    create_post_Comment,
    update_comment,
    getAllPostOfUser,
    getAllUserOfLikeOfPostId,
    getAllUserOfCommentOfPostId,
    post_comment_reply,
    UpdateCommentReply,
    commentLike,
    commentReplyLike,
    commentDelete ,
    commentReplyDelete,
    commentLikeDelete,
    commentReplyLikeDelete,
    deletePostRequest,
    deletePostLikeRequest,
    followUser,
    FollowrequestAccept
    )


app = Flask(__name__)


# initalize with app
initialize_jwt(app)

# register blueprint    
app.register_blueprint(register_user_db)
app.register_blueprint(read_user)
app.register_blueprint(sent_user_otp)
app.register_blueprint(verify_user_otp)
app.register_blueprint(login)
app.register_blueprint(logout)
app.register_blueprint(forget_pwd)
app.register_blueprint(change_pwd)
app.register_blueprint(delete_act)
app.register_blueprint(refresh)
app.register_blueprint(createpost)
app.register_blueprint(updatePost)
app.register_blueprint(Postlike)
app.register_blueprint(create_post_Comment)
app.register_blueprint(update_comment)
app.register_blueprint(getAllUser)
app.register_blueprint(getAllPostOfUser)
app.register_blueprint(getAllUserOfLikeOfPostId)
app.register_blueprint(getAllUserOfCommentOfPostId)
app.register_blueprint(post_comment_reply)
app.register_blueprint(UpdateCommentReply)
app.register_blueprint(commentLike)
app.register_blueprint(commentReplyLike)
app.register_blueprint(commentDelete)
app.register_blueprint(commentReplyDelete)
app.register_blueprint(commentLikeDelete)
app.register_blueprint(commentReplyLikeDelete)
app.register_blueprint(deletePostRequest)
app.register_blueprint(deletePostLikeRequest)
app.register_blueprint(followUser)
app.register_blueprint(FollowrequestAccept)


#  config with database config
app.config.from_object(Config)

# initalize with app
db.init_app(app)

# initalize with app
jwt.init_app(app)

# app.app_context().push()

# # create db model
# with app.app_context():
#     db.create_all()



if __name__ == "__main__":
    app.run(debug=True)