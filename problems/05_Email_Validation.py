import re

pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$"

def validate_email(email):
    return bool(re.match(pattern, email))

print(validate_email("test@gmail.com"))
