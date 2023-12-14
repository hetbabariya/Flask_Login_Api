import os
import smtplib
from random import randint
from email.message import EmailMessage
from flask import jsonify


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
