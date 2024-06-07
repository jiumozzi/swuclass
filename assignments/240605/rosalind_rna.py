with open("rosalind_rna_dataset.txt", "r") as handle:
    seq = ""

    for line in handle:
        for nt in line:
            if nt == "T":
                seq += "U"
            else:
                seq += nt

print(seq)
