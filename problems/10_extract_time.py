import re

pattern = r"\b([01]?\d|2[0-3]):[0-5]\d\b"

def extract_time(text):
    return re.findall(pattern, text)


samples = [
    "Time: 14:30",
    "Logged at 09:15 and 18:45",
    "No time here"
]

for s in samples:
    print(extract_time(s))