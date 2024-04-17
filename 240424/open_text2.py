with open("test.txt") as handle:
    for line in handle:
        print(line.strip())

# with ~ as ~ 를 사용해서 open
# for문이 안쪽으로 들어감
# with open을 하면 close 안 써도 됨
## 한 블록에 해당하기 때문에 자동으로 닫힘
