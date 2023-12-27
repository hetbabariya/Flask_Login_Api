from flask import abort , jsonify
from src.database.model.post_like import PostLike
from schemaObj import Post_like_all_user_response_schema
from src.utilities.helper.get_post_by_postid import get_post_by_post_id

def all_like_by_post_id(post_id):
    post = get_post_by_post_id(post_id=post_id)
    
    likes = PostLike.query.filter_by(post_id = post_id).all()

    if likes is None:
        abort(404 , "Not Any Like!")

    return Post_like_all_user_response_schema.dump(likes)