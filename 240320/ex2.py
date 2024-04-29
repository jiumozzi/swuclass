# 두 숫자를 argparse를 사용하여 입력 받아 결과 출력하기

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--num1", "-n1", required=True)
parser.add_argument("--num2", required=True)
# required=True : 입력 받아야 실행되도록.

args = parser.parse_args()
# "argparse" library에 있는 어떤 함수를 실행시키기 위함.
## 이 command를 쓰면 "--num1" 뒤에 연결되는 숫자를 input으로.


num1 = int(args.num1)
num2 = int(args.num2)


print(f"{num1} + {num2} = {num1+num2}")
