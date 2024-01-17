from flask import jsonify , abort
from src.database.model.follower_following import FollowerFollowing

def get_follow_following_data(id):
    data = FollowerFollowing.query.filter_by(id=id).first() 

    if data is None :
        return abort({"message": "No data found"}), 404

    return data 