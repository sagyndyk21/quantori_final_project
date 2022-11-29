import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from data.models import Base, Dna, Rna, Codon, AminoAcid
from data.genetic_code import dna_rna_table, codons_table


user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
hostname = os.environ['POSTGRES_HOST']
database_name = os.environ['POSTGRES_DB']


def create_db_and_tables() -> None:
    engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{hostname}/{database_name}')
    Base.metadata.create_all(engine, checkfirst=True)  # does not create tables if they already exist

    with Session(engine) as session:
        for dna_base, rna_base in dna_rna_table.items():
            rna = Rna(base=rna_base)
            dna = Dna(base=dna_base, rna_base=rna)
            session.add(dna)
        session.commit()

        for amino_acid, codons in codons_table.items():
            amino = AminoAcid(amino_acid=amino_acid)
            for codon in codons:
                codon = Codon(codon=codon, amino_acid=amino)
                session.add(codon)
        session.commit()


if __name__ == '__main__':
    create_db_and_tables()
