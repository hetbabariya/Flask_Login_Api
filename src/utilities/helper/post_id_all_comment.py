from flask import abort , jsonify
from src.database.model.post_comment import PostComment
from src.database.model.comment_reply import PostCommentReply
from schemaObj import post_comment_all_user_response_schema , post_comment_reply_all_user_response_schema
from src.utilities.helper.get_post_by_postid import get_post_by_post_id
from src.utilities.helper.get_comment_by_id import get_comment_by_id

def all_comment_by_post_id(post_id):

    post = get_post_by_post_id(post_id=post_id)

    comments = PostComment.query.filter_by(post_id = post_id).all()

    if comments is None or comments == []:
        abort(404 , "Not Any Comments Yet!")

    return post_comment_all_user_response_schema.dump(comments)

def all_comment_reply_by_comment_id(comment_id):

    comment = get_comment_by_id(comment_id=comment_id)

    comments = PostCommentReply.query.filter_by(comment_id=comment_id).all()

    if comments is None or comments == []:
        abort(404 , "Not Any Comments Yet!")

    return post_comment_reply_all_user_response_schema.dump(comments)