from flask import jsonify , abort
from schemaObj import post_response
from src.database.crud import get_user_by_id
from src.database.model.post_model import Post

def get_post_by_post_id( post_id):
    
    post = Post.query.filter_by(id = post_id , is_delete = False).first()
    if post is None : 
        abort(404 , "Post Not Exists!")

    return post

    

