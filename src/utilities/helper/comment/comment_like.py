from flask import abort , jsonify
from src.utilities.helper.comment.get_comment_by_id import get_comment_by_id
from src.database.model.post_comment_like import PostCommentLike
from schemaObj import post_comment_like_response_schema

def post_comment_like(comment_id , db , user_id) :

    comment_data = get_comment_by_id(comment_id=comment_id)

    existing_like = PostCommentLike.query.filter_by(comment_id = comment_id , user_id=user_id).first()
    if existing_like:
            return jsonify({"message": "User already liked the Comment"}), 400

    post_comment_like = PostCommentLike(post_id = comment_data.post_id , comment_id = comment_id , user_id = user_id , reply_id = None)

    comment_data.comment_like_count += 1

    db.session.add(post_comment_like)
    db.session.commit()



    return post_comment_like_response_schema.dump({"message": "comment like successfuly", "data": [post_comment_like]})
    