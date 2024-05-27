ava = list(map(int, input().split()))
needs = list(map(int, input().split()))

res = 0

for i, j in zip(ava, needs):
    if i - j < 0:
        res += j - i
print(res)
