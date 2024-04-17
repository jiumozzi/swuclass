seq = ""

with open("test_aa.fasta") as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        seq += line.strip()

data = dict()  # data가 dictionary 변수 (빈dict)
# data = {}
for base in seq:
    if base not in data:
        data[base] = 0
    data[base] += 1

print(data)
