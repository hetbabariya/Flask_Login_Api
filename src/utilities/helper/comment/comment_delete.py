from flask import jsonify , abort
from src.utilities.helper.comment.get_comment_by_id import get_comment_by_id
from src.utilities.helper.post.get_post_by_postid import get_post_by_post_id

def comment_delete(comment_id , db , user_id):

    comment_data = get_comment_by_id(comment_id=comment_id)
    post_data = get_post_by_post_id(post_id=comment_data.post_id)

    if user_id != str(comment_data.user_id) :
            abort(401, "Unauthorized!")

    post_data.comment_count -= 1
    db.session.delete(comment_data)
    db.session.commit()

    return jsonify({"message" : "Post comment Deleted!"}),204