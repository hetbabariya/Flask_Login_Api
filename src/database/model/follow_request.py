from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from src.database.ext import db

class FollowRequest(db.Model):
    __tablename__ = "follow_request"
    
    id = db.Column(UUID(as_uuid=True), primary_key=True , default = uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("user.id") , nullable = False , index = True)
    request_user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("user.id") , nullable = False , index = True)
    accepted = db.Column(db.Boolean , default = False)
    request_at = db.Column(db.DateTime() , default = datetime.now())


    followRequest_userid_table_user_relation = db.relationship('User' , back_populates = "followRequest_userid_user_relation" , foreign_keys = [user_id])
    followRequest_request_id_table_user_relation = db.relationship('User' , back_populates = "followRequest_requestid_user_relation" , foreign_keys = [request_user_id])