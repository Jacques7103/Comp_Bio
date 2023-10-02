def amino_to_mrna(sequence):
    codon = {
        "F": ["UUU", "UUC"],
        "L": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
        "I": ["AUU", "AUC", "AUA"],
        "M": ["AUG"],
        "V": ["GUU", "GUC", "GUA", "GUG"],
        "S": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
        "P": ["CCU", "CCC", "CCA", "CCG"],
        "T": ["ACU", "ACC", "ACA", "ACG"],
        "A": ["GCU", "GCC", "GCA", "GCG"],
        "Y": ["UAU", "UAC"],
        "H": ["CAU", "CAC"],
        "Q": ["CAA", "CAG"],
        "N": ["AAU", "AAC"],
        "K": ["AAA", "AAG"],
        "D": ["GAU", "GAC"],
        "E": ["GAA", "GAG"],
        "C": ["UGU", "UGC"],
        "W": ["UGG"],
        "R": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
        "G": ["GGU", "GGC", "GGA", "GGG"],
        "*": ["UAA", "UAG", "UGA"],
    }
    
    mrna_sequence = ""
    for amino_acid in sequence:
        codons = codon.get(amino_acid, [""])
        if not codons:
            print("Unknown amino acid :", amino_acid)
            continue
        mrna_sequence += codons[0]
    
    return mrna_sequence

def frequency(mrna_sequence):
    frequency = {}
    for i in range(0, len(mrna_sequence), 3):
        codon = mrna_sequence[i:i + 3]
        frequency[codon] = frequency.get(codon, 0) + 1

    return frequency

amino = input("Amino Acid : ")
codons_for_amino = amino_to_mrna(amino)
mrna_sequence = "".join(codons_for_amino)
frequency = frequency(mrna_sequence)

print("mRNA Sequence :", mrna_sequence)
print("Frequency for", amino, ":", frequency)
