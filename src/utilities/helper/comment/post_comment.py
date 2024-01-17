from flask import jsonify
from src.utilities.helper.post.get_post_by_postid import get_post_by_post_id
from src.utilities.helper.User.crud import get_user_by_id
from src.database.model.user import User

def add_post_comment(db , PostComment , comment , post_id , user_id):
    try :
        post = get_post_by_post_id(post_id=post_id)

        user = get_user_by_id(user_id=user_id)

        new_comment = PostComment(comment = comment , user_id = user_id , post_id = post_id)
        db.session.add(new_comment)
        db.session.commit()

        post.comment_count += 1
        db.session.commit()

        return jsonify({"message" : "comment add Successfully!"})

    except Exception as e :
        return jsonify({"error " : str(e)})
