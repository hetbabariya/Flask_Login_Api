from flask import jsonify
from src.utilities.helper.get_comment_like_by_id import get_comment_like_by_id
from src.utilities.helper.get_comment_reply_by_id import get_comment_reply_by_id

def comment_reply_like_delete(comment_like_id , db):

    comment_reply_like_data = get_comment_like_by_id(comment_like_id=comment_like_id)

    if comment_reply_like_data.reply_id : 
        comment_reply_data = get_comment_reply_by_id(reply_id=comment_reply_like_data.reply_id)
        comment_reply_data.reply_like_count -= 1
        
    db.session.delete(comment_reply_like_data)
    db.session.commit()

    return jsonify({"message" : "Post comment Reply Deleted!"}),204