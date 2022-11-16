from data.genetic_code import codons_table


def convert_dna_to_rna(dna: str) -> str:
    return dna.replace('T', 'U')


def convert_rna_to_protein(rna: str) -> str:
    codons = [rna[i:i+3] for i in range(0, len(rna), 3)]
    protein = ''
    for codon in codons:
        protein += codons_table.get(codon, '')

    return protein


def test():
    rna_tests = {
        'ATTTGGCTACTAACAATCTA': 'AUUUGGCUACUAACAAUCUA',
        'GTTGTAATGGCCTACATTA': 'GUUGUAAUGGCCUACAUUA',
        'CAGGTGGTGTTGTTCAGTT': 'CAGGUGGUGUUGUUCAGUU',
        'GCTAACTAAC': 'GCUAACUAAC',
        'GCTAACTAACATCTTTGGCACTGTT': 'GCUAACUAACAUCUUUGGCACUGUU',
        'TATGAAAAACTCAAA': 'UAUGAAAAACUCAAA',
        'CCCGTCCTTGATTGGCTTGAAGAGAAGTTT': 'CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU'
    }

    protein_tests = {
        'AUUUGGCUACUAACAAUCUA': 'IWLLTI',
        'GUUGUAAUGGCCUACAUUA': 'VVMAYI',
        'CAGGUGGUGUUGUUCAGUU': 'QVVLFS',
        'GCUAACUAAC': 'AN.',
        'GCUAACUAACAUCUUUGGCACUGUU': 'AN.HLWHC',
        'UAUGAAAAACUCAAA': 'YEKLK',
        'CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU': 'PVLDWLEEKF'
    }

    for dna, rna in rna_tests.items():
        if convert_dna_to_rna(dna) != rna:
            print('convert_dna_to_rna does not work properly')
            return False

    for rna, protein in protein_tests.items():
        if convert_rna_to_protein(rna) != protein:
            print('convert_rna_to_protein does not work properly')
            return False

    print('Everything is ok!')
    return True


if __name__ == '__main__':
    test()
