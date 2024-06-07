Acount = 0
Ccount = 0
Gcount = 0
Tcount = 0

with open("rosalind_dna_sample_dataset.txt") as handle:
    for line in handle:
        for nt in line:
            if nt == "A":
                Acount += 1
            elif nt == "C":
                Ccount += 1
            elif nt == "G":
                Gcount += 1
            else:
                Tcount += 1
print(Acount, Ccount, Gcount, Tcount)
