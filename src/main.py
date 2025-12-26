from excel_reader import user_email
from mail_sender import send_email
from personalized_message import personalize_message

for name,email in user_email.items():
    send_email(
        to_email= email,
        subject="پیام تست پروژه ایمیل‌رسان",
        message_body = personalize_message(name)
    )

