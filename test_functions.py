from script import convert_dna_to_rna, convert_rna_to_protein


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
