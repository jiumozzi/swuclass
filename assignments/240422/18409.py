N = int(input())
S = input()
vowel = ["a", "i", "u", "e", "o"]

result = 0

for i in S:
    if i in vowel:
        result += 1
    else:
        continue
print(result)
