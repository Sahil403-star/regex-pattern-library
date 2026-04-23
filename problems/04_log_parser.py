import re

# Extracting IPs from logs

pattern = r"\b\d{1,3}(\.\d{1,3}){3}\b"

logs = [
    "User login from 192.168.1.1",
    "Invalid IP 999.999.999.999"
]

for log in logs:
    print(log, "->", re.findall(pattern, log))
