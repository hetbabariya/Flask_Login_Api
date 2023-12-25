from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from src.database.ext import db


class FollowerFollowing(db.Model):
    __tablename__ = "follower_following"

    id = db.Column(UUID(as_uuid=True), primary_key=True , default = uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("user.id") , nullable = False , index = True)
    followed_by = db.Column(UUID(as_uuid=True), db.ForeignKey("user.id") , nullable = False , index = True)
    followed_at = db.Column(db.DateTime() , default = datetime.now())

    following_table_user_relation = db.relationship('User' , back_populates = "following_user_relation" ,foreign_keys=[user_id])
    follower_table_user_relation = db.relationship('User' , back_populates = "follower_user_relation" ,foreign_keys=[followed_by])


    