from data.genetic_code import codons_table


CODON_LENGTH = 3


def convert_dna_to_rna(dna: str) -> str:
    return dna.replace('T', 'U')


def convert_rna_to_protein(rna: str) -> str:
    codons = [rna[i:i+CODON_LENGTH] for i in range(0, len(rna), CODON_LENGTH)]
    protein = ''
    for codon in codons:
        protein += codons_table.get(codon, '')

    return protein


if __name__ == '__main__':
    pass
