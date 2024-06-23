import os
import random
import time
from twilio.rest import Client
from ch import verification_code

def main_SMS():
    global verification_code

    # Retrieve Twilio credentials and phone numbers from environment variables
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')
    target_phone_number = os.getenv('TARGET_PHONE_NUMBER')

    if not account_sid or not auth_token or not twilio_phone_number or not target_phone_number:
        raise ValueError("Twilio credentials and phone numbers must be set in environment variables")

    # Initialize the Twilio client
    client = Client(account_sid, auth_token)


    print(f"Generated verification code: {verification_code}")

    # Send the verification code via SMS
    message = client.messages.create(
        body=f"Your verification code is {verification_code}. It will expire in 30 seconds.",
        from_=twilio_phone_number,
        to=target_phone_number
    )
    print(f"Sent message: {message.sid}")

# Wait for 30 seconds to expire the code
#time.sleep(30)

# Expire the code (in this example, we'll just set it to None)
#verification_code = None
#print("Verification code has expired.")
