import re

pattern = r"^[A-Za-z\s']+"

def extract_store(text):
    match = re.search(pattern, text)
    return match.group().strip() if match else None


samples = [
    "DMART Total ₹1,299",
    "Big Bazaar Tot al Rs 450"
]

for s in samples:
    print(extract_store(s))
