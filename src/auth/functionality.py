# from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token , unset_jwt_cookies ,create_refresh_token , decode_token
from flask import abort , jsonify , make_response , g
from src.database.crud import get_user_by_username
from src.utilities.functionality import verify_password


# login 
def login_user(User , username , password):
    user_data = get_user_by_username(User = User , username=username)

    if not user_data or not verify_password(plain_password= password, hashed_password=user_data.password) :
        abort(404 , 'Wrong Username and password')

    if user_data.is_delete == True:
        abort(404,"Data Not Found")

    access_token =  create_access_token(identity=user_data.username)
    referesh_token = create_refresh_token(identity=user_data.username)

    # headers = request.headers
    # bearer = headers.get('Authorization')    # Bearer YourTokenHere
    # token = bearer.split()[1]
    g.user = decode_token(access_token)

    return jsonify(access_token = access_token , refersh_token = referesh_token)

# logout
def logout_user():
    try : 
        response = jsonify({"msg": "logout successful"})
        unset_jwt_cookies(response)
        return response
    except Exception as e:
        return jsonify({"error " : str(e)})
    
