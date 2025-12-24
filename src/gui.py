import tkinter as tk
from tkinter import filedialog, messagebox

# این‌ها بعداً به کد رفیع و ناصری وصل می‌شوند
# from excel_reader import read_users
# from mail_sender import send_email


class EmailResanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("EmailResan - پروژه ایمیل‌رسان")
        self.root.geometry("700x600")
        self.root.resizable(False, False)

        self.excel_path = ""
        self.txt_path = ""

        # Title
        tk.Label(
            root,
            text="📧 پروژه ایمیل‌رسان",
            font=("Vazirmatn", 20, "bold")
        ).pack(pady=10)

        # Excel Button
        tk.Button(
            root,
            text="انتخاب فایل Excel",
            width=25,
            command=self.select_excel
        ).pack(pady=5)

        # TXT Button
        tk.Button(
            root,
            text="انتخاب فایل متن پیام",
            width=25,
            command=self.select_txt
        ).pack(pady=5)

        # Send Button
        tk.Button(
            root,
            text="ارسال ایمیل‌ها",
            width=25,
            bg="green",
            fg="white",
            command=self.send_emails
        ).pack(pady=20)

        # Status Label
        self.status_label = tk.Label(root, text="", fg="blue")
        self.status_label.pack()

    def select_excel(self):
        self.excel_path = filedialog.askopenfilename(
            filetypes=[("Excel Files", "*.xlsx")]
        )
        if self.excel_path:
            self.status_label.config(text="فایل Excel انتخاب شد")

    def select_txt(self):
        self.txt_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt")]
        )
        if self.txt_path:
            self.status_label.config(text="فایل متن انتخاب شد")

    def send_emails(self):
        if not self.excel_path or not self.txt_path:
            messagebox.showerror(
                "خطا",
                "لطفاً هر دو فایل را انتخاب کنید"
            )
            return

        # اینجا بعداً منطق اصلی وصل می‌شود
        messagebox.showinfo(
            "موفق",
            "ارسال ایمیل‌ها با موفقیت انجام شد (نسخه تست)"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = EmailResanGUI(root)
    root.mainloop()
