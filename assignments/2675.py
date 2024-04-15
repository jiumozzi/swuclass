T = int(input())

for i in range(T):
    R, S = input().split()
    for j in S:
        print(j * int(R), end="")
        # end 옵션 넣지 않으면 자동으로 줄넘김됨
    print()
