import re

pattern = r"^(https?://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}"

def validate_url(url):
    return bool(re.match(pattern, url))

print(validate_url("https://google.com"))
