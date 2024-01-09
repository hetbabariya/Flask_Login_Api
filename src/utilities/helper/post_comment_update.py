from flask import jsonify , abort
from datetime import datetime
from src.utilities.helper.get_comment_by_id import get_comment_by_id


def update_post_comment(db , comment_id , comment , user_id):
    try : 
        comment_data = get_comment_by_id(comment_id=comment_id)

        if user_id != str(comment_data.user_id) :
            abort(401, "Unauthorized!")

        comment_data.comment = comment
        comment_data.modified_at =  datetime.now()
        db.session.commit()

        return jsonify({"message" : "post comment update successully!"})
    except Exception as e :
        return jsonify({"error " : str(e)})