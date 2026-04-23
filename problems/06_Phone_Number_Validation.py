import re

pattern = r"^[6-9]\d{9}$"

def validate_phone(phone):
    return bool(re.match(pattern, phone))

print(validate_phone("9876543210"))
