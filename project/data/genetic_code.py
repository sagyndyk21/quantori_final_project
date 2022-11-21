dna_rna_table = {
    'A': 'A',
    'T': 'U',
    'G': 'G',
    'C': 'C'
}


codons_table = {
    'F': ('UUU', 'UUC'), 'L': ('UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'), 
    'S': ('UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'), 'Y': ('UAU', 'UAC'), 
    '.': ('UAA', 'UAG', 'UGA'), 'C': ('UGU', 'UGC'), 'W': ('UGG',), 'M': ('AUG',),
    'P': ('CCU', 'CCC', 'CCA', 'CCG'), 'H': ('CAU', 'CAC'), 'Q': ('CAA', 'CAG'),
    'R': ('CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'), 'N': ('AAU', 'AAC'),
    'I': ('AUU', 'AUC', 'AUA'), 'T': ('ACU', 'ACC', 'ACA', 'ACG'), 'K': ('AAA', 'AAG'),
    'V': ('GUU', 'GUC', 'GUA', 'GUG'), 'G': ('GGU', 'GGC', 'GGA', 'GGG'),
    'A': ('GCU', 'GCC', 'GCA', 'GCG'), 'D': ('GAU', 'GAC'), 'E': ('GAA', 'GAG'),
}
