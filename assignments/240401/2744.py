a = input()
result = ""

for c in a:
    if c.islower():
        result += c.upper()
    else:
        result += c.lower()


print(result)
