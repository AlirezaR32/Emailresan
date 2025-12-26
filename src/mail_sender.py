import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import (
    EMAIL_ADDRESS,
    EMAIL_PASSWORD,
    SMTP_SERVER,
    SMTP_PORT
)


def send_email(to_email, subject, message_body):
    try:
        # sakht sakhtar email ba MIMEMultipart
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(message_body, "plain", "utf8"))

        # config server 
        server = smtplib.SMTP(SMTP_SERVER , SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("email sended successfully")

        return(True)
    # error 
    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")
        return False

# test
if __name__ == "__main__":
    test_message = "سلام ناصری عزیز\nاین ایمیل تست است."
    send_email("alireza.13rafe@gmail.com", "Test Email", test_message)
