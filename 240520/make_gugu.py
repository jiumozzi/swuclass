# 함수 지정
# def func_name(arg1, arg2):
#     ~
#     Return


# ex
# def func(arg1):
#     result = arg1 * 3
#     return result

# res = func(2)
# print(res)  # 6
# for i in range(1, 4):
#     print(func(i)) # 3 6 9

# ======================================================================


def make_gugu(num):
    for i in range(2, 10):
        print(f"{num} x {i} = {num*i}")


make_gugu(2)  # 2단


def make_gugu_f(num):
    with open(f"gugu_{num}_result.txt", "w") as handle:
        for i in range(1, 10):
            handle.write(f"{num} x {i} = {num*i}\n")


make_gugu_f(3)  # 3단 txt 파일 생성


for i in range(1, 101):
    make_gugu(i)  # 100단 까지 print

for i in range(1, 101):
    make_gugu_f(i)  # 10단 까지 file 생성
