import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from data.models import Dna, Rna, Codon, AminoAcid


user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
hostname = os.environ['POSTGRES_HOST']
database_name = os.environ['POSTGRES_DB']

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{hostname}/{database_name}')


def get_rna_base(dna_base: str) -> str:
    with Session(engine) as session:
        query = session.query(Rna).join(Dna).where(Dna.base == dna_base)
        return query[0].base


def get_protein(codon: str) -> str:
    with Session(engine) as session:
        query = session.query(AminoAcid).join(Codon).where(Codon.codon == codon)
        return query[0].amino_acid
