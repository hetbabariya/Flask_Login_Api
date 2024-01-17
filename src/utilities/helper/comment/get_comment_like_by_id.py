from flask import abort, jsonify
from src.database.model.post_comment_like import PostCommentLike

def get_comment_like_by_id(comment_like_id ):

    comment_like_data = PostCommentLike.query.filter_by(id = comment_like_id).first()
    
    if not comment_like_data:
        return abort({"message": "No data found"}), 404
    
    return comment_like_data