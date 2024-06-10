def count_base(dataset: str):
    Ac, Cc, Gc, Tc = 0, 0, 0, 0
    with open(dataset) as handle:
        for line in handle:
            for base in line.strip():
                if base == "A":
                    Ac += 1
                elif base == "C":
                    Cc += 1
                elif base == "G":
                    Gc += 1
                else:
                    Tc += 1
    return f"{Ac} {Cc} {Gc} {Tc}"


if __name__ == "__main__":
    data = count_base("dna_dataset.txt")
    print(data)
