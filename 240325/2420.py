A, B = list(map(int, input().split()))
# A = int(A), B = int(B)
# input().split
# 2 3 -> ["2", "3"]

if A > B:
    print(A - B)
else:
    print(A + B)
