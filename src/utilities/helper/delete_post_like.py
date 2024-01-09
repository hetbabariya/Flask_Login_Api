from flask import jsonify
from src.utilities.helper.get_post_like_by_id import get_post_like_by_id
from src.utilities.helper.get_post_by_postid import get_post_by_post_id

def delete_post_like(db , post_id , user_id):

    like_data = get_post_like_by_id(post_id , user_id)

    post_data = get_post_by_post_id(post_id=post_id)

    post_data.like_count -= 1
    
    db.session.delete(like_data)
    db.session.commit()


    return jsonify({"message" : "post Like Deleted!"}),204
