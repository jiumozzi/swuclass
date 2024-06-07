with open("rosalind_rna_dataset.txt") as handle:
    DNA = handle.read()


def transcription(s):
    RNA = ""
    for i in s:
        if i == "T":
            RNA += "U"
        else:
            RNA += i
    return RNA


print(transcription(DNA))
