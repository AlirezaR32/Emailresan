def personalize_message(name, file_path: str = "../data/message.txt") -> str:
    """Read template from `file_path` and replace the {name} placeholder.

    Raises IOError if the template cannot be read.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            template = f.read()
    except Exception as e:
        raise

    message = template.replace("{name}", name)
    return message


# test
if __name__ == "__main__":
    try:
        msg = personalize_message("علیرضا")
        print(msg)
    except Exception as e:
        print(f"Error: {e}")