from sqlalchemy import Column, Integer, String, ForeignKey

from db.infra_sqlalchemy.configs.base import Base


class ConverteUnidadeMedida(Base):
    __tablename__ = "converte_unidade_medida"
    id = Column(Integer, primary_key=True)
    id_sigla_origem = Column(Integer, ForeignKey('unidade_medida.id'))
    id_sigla_destino = Column(Integer, ForeignKey('unidade_medida.id'))
    calculo = Column(String, nullable=False)

    def __repr__(self):
        return f"tabela:{self.__tablename__}, (id:{self.id}, id_sigla_origem:{self.id_sigla_origem}, id_sigla_destino:{self.id_sigla_destino} calculo:{self.calculo})"
