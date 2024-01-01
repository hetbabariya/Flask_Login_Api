from flask import jsonify
from src.utilities.helper.get_post_by_postid import get_post_by_post_id
from src.database.crud import get_user_by_id

def delete_post(db , post_id):

    post_data = get_post_by_post_id(post_id=post_id)

    user_data = get_user_by_id(user_id=post_data.user_id)

    user_data.post_count -= 1
    post_data.is_delete = True

    db.session.commit()


    return jsonify({"message" : "post Deleted!"}),204
