from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token , create_refresh_token  , set_access_cookies , unset_jwt_cookies
from flask import abort , jsonify , make_response

# login 
def login_user(User , username , password):
    try :
        user_data = User.query.filter_by(username = username).one_or_none()
        print("userdata",user_data)
        if not user_data or not check_password_hash(user_data.password , password) :
            abort(404 , 'Wrong Username and password')

        access_token = create_access_token(identity=user_data.id)

        # Create a Flask response object
        response = make_response(jsonify({"msg": "login successful"})) 

        # Set the access cookies on the response object
        set_access_cookies(response, access_token)

        return response
    except Exception as e:
        return jsonify({"error " : str(e)})

# logout
def logout_user():
    try : 
        response = jsonify({"msg": "logout successful"})
        unset_jwt_cookies(response)
        return response
    except Exception as e:
        return jsonify({"error " : str(e)})
    
