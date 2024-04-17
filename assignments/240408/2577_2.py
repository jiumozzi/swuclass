A = int(input())
B = int(input())
C = int(input())
D = str(A * B * C)

data = dict()
for i in D:
    if i not in data:
        data[i] = 0
    data[i] += 1

for i in range(10):
    print(data.get(str(i), 0))  # get : dictionary의 method
