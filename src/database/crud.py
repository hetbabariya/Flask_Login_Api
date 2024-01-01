from flask import abort , jsonify ,request
from passlib.context import CryptContext
from schemaObj import user_request, user_registration_response_schema , all_user_response_schema
from src.database.model.user import User

# genrate hash pwd
pwd_context = CryptContext(schemes=['bcrypt'] , deprecated = "auto")

def generate_hash_password(plain_password):
    return pwd_context.hash(plain_password)

# create user
def create_user(db , User):
    try:
        user_data = user_request.load(request.json)
        hashed_password = generate_hash_password(user_data['password'])
        new_user = User(username = user_data['username'] ,email =  user_data['email'] , password = hashed_password , is_public = user_data['is_public'])
        db.session.add(new_user)
        db.session.commit()
        return user_registration_response_schema.dump({"message" : "data created" , "data" : [new_user]})
    except Exception as e:
        return jsonify({"error " : str(e)})
    





# get all user
def get_all_user(User):
    user_data = User.query.all()
    if not user_data : 
        abort(404)
    print(user_data)
    return all_user_response_schema.dump({"data" : user_data})

# get user by username
def get_user_by_username(User , username):
    user_data = User.query.filter_by(username = username , is_delete = False).first()
    if user_data is None : 
        abort(404)
    return user_data

# get by id
def get_user_by_id(user_id):
    user_data = User.query.filter_by(id = user_id , is_delete = False).first()

    if user_data is None : 
        abort(404)

    return user_data

# get user by email
def get_user_by_email(User , email):
    user_data = User.query.filter_by(email = email , is_delete = False).one_or_none()

    if user_data is None : 
        abort(404 , {"message": "Data Not Found"})
    return user_data
    