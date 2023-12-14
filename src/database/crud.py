from flask import abort , jsonify ,request
from marshmallow import ValidationError

from schemaObj import user_response ,user_request
from src.utilities.functionality import generate_OTP , send_otp_email

# create user
def create_user(db , User):
    try:
        user_data = user_request.load(request.json)
        new_user = User(username = user_data['username'] ,email =  user_data['email'] , password = user_data['password'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message" : "data created"}),200
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400


# get user by username
def get_user_by_username(User , username):
    try :
        user_data = User.query.filter_by(username = username).one_or_none()
        if user_data is None : 
            abort(404 , {"message": "Data Not Found"})
        return user_response.jsonify(user_data)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

# get user by email
def get_user_by_email(User , email):
    try :
        user_data = User.query.filter_by(email = email).one_or_none()
        if user_data is None : 
            abort(404 , {"message": "Data Not Found"})
        return user_response.jsonify(user_data)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400
    
#store otp
def store_otp(db , User):
    try:
        # user_data = request.json
        user_data = request.args.get("email")
        print("email : ",user_data)
        # user = get_user_by_email(User,user_data['email'] )
        user = get_user_by_email(User,user_data )
        
        if not user :
             abort(404 , {"message": "email Not Found"})
        
        otp = generate_OTP()
        send_otp_email(to_email=user_data , otp=otp)

        user_data_In_db = User.query.filter_by(email = user_data).one_or_none()
        user_data_In_db.OTP = otp
        # db.session.add(user_otp)
        db.session.commit()
        return jsonify({"message" : "OTP sent succesfully"}),200
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400



    