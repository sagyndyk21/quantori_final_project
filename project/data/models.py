from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Dna(Base):
    __tablename__ = 'dna_bases'

    id = Column(Integer, primary_key=True)
    base = Column(String(1))
    rna_base = relationship('Rna', back_populates='dna_base')
    rna_id = Column(Integer, ForeignKey('rna_bases.id'))


class Rna(Base):
    __tablename__ = 'rna_bases'

    id = Column(Integer, primary_key=True)
    base = Column(String(1))
    dna_base = relationship('Dna', back_populates='rna_base')


class Codon(Base):
    __tablename__ = 'codons'

    id = Column(Integer, primary_key=True)
    codon = Column(String(3))
    amino_acid = relationship('AminoAcid', back_populates='codon')
    acid_id = Column(Integer, ForeignKey('amino_acids.id'))


class AminoAcid(Base):
    __tablename__ = 'amino_acids'

    id = Column(Integer, primary_key=True)
    amino_acid = Column(String(1))
    codon = relationship('Codon', back_populates='amino_acid')
