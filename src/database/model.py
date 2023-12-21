from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime , timezone
from src.database.post_model import Post
from src.database.post_like import PostLike
import uuid

from src.database.ext import db

class User(db.Model):
    __tablename__ = "user_db"

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


    post_relation = db.relationship('Post' , back_populates = "user_relation")
    post_like_user_relation = db.relationship('PostLike' , back_populates = "post_table_user_relation")