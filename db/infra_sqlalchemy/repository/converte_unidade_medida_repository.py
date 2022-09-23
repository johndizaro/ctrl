from db.infra_sqlalchemy.configs.connection import DBConnectionHandler
from db.infra_sqlalchemy.entiteis.converte_unidade_medida import ConverteUnidadeMedida


class ConverteUnidadeMedidaReposistory:

    def select(self):
        with DBConnectionHandler() as db:
            # data = db.session.query(ConverteUnidadeMedida).with_entities(ConverteUnidadeMedida.calculo).all()
            data = db.session.query(ConverteUnidadeMedida).all()
            return data

    def delete(self, id):
        with DBConnectionHandler() as db:
            db.session.query(ConverteUnidadeMedida).filter(ConverteUnidadeMedida.id == id).delete()
            db.session.commit()

    def insert(self, sigla, descricao):
        with DBConnectionHandler() as db:
            data_insert = ConverteUnidadeMedida(sigla=sigla, descricao=descricao)
            db.session.add(data_insert)
            db.session.commit()

    def update(self, id, id_sigla_origem, id_sigla_destino, calculo):
        with DBConnectionHandler() as db:
            db.session.query(ConverteUnidadeMedida).filter(ConverteUnidadeMedida.id == id).update({
                'id_sigla_origem': id_sigla_origem, 'id_sigla_destino': id_sigla_destino, 'calculo': calculo})
            db.session.commit()
