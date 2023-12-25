from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from src.database.ext import db


class PostCommentLike(db.Model):
    __tablename__ = "post_comment_like"

    id = db.Column(UUID(as_uuid=True), primary_key=True , default = uuid.uuid4)
    post_id = db.Column(UUID(as_uuid=True), db.ForeignKey("posts.id") , nullable = False , index = True)
    reply_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Post_comment_reply.id") , nullable = False , index = True)
    comment_id = db.Column(UUID(as_uuid=True), db.ForeignKey("post_comment.id") , nullable = False , index = True)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("user.id") , nullable = False , index = True)
    comment_like_at = db.Column(db.DateTime() , default = datetime.now())


    postCommentLike_table_post_relation = db.relationship('Post' , back_populates = "postCommentLike_post_relation")
    postCommentLike_table_user_relation = db.relationship('User' , back_populates = "postCommentLike_user_relation")
    postCommentLike_table_postCommentReply_relation = db.relationship('PostCommentReply', back_populates="postCommentReply_table_commentLike_relation") 
    postCommentLike_table_postComment_relation = db.relationship('PostComment' , back_populates = "postComment_table_postCommentLike_relation")