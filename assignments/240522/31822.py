sub_code = input()
n = int(input())
res = 0

for i in range(n):
    ava_code = input()
    if sub_code[0:5] == ava_code[0:5]:
        res += 1

print(res)
