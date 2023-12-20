from flask_jwt_extended import JWTManager
from datetime import timedelta
import secrets

jwt = JWTManager()

def initialize_jwt(app):
    secret_key = secrets.token_hex(32)
    app.config['JWT_SECRET_KEY'] = secret_key
    app.config['JWT_TOKEN_LOCATION'] = ["headers"]
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=3)
    jwt.init_app(app)
