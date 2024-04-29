import gzip


with gzip.open("test.txt.gz", "rt") as handle:  # rt = read text mode
    for line in handle:
        print(line.strip())


# gzip으로 굳이 여는 이유 : 작은 용량으로 열 수 있음
