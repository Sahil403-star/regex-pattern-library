import re

pattern = r"([A-Za-z\s]+).*?(₹|Rs)?\s*([\d,\. ]+)"

def parse_receipt(text):
    match = re.search(pattern, text)
    if match:
        store = match.group(1).strip()
        amount = match.group(3).replace(" ", "")
        return {"store": store, "amount": amount}
    return None


samples = [
    "DMART Total ₹1,299",
    "Big Bazaar Tot al Rs 450",
    "Amount Payable 1200"
]

for s in samples:
    print(parse_receipt(s))