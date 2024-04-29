import gzip

result = 0

with gzip.open("sample.ann.vcf.gz", "rt") as handle:
    for line in handle:
        if line.startswith("#"):
            continue

        row = line.split()
        # print(row[5])  #list중 5번째 값 가져옴

        if float(row[5]) >= 1000:  # float는 소수점 있는 실수
            result += 1

print(result)
