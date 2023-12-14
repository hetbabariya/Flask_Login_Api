from flask import Flask

from src.database.model import  User , db
from config import Config
from view import register_user_db , read_user , sent_otp

app = Flask(__name__)

# register blueprint
app.register_blueprint(register_user_db)
app.register_blueprint(read_user)
app.register_blueprint(sent_otp)


#  config with database config
app.config.from_object(Config)

# initalize with app
db.init_app(app)

# create db model
with app.app_context():
    db.create_all()





if __name__ == "__main__":
    app.run(debug=True)