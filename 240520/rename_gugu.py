# #file name을 rename 하는 방법
# import os
# os.rename( a , b ) #파일 이름을 a에서 b로 바꿈

import os

for i in range(11, 101):
    os.rename(f"gugu_{i}_result.txt", f"gugu_{i}_dan.txt")
    # "gugu_1_result.txt" -> "gugu_1_dan.txt" 로 rename
