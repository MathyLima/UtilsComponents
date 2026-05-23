import os
import smtplib

from dataclasses import dataclass

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .models import MailPayload

from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")



class Poster:

    def __init__(self):
        pass

    def post(self, payload: MailPayload):

        message = MIMEMultipart()

        message["From"] = EMAIL_ADDRESS
        message["To"] = payload.receiver
        message["Subject"] = payload.subject

        message.attach(
            MIMEText(payload.body, "plain")
        )

        try:

            with smtplib.SMTP(
                "smtp.gmail.com",
                587
            ) as server:

                server.starttls()

                server.login(
                    EMAIL_ADDRESS,
                    EMAIL_PASSWORD
                )

                server.send_message(message)

                print("Email enviado com sucesso!")

        except Exception as e:

            print(f"Erro ao enviar email: {e}")