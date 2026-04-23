import re

# Found this issue during testing:
# Sometimes total comes on next line

text = """Total
₹1,299"""

pattern = r"Total\s*\n\s*(₹|Rs)?\s*(\d{1,3}(,\d{3})+|\d+)"

match = re.search(pattern, text)

if match:
    print("Extracted:", match.group(2).replace(",", ""))
