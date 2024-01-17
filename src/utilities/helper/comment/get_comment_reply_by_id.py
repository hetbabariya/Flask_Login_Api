from flask import abort
from src.database.model.comment_reply import PostCommentReply

def get_comment_reply_by_id(reply_id):
    comment_reply_data = PostCommentReply.query.filter_by(id = reply_id).first()

    if comment_reply_data is None : 
        abort(404 , "comment not Found!")

    return comment_reply_data
    