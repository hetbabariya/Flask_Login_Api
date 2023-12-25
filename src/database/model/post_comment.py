from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from src.database.model.post_comment_like import PostCommentLike
from src.database.model.comment_reply import PostCommentReply

import uuid

from src.database.ext import db


class PostComment(db.Model):
    __tablename__ = "post_comment"

    id = db.Column(UUID(as_uuid=True), primary_key=True , default = uuid.uuid4)
    comment = db.Column(db.String , nullable = False)
    post_id = db.Column(UUID(as_uuid=True), db.ForeignKey("posts.id") , nullable = False , index = True)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("user.id") , nullable = False , index = True)
    comment_at = db.Column(db.DateTime() , default = datetime.now())
    modified_at = db.Column(db.DateTime() )
    comment_like_count = db.Column(db.Integer , default = 0)
    comment_reply_count = db.Column(db.Integer , default = 0)


    postComment_table_post_relation = db.relationship('Post' , back_populates = "postComment_post_relation")
    postComment_table_user_relation = db.relationship('User' , back_populates = "postComment_user_relation")
    postComment_table_postCommentLike_relation = db.relationship('PostCommentLike' , back_populates = "postCommentLike_table_postComment_relation")
    postComment_table_comment_reply_relation = db.relationship('PostCommentReply' , back_populates = "postCommentReply_table_comment_relation")