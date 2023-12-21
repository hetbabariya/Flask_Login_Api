from flask import abort , jsonify ,request
from passlib.context import CryptContext

# from src.database.model import User
from schemaObj import user_request

# genrate hash pwd
pwd_context = CryptContext(schemes=['bcrypt'] , deprecated = "auto")

def generate_hash_password(plain_password):
    return pwd_context.hash(plain_password)

# create user
def create_user(db , User):
    try:
        user_data = user_request.load(request.json)
        hashed_password = generate_hash_password(user_data['password'])
        new_user = User(username = user_data['username'] ,email =  user_data['email'] , password = hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message" : "data created"}),201
    except Exception as e:
        return jsonify({"error " : str(e)})


# get user by username
def get_user_by_username(User , username):
    user_data = User.query.filter_by(username = username).first()

    if user_data is None : 
        abort(404)

    return user_data

# get by id
def get_user_by_id(User , user_id):
    user_data = User.query.filter_by(user_id = user_id).first()

    if user_data is None : 
        abort(404)

    return user_data

# get user by email
def get_user_by_email(User , email):
    try :
        user_data = User.query.filter_by(email = email).one_or_none()
        if user_data is None : 
            abort(404 , {"message": "Data Not Found"})
        return user_data
    except Exception as e:
        return jsonify({"error " : str(e)})
    