def personalize_message(name, file_path = "../data/message.txt"):
    # khondan file  
    with open(file_path, "r", encoding="utf-8") as f:
        template = f.read()
    
    # tagir bedeh
    message = template.replace("{name}", name)
    return message

# test
if __name__ == "__main__":
    msg = personalize_message("علیرضا")
    print(msg)