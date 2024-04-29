# 두 숫자를 sys.argv 로 받아서 결과 출력하기


import sys

print(sys.argv)

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])


print(f"{num1} + {num2} = {num1+num2}")
