from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from data.models import Base, Dna, Rna, Codon, AminoAcid
from data.genetic_code import dna_rna_table, codons_table


engine = create_engine('sqlite:///database.db')


def create_db_and_tables() -> None:
    Base.metadata.create_all(engine)

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


def get_rna_base(dna_base: str) -> str:
    with Session(engine) as session:
        query = session.query(Rna).join(Dna).where(Dna.base == dna_base)
        return query[0].base


def get_protein(codon: str) -> str:
    print(codon)
    with Session(engine) as session:
        query = session.query(AminoAcid).join(Codon).where(Codon.codon == codon)
        return query[0].amino_acid


if __name__ == '__main__':
    create_db_and_tables()
