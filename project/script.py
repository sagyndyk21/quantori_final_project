import sys

from data.get_data import get_rna_base, get_protein
from data.create_tables import create_db_and_tables

from gc_ratio_plot import plot_gc_content

from helper_functions import read_input, conversion_format


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


def run_on_input_files() -> None:
    dna_inputs = read_input('data/inputs/dna_inputs.txt')
    rna_inputs = read_input('data/inputs/rna_inputs.txt')
    gc_inputs = read_input('data/inputs/gc_inputs.txt')

    print('DNA to RNA conversion:')
    for dna in dna_inputs:
        rna = convert_dna_to_rna(dna)
        print(conversion_format(dna, rna))

    print('RNA to Protein conversion:')
    for rna in rna_inputs:
        protein = convert_rna_to_protein(rna)
        print(conversion_format(rna, protein))

    for i, seq in enumerate(gc_inputs):
        image_file_name = f'{i}_genomic_data'
        plot_gc_content(seq, image_file_name=image_file_name)
        print(f'GC content plot saved: images/{image_file_name}.png')


if __name__ == '__main__':
    create_db_and_tables()
    if len(sys.argv) == 3:
        mode = sys.argv[1].strip()
        sequence = sys.argv[2].strip()
        if mode == 'dna_to_rna':
            print(conversion_format(sequence, convert_dna_to_rna(sequence)))
        elif mode == 'rna_to_protein':
            print(conversion_format(sequence, convert_rna_to_protein(sequence)))
        elif mode == 'gc_content':
            plot_gc_content(sequence, image_file_name='gc_content_of_sequence_as_argument')
            print('GC content plot saved in images/')
        else:
            print('Wrong mode! Allowed modes: dna_to_rna, rna_to_protein, gc_content')
    else:
        run_on_input_files()
