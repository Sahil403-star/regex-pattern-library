import re

pattern = r"(₹|Rs|INR)"

def extract_currency(text):
    match = re.search(pattern, text)
    return match.group() if match else "None"


samples = [
    "DMART Total ₹1,299",
    "Tot al Rs 450"
]

for s in samples:
    print(extract_currency(s))
