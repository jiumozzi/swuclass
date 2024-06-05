a = input()

res = ""

for i in a:
    if i.islower():
        res += i.upper()
    else:
        res += i.lower()
print(res)
