from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime , timezone
from src.database.model.post_model import Post
from src.database.model.post_like import PostLike
from src.database.model.post_comment import PostComment
from src.database.model.follower_following import FollowerFollowing
from src.database.model.post_comment_like import PostCommentLike
from src.database.model.comment_reply import PostCommentReply
from src.database.model.follow_request import FollowRequest

import uuid

from src.database.ext import db

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(UUID(as_uuid=True), primary_key=True , default = uuid.uuid4)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    
    is_valid = db.Column(db.Boolean, nullable=False , default = False)
    is_active = db.Column(db.Boolean, nullable=False , default = True)
    is_delete = db.Column(db.Boolean, nullable=False , default = False)
    is_public = db.Column(db.Boolean, nullable=False)

    OTP = db.Column(db.String)
    otp_send_at = db.Column(db.DateTime()) 
    created_at = db.Column(db.DateTime(), default=datetime.now())

    follower_count = db.Column(db.Integer, nullable=True , default = 0)
    following_count = db.Column(db.Integer, nullable=True , default = 0)
    post_count = db.Column(db.Integer, nullable=True , default = 0)


    post_relation = db.relationship('Post' , back_populates = "user_relation")
    post_like_user_relation = db.relationship('PostLike' , back_populates = "post_table_user_relation")
    postComment_user_relation = db.relationship('PostComment' , back_populates = "postComment_table_user_relation")
    postCommentLike_user_relation = db.relationship('PostCommentLike' , back_populates = "postCommentLike_table_user_relation")
    postCommentReply_user_relation = db.relationship('PostCommentReply' , back_populates = "postCommentReply_table_user_relation")
    following_user_relation = db.relationship('FollowerFollowing' , back_populates = "following_table_user_relation" , foreign_keys="FollowerFollowing.user_id" )
    follower_user_relation = db.relationship('FollowerFollowing' , back_populates = "follower_table_user_relation" , foreign_keys="FollowerFollowing.followed_by" )
    followRequest_userid_user_relation = db.relationship('FollowRequest' , back_populates = "followRequest_userid_table_user_relation" , foreign_keys="FollowRequest.user_id" )
    followRequest_requestid_user_relation = db.relationship('FollowRequest' , back_populates = "followRequest_request_id_table_user_relation" , foreign_keys="FollowRequest.request_by_user_id")   