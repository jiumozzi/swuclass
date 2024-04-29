data = list()
for i in range(9):
    num = int(input())
    data.append(num)

max_num = max(data)
print(max_num)
print(data.index(max_num) + 1)
