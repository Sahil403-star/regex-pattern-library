import re

# Keeping it simple for now
# Might fail for edge cases like invalid dates

pattern = r"\b\d{2}[-/]\d{2}[-/]\d{2,4}\b"

samples = [
    "12-03-26",
    "12/03/2026",
    "Date: 99/99/9999"  # should ideally be invalid
]

for s in samples:
    print(s, "->", re.findall(pattern, s))
