from datetime import datetime
from flask import jsonify , abort
from src.utilities.helper.get_post_by_postid import get_post_by_post_id

def update_post_caption(post_id, caption , db , user_id):
    try :


        post_data = get_post_by_post_id(post_id=post_id)

        if user_id != str(post_data.user_id) :
            abort(401, "Unauthorized!")
            
        post_data.caption = caption
        post_data.modified_at = datetime.now()
        db.session.commit()
        return jsonify({"message" : "Post Caption Update Successfully!"})
    except Exception as e :
        return jsonify({"error " : str(e)})