import re

# Common pattern, works for most cases
# Haven't handled very rare formats yet

pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

data = [
    "test@gmail.com",
    "user.name+tag@domain.co.in",
    "invalid-email@"
]

for d in data:
    print(d, "->", re.findall(pattern, d))
