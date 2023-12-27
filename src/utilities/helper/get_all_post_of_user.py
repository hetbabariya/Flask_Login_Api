from flask import jsonify , abort
from src.database.model.user import User
from src.database.model.post_model import Post
from schemaObj import post_response_all

def get_all_posts_of_user( current_user_id):

    all_posts = Post.query.filter_by(user_id  = current_user_id).all() 

    if all_posts is None:
        abort(404 , "Not Any Post Yet!")

    return post_response_all.dump(all_posts)
