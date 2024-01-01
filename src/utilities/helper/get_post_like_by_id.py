from flask import abort, jsonify
from src.database.model.post_like import PostLike

def get_post_like_by_id(like_id ):

    post_like_data = PostLike.query.filter_by(id = like_id).first()
    
    if not post_like_data:
        return abort({"message": "No data found"}), 404
    
    return post_like_data