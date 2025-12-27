import tkinter as tk
from tkinter import filedialog, messagebox
from main import main

# from excel_reader import read_users
# from mail_sender import send_email


class EmailResanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("EmailResan - پروژه ایمیل‌رسان")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        # Modern color scheme
        bg_color = "#f5f6fa"
        accent_color = "#4078c0"
        button_color = "#00b894"
        button_fg = "#fff"
        frame_color = "#dfe6e9"

        self.root.configure(bg=bg_color)

        self.excel_path = ""
        self.txt_path = ""

        # Main frame for padding and rounded corners
        main_frame = tk.Frame(root, bg=frame_color, bd=2, relief="groove")
        main_frame.place(relx=0.5, rely=0.5, anchor="center", width=420, height=380)

        # Title
        tk.Label(
            main_frame,
            text="📧 پروژه ایمیل‌رسان",
            font=("Vazirmatn", 22, "bold"),
            bg=frame_color,
            fg=accent_color
        ).pack(pady=(20, 10))

        # Excel Button
        self.excel_btn = tk.Button(
            main_frame,
            text="انتخاب فایل Excel",
            font=("Vazirmatn", 13),
            width=22,
            bg=button_color,
            fg=button_fg,
            activebackground=accent_color,
            activeforeground=button_fg,
            relief="flat",
            cursor="hand2",
            command=self.select_excel
        )
        self.excel_btn.pack(pady=8)

        # TXT Button
        self.txt_btn = tk.Button(
            main_frame,
            text="انتخاب فایل متن پیام",
            font=("Vazirmatn", 13),
            width=22,
            bg=button_color,
            fg=button_fg,
            activebackground=accent_color,
            activeforeground=button_fg,
            relief="flat",
            cursor="hand2",
            command=self.select_txt
        )
        self.txt_btn.pack(pady=8)

        # Send Button
        self.send_btn = tk.Button(
            main_frame,
            text="ارسال ایمیل‌ها",
            font=("Vazirmatn", 14, "bold"),
            width=22,
            bg=accent_color,
            fg=button_fg,
            activebackground=button_color,
            activeforeground=button_fg,
            relief="flat",
            cursor="hand2",
            command=self.send_emails
        )
        self.send_btn.pack(pady=18)

        # Status Label
        self.status_label = tk.Label(main_frame, text="", fg=accent_color, bg=frame_color, font=("Vazirmatn", 12))
        self.status_label.pack(pady=(10, 0))

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

        main(self.excel_path , self.)
        messagebox.showinfo(
            "موفق",
            "ارسال ایمیل‌ها با موفقیت انجام شد (نسخه تست)"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = EmailResanGUI(root)
    root.mainloop()
