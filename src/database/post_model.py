from src.database.ext import db
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime , timezone
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
    user_id = db.Column(UUID(as_uuid=True) , db.ForeignKey("user_db.id") , nullable = False , index = True)

    like_count = db.Column(db.Integer , default = 0)
    comment_count = db.Column(db.Integer , default = 0)

    user_relation = db.relationship('User' , back_populates = "post_relation")
    post_like_post_relation = db.relationship('PostLike' , back_populates = "post_table_post_relation")