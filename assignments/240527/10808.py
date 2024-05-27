# ord(문자) >> 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수 반환
# chr(정수) >> 정수를 인자로 받고 해당 정수에 해당하는 유니코드 문자 반환
## ord('a') >> 97
## chr(97) >> 'a'
### 알파벳 a ~ z == 97 ~ 122
### print(ord("a")) > 97
### print(chr(98)) > b

S = input()
alphabet = [0] * 26

for i in S:
    alphabet[ord(i) - 97] += 1

for i in alphabet:
    print(i, end=" ")
