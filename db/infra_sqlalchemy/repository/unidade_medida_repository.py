from db.infra_sqlalchemy.configs.connection import DBConnectionHandler
from db.infra_sqlalchemy.entiteis.unidade_medida import UnidadeMedida


class UnidadeMedidaReposistory:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(UnidadeMedida).all()
            return data

    def delete(self, id):
        with DBConnectionHandler() as db:
            db.session.query(UnidadeMedida).filter(UnidadeMedida.id==id).delete()
            db.session.commit()


    def insert(self, sigla, descricao):
        with DBConnectionHandler() as db:
            data_insert = UnidadeMedida(sigla=sigla, descricao=descricao)
            db.session.add(data_insert)
            db.session.commit()

    def update(self, id, sigla, descricao):
        with DBConnectionHandler() as db:
            db.session.query(UnidadeMedida).filter(UnidadeMedida.id == id).update({'sigla':sigla,'descricao': descricao})
            db.session.commit()

