import gzip

gt_count = dict()

with gzip.open("sample.ann.vcf.gz", "rt") as handle:
    for line in handle:
        if line.startswith("#"):
            continue

        # print(line)
        # _ = input()   #한 line씩 출력하게 함 #위 code 확인 위함

        row = line.strip().split("\t")  # "\t" 기준으로 나눔 ==> vcf 한줄을 결과로
        # print(row)  # 한 line이 결과로 나오고 list로 출력됨
        # _ = input()

        gt = row[-1].split(":")[0].replace("|", "/")
        # 한 line에서 -1번째 index 즉, 마지막 index를 ":"으로 나눈 것 중에 0번째 index
        # "|"를 "/"로 문자열 바꿈
        # gt = 0/1, 1/1, 1/2 (genotype)

        if gt not in gt_count:
            gt_count[gt] = 0  # gt=key, gt_count[gt]=value
            # gt_count dictionary에 gt 없으면 value를 0으로

        gt_count[gt] += 1
        # gt_count dictionary에 gt 있으면 value에 1 더함

print(gt_count)
# dictionary 출력
# genotype=key, genotype 갯수=value
