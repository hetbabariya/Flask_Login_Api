from datetime import datetime
from flask import jsonify , abort
from src.utilities.helper.comment.get_comment_by_id import get_comment_by_id
from src.database.model.comment_reply import PostCommentReply
from schemaObj import post_comment_reply_response_schema


def get_data_by_comment_reply(reply_id):
    data = PostCommentReply.query.filter_by(id = reply_id).first()

    if data is None :
        abort(404 , "Data Not Found!")

    return data

def update_comment_reply(reply_id , updated_comment_reply , db , user_id):

    comment_reply_data = get_data_by_comment_reply(reply_id= reply_id)

    if user_id != str(comment_reply_data.user_id) :
            abort(401, "Unauthorized!")

    comment_reply_data.comment_reply = updated_comment_reply
    comment_reply_data.modified_at = datetime.now()
    db.session.commit()

    return jsonify({"messagse" : "comment reply update successfuly!"})

