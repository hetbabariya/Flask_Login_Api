import os
import smtplib
from random import randint
from email.message import EmailMessage
from flask import jsonify , abort , request
from datetime import datetime  , timedelta
import hashlib

from src.database.crud import get_user_by_email , generate_hash_password , get_user_by_username
from src.database.model import db
from src.database.crud import pwd_context



# genrate random Otp
def generate_OTP():
    return randint(100000 , 999999)

# sent otp
def send_otp_email(to_email, otp):
    email_user = os.getenv("email_user")
    email_password = os.getenv("email_password")
    subject = "Your OTP"
    body = f"Your Verification OTP is : {otp}"

    try:
        # Create an EmailMessage object
        message = EmailMessage()
        message.set_content(body)
        message["Subject"] = subject
        message["From"] = email_user
        message["To"] = to_email

        # Establish the SMTP connection
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email_user, email_password)

            # Send the email message
            server.send_message(message)

        # return jsonify({"message" : "Email sent successfully"})

    except smtplib.SMTPException as e:
        return {"error": f"Error sending email: {str(e)}"}
    

# verify password
def verify_password(plain_password , hashed_password):
    return pwd_context.verify(plain_password , hashed_password)

# genrate hash otp
def generate_hash_otp(otp):
    hashed_otp = hashlib.sha256(str(otp).encode()).hexdigest()
    return hashed_otp

# verify hash otp
def verify_hash_otp(input_otp, hashed_otp):
    input_hashed_otp = generate_hash_otp(input_otp)
    return input_hashed_otp == hashed_otp


# send and store otp
def store_otp(db , User):
    try:
        user_request_data = request.get_json()
        user = get_user_by_email(User,user_request_data['email'] )

        if not user_request_data :
             abort(404 , {"message": "email Not Found"})
        
        otp = generate_OTP()

        send_otp_email(to_email=user.email , otp=otp)

        Hashed_otp = generate_hash_otp(otp)
        user.OTP = Hashed_otp
        user.otp_send_at = datetime.now()
        db.session.commit()

        return jsonify({"message" : "OTP sent successfuly"}),200

    except Exception as e:
        return jsonify({"error " : str(e)})
    
# verify OTP
def verify_otp(User , email , otp ):
    try:

        user_data = get_user_by_email(User = User,email = email )

        if user_data is None:
            abort(404, 'OTP Not Found')

        current_utc_time = datetime.now()

        
        if current_utc_time > user_data.otp_send_at + timedelta(minutes=3):
            abort(410, "OTP is Expired")

        if not(verify_hash_otp(otp , user_data.OTP)):
            abort(401, "OTP is Not Valid")

        user_data.is_valid = True
        db.session.commit()
        return jsonify({"message": "Otp is verified successfully"})
    
    except Exception as e:
        return jsonify({"error": str(e)}) 
    

# forget password 
def forget_password(new_pwd , email , otp , User):
    try:
        
        user_data = get_user_by_email(User,email )
        
        current_utc_time = datetime.now()

        if current_utc_time > user_data.otp_send_at + timedelta(minutes=3):
            abort(410, "OTP is Expired")

        if not(verify_hash_otp(otp , user_data.OTP))  :
            abort(401, "OTP is Not Valid")
        
        # update new pwd
        hashed_password = generate_hash_password(new_pwd)
        user_data.password = hashed_password
        db.session.commit()

        return jsonify({"message" : "New password set successfully"}),200

    except Exception as e:
        return jsonify({"error " : str(e)})
    
# change pwd
def change_password(old_pwd , new_pwd , current_user , User):
    try :
        user_data = get_user_by_username(User=User , username=current_user)

        if not verify_password(old_pwd , user_data.password) :
            abort(404 , "Wrong old Password")

        hashed_password = generate_hash_password(new_pwd)
        user_data.password = hashed_password
        db.session.commit()

        return jsonify({"message":"Password changed Successfully"}),200
    except Exception as e:
        return jsonify({"error " : str(e)})
    

# delete user
def delete_user(current_user , User):

    user_data = get_user_by_username(User , username=current_user)
    user_data.is_delete = True
    db.session.commit()
    return jsonify({"message" : f"{current_user} has been deleted "}),204