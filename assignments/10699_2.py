import time

now = time

# print(now)  # output: <module 'time' (built-in)>
# print(now.localtime)  # output: <built-in function localtime>
# print(now.time)  # output: <built-in function time>
# print(now.localtime().tm_year)  # output: 2024
# print(now.localtime().tm_mon)  # output:4
# print(now.localtime().tm_mday)  # output: 17
# print(now.strftime("%Y-%m-%d %H:%M:%S"))  #output: 2024-04-17 10:39:57

print(now.strftime("%Y-%m-%d"))
