# EmailResan — مستندات پروژه (فارسی)

EmailResan یک ابزار ساده و کاربردی برای ارسال ایمیل‌های شخصی‌سازی‌شده از روی یک فایل Excel و یک قالب متن است. این مستند راهنمای کامل نصب، پیکربندی، اجرا و ساختار پروژه را به‌صورت حرفه‌ای و قدم‌به‌قدم ارائه می‌دهد.

---

فایل‌ها و ساختار پروژه

- readme.md — این مستند
- requirements.txt — وابستگی‌های پروژه (فقط کتابخانه‌های ضروری مثل openpyxl)
- data/
  - message.txt — قالب پیام (UTF-8)
  - test.xlsx — (نمونه) فایل Excel با ستون‌های نام و ایمیل
- src/
  - main.py — اسکریپت نمونه برای ارسال ایمیل به همهٔ گیرنده‌ها
  - excel_reader.py — خواندن لیست نام‌ها و ایمیل‌ها از فایل Excel
  - personalized_message.py — ساخت پیام شخصی‌سازی‌شده با جایگزینی `{name}`
  - mail_sender.py — ارسال ایمیل از طریق SMTP
  - gui.py — رابط گرافیکی ساده برای انتخاب فایل‌ها (نسخهٔ آزمایشی)

---

پیش‌نیازها

- Python 3.8 یا بالاتر
- نصب بسته‌های مورد نیاز (در نسخهٔ فعلی فرض شده فقط کتابخانهٔ ضروری نصب شود):

  1. ایجاد و فعال‌سازی محیط مجازی
     - Linux / macOS:
       ```bash
       python -m venv venv
       source venv/bin/activate
       ```
     - Windows (PowerShell):
       ```powershell
       python -m venv venv
       .\\venv\\Scripts\\Activate.ps1
       ```

  2. نصب بسته‌ها
     ```bash
     pip install -r requirements.txt
     ```

تذکر: در این مخزن فرض شده requirements.txt تنها شامل بسته‌های ضروری (مثلاً openpyxl) است. اگر می‌خواهید از فایل‌های .env یا بسته‌های اضافی استفاده کنید، آن‌ها را به requirements اضافه کنید.

---

پیکربندی (SMTP و Credential)

برای ارسال ایمیل لازم است اطلاعات حساب ایمیل در دسترس برنامه قرار گیرد. دو روش متداول:

روش 1 — فایل پیکربندی محلی (ساده‌ترین، مناسب توسعه محلی)

- یک فایل جدید بسازید: `src/config.py`
- محتوای نمونه:

```python
# src/config.py (نمونه — هرگز این فایل را در مخزن عمومی قرار ندهید)
EMAIL_ADDRESS = "your-email@example.com"
EMAIL_PASSWORD = "your-app-password-or-password"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
```

نکات امنیتی:
- برای حساب‌های Gmail فعال‌سازی 2FA و استفاده از App Password توصیه می‌شود.
- هرگز کلیدها یا رمزهای واقعی را در مخزن عمومی قرار ندهید.

روش 2 — متغیرهای محیطی (پیشنهاد برای تولید)

- تنظیم متغیرها در سیستم یا CI:
  - Linux/macOS:
    ```bash
    export EMAIL_ADDRESS=you@example.com
    export EMAIL_PASSWORD=your_secret
    export SMTP_SERVER=smtp.gmail.com
    export SMTP_PORT=587
    ```
  - Windows (PowerShell):
    ```powershell
    $env:EMAIL_ADDRESS = 'you@example.com'
    $env:EMAIL_PASSWORD = 'your_secret'
    $env:SMTP_SERVER = 'smtp.gmail.com'
    $env:SMTP_PORT = '587'
    ```

برای استفاده از .env می‌توانید python-dotenv نصب کرده و در کد آن را بخوانید (در نسخه فعلی کد مستقیم از src/config.py استفاده می‌کند).

---

فرمت فایل Excel

- فرمت پیشنهادی:
  - ستون A: نام
  - ستون B: ایمیل
  - ردیف 1: هدر (خواندن از ردیف 2 شروع می‌شود)

مثال:

| A (Name) | B (Email) |
|----------|-----------|
| name     | email     |
| علی      | ali@example.com |
| سارا     | sara@example.com |

نکات:
- ردیف‌هایی که نام یا ایمیل ندارند نادیده گرفته خواهند شد.
- در نسخه‌های بعدی پیشنهاد می‌شود اعتبارسنجی ایمیل و جلوگیری از ارسال تکراری اضافه شود.

---

قالب پیام

- فایل قالب در `data/message.txt` قرار دارد و باید با UTF-8 ذخیره شود.
- برای درج نام از `{name}` استفاده کنید.

نمونه:

```
سلام {name} عزیز

این یک ایمیل تستی برای پروژه ایمیل‌رسان است.

موفق باشید
```

---

نحوهٔ اجرا

1) اجرای در خط فرمان (بدون GUI)

- به پوشهٔ `src` بروید:
  ```bash
  cd src
  ```
- مطمئن شوید `src/config.py` یا متغیرهای محیطی تنظیم شده و فایل‌های `data/test.xlsx` و `data/message.txt` در مسیر درست قرار دارند.
- اجرا:
  ```bash
  python main.py
  ```

2) اجرای رابط گرافیکی (GUI)

- به پوشهٔ `src` بروید و اجرا کنید:
  ```bash
  python gui.py
  ```
- در نسخهٔ فعلی GUI فقط امکان انتخاب فایل‌ها و نمایش پیام موفقیت (نسخهٔ تست) وجود دارد. برای فعال‌سازی ارسال از طریق GUI لازم است متد `send_emails` در `gui.py` به منطق خواندن Excel و ارسال واقعی متصل شود.

---

مسائل فنی و پیشنهادات بهبود

- مسیرهای مطلق را حذف و از مسیرهای نسبی یا پارامتر ورودی استفاده کنید.
- `personalized_message.py` نباید مسیر مطلق داشته باشد؛ مسیر پیش‌فرض بهتر است نسبی به دایرکتوری پروژه باشد.
- `mail_sender.py` باید در بلوک try/except/finally اتصال به سرور SMTP را امن ببندد و از `ssl.create_default_context()` هنگام starttls استفاده کند.
- از `logging` برای ثبت نتایج ارسال (موفق/ناموفق) استفاده شود.
- برای تولید، از متغیرهای محیطی یا سرویس‌های مدیریت اسرار (Secret Manager) استفاده کنید.
- اضافه کردن تست واحد برای هر ماژول و نمونه فایل Excel در پوشهٔ `data/samples` مفید است.

---

رفع خطاهای رایج

- AuthenticationError در SMTP:
  - بررسی کنید `EMAIL_ADDRESS` و `EMAIL_PASSWORD` درست هستند و اگر از Gmail استفاده می‌کنید از App Password بهره بگیرید.
- خطا در خواندن Excel:
  - مطمئن شوید openpyxl نصب است: `pip install openpyxl` و مسیر فایل درست است.
- مشکلات encoding برای متن فارسی:
  - فایل `message.txt` را با UTF-8 ذخیره کنید.

---

مشارکت و لایسنس

- اگر مایل به مشارکت هستید، لطفاً یک issue باز کنید یا pull request ارسال نمایید.
- لایسنس پیشنهادی: MIT — در صورت تمایل می‌توانم فایل LICENSE را اضافه کنم.

---

توضیح نهایی

این README برای نسخه‌ای نوشته شده که "فقط کتابخانه‌های ضروری" در requirements.txt ذکر شده‌اند. چنانچه خواستید من README را طوری تغییر دهم که نصب python-dotenv، validators یا بسته‌های دیگر را نیز در بر گیرد، بگویید تا نسخهٔ دیگری ایجاد کنم.
