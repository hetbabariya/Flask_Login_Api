import os
import smtplib
from random import randint
from email.message import EmailMessage
from flask import jsonify , abort
from datetime import datetime , timedelta

from schemaObj import user_otp
# from src.database.crud import get_user_by_username

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

        return jsonify({"message" : "Email sent successfully"})

    except smtplib.SMTPException as e:
        print(f"Error sending email: {str(e)}")
        return {"error": f"Error sending email: {str(e)}"}
    


# get user using otp
def get_user_by_otp(User , otp):
    try :
        user_data = User.query.filter_by(OTP = otp).one_or_none()
        if user_data is None:
            return False
        
        return user_otp.jsonify(user_data)

    except Exception as e:
        return jsonify({"error " : str(e)})
    
# verify OTP
def verify_otp(user , otp):
    try:
        response = get_user_by_otp(User=user , otp=otp)

        if response == False :
            abort(404, 'OTP Not Found')
        
        user_data = response.get_json()
        current_utc_time = datetime.utcnow()
       
        user_otp_time = datetime.strptime(user_data['otp_send_at'], '%Y-%m-%dT%H:%M:%S.%f')
       
        if current_utc_time > user_otp_time + timedelta(minutes=3):
            abort(410 , "OTP is Expired")
    
        return jsonify({"message" : "Otp is verify successfully"})
    except Exception as e:
        return {"error : " : str(e)} 

    
