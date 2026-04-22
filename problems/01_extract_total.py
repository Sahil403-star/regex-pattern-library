import re

# Initially I tried:
# pattern = r"\d+"
# but it was matching wrong things like 12,34

# Updated version (handles both formatted + unformatted)

pattern = r"(Total|T0tal|Tot al|Amount Payable)\s*[:\-]?\s*(₹|Rs)?\s*(\d{1,3}(,\d{3})+|\d+)"

cases = [
    "Total 100",
    "T0tal ₹1,299",
    "Tot al Rs 450",
    "Amount Payable 1200",
    "Total ₹12,34"  # invalid case
]

for c in cases:
    print("Checking:", c)
    match = re.search(pattern, c)
    
    if match:
        value = match.group(3).replace(",", "")
        print("-> Extracted:", value)
    else:
        print("-> No match")
