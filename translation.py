def complement(dna):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    sequence = ''.join(complement_dict[base] for base in dna)
    return sequence

def dna_to_mrna(sequence):
    return sequence.replace('T', 'U')

def mrna_to_protein(mrna_sequence):
    codon = {
        "UUU": "Phenylalanine (F)", "UUC": "Phenylalanine (F)", "UUA": "Leucine (L)", "UUG": "Leucine (L)",
        "UCU": "Serine (S)", "UCC": "Serine (S)", "UCA": "Serine (S)", "UCG": "Serine (S)",
        "UAU": "Tyrosine (Y)", "UAC": "Tyrosine (Y)", "UAA": "Stop codon (*)", "UAG": "Stop codon (*)",
        "UGU": "Cysteine (C)", "UGC": "Cysteine (C)", "UGA": "Stop codon (*)", "UGG": "Tryptophan (W)",
        "CUU": "Leucine (L)", "CUC": "Leucine (L)", "CUA": "Leucine (L)", "CUG": "Leucine (L)",
        "CCU": "Proline (P)", "CCC": "Proline (P)", "CCA": "Proline (P)", "CCG": "Proline (P)",
        "CAU": "Histidine (H)", "CAC": "Histidine (H)", "CAA": "Glutamine (Q)", "CAG": "Glutamine (Q)",
        "CGU": "Arginine (R)", "CGC": "Arginine (R)", "CGA": "Arginine (R)", "CGG": "Arginine (R)",
        "AUU": "Isoleucine (I)", "AUC": "Isoleucine (I)", "AUA": "Isoleucine (I)", "AUG": "Methionine (M)",
        "ACU": "Threonine (T)", "ACC": "Threonine (T)", "ACA": "Threonine (T)", "ACG": "Threonine (T)",
        "AAU": "Asparagine (N)", "AAC": "Asparagine (N)", "AAA": "Lysine (K)", "AAG": "Lysine (K)",
        "AGU": "Serine (S)", "AGC": "Serine (S)", "AGA": "Arginine (R)", "AGG": "Arginine (R)",
        "GUU": "Valine (V)", "GUC": "Valine (V)", "GUA": "Valine (V)", "GUG": "Valine (V)",
        "GCU": "Alanine (A)", "GCC": "Alanine (A)", "GCA": "Alanine (A)", "GCG": "Alanine (A)",
        "GAU": "Aspartic Acid (D)", "GAC": "Aspartic Acid (D)", "GAA": "Glutamic Acid (E)", "GAG": "Glutamic Acid (E)",
        "GGU": "Glycine (G)", "GGC": "Glycine (G)", "GGA": "Glycine (G)", "GGG": "Glycine (G)",
    }
    
    protein_sequence = ""
    for i in range(0, len(mrna_sequence), 3):
        codons = mrna_sequence[i:i+3]
        amino_acid = codon.get(codons, "X")
        if i == len(mrna_sequence) - 3:
            pass
        else:
            amino_acid = amino_acid + " - "
        protein_sequence += amino_acid
    return protein_sequence

dna = input("DNA : ")
complement = complement(dna)
mrna_sequence = dna_to_mrna(complement)
protein_sequence = mrna_to_protein(mrna_sequence)

print("Complement :", complement)
print("mRNA Sequence :", mrna_sequence)
print("Protein Sequence :", protein_sequence)