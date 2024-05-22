from glob import glob

filelist = glob("gugu*.txt")

# print(filelist)  # gugu로 시작하는 file을 list로 print
# print(len(filelist))  # 100

with open("gugu_all.txt", "w") as handle:
    for filepath in filelist:
        with open(filepath) as handle_read:
            for line in handle_read:
                handle.write(line)
# gugu_all.txt에는 순서대로 정렬 안되어 있음
