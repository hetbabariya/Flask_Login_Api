from src.database.ext import db
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime , timezone
from src.database.model.post_like import PostLike
from src.database.model.post_comment_like import PostCommentLike
from src.database.model.post_comment import PostComment
from src.database.model.comment_reply import PostCommentReply
import uuid

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(UUID(as_uuid=True), primary_key=True , default = uuid.uuid4)
    post = db.Column(db.String, nullable=False )
    caption = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime() , default = datetime.now())
    modified_at = db.Column(db.DateTime())
    is_archieve = db.Column(db.Boolean , default = False)
    is_delete = db.Column(db.Boolean , default = False)
    user_id = db.Column(UUID(as_uuid=True) , db.ForeignKey("user.id") , nullable = False , index = True)
    like_count = db.Column(db.Integer , default = 0)
    comment_count = db.Column(db.Integer , default = 0)

# Relationship
    user_relation = db.relationship('User' , back_populates = "post_relation")
    post_like_post_relation = db.relationship('PostLike' , back_populates = "post_table_post_relation")
    postCommentLike_post_relation = db.relationship('PostCommentLike' , back_populates = "postCommentLike_table_post_relation")
    postComment_post_relation = db.relationship('PostComment' , back_populates = "postComment_table_post_relation")
    postCommentreply_post_relation = db.relationship('PostCommentReply' , back_populates = "postCommentReply_table_post_relation")