import os
from dotenv import load_dotenv

from flask_jwt_extended import JWTManager
from datetime import timedelta
import secrets

load_dotenv()

jwt = JWTManager()

def initialize_jwt(app):
    secret_key = secrets.token_hex(32)
    app.config['JWT_SECRET_KEY'] = secret_key
    app.config['JWT_TOKEN_LOCATION'] = ["headers"]
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES')))
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=int(os.getenv('JWT_REFRESH_TOKEN_EXPIRES')))
    jwt.init_app(app)
 