import re

# Standard validation problem

pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"

cases = [
    "Password1!",
    "weakpass",
    "NoSpecial1"
]

for c in cases:
    print(c, "->", bool(re.match(pattern, c)))
