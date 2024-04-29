import gzip

result = 0

with gzip.open("sample.ann.vcf.gz", "rt") as handle:
    for line in handle:
        if line.startswith("##"):
            continue

        if line.startswith("#"):
            header = line.split("\t")
            qual_idx = header.index("QUAL")  # 5
            continue

        row = line.split("\t")  # \t = tap
        if float(row[qual_idx]) >= 1000:
            result += 1

print(result)
