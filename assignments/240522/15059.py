# zip()
#: 순회 가능한 객체(iterable)를 인자로 받고
#  각 자료형의 각 요소를 나눈 후 인덱스끼리 잘라서 리스트로 반환해줌
## lst1 = [1, 2, 3, 4]
## lst2 = ["one", "two", "three", "four"]
## for x, y in zip(lst1, lst2):
##     print(x, y)
## > 1 one
## > 2 two
## > 3 three
## > 4 four


ava = list(map(int, input().split()))
needs = list(map(int, input().split()))

res = 0

for i, j in zip(ava, needs):
    if i - j < 0:
        res += j - i
print(res)
