from flask import jsonify , abort
from src.utilities.helper.User.crud import get_user_by_id
from src.utilities.helper.post.get_post_by_postid import get_post_by_post_id
from src.database.model.user import User

def post_like_by_user(db , PostLike , post_id , current_user_id):
    try :
        user = get_user_by_id(user_id=current_user_id)
        
        post = get_post_by_post_id(post_id=post_id)

        # check like already exist 
        existing_like = PostLike.query.filter_by(post_id=post_id, user_id=current_user_id).first()
        if existing_like:
            return jsonify({"message": "User already liked the post"}), 400

        post_like = PostLike(post_id = post_id , user_id = current_user_id)
        db.session.add(post_like)
        db.session.commit()

        post.like_count += 1
        db.session.commit()

        return jsonify({"message" : "like add successfuly!"})

    except Exception as e :
        return jsonify({"error " : str(e)})

