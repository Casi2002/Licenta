import smtplib
import random
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to generate a random number
def generate_random_number():
    return random.randint(1000, 9999)  # Change the range as needed

# Function to send email
def send_email(sender_email, sender_password, recipient_email, number):
    # Email content
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = 'Random Number'

    body = f'Here is your random number: {number}'
    message.attach(MIMEText(body, 'plain'))

    # Connect to Yahoo Mail SMTP server with SSL/TLS encryption
    server = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
    server.login(sender_email, sender_password)

    # Send email
    server.sendmail(sender_email, recipient_email, message.as_string())
    print("Email sent successfully!")

    # Quit SMTP server
    server.quit()

if __name__ == "__main__":
    # Recipient email address
    recipient_email = "nicolae.fara@student.upt.ro"  # Replace with recipient's email address

    # Generate random number
    random_number = generate_random_number()

    # Sender email credentials (replace with your Yahoo Mail email credentials)
    sender_email = "test_licenta21@yahoo.com"  # Replace with your Yahoo Mail email address
    sender_password = "Casi2103?!"  # Replace with your Yahoo Mail password

    # Send email
    send_email(sender_email, sender_password, recipient_email, random_number)
