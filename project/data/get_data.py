from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from data.models import Dna, Rna, Codon, AminoAcid


engine = create_engine('sqlite:///./data/database.db')


def get_rna_base(dna_base: str) -> str:
    with Session(engine) as session:
        query = session.query(Rna).join(Dna).where(Dna.base == dna_base)
        return query[0].base


def get_protein(codon: str) -> str:
    with Session(engine) as session:
        query = session.query(AminoAcid).join(Codon).where(Codon.codon == codon)
        return query[0].amino_acid
