from sqlalchemy import Column, Integer, String

from db.infra_sqlalchemy.configs.base import Base


class UnidadeMedida(Base):
    __tablename__ = "unidade_medida"
    id = Column(Integer, primary_key=True)
    sigla = Column(String, nullable=False)
    descricao = Column(String, nullable=False)

    def __repr__(self):
        return f"tabela:{self.__tablename__}, (id:{self.id}, sigla:{self.sigla}, descricao:{self.descricao})"
