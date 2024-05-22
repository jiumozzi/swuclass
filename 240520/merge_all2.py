from glob import glob

filelist = glob("gugu*.txt")

fw = open("gugu_all2.txt", "w")

for filepath in filelist:
    with open(filepath) as fr:
        for line in fr:
            fw.write(line)

fw.close
