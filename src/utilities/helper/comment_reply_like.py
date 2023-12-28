from flask import abort , jsonify
from src.utilities.helper.get_comment_reply_by_id import get_comment_reply_by_id
from src.database.model.post_comment_like import PostCommentLike
from schemaObj import post_comment_like_response_schema

def post_comment_reply_like(reply_id , db , user_id) :

    comment_reply_data =get_comment_reply_by_id(reply_id=reply_id)

    existing_like = PostCommentLike.query.filter_by(reply_id = reply_id , user_id=user_id).first()
    if existing_like:
            return jsonify({"message": "User already liked the Comment"}), 400

    post_comment_reply_like = PostCommentLike(post_id = comment_reply_data.post_id , comment_id = comment_reply_data.comment_id , user_id = user_id , reply_id = reply_id)
    
    comment_reply_data.reply_like_count += 1
    db.session.add(post_comment_reply_like)
    db.session.commit()

    return post_comment_like_response_schema.dump({"message": "comment like successfuly", "data": [post_comment_reply_like] })
    