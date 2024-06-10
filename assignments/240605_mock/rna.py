def transcribe(dataset: str):
    seq = ""
    with open(dataset) as handle:
        for line in handle:
            for base in line.strip():
                if base == "T":
                    seq += "U"
                else:
                    seq += base
    return seq


if __name__ == "__main__":
    data = transcribe("rna_dataset.txt")
    print(data)
