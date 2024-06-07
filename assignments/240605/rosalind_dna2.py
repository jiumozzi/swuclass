with open("rosalind_dna_sample_dataset.txt") as handle:
    DNA = handle.read()


def counter(s):
    Ac, Cc, Gc, Tc = 0, 0, 0, 0
    for i in s:
        if i == "A":
            Ac += 1
        elif i == "C":
            Cc += 1
        elif i == "G":
            Gc += 1
        else:
            Tc += 1
    return f"{Ac} {Cc} {Gc} {Tc}"


print(counter(DNA))
