from datetime import datetime

now = datetime.now()
# print(now)  # output: 2024-04-17 10:20:58.180736
# print(now.date())  # output: 2024-04-17
# print(now.time())  # output: 10:22:58.970617
# print(now.year)  # output: 2024
# print(now.weekday())  # output: 2(수)
# print(now.strftime("%Y-%m-%d %H:%M:%S"))  # output: 2024-04-17 10:25:38

print(now.strftime("%Y-%m-%d"))


Y = str(now.year)
M = str(now.month)
m = len(M)
if m == 1:
    M = "0" + M
D = str(now.day)

print(Y + "-" + M + "-" + D)
