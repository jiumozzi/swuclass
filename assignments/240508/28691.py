f = input()

f_list = ["M", "W", "C", "A", "$"]

c_list = ["MatKor", "WiCys", "CyKor", "AlKor", "$clear"]

for a in range(5):
    if f == f_list[a]:
        print(c_list[a])
    else:
        continue
