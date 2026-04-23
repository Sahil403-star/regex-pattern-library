import re

pattern = r"^(https?:\/\/)?(www\.)?[a-zA-Z0-9\-]+\.[a-zA-Z]{2,}(\/\S*)?$"

def validate_url(url):
    return bool(re.match(pattern, url))


samples = [
    "https://www.google.com",
    "http://example.org",
    "www.github.com",
    "invalid_url"
]

for s in samples:
    print(s, "=>", validate_url(s))