import re

def clean_ocr(text):
    # Fix common OCR issues
    text = text.replace("0", "o")
    text = text.replace("T0tal", "Total")

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


samples = [
    "DMART T0tal ₹1,2 9 9",
    "Tot al Rs 450",
    "Amount   Payable   1200"
]

for s in samples:
    print(clean_ocr(s))