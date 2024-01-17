from flask import abort, jsonify
from src.database.model.post_like import PostLike

def get_post_like_by_id(post_id , user_id):

    post_like_data = PostLike.query.filter_by(post_id = post_id , user_id = user_id).first()
    
    if not post_like_data:
        return abort(404 , "No data found")
    
    return post_like_data