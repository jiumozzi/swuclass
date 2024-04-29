data = []

for i in range(5):
    num = int(input())

    if num in data:
        data.remove(num)
    else:
        data.append(num)

print(data[0])
