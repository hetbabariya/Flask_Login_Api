from flask import abort, jsonify
from src.database.model.post_comment import PostComment

def get_comment_by_id(comment_id):
    
    comment_data = PostComment.query.filter_by(id = comment_id).first()

    if comment_data is None : 
        abort(404 , "comment not Found!")

    return comment_data
    