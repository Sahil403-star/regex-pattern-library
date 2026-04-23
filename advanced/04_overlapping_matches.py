import re

# Learned that regex skips overlaps by default

text = "aaaa"

pattern = r"(?=(aa))"

print(re.findall(pattern, text))
