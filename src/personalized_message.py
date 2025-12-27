def personalize_message(name, file_path = "../data/message.txt"):
    # فایل رو بخون
    with open(file_path, "r", encoding="utf-8") as f:
        template = f.read()
    
    # جایگزین کن
    message = template.replace("{name}", name)
    return message

# تست
if __name__ == "__main__":
    msg = personalize_message("علیرضا")
    print(msg)