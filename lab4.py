import re

def validateStr(str):
    if re.match("^\d{1,}$", str):
        return f"{str} is an integer"
    elif re.match("^\d{0,}.\d{1,}", str):
        return f"{str} is a float"
    elif re.match("^\w$", str):
        return f"{str} is a character"
    else:
        return f"{str} is a string"

inp = ["123", "3.14", "a", "abc"]
for i in inp:
    print(validateStr(i))


