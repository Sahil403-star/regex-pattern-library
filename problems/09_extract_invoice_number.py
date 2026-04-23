import re

pattern = r"(Invoice\s*No[:\-\s]*)([A-Z0-9\-]+)"

def extract_invoice(text):
    match = re.search(pattern, text, re.IGNORECASE)
    return match.group(2) if match else None


samples = [
    "Invoice No: INV-12345",
    "InvoiceNo INV999",
    "No invoice here"
]

for s in samples:
    print(extract_invoice(s))