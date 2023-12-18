from flask import Flask

# from src.database.model import  db
from src.database.ext import  db
from config import Config
from view import register_user_db, read_user, sent_user_otp, verify_user_otp, login, logout
from src.auth.config import jwt , initialize_jwt


app = Flask(__name__)


# initalize with app
initialize_jwt(app)

# register blueprint    
app.register_blueprint(register_user_db)
app.register_blueprint(read_user)
app.register_blueprint(sent_user_otp)
app.register_blueprint(verify_user_otp)
app.register_blueprint(login)
app.register_blueprint(logout)


#  config with database config
app.config.from_object(Config)

# initalize with app
db.init_app(app)

# initalize with app
jwt.init_app(app)

# app.app_context().push()

# # create db model
# with app.app_context():
#     db.create_all()



if __name__ == "__main__":
    app.run(debug=True)