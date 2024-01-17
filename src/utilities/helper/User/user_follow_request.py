from flask import abort , jsonify
from src.utilities.helper.User.crud import get_user_by_id
from src.database.model.follower_following import FollowerFollowing
from src.database.model.follow_request import FollowRequest

def check_already_follow(current_user_id , follow_by_id) :

    if current_user_id == str(follow_by_id) :
        return abort(400,"you Not Follow yourself!")
    
    if FollowerFollowing.query.filter_by(user_id = follow_by_id , followed_by = current_user_id).first() :
        return abort(400,"you already follow")

def user_follow(db , follow_by_id , current_user_id):
    user_follower_data = get_user_by_id(user_id=follow_by_id)
    user_following_data = get_user_by_id(user_id=current_user_id)

    check_already_follow(current_user_id=current_user_id , follow_by_id=follow_by_id)

    # for public account
    if user_follower_data.is_public :

        folloW_data = FollowerFollowing(user_id = follow_by_id , followed_by = current_user_id)
        
        user_following_data.following_count += 1
        user_follower_data.follower_count += 1
        
        db.session.add(folloW_data)
        db.session.commit()

        response = jsonify({"message" : "user add successfuly"}),200
    # for private account
    else : 

        follow_request_data = FollowRequest(user_id = follow_by_id , request_by_user_id = current_user_id)
        
        db.session.add(follow_request_data)
        db.session.commit()

        response = jsonify({"message" : "send request successfuly"}),200

    return response


    