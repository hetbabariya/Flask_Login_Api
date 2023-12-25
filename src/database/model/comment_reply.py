from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from src.database.model.post_comment_like import PostCommentLike
import uuid

from src.database.ext import db


class PostCommentReply(db.Model):
    __tablename__ = "Post_comment_reply"

    id = db.Column(UUID(as_uuid=True), primary_key=True , default = uuid.uuid4)
    comment_reply = db.Column(db.String , nullable = False)
    comment_id = db.Column(UUID(as_uuid=True), db.ForeignKey("post_comment.id") , nullable = False , index = True)
    post_id = db.Column(UUID(as_uuid=True), db.ForeignKey("posts.id") , nullable = False , index = True)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("user.id") , nullable = False , index = True)
    reply_at = db.Column(db.DateTime() , default = datetime.now())
    modified_at = db.Column(db.DateTime() )
    reply_like_count = db.Column(db.Integer , default = 0)


    postCommentReply_table_comment_relation = db.relationship('PostComment' , back_populates = "postComment_table_comment_reply_relation")
    postCommentReply_table_user_relation = db.relationship('User' , back_populates = "postCommentReply_user_relation")
    postCommentReply_table_commentLike_relation = db.relationship('PostCommentLike', back_populates = "postCommentLike_table_postCommentReply_relation")
    postCommentReply_table_post_relation = db.relationship('Post', back_populates = "postCommentreply_post_relation")
