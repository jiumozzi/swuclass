str = input()
vow = int()
vow_2 = int()

for i in str:
    if i in ("a", "e", "i", "o", "u", "y"):
        vow += 1
    if i in ("a", "e", "i", "o", "u"):
        vow_2 += 1
print(f"{vow_2} {vow}")
