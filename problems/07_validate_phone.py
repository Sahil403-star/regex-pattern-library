import re

# Validates Indian phone numbers (with +91, 0, or plain)
pattern = r"^(?:\+91[\-\s]?|0)?[6-9]\d{9}$"

def validate_phone(phone):
    return bool(re.match(pattern, phone))


samples = [
    "+91 9876543210",
    "09876543210",
    "9876543210",
    "1234567890"
]

for s in samples:
    print(s, "=>", validate_phone(s))