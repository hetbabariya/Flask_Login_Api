from flask import jsonify
from datetime import datetime
from src.utilities.helper.get_comment_by_id import get_comment_by_id


def update_post_comment(db , comment_id , comment):
    try : 
        comment_data = get_comment_by_id(comment_id=comment_id)

        comment_data.comment = comment
        comment_data.modified_at =  datetime.now()
        db.session.commit()

        return jsonify({"message" : "post comment update successully!"})
    except Exception as e :
        return jsonify({"error " : str(e)})