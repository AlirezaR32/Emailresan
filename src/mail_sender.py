import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Try to import a `config.py` file, otherwise fall back to environment variables.
try:
    from config import (
        EMAIL_ADDRESS,
        EMAIL_PASSWORD,
        SMTP_SERVER,
        SMTP_PORT,
    )
except Exception:
    EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
    EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
    SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))


def send_email(to_email, subject, message_body):
    try:
        # sakht sakhtar email ba MIMEMultipart
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(message_body, "plain", "utf-8"))

        # choose secure connection type depending on port
        if SMTP_PORT == 465:
            server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        else:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30)
            server.ehlo()
            server.starttls()
            server.ehlo()

        if EMAIL_ADDRESS and EMAIL_PASSWORD:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        server.send_message(msg)
        server.quit()
        print("email sent successfully")

        return True
    # error 
    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")
        return False

# test
if __name__ == "__main__":
    test_message = "سلام ناصری عزیز\nاین ایمیل تست است."
    send_email("alireza.13rafe@gmail.com", "Test Email", test_message)
