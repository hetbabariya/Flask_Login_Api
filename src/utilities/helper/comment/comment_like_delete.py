from flask import jsonify , abort
from src.utilities.helper.comment.get_comment_like_by_id import get_comment_like_by_id
from src.utilities.helper.comment.get_comment_by_id import get_comment_by_id

def comment_like_delete(comment_like_id , db,user_id):

    comment_like_data = get_comment_like_by_id(comment_like_id=comment_like_id)
    comment_data = get_comment_by_id(comment_id=comment_like_data.comment_id)

    if user_id != str(comment_like_data.user_id) :
            abort(401, "Unauthorized!")

    comment_data.comment_like_count -= 1
    db.session.delete(comment_like_data)
    db.session.commit()

    return jsonify({"message" : "Post comment Reply Deleted!"}),204