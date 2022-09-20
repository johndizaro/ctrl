from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()


class Unidade_Medida(Base):
    __tablename__ = "unidade_medida"

    id = Column(Integer, primary_key=True)
    sigla = Column(String)
    descricao = Column(String)

    def __repr__(self):
        return f"Table:{Unidade_Medida.__tablename__} id:{self.id} sigla:{self.sigla} descricao:{self.descricao}"

    @classmethod
    def find_by_sigla(cls, session, sigla):
        return session.query(cls).filter_by(sigla=sigla).all()


Base.metadata.create_all(engine)

um = Unidade_Medida(sigla="Kg", descricao="Kilograma")
# session.add(um)
print(um)
