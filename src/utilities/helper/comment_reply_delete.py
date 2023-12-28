from flask import jsonify
from src.utilities.helper.get_comment_reply_by_id import get_comment_reply_by_id
from src.utilities.helper.get_comment_by_id import get_comment_by_id

def comment_reply_delete(comment_reply_id , db):

    comment_reply_data = get_comment_reply_by_id(reply_id=comment_reply_id)
    comment_data = get_comment_by_id(comment_id=comment_reply_data.comment_id)

    comment_data.comment_reply_count -= 1
    db.session.delete(comment_reply_data)
    db.session.commit()

    return jsonify({"message" : "Post comment Reply Deleted!"}),204