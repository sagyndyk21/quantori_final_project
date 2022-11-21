from data.get_data import get_rna_base, get_protein


CODON_LENGTH = 3


def convert_dna_to_rna(dna: str) -> str:
    rna = ''
    for base in dna:
        rna += get_rna_base(base)

    return rna


def convert_rna_to_protein(rna: str) -> str:
    codons = [rna[i:i+CODON_LENGTH] for i in range(0, len(rna), CODON_LENGTH)]
    protein = ''
    for codon in codons:
        if len(codon) != CODON_LENGTH:
            break
        protein += get_protein(codon)

    return protein


if __name__ == '__main__':
    pass
