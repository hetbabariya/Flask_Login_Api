from src.database.crud import get_user_by_id
from src.database.model.follower_following import FollowerFollowing
from src.database.model.follow_request import FollowRequest


def store_in_follower_table(db , follow_by_id , current_user_id):

    user_follower_data = get_user_by_id(user_id=follow_by_id)
    user_following_data = get_user_by_id(user_id=current_user_id)

    folloW_data = FollowerFollowing(user_id = follow_by_id , followed_by = current_user_id)
        
    user_following_data.following_count += 1
    user_follower_data.follower_count += 1

    follow_request_data = FollowRequest.query.filter_by(user_id = follow_by_id , request_by_user_id = current_user_id).first()

    db.session.add(folloW_data)
    db.session.delete(follow_request_data)
    db.session.commit()
