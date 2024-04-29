# vcf 파일에서 변이 있는 data 줄만 갯수 세기

import gzip

result = 0
with gzip.open("sample.ann.vcf.gz", "rt") as handle:
    for line in handle:
        if line.startswith("#"):
            continue

        result += 1
print(result)
