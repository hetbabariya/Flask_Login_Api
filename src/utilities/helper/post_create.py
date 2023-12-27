from flask import jsonify , abort
from src.database.crud import get_user_by_id
from src.database.model.user import User

def create_post_In_db(identity  , user_post , caption , db , Post):
    try :
        new_post = Post(post = user_post , caption = caption , user_id = identity)
        db.session.add(new_post)
        db.session.commit()

        user = get_user_by_id(User=User , user_id=identity)
        user.post_count += 1
        db.session.commit()

        return jsonify({"message": "Post created successfully!"})
    except Exception as e :
        return jsonify({"error " : str(e)})
    


    


