import re

# More strict than basic pattern
# Ensures range 0–255

pattern = r"\b((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b"

tests = [
    "192.168.1.1",
    "255.255.255.255",
    "999.999.999.999"
]

for t in tests:
    print(t, "->", bool(re.fullmatch(pattern, t)))
