handle = open("test.txt")
for line in handle:
    print(line)

handle.close()
# 파일 열고 닫고 python script 종료
# 나중에 오류 생길 수 있으니 open 하면 close도 하기

# 결과가 txt 그대로 안나오고 사이에 엔터 쳐서 나오는 이유
## 원래 txt에 있던 엔터 + print()의 엔터
## 없애려면 print(line.strip())
# strip(): 양쪽의 공백 없애줌

handle = open("test.txt")
for line in handle:
    print(line.strip())

handle.close()
