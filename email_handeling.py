import smtplib
from email.message import EmailMessage
import os 
from dotenv import load_dotenv,find_dotenv

path=find_dotenv()
load_dotenv(path)

sender = os.getenv('sender')
receiver = os.getenv('receiver')
app_password = os.getenv('app_password')

msg = EmailMessage()


def send_email(message):

    msg["Subject"] = "Game-Killer Alert"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content(message)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, app_password)
        smtp.send_message(msg)
        print("Send")

# send_email("Hi")