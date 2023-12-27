from flask import abort , jsonify
from src.database.model.post_comment import PostComment
from schemaObj import post_comment_all_user_response_schema
from src.utilities.helper.get_post_by_postid import get_post_by_post_id

def all_comment_by_post_id(post_id):

    post = get_post_by_post_id(post_id=post_id)

    comments = PostComment.query.filter_by(post_id = post_id).all()

    if comments is None or comments == []:
        abort(404 , "Not Any Comments Yet!")

    return post_comment_all_user_response_schema.dump(comments)