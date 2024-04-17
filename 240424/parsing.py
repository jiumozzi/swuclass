seq = ""

with open("test.fasta") as handle:
    for line in handle:
        if line.startswith(">"):
            continue  # for문 끝나고 다음으로 넘어감

        seq += line.strip()

print(len(seq))
print(f'A: {seq.count("A")}{"개"}')
print(f'C: {seq.count("C")}')
print(f'G: {seq.count("G")}')
print("T: " + str(seq.count("T")))
