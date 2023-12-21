from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from src.database.ext import db


class PostLike(db.Model):
    __tablename__ = "post_likes"

    id = db.Column(UUID(as_uuid=True), primary_key=True , default = uuid.uuid4)
    post_id = db.Column(UUID(as_uuid=True), db.ForeignKey("posts.id") , nullable = False , index = True)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("user_db.id") , nullable = False , index = True)
    like_at = db.Column(db.DateTime() , default = datetime.now())


    post_table_post_relation = db.relationship('Post' , back_populates = "post_like_post_relation")
    post_table_user_relation = db.relationship('User' , back_populates = "post_like_user_relation")