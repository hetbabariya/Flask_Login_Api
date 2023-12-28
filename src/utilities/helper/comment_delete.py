from flask import jsonify
from src.utilities.helper.get_comment_by_id import get_comment_by_id
from src.utilities.helper.get_post_by_postid import get_post_by_post_id

def comment_delete(comment_id , db):

    comment_data = get_comment_by_id(comment_id=comment_id)
    post_data = get_post_by_post_id(post_id=comment_data.post_id)

    post_data.comment_count -= 1
    db.session.delete(comment_data)
    db.session.commit()

    return jsonify({"message" : "Post comment Deleted!"}),204